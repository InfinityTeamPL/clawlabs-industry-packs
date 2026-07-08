#!/usr/bin/env python3
"""
isap_kp.py - pobiera aktualny tekst Kodeksu Pracy + kluczowe ustawy z ISAP/RCL.

Zrodlo: api.sejm.gov.pl/eli/ (ISAP - oficjalne, domena publiczna, bez API key)
Output: kadry/kb/akty-prawne/<rok>_<id>_<tytul>.md (markdown z metadanymi + tekst)

Uzycie:
    python isap_kp.py                           # pobiera default zestaw kluczowych ustaw
    python isap_kp.py --acts DU/1974/24/141     # konkretny akt
    python isap_kp.py --version-date 2026-01-27 # tekst na konkretna date

Default zestaw kadrowy:
    - Kodeks Pracy (DU/1974/24/141)
    - Ustawa o systemie ubezpieczen spolecznych (DU/1998/137/887)
    - Ustawa o swiadczeniach z ubezp. spol. w razie choroby/macierzynstwa
    - Ustawa o PIT (DU/1991/80/350)
    - Ustawa o minimalnym wynagrodzeniu za prace (DU/2002/200/1679)
    - Ustawa o PPK (DU/2018/2215)
    - Ustawa o ZFSS
    - Ustawa o zwiazkach zawodowych
"""
from __future__ import annotations

import argparse
import json
import logging
import re
import sys
import time
from datetime import datetime
from pathlib import Path

try:
    import requests
except ImportError:
    print("pip install requests", file=sys.stderr)
    sys.exit(1)

logging.basicConfig(level=logging.INFO, format="%(asctime)s %(levelname)s %(message)s")
log = logging.getLogger("isap_kp")

ELI_API = "https://api.sejm.gov.pl/eli"
USER_AGENT = "clawlabs-industry-packs/0.1 (+isap; contact@infinityteam.io)"
SESSION = requests.Session()
SESSION.headers.update({"User-Agent": USER_AGENT})

# Default kluczowe ustawy dla kadrowca
# ELI format: {publisher}/{year}/{position} - 3 czesci, gdzie position to NUMER POZYCJI W ROKU.
# Skrypt automatycznie probuje fallback z volume jezeli 404 (np. DU/1974/24/141).
DEFAULT_ACTS = [
    {"eli": "DU/1974/141",  "fallback_eli": "DU/1974/24/141",  "name": "Kodeks Pracy", "category": "kodeksy"},
    {"eli": "DU/1998/887",  "fallback_eli": "DU/1998/137/887", "name": "Ustawa o systemie ubezpieczen spolecznych", "category": "ubezpieczenia"},
    {"eli": "DU/1999/636",  "fallback_eli": "DU/1999/60/636",  "name": "Ustawa o swiadczeniach pienieznych z ubezp. spol. (choroba/macierzynstwo)", "category": "ubezpieczenia"},
    {"eli": "DU/1991/350",  "fallback_eli": "DU/1991/80/350",  "name": "Ustawa o PIT", "category": "podatki"},
    {"eli": "DU/2002/1679", "fallback_eli": "DU/2002/200/1679","name": "Ustawa o minimalnym wynagrodzeniu za prace", "category": "wynagrodzenia"},
    {"eli": "DU/2018/2215", "fallback_eli": None,              "name": "Ustawa o pracowniczych planach kapitalowych (PPK)", "category": "wynagrodzenia"},
    {"eli": "DU/1994/163",  "fallback_eli": "DU/1994/43/163",  "name": "Ustawa o zakladowym funduszu swiadczen socjalnych (ZFSS)", "category": "wynagrodzenia"},
    {"eli": "DU/1991/234",  "fallback_eli": "DU/1991/55/234",  "name": "Ustawa o zwiazkach zawodowych", "category": "zbiorowe"},
    {"eli": "DU/2003/1608", "fallback_eli": "DU/2003/166/1608","name": "Ustawa o powszechnym ubezpieczeniu zdrowotnym (NFZ)", "category": "ubezpieczenia"},
    {"eli": "DU/2004/2135", "fallback_eli": "DU/2004/210/2135","name": "Ustawa o swiadczeniach opieki zdrowotnej fin. ze srodkow publicznych", "category": "ubezpieczenia"},
    {"eli": "DU/2007/589",  "fallback_eli": "DU/2007/89/589",  "name": "Ustawa o Panstwowej Inspekcji Pracy (PIP)", "category": "kontrola"},
    {"eli": "DU/2017/60",   "fallback_eli": None,              "name": "Ustawa o zatrudnianiu pracownikow tymczasowych", "category": "zatrudnienie"},
    {"eli": "DU/2018/1000", "fallback_eli": None,              "name": "Ustawa o ochronie danych osobowych (PL implementacja RODO)", "category": "rodo"},
    {"eli": "DU/2023/1465", "fallback_eli": None,              "name": "Kodeks Pracy - tekst jednolity 2023", "category": "kodeksy"},
]


