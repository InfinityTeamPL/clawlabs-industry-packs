# Rejestr czynności przetwarzania — art. 30 RODO

_Dokument obowiązkowy dla firm zatrudniających pracowników (niezależnie od wielkości, jeśli przetwarzają dane szczególnej kategorii — a HR przetwarza)._

## Kiedy obowiązek

Art. 30 RODO — rejestr prowadzą:
- **Wszystkie firmy** zatrudniające ≥ 250 pracowników
- **Firmy < 250** — gdy przetwarzanie:
  - Nie ma charakteru sporadycznego, **LUB**
  - Obejmuje **dane szczególnej kategorii** (art. 9), **LUB**
  - Może powodować ryzyko naruszenia praw osób

**HR zawsze mieści się w którejś z kategorii (dane o zdrowiu), więc rejestr jest OBOWIĄZKOWY dla każdego pracodawcy.**

## Co zawiera (art. 30 ust. 1)

Dla każdej czynności przetwarzania:

1. **Nazwa i dane kontaktowe administratora** (oraz IOD, jeśli powołany)
2. **Cele przetwarzania**
3. **Kategorie osób** (np. pracownicy, kandydaci, byli pracownicy)
4. **Kategorie danych osobowych** (dane identyfikacyjne, dane o zdrowiu, itp.)
5. **Kategorie odbiorców** — w tym państw trzecich
6. **Planowane terminy usunięcia**
7. **Ogólny opis środków bezpieczeństwa** (art. 32)

## Forma

- **Pisemna** (papier lub elektroniczna)
- **Dostępna na żądanie UODO**
- **Aktualizacja** przy każdej zmianie (nowy system, nowy kontrahent, nowy cel)

---

## Wzór rejestru — typowe czynności w HR

### Czynność 1 — Rekrutacja

| Pole | Wartość |
|------|---------|
| **Cel** | Przeprowadzenie procesu rekrutacji, selekcja kandydatów |
| **Podstawa prawna** | art. 6(1)(b) RODO (działania przed zawarciem umowy); art. 22¹ KP |
| **Kategorie osób** | Kandydaci do pracy |
| **Kategorie danych** | Imię, nazwisko, dane kontaktowe, wykształcenie, doświadczenie, umiejętności |
| **Odbiorcy** | Dostawca ATS: [nazwa]; dostawca hostingu poczty: [Google / Microsoft]; doradcy rekrutacyjni |
| **Państwa trzecie** | USA (Google Workspace — Data Privacy Framework) |
| **Termin retencji** | 6 miesięcy po zakończeniu rekrutacji (chyba że zgoda na przyszłe: 24 mies.) |
| **Środki bezpieczeństwa** | Kontrola dostępu (role i uprawnienia w ATS), szyfrowanie bazy, backupy, audyty dostępów |

### Czynność 2 — Zawarcie i wykonanie umowy o pracę

| Pole | Wartość |
|------|---------|
| **Cel** | Zawarcie umowy, wypłata wynagrodzenia, rozliczenia podatkowo-składkowe, ewidencja czasu pracy |
| **Podstawa prawna** | art. 6(1)(b), art. 6(1)(c) RODO; KP, ustawa o systemie ubezpieczeń społecznych, ustawa o PIT |
| **Kategorie osób** | Pracownicy |
| **Kategorie danych** | Imię, nazwisko, PESEL, adres, dane kontaktowe, dane rodziny (do ulg), numer konta bankowego, dane o wykształceniu, przebieg zatrudnienia |
| **Odbiorcy** | Biuro rachunkowe: [nazwa]; bank; ZUS; US; HRIS: [nazwa]; PPK operator: [nazwa] |
| **Państwa trzecie** | [jak dla rekrutacji lub nie dotyczy] |
| **Termin retencji** | 10 lat po ustaniu zatrudnienia (art. 94⁴ KP, jeśli zatrudniony od 1.01.2019) |
| **Środki bezpieczeństwa** | Szyfrowanie bazy, kontrola dostępu, archiwizacja na nośnikach szyfrowanych, akta papierowe w zamykanych szafach |

### Czynność 3 — Dane o zdrowiu pracowników (zwolnienia, badania)

| Pole | Wartość |
|------|---------|
| **Cel** | Realizacja obowiązków z zakresu prawa pracy (zwolnienia, zasiłki, BHP, medycyna pracy) |
| **Podstawa prawna** | art. 6(1)(c) + art. 9(2)(b) RODO (prawo pracy); art. 229 KP |
| **Kategorie osób** | Pracownicy |
| **Kategorie danych** | Orzeczenia lekarskie (zdolny/niezdolny), fakt zwolnienia lekarskiego (bez diagnozy), orzeczenia o niepełnosprawności |
| **Odbiorcy** | ZUS; medycyna pracy (przetwarzają jako oddzielny administrator); biuro rachunkowe (przy rozliczaniu zasiłków) |
| **Państwa trzecie** | Zwykle: nie |
| **Termin retencji** | 10 lat (jak akta osobowe) |
| **Środki bezpieczeństwa** | Ograniczony dostęp (tylko HR + księgowa), osobne pliki w aktach (część B), hasło na plikach elektronicznych |

### Czynność 4 — Monitoring wizyjny

