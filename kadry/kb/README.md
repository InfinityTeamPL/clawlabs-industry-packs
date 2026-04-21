# Baza wiedzy Janiny Kadrowej

_Stan: 2026-04-21. Rok 2026._

## Co to jest

Robocza baza wiedzy dla agentki AI **Janina Kadrowa**. Pliki ładowane są do `memory/` na VM-ce agenta i służą jako kontekst przy odpowiadaniu klientowi. Nie zastępują prawnika, radcy, ani księgowej — to opracowania praktyczne oparte na oficjalnych źródłach z linkami do pełnych tekstów.

## Zawartość

```
kadry/
├── README.md                      # ten plik
├── aktualizacje-2026.md           # co się zmieniło w 2026 i co dalej śledzimy
├── kodeks-pracy/                  # KP — działy, kluczowe artykuły, praktyka
├── rodo/                          # RODO dla HR — podstawy prawne + klauzule
├── wzory-umow/                    # szablony umów i pism kadrowych
├── wynagrodzenia/                 # płaca minimalna, składki, potrącenia
├── bhp/                           # szkolenia, badania, wypadki
├── urlopy/                        # wymiar, naliczanie, rodzaje
└── checklisty/                    # onboarding/offboarding/rekrutacja/audyt
```

## Źródła (używamy tylko oficjalnych)

- **ISAP Sejm** — pełny tekst aktów: <https://isap.sejm.gov.pl>
- **Kodeks Pracy** — Dz.U. 1974 Nr 24 poz. 141 ze zm. <https://isap.sejm.gov.pl/isap.nsf/DocDetails.xsp?id=WDU19740240141>
- **RODO** — Rozporządzenie 2016/679. <https://eur-lex.europa.eu/legal-content/PL/TXT/?uri=CELEX%3A32016R0679>
- **Ustawa o minimalnym wynagrodzeniu** — Dz.U. 2002 Nr 200 poz. 1679. <https://isap.sejm.gov.pl/isap.nsf/DocDetails.xsp?id=WDU20022001679>
- **PIP** — Państwowa Inspekcja Pracy. <https://www.pip.gov.pl>
- **Ministerstwo Rodziny, Pracy i Polityki Społecznej** — <https://www.gov.pl/web/rodzina>
- **Biznes.gov.pl** — poradniki urzędowe. <https://www.biznes.gov.pl>
- **UODO** — Urząd Ochrony Danych Osobowych. <https://uodo.gov.pl>
- **ZUS** — składki, świadczenia. <https://www.zus.pl>

## Disclaimer (Janina musi to rozumieć)

> **Te materiały są opracowaniem roboczym, nie poradą prawną.** Dla konkretnej sprawy klienta Janina przedstawia opcje, wskazuje podstawę prawną, ale ostateczna decyzja należy do człowieka. W sprawach spornych (sądowych, mobbingowych, dyskryminacji, roszczeń) Janina kieruje do radcy prawnego. W sprawach podatkowo-księgowych (listy płac, deklaracje) — do biura rachunkowego.
>
> Prawo zmienia się — każdą kwotę i każdy paragraf sprawdzamy w dniu użycia w ISAP lub na stronach urzędowych.

## Jak Janina korzysta z tej bazy

1. **Zawsze czyta najpierw** `aktualizacje-2026.md` przy starcie nowej rozmowy — żeby mieć aktualny kontekst zmian roku
2. **Przed odpowiedzią na pytanie prawne** — szuka po kluczowym terminie w odpowiednim folderze (np. "okres wypowiedzenia" → `kodeks-pracy/02-rozwiazanie-umowy.md`)
3. **Przed wygenerowaniem dokumentu** — szuka wzoru w `wzory-umow/` i adaptuje do danych klienta; nie zmyśla klauzul
4. **Gdy dane się nie zgadzają / przekracza swoją wiedzę** — jasno mówi "sprawdź u radcy prawnego" + wskazuje źródło ISAP
5. **Cytując kwoty (płaca min., składki)** — zawsze dodaje rok: "płaca minimalna 2026 = 4806 zł brutto" — nigdy bez daty

## Co NIE jest w tej bazie (świadomie)

- Gotowe listy płac ani wyliczenia podatku — to robi księgowa
- Specyfika branż regulowanych (medycyna, transport, budownictwo) — to dodatkowe bazy per-klient
- Orzecznictwo — za krótko żyjemy. Janina szuka w LEX/Legalis tylko gdy klient wyraźnie prosi
- Prawo pracy państw obcych — Janina pracuje na polskim prawie; dla obcokrajowców w PL tak, ale dla Polaków za granicą kieruje do lokalnych specjalistów

## Status wypełnienia (21.04.2026)

- [x] Struktura plików
- [x] Zmiany 2026
- [x] Kodeks Pracy — rodzaje umów, rozwiązanie, czas pracy, urlopy, rodzicielskie, BHP, mobbing, jawność płac, staż
- [x] RODO — podstawy, klauzule, prawa osób, rejestr, naruszenia
- [x] Wzory umów — UoP, zlecenie, B2B, wypowiedzenia, świadectwo pracy
- [x] Wynagrodzenia — płaca minimalna, składniki, potrącenia
- [x] BHP — szkolenia, badania
- [x] Urlopy — wymiar, rodzaje
- [x] Checklisty — onboarding, offboarding, rekrutacja, audyt
- [ ] Specyficzne branżowe (dodajemy per klient)
- [ ] Aktualizacja co kwartał (cron na PIP/ISAP — do zbudowania)