def api_get(path: str, accept: str = "application/json") -> dict | bytes | None:
    url = f"{ELI_API}{path}"
    try:
        r = SESSION.get(url, headers={"Accept": accept}, timeout=60)
        time.sleep(0.3)
        if r.status_code == 404:
            log.warning("404: %s", url)
            return None
        r.raise_for_status()
        if accept == "application/json":
            return r.json()
        return r.content
    except Exception as e:
        log.error("fail %s: %s", url, e)
        return None


def fetch_act_meta(eli: str) -> dict | None:
    """Metadane aktu (tytul, daty, status, lista ujednoliconych tekstow)."""
    return api_get(f"/acts/{eli}")


def fetch_act_text_html(eli: str, version_date: str | None = None) -> str | None:
    """Probuje pobrac tekst HTML aktu w roznych endpointach."""
    paths_to_try = []
    if version_date:
        paths_to_try.append(f"/acts/{eli}/text/T/{version_date}")
        paths_to_try.append(f"/acts/{eli}/text/{version_date}")
    paths_to_try.append(f"/acts/{eli}/text.html")
    paths_to_try.append(f"/acts/{eli}/text/html")
    paths_to_try.append(f"/acts/{eli}/text")

    for path in paths_to_try:
        content = api_get(path, accept="text/html")
        if content:
            text = content.decode("utf-8", errors="replace") if isinstance(content, bytes) else content
            if isinstance(text, dict):
                continue  # JSON odpowiedz, nie HTML
            if isinstance(text, str) and len(text) > 1000:
                return text
    return None


def fetch_act_text_pdf(eli: str, version_date: str | None = None) -> bytes | None:
    """Wykrywa WAF i odrzuca pseudo-PDFy. Probuje API + frontend ISAP."""
    # Najpierw API (api.sejm.gov.pl) - moze blokowac WAF
    paths = []
    if version_date:
        paths.append(f"/acts/{eli}/text/T/{version_date}.pdf")
    paths.append(f"/acts/{eli}/text.pdf")
    for p in paths:
        c = api_get(p, accept="application/pdf")
        if c and isinstance(c, bytes) and len(c) > 1000 and c.startswith(b"%PDF-"):
            return c

    # FALLBACK: ISAP frontend download.xsp (omija WAF API)
    # ELI: DU/{year}/{position} -> WDU{year}{volume_or_zeros}{position_padded}
    parts = eli.split("/")
    if len(parts) >= 3:
        publisher = "WDU" if parts[0] == "DU" else "WMP" if parts[0] == "MP" else parts[0]
        year = parts[1]
        # Format pozycji w URL: 4 cyfry padded
        if len(parts) == 3:
            volume = "0000"  # gdy ELI ma tylko publisher/year/position
            position = parts[2].zfill(4)
        else:
            volume = parts[2].zfill(4)
            position = parts[3].zfill(4)

        # Probuj rozne kombinacje URL frontend-u ISAP
        nsf_id = f"{publisher}{year}{volume}{position}"
        front_paths = [
            f"https://isap.sejm.gov.pl/isap.nsf/download.xsp/{nsf_id}/U/D{year}{position}Lj.pdf",  # tekst jednolity
            f"https://isap.sejm.gov.pl/isap.nsf/download.xsp/{nsf_id}/U/D{year}{position}T.pdf",   # tekst pierwotny
            f"https://isap.sejm.gov.pl/isap.nsf/download.xsp/{nsf_id}/O/D{year}{position}.pdf",    # ogloszenie
        ]
        for url in front_paths:
            log.info("    probuje frontend: %s", url[-50:])
            try:
                # browser-like User-Agent zeby uniknac blokad
                headers = {
                    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
                    "Accept": "application/pdf,*/*",
                    "Accept-Language": "pl-PL,pl;q=0.9",
                    "Referer": "https://isap.sejm.gov.pl/",
                }
                r = requests.get(url, headers=headers, timeout=60, allow_redirects=True)
                time.sleep(0.5)
                if r.status_code == 200 and r.content.startswith(b"%PDF-") and len(r.content) > 5000:
                    log.info("    OK frontend dal PDF: %.1f KB", len(r.content)/1024)
                    return r.content
                else:
                    log.info("    frontend zwrocil: status=%d, size=%d, head=%r", r.status_code, len(r.content), r.content[:30])
            except Exception as e:
                log.warning("    frontend fail: %s", e)
    return None