| Pole | Wartość |
|------|---------|
| **Cel** | Bezpieczeństwo, ochrona mienia, kontrola produkcji |
| **Podstawa prawna** | art. 22² § 1 KP + art. 6(1)(c), art. 6(1)(f) RODO |
| **Kategorie osób** | Pracownicy, klienci, osoby wchodzące na teren zakładu |
| **Kategorie danych** | Wizerunek |
| **Odbiorcy** | Dostawca systemu monitoringu: [nazwa]; organy państwowe na żądanie |
| **Państwa trzecie** | — |
| **Termin retencji** | Max 3 miesiące (nadpisywanie w systemie) |
| **Środki bezpieczeństwa** | Ograniczony dostęp do nagrań, logowanie dostępów, zabezpieczenie serwerów |

### Czynność 5 — Benefity pozapłacowe

| Pole | Wartość |
|------|---------|
| **Cel** | Obsługa pakietów medycznych, sportowych, ubezpieczeń grupowych |
| **Podstawa prawna** | art. 6(1)(a) RODO (zgoda pracownika) lub art. 6(1)(b) jeśli w umowie |
| **Kategorie osób** | Pracownicy + członkowie rodzin (jeśli objęci) |
| **Kategorie danych** | Imię, nazwisko, PESEL, data urodzenia, adres |
| **Odbiorcy** | Operator benefitów: [nazwa]; ubezpieczyciel: [nazwa] |
| **Państwa trzecie** | zazwyczaj nie |
| **Termin retencji** | Do końca świadczenia benefitu + termin przedawnienia roszczeń (6 lat) |
| **Środki bezpieczeństwa** | Umowa powierzenia z operatorami |

### Czynność 6 — Monitoring poczty i narzędzi IT

| Pole | Wartość |
|------|---------|
| **Cel** | Zapewnienie właściwego wykorzystania czasu pracy, ochrona przed wyciekami |
| **Podstawa prawna** | art. 22³ KP + art. 6(1)(f) RODO |
| **Kategorie osób** | Pracownicy |
| **Kategorie danych** | Logi, treści korespondencji służbowej, ruch sieciowy |
| **Odbiorcy** | Administrator IT wewnętrzny; dostawca SIEM/DLP: [nazwa] |
| **Państwa trzecie** | [zależy od dostawcy] |
| **Termin retencji** | [ustalić — zwykle do 12 miesięcy logów] |
| **Środki bezpieczeństwa** | Szyfrowanie, kontrola dostępu, logowanie audytowe |

### Czynność 7 — Archiwum akt osobowych byłych pracowników

| Pole | Wartość |
|------|---------|
| **Cel** | Wywiązanie się z obowiązku ustawowego (art. 94⁴ KP) |
| **Podstawa prawna** | art. 6(1)(c) RODO + KP |
| **Kategorie osób** | Byli pracownicy |
| **Kategorie danych** | Pełne akta osobowe (A, B, C, D) |
| **Odbiorcy** | ZUS, US, komornik (na żądanie) |
| **Państwa trzecie** | — |
| **Termin retencji** | 10 lat po ustaniu zatrudnienia (lub 50 lat dla starszych) |
| **Środki bezpieczeństwa** | Archiwum fizyczne (zamknięte), archiwum elektroniczne (szyfrowane), ograniczony dostęp |

---

## Rejestr kategorii czynności przetwarzania — gdy jesteśmy procesorem (art. 30 ust. 2)

**Dotyczy** jeśli firma przetwarza dane **na zlecenie innego administratora** (np. agencja HR dla klienta, biuro rachunkowe). **Rzadko dotyczy typowej firmy-pracodawcy.** Jeśli jednak:

- Nazwa administratora (za kogo przetwarzamy)
- Kategorie przetwarzań
- Przekazywanie do państw trzecich
- Ogólny opis środków bezpieczeństwa

---

## Narzędzia do prowadzenia rejestru

### Minimum (dobrze dla małych firm)
- **Arkusz kalkulacyjny** (Excel / Google Sheets) z zakładkami per czynność
- Kopia bezpieczeństwa, kontrola wersji
- Przegląd co 6-12 mies.

### Dla średnich/dużych
- Dedykowane narzędzia GDPR (OneTrust, BigID, Exterro, Netwrix, lokalne rozwiązania typu Kadromierz ZPO)
- Automatyczny import listy systemów, kontrahentów
- Alerty o zmianach

---

## Częste błędy

1. **Ogólnikowe opisy** — "przetwarzamy dane HR" → niewystarczające; trzeba precyzyjnie
2. **Brak aktualizacji** — firma dodała nowy system ATS, a w rejestrze stary
3. **Brak odbiorców państw trzecich** — zapomnieliśmy o Google, Microsoft, innych SaaS z USA
4. **Przesadnie krótka retencja** — pracodawca podaje 3 lata, a KP wymaga 10
5. **Brak środków bezpieczeństwa** — pole puste lub "backup" to za mało

## Źródła
- [RODO art. 30](https://eur-lex.europa.eu/legal-content/PL/TXT/?uri=CELEX%3A32016R0679)
- [UODO — wzory rejestru](https://uodo.gov.pl/pl/123/215)
