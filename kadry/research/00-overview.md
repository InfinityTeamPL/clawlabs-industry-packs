# Research — rozbudowa Janiny Kadrowej (2026-04-22)

8 równoległych subagentów, zakres: źródła danych + integracje + OpenClaw capabilities.

## Pliki

1. `01-portale-hr.md` — polskie portale HR (RSS/sitemap/scrape)
2. `02-isap-rcl.md` — oficjalne źródła prawne (ISAP, RCL, Sejm API)
3. `03-uodo-erod.md` — RODO dla HR (UODO, EROD, decyzje)
4. `04-pip.md` — PIP: kontrole, komunikaty, zmiany 2026
5. `05-zus-kis.md` — ZUS + interpretacje KIS
6. `06-openclaw.md` — OpenClaw 2026 features dla HR agenta
7. `07-hr-tech-api.md` — polskie HRIS/ATS z API
8. `08-e-podpis.md` — e-podpis umów o pracę PL + eIDAS 2

## Co jest surowymi danymi

Każdy plik zawiera wyłącznie **fakty, URL-e, dane liczbowe** zebrane przez subagentów z weryfikowalnych źródeł. Brak wniosków, hipotez, SWOT, rekomendacji. Decyzje kierunkowe — osobno, po zapoznaniu się z danymi.

## Status weryfikacji

Agenci używali WebFetch i sprawdzali HTTP status feed-ów (np. `https://legalis.pl/feed/` → 200, pobiera XML z itemami). Gdzie źródło jest 404 lub wymaga logowania, jest to oznaczone w raporcie.