def html_to_markdown(html: str) -> str:
    """Bardzo proste HTML -> markdown. Zachowuje strukture, usuwa szum."""
    # usun script/style
    html = re.sub(r"<script[^>]*>.*?</script>", "", html, flags=re.DOTALL | re.IGNORECASE)
    html = re.sub(r"<style[^>]*>.*?</style>", "", html, flags=re.DOTALL | re.IGNORECASE)
    # naglowki
    html = re.sub(r"<h1[^>]*>(.*?)</h1>", r"\n\n# \1\n\n", html, flags=re.DOTALL | re.IGNORECASE)
    html = re.sub(r"<h2[^>]*>(.*?)</h2>", r"\n\n## \1\n\n", html, flags=re.DOTALL | re.IGNORECASE)
    html = re.sub(r"<h3[^>]*>(.*?)</h3>", r"\n\n### \1\n\n", html, flags=re.DOTALL | re.IGNORECASE)
    html = re.sub(r"<h4[^>]*>(.*?)</h4>", r"\n\n#### \1\n\n", html, flags=re.DOTALL | re.IGNORECASE)
    # paragraphs/breaks
    html = re.sub(r"<br\s*/?>", "\n", html, flags=re.IGNORECASE)
    html = re.sub(r"</p\s*>", "\n\n", html, flags=re.IGNORECASE)
    # bold/italic
    html = re.sub(r"<(b|strong)>(.*?)</\1>", r"**\2**", html, flags=re.DOTALL | re.IGNORECASE)
    html = re.sub(r"<(i|em)>(.*?)</\1>", r"*\2*", html, flags=re.DOTALL | re.IGNORECASE)
    # remove all other tags
    html = re.sub(r"<[^>]+>", "", html)
    # decode HTML entities (basic)
    entities = {"&nbsp;": " ", "&amp;": "&", "&lt;": "<", "&gt;": ">", "&quot;": '"',
                "&#160;": " ", "&#8217;": "'", "&#8220;": '"', "&#8221;": '"',
                "&#8211;": "–", "&#8212;": "—", "&#243;": "ó", "&oacute;": "ó",
                "&#347;": "ś", "&sacute;": "ś", "&#322;": "ł", "&lstrok;": "ł"}
    for k, v in entities.items():
        html = html.replace(k, v)
    # numeric entities
    html = re.sub(r"&#(\d+);", lambda m: chr(int(m.group(1))), html)
    # whitespace cleanup
    html = re.sub(r"\n{3,}", "\n\n", html)
    html = re.sub(r"[ \t]+", " ", html)
    return html.strip()


