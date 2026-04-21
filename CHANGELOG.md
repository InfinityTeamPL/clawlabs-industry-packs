# Changelog

Wszystkie istotne zmiany w paczkach branżowych. Format: [Keep a Changelog](https://keepachangelog.com/pl/1.1.0/).

---

## [Unreleased]

### kadry
- (in progress) testowanie Janiny na żywej VM — iteracje SOUL/IDENTITY/KB po rozmowach testowych

---

## [kadry/0.1.0] — 2026-04-21

Pierwsze wdrożenie paczki kadrowej. Janina Kadrowa powstała przez transformację agenta "Neo" admina (fb0313cc-0e05-4459-9d0c-bf16b80a132c) na ClawLabs PRO.

### Added
- 36 plików KB, 328 KB:
  - `kodeks-pracy/` — 9 plików (rodzaje umów, rozwiązanie, czas pracy, urlopy, uprawnienia rodzicielskie, BHP, mobbing, jawność płac 2026, staż pracy 2026)
  - `rodo/` — 7 plików (podstawy, art. 6/9, klauzule rekrutacja/zatrudnienie/monitoring, prawa art. 15-22, rejestr art. 30, naruszenia art. 33-34)
  - `wzory-umow/` — 7 plików (UoP próba/nieokreślona, zlecenie, B2B, wypowiedzenie, porozumienie, świadectwo pracy)
  - `wynagrodzenia/` — 2 pliki (płaca minimalna 2026 = 4 806 zł, składniki/potrącenia)
  - `bhp/` — 2 pliki (szkolenia terminy, badania lekarskie)
  - `urlopy/` — 2 pliki (wymiar/naliczanie, rodzaje)
  - `checklisty/` — 4 pliki (onboarding, offboarding, rekrutacja, audyt kadrowy)
  - `aktualizacje-2026.md` — zmiany 2026: staż pracy, jawność płac (dyrektywa 2023/970), ekwiwalent urlopowy, elektronizacja dokumentów, mobbing
  - `README.md` — jak korzystać z bazy, źródła, disclaimery

### Kluczowe dane 2026 w KB
- Płaca minimalna: 4 806 zł brutto / ~3 605 netto
- Stawka godzinowa (zlecenie): 31,40 zł brutto / ~25,36 netto
- Ekwiwalent urlopowy: wypłata do 25 maja (zmiana z "niezwłocznie")
- Staż pracy: od 1.05.2026 wliczają się zlecenia, JDG, praca za granicą
- Jawność płac: implementacja dyrektywy 2023/970 do 7.06.2026

### Source
- Treści zbudowane z oficjalnych źródeł: ISAP, EUR-Lex, gov.pl, UODO, PIP, ZUS
- Dane 2026 potwierdzone web searchem (biznes.gov.pl, PIP Gdańsk/Białystok, Infor.pl) 2026-04-21

### Status
- Wgrane na żywą VM Janiny (IP 204.168.188.45) do `/root/agent/openclaw/workspace/memory/kadry/`
- Skille zainstalowane: 8/13 (5 brakuje w ClawHub — pdf-reader, email-drafter, knowledge-base, translator, url-reader)
- **Nie snapshotowane** — Janina w fazie trenowania, snapshot po walidacji u admina

### Known issues
- Kwoty ZUS, diety, ryczałty KM — placeholdery "sprawdź aktualną wartość" (zmienne w ciągu roku)
- Projekt ustawy antymobbingowej (min. odszkodowanie 6× min) — status legislacyjny do aktualizacji
- Niedziele handlowe 2026 — kalendarz do uzupełnienia per rok
