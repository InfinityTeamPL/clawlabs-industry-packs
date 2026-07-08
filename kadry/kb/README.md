# Baza wiedzy Janiny Kadrowej

_Stan: 2026-07-08. Rok 2026._

## Co to jest

Robocza baza wiedzy dla agentki AI **Janina Kadrowa**. Pliki ładowane są do `memory/` na VM-ce agenta i służą jako kontekst przy odpowiadaniu klientowi. Nie zastępują prawnika, radcy, ani księgowej — to opracowania praktyczne oparte na oficjalnych źródłach z linkami do pełnych tekstów.

## Zawartość

```
kadry/
├── README.md                      # ten plik
├── aktualizacje-2026.md           # co się zmieniło w 2026 i co dalej śledzimy (CZYTAJ PIERWSZE)
├── kalendarz-2026.md              # święta, wymiar czasu pracy, terminy kadrowe
├── reforma-pip-2026.md            # PIP przekształca B2B w etat (od 8.07.2026)
├── l4-kontrole-zus-2026.md        # nowe zasady L4 i kontroli ZUS (od 13.04.2026)
├── kontrola-pip-checklist.md      # jak przygotować się do kontroli PIP
├── cudzoziemcy-zatrudnienie.md    # zatrudnianie cudzoziemców (nowa ustawa od 1.06.2025)
├── rynek-pracy-sluzby-zatrudnienia-2025.md  # nowa ustawa od 1.06.2025 (promocja zatrudnienia UCHYLONA)
├── zfss.md                        # Zakładowy Fundusz Świadczeń Socjalnych (odpis 2026, kryterium socjalne)
├── niepelnosprawni-pfron.md       # zatrudnianie osób niepełnosprawnych, SODiR, wpłaty PFRON
├── odpowiedzialnosc-zakaz-konkurencji.md  # odpowiedzialność materialna + zakaz konkurencji
├── slownik-skrotow.md             # skróty kadrowe
├── kodeks-pracy/                  # KP — działy, kluczowe artykuły, praktyka
│   ├── 08-jawnosc-plac-2026.md    #   etap I obowiązuje od 24.12.2025; luka płacowa ~2027
│   ├── 09-staz-pracy-2026.md      #   art. 302¹ KP — JDG/zlecenia w stażu
│   ├── 10-e-wnioski-ekwiwalent-2026.md  # e-wnioski + art. 171 §4 KP (od 27.01.2026)
│   ├── 11-uklady-zbiorowe-2025.md #   dział XI KP UCHYLONY → odrębna ustawa
│   └── 12-ochrona-sygnalistow.md  #   ustawa o sygnalistach (Dz.U. 2024 poz. 928, od 25.09.2024)
├── procedury/                     # kary-porzadkowe.md, zwolnienia-grupowe.md
├── rodo/                          # RODO dla HR — podstawy prawne + klauzule
├── wzory-umow/                    # szablony umów i pism kadrowych
├── wynagrodzenia/                 # płaca minimalna, składki, potrącenia; zasilki-zus-2026, przyklady-wyliczen, oskladkowanie-zlecen-fakty
├── bhp/                           # szkolenia, badania, wypadki, kontrola-trzezwosci
├── urlopy/                        # wymiar, naliczanie, rodzaje
├── checklisty/                    # onboarding/offboarding/rekrutacja/audyt
└── akty-prawne/custom/            # pełne teksty ustaw (chunki + _overview.md z regułą IN_FORCE)
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
- Kompletna baza orzecznictwa — mamy WYBRANE, zweryfikowane tezy SN dla najczęstszych sporów w `orzecznictwo/` (sygnatury sprawdzone w saos.org.pl/sn.pl) + `interpretacje/jak-korzystac.md` (ZUS/KIS/PIP, szare strefy). Poza tym zakresem Janina szuka w LEX/SAOS i NIE zmyśla sygnatur
- Prawo pracy państw obcych — Janina pracuje na polskim prawie; dla obcokrajowców w PL tak, ale dla Polaków za granicą kieruje do lokalnych specjalistów

## Status wypełnienia (8.07.2026)

- [x] **Audyt aktualności 8.07.2026** — 8 zmian prawa obowiązujących w 2025/2026 wgranych: reforma PIP (473), jawność etap I (807), staż art. 302¹ (1423), e-wnioski/ekwiwalent (25), układy zbiorowe (1661), L4/ZUS (26), minimalna (1242), cudzoziemcy (621) + wpisy anty-halucynacyjne (luka płacowa ~2027, oskładkowanie zleceń porzucone)
- [x] **Pełny audyt KB 8.07.2026 (11 agentów) + naprawy** — poprawki P0/P1: terminy odwołania 21 dni (art. 264 KP), współczynnik ekwiwalentu 20,92, limit 30-krotności 282 600, kwoty wolne od potrąceń netto, PPK 1,5%, świadectwo pracy (pola 2023), RODO zakaz pytania o zarobki, BHP instruktaż 3h + kontrola trzeźwości, mobbing (status noweli), niedziele handlowe 2026. Nowe notatki: kontrola trzeźwości, sygnaliści, ustawa o rynku pracy, uzupełniający urlop macierzyński (wcześniaki), świadczenie rodzicielskie, zasiłki ZUS 2026 + zasiłek pogrzebowy 7000 zł, przykłady wyliczeń, ZFŚS, PFRON, kary porządkowe, zwolnienia grupowe, odpowiedzialność materialna/zakaz konkurencji. Nowe akty: 1871 (wcześniaki), 620 (rynek pracy), 718 (pogrzebowy), 570 (zwolnienia grupowe)
- [x] **Baza orzecznictwa SN + interpretacji (differentiator vs LEX/INFORLEX)** — `orzecznictwo/` (**75 zweryfikowanych tez SN w 12 tematach**: ustalenie stosunku pracy/B2B, wypowiedzenie/utrata zaufania, art. 52, czas pracy/nadgodziny, mobbing, odpowiedzialność/zakaz konkurencji, urlopy, uprawnienia rodzicielskie, równe traktowanie/dyskryminacja płacowa, przejście zakładu pracy art. 23¹, wynagrodzenie/premie/potrącenia, monitoring/dane — każda sygnatura sprawdzona osobno w saos.org.pl/sn.pl, halucynacje odrzucone) + `interpretacje/jak-korzystac.md` (ZUS/KIS/PIP + szare strefy)
- [x] **Rozbudowa wzorów pism/dokumentów (flagowa funkcja PDF)** — `wzory-umow/` + `procedury/`: informacja o warunkach zatrudnienia (art. 29 §3), wypowiedzenie zmieniające (art. 42), kara porządkowa + protokół wysłuchania, skierowanie na badania, zaświadczenie o zatrudnieniu i zarobkach, zgoda na potrącenie (art. 91), umowa o zakazie konkurencji, umowa o odpowiedzialności materialnej, wnioski urlopowe (6 rodzajów), PPK rezygnacja/deklaracje, regulamin pracy zdalnej, porozumienie zmieniające
- [x] **Notatka `wynagrodzenia/ryczalt-praca-zdalna.md`** (art. 67²⁵ KP + interpretacje ZUS/KIS zweryfikowane)

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