def _split_oversized(text: str, max_chars: int) -> list[str]:
    """Rozbija fragment dluzszy niz max_chars na coraz drobniejszych granicach, BEZ gubienia
    znakow. Potrzebne dla ustaw nowelizujacych, gdzie caly „Art. 1" to jeden wielki blok
    (wewnetrzne odwolania to male „art." albo cytowane „Art., ktorych regex granic nie lapie).

    Kolejno probuje: podpunkty (1)/1.), litery a), akapit, koniec zdania, spacja.
    re.split z grupa przechwytujaca zachowuje separatory, wiec ''.join(parts) == text (nic nie ginie).
    """
    if len(text) <= max_chars:
        return [text]
    for pat in (r"(\n(?=\d+[\.\)]\s))",   # 1. / 1)  (podpunkty)
                r"(\n(?=[a-z]\)\s))",       # a) / b)  (litery)
                r"(\n+)",                    # dowolna nowa linia / akapit
                r"((?<=[.;])\s+)",           # koniec zdania
                r"(\s+)"):                    # ostatecznie spacja
        parts = re.split(pat, text)
        merged: list[str] = []
        cur = ""
        for p in parts:
            if cur and len(cur) + len(p) > max_chars:
                merged.append(cur)
                cur = p
            else:
                cur += p
        if cur:
            merged.append(cur)
        if len(merged) > 1:
            # niektore czesci moga wciaz przekraczac limit (np. dlugi akapit) -> rekurencja
            out: list[str] = []
            for m in merged:
                out.extend(_split_oversized(m, max_chars) if len(m) > max_chars else [m])
            return out
    # zupelnie niepodzielny ciag (jeden token > max_chars) -> twardy podzial, ale NIC nie gubimy
    return [text[i:i + max_chars] for i in range(0, len(text), max_chars)]


def split_into_chunks(text: str, max_chars: int = 14000, eli: str = "") -> list[str]:
    """Dzieli dlugi tekst na chunki <= max_chars, na granicach naturalnych (DZIAL/Rozdzial/Art.).

    Gwarancja: zaden zwrocony chunk nie przekracza max_chars i CALY tekst jest zachowany
    (zadne znaki nie sa obcinane). Sekcje ktore same przekraczaja limit sa rozbijane
    drobniej przez _split_oversized() zamiast trafiac do chunku, ktory potem bylby przyciety.
    """
    # granice 1. rzedu: DZIAL / Rozdzial / Art. N
    sections = re.split(r"\n(?=DZIA[ŁL]\s+[IVXLCDM]+|Rozdzia[lł]\s+\d+|Art\.\s*\d+)", text)
    # kazda sekcja przekraczajaca limit rozbij drobniej — inaczej powstalby chunk > max_chars
    units: list[str] = []
    for sec in sections:
        units.extend(_split_oversized(sec, max_chars) if len(sec) > max_chars else [sec])
    # scal jednostki w chunki <= max_chars
    chunks: list[str] = []
    current = ""
    for u in units:
        if current and len(current) + len(u) + 1 > max_chars:
            chunks.append(current.strip())
            current = u
        else:
            current = f"{current}\n{u}" if current else u
    if current.strip():
        chunks.append(current.strip())
    return chunks


def safe_slug(s: str, max_len: int = 60) -> str:
    s = s.lower()
    s = re.sub(r"[ąćęłńóśźż]", lambda m: {"ą":"a","ć":"c","ę":"e","ł":"l","ń":"n","ó":"o","ś":"s","ź":"z","ż":"z"}[m.group()], s)
    s = re.sub(r"[^a-z0-9]+", "-", s)
    return s.strip("-")[:max_len] or "untitled"


