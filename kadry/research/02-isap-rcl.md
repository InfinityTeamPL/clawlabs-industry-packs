# Monitoring prawa — ISAP / RCL / Sejm / EUR-Lex

## 1. Oficjalne API (bez klucza, rate ~5 req/s bezpiecznie)

**ISAP (Sejm) — OpenAPI**
- Base: https://api.sejm.gov.pl/eli/openapi/
- Akt: `GET /eli/acts/{publisher}/{year}/{position}`
- Zmiany (nowelizacje): `GET /eli/acts/{publisher}/{year}/{position}/references`
- Wyszukiwanie: `GET /eli/acts/search?keyword=kodeks+pracy&pubDateFrom=2026-01-01`
- RSS: brak; polling po `publishDate`

**RCL — Dziennik Ustaw / Monitor Polski**
- API: https://api.dziennikustaw.gov.pl/, https://api.monitorpolski.gov.pl/
- Lista pozycji: `GET /du/{year}` → JSON (`pos`, `title`, `date`)
- PDF aktu: `GET /du/{year}/{position}/text.pdf`

**RCL — projekty (konsultacje)**
- Brak oficjalnego API
- RSS: https://legislacja.rcl.gov.pl/rss/projekty (wszystkie, filtr po stronie klienta)
- HTML: `/projekty` + `/projekt/{id}`

**Sejm — proces legislacyjny**
- API: https://api.sejm.gov.pl/sejm/openapi/
- Druki: `GET /sejm/term{N}/prints`
- Głosowania: `GET /sejm/term{N}/votings/{sitting}`

**Senat** — https://api-senat.senat.gov.pl/ (OpenAPI)

**EUR-Lex**
- REST CELLAR: https://api.publications.europa.eu/ (bez klucza, ~100 req/min)
- SPARQL: https://publications.europa.eu/webapi/rdf/sparql
- SOAP Web Service: https://eur-lex.europa.eu/EURLexWebService (wymaga rejestracji)
- RSS per temat: https://eur-lex.europa.eu/EN/display-feed.rss?myRssId=... (konfigurowalny po "Employment law", "Data protection")

**NSA/SN** — scraping HTML
- orzeczenia.nsa.gov.pl — parametr `?q=` + paginacja
- sn.pl/orzecznictwo — RSS SharePoint

**MRPiPS** — https://www.gov.pl/web/rodzina/rss.xml (komunikaty, projekty rozporządzeń)

**UODO** — https://uodo.gov.pl/pl/feed (decyzje, komunikaty RODO)

## 2. Przykład response JSON (ISAP)

```json
{
  "ELI": "DU/2026/123",
  "title": "Ustawa o zmianie ustawy — Kodeks pracy",
  "publishDate": "2026-03-15",
  "changes": [{"act": "DU/1974/24/141", "type": "amends"}]
}
```

## 3. Strategia monitoringu art. 36 KP

1. Cron dziennie: `GET api.sejm.gov.pl/eli/acts/DU/1974/24/141/references?changesSince=YYYY-MM-DD`
2. Polling RCL RSS + filtr po `/kodeks pracy|art\.?\s*36/i`
3. Sejm druki: `GET /sejm/term10/prints` → filtr `title` po "Kodeks pracy"
4. Diff tekstu jednolitego: `GET /eli/acts/DU/1974/24/141/text.html` + porównywanie wersji (`versions` endpoint)

## 4. Biblioteki

**npm:** `rss-parser`, `fast-xml-parser`, `node-fetch`, `cheerio` (scraping NSA/SN), `eur-lex-client` (nieoficjalna), `diff-match-patch`

**pypi:** `feedparser`, `lxml`, `requests`, `eurlex` (SOAP wrapper), `sejm-api` (nieoficjalny), `beautifulsoup4`, `scrapy`

## 5. Pokrycie tematyczne

- ISAP + dziennikustaw/monitorpolski: tylko ogłoszone akty
- RCL legislacja: projekty + OSR + konsultacje
- Sejm/Senat API: proces legislacyjny (druki, poprawki, głosowania)
- EUR-Lex: dyrektywy UE + projekty COM
- orzeczenia.nsa / sn.pl: orzecznictwo
- UODO feed: decyzje + wytyczne RODO