def process_act(act: dict, version_date: str | None, out_dir: Path) -> bool:
    eli = act["eli"]
    log.info("=== %s — %s ===", eli, act["name"])

    meta = fetch_act_meta(eli)
    if not meta and act.get("fallback_eli"):
        log.info("  fallback: %s", act["fallback_eli"])
        eli = act["fallback_eli"]
        meta = fetch_act_meta(eli)
    if not meta:
        log.warning("Brak metadanych dla %s, skipuje", eli)
        return False

    title = meta.get("title", act["name"]) if isinstance(meta, dict) else act["name"]
    promulgation = meta.get("promulgation", "") if isinstance(meta, dict) else ""
    in_force = meta.get("inForce", "") if isinstance(meta, dict) else ""
    last_change = meta.get("lastChangeDate", "") if isinstance(meta, dict) else ""
    address = meta.get("address") if isinstance(meta, dict) else None
    pub_date = (address.get("date") if isinstance(address, dict) else address) or ""

    log.info("  Tytul: %s", title[:80])
    log.info("  W mocy: %s, ostatnia zmiana: %s", in_force, last_change)

    # PRIMARY: PDF (HTML endpoint w api.sejm.gov.pl zwraca dummy 348-char stub)
    text_md = ""
    log.info("  Probuje PDF...")
    pdf_bytes = fetch_act_text_pdf(eli, version_date=version_date)

    if pdf_bytes:
        # zapisz PDF zawsze
        pdf_path = out_dir / act.get("category", "inne") / f"{safe_slug(eli)}_{safe_slug(title, 30)}.pdf"
        pdf_path.parent.mkdir(parents=True, exist_ok=True)
        pdf_path.write_bytes(pdf_bytes)
        log.info("  zapisano PDF: %s (%.1f KB)", pdf_path.name, len(pdf_bytes)/1024)

        try:
            from pypdf import PdfReader
            from io import BytesIO
            reader = PdfReader(BytesIO(pdf_bytes))
            text_md = "\n\n".join(p.extract_text() or "" for p in reader.pages)
            log.info("  Tekst PDF: %d stron, %d znakow", len(reader.pages), len(text_md))
        except ImportError:
            log.warning("  pypdf nie zainstalowany — zapisuje TYLKO PDF, brak chunkowania tekstu")
            log.warning("  pip install pypdf  i odpal ponownie")
            return True  # PDF zapisany, OK
        except Exception as e:
            log.error("  PDF parse fail: %s — zapisany sam PDF", e)
            return True
    else:
        # FALLBACK na HTML (rzadko działa, ale spróbuj)
        log.info("  PDF 404 — probuje HTML jako fallback...")
        text_html = fetch_act_text_html(eli, version_date=version_date)
        if text_html:
            text_md = html_to_markdown(text_html)
            log.info("  Tekst HTML: %d znakow", len(text_md))

    if not text_md or len(text_md) < 500:
        log.warning("  Pusty/za krotki tekst (%d znakow) dla %s, skipuje", len(text_md), eli)
        return False

    # SANITY CHECK: czy to nie PRL-owski tekst pierwotny?
    PRL_MARKERS = ["Polskiej Rzeczypospolitej Ludowej", "ludu pracującego", "socjalistyczn",
                   "Polska Rzeczpospolita Ludowa", "Polskiej Rzeczypospolitej  Ludowej"]
    prl_hits = sum(1 for m in PRL_MARKERS if m.lower() in text_md.lower())
    if prl_hits >= 2:
        log.error("  ⚠️  WYKRYTO PRL-owski TEKST PIERWOTNY (znaleziono %d markerów)!", prl_hits)
        log.error("  ⚠️  ODRZUCAM — to NIE jest aktualny tekst. Znajdź ELI tekstu jednolitego (TJ).")
        log.error("  ⚠️  Przykład: zamiast DU/1974/141 (KP) → użyj DU/2025/277 (KP TJ luty 2025)")
        return False

    # Subdirectory per kategoria
    cat_dir = out_dir / act.get("category", "inne") / f"{safe_slug(eli)}_{safe_slug(title, 40)}"
    cat_dir.mkdir(parents=True, exist_ok=True)

    # Plik 1: overview
    overview = []
    overview.append("---")
    overview.append(f"act_eli: {eli}")
    overview.append(f"title: {json.dumps(title, ensure_ascii=False)}")
    overview.append(f"promulgation_date: {promulgation}")
    overview.append(f"last_change_date: {last_change}")
    overview.append(f"in_force: {in_force}")
    overview.append(f"version_date: {version_date or 'latest'}")
    overview.append(f"source: ISAP / api.sejm.gov.pl/eli/")
    overview.append(f"source_url: https://isap.sejm.gov.pl/isap.nsf/DocDetails.xsp?id={eli.replace('/', '+')}")
    overview.append(f"license: domena publiczna (akty prawne, art. 4 pr.aut.)")
    overview.append(f"category: {act.get('category', 'inne')}")
    overview.append(f"chunks_count: TBD")
    overview.append("---")
    overview.append("")
    overview.append(f"# {title}")
    overview.append("")
    overview.append(f"**ELI:** `{eli}`  ")
    overview.append(f"**Promulgacja:** {promulgation}  ")
    overview.append(f"**W mocy od:** {in_force}  ")
    overview.append(f"**Ostatnia zmiana:** {last_change}  ")
    overview.append(f"**Wersja tekstu:** {version_date or 'aktualna na dziś'}")
    overview.append("")
    overview.append("## Co to jest")
    overview.append("")
    overview.append(f"Akt prawny w bazie ISAP. Pobrany z oficjalnego API Sejmu.")
    overview.append(f"Pełny tekst rozbity na chunki w plikach `chunk_NN.md` w tym katalogu.")
    overview.append("")
    overview.append("## Linki")
    overview.append(f"- ISAP: https://isap.sejm.gov.pl")
    overview.append(f"- API: {ELI_API}/acts/{eli}")
    overview.append("")
    (cat_dir / "_overview.md").write_text("\n".join(overview), encoding="utf-8")

    # Chunki tekstu
    chunks = split_into_chunks(text_md)
    log.info("  Chunkow: %d", len(chunks))
    for i, chunk in enumerate(chunks, 1):
        chunk_md = []
        chunk_md.append("---")
        chunk_md.append(f"act_eli: {eli}")
        chunk_md.append(f"chunk: {i}/{len(chunks)}")
        chunk_md.append(f"title_short: {json.dumps(title[:60], ensure_ascii=False)}")
        chunk_md.append(f"version_date: {version_date or 'latest'}")
        chunk_md.append("---")
        chunk_md.append("")
        chunk_md.append(f"# {title} — chunk {i}/{len(chunks)}")
        chunk_md.append("")
        # NIE przycinamy — split_into_chunks() gwarantuje chunk <= max_chars, a slice [:14000]
        # bezszelestnie gubil nadmiar (przyczyna luki str. 6-8 w DU/2026/473 i in.)
        chunk_md.append(chunk)
        (cat_dir / f"chunk_{i:02d}.md").write_text("\n".join(chunk_md), encoding="utf-8")

    return True


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--branza", default="kadry", help="branza docelowa (domyslnie: kadry)")
    ap.add_argument("--acts", nargs="*", default=None,
                    help="lista ELI do pobrania (np. DU/1974/24/141). Jezeli pominiete - default zestaw kadrowy.")
    ap.add_argument("--version-date", default=None,
                    help="tekst ujednolicony na konkretna date (YYYY-MM-DD), np. 2026-01-27 dla KP po nowelizacji")
    args = ap.parse_args()

    repo_root = Path(__file__).resolve().parent
    branza_dir = repo_root / args.branza
    out_dir = branza_dir / "kb" / "akty-prawne"
    out_dir.mkdir(parents=True, exist_ok=True)

    acts = []
    if args.acts:
        for eli in args.acts:
            acts.append({"eli": eli, "name": f"Akt {eli}", "category": "custom"})
    else:
        acts = DEFAULT_ACTS

    log.info("Pobieram %d aktow z ISAP", len(acts))
    success = 0
    for act in acts:
        if process_act(act, args.version_date, out_dir):
            success += 1

    log.info("DONE. Pobrano %d/%d aktow do %s", success, len(acts), out_dir)


if __name__ == "__main__":
    main()
