# Prawa pracownika w RODO — art. 15-22

_Terminy, ograniczenia, procedura obsługi w HR._

## Ogólne zasady

### Termin odpowiedzi (art. 12 RODO)
- **1 miesiąc** od otrzymania wniosku
- Można przedłużyć o **kolejne 2 miesiące** jeśli sprawa skomplikowana (wtedy informujemy o przedłużeniu + powodzie w ciągu 1 mies.)
- **Bez zbędnej zwłoki** — gdy proste

### Forma odpowiedzi
- Na tej samej drodze co wniosek (mail → mail), chyba że osoba zażądała inaczej
- **Zrozumiała, jasna** — unikamy żargonu prawniczego
- **Nieodpłatna** — 1 raz; kolejne lub "nadmiarowe" mogą być za opłatę administracyjną

### Weryfikacja tożsamości
Przed udostępnieniem danych — weryfikujemy że wnioskujący = osoba, której dane dotyczą. Metody:
- Podanie dodatkowych informacji znanych tylko właścicielowi (data urodzenia, numer pracownika)
- W razie wątpliwości — **prośba o potwierdzenie tożsamości** (np. skan dokumentu)

---

## Art. 15 — Prawo dostępu

### Co daje
Pracownik może żądać:
- **Potwierdzenia, czy przetwarzamy jego dane**
- **Kopii** przetwarzanych danych
- **Informacji** o: celach, kategoriach danych, odbiorcach, okresach przechowywania, źródłach danych, zautomatyzowanych decyzjach

### Co dajemy w odpowiedzi
1. Kopia akt osobowych (części A, B, C, D — opcjonalnie części, które są istotne)
2. Kopie list płac za wskazany okres
3. Ewidencja czasu pracy
4. Nagrania monitoringu (jeśli są aktualne i dotyczą tego pracownika)
5. Informacja o tym co i komu przekazano

### Czego NIE dajemy
- Danych innych pracowników (anonimizujemy np. na listach płac zbiorczych)
- Informacji stanowiących tajemnicę przedsiębiorstwa (konkrety nie dotyczą danych tego pracownika)
- Notatek przygotowawczych / opinii managerskich niepotwierdzonych (dokumenty robocze) — ograniczenie wynikające z praktyki

### Szablon odpowiedzi
```
Szanowna/y Pani/Panie,
w odpowiedzi na wniosek z dnia [data] o udostępnienie danych osobowych,
przekazujemy:

1. Potwierdzenie: administrator przetwarza Pani/Pana dane osobowe w celach
   [wykaz].
2. Kopia akt osobowych — załącznik nr 1
3. Kopie list płac za okres [zakres] — załącznik nr 2
4. Ewidencja czasu pracy za okres [zakres] — załącznik nr 3
5. Informacja o odbiorcach danych: [lista]
6. Okresy przechowywania: [zgodnie z klauzulą informacyjną z dnia...]

Mają Państwo prawo do sprostowania, usunięcia, ograniczenia przetwarzania,
przenoszenia danych oraz skargi do UODO. W razie pytań — [kontakt].

Z poważaniem,
[Imię, stanowisko]
```

---

## Art. 16 — Prawo do sprostowania

### Co daje
Żądanie poprawienia **nieprawidłowych** danych lub uzupełnienia **niekompletnych**.

### Typowe przypadki w HR
- Zmiana adresu, numeru telefonu, nazwiska (po ślubie)
- Korekta błędu w dacie urodzenia w aktach
- Aktualizacja numeru konta
- Uzupełnienie stanu cywilnego (dla celów urlopu okolicznościowego)

### Procedura
- Termin: **1 miesiąc**
- **Sprawdzamy** czy roszczenie jest zasadne (np. przy zmianie nazwiska — dokument tożsamości)
- **Aktualizujemy** w systemach, powiadamiamy ZUS, US, bank
- **Potwierdzamy** pracownikowi wykonanie

---

## Art. 17 — Prawo do usunięcia / "bycia zapomnianym"

### Podstawy żądania
Dane **nie są już potrzebne** do celów, w jakich zostały zebrane.

### Ograniczenia w HR
**NIE możemy usunąć** danych, które jesteśmy zobowiązani przetwarzać:
- Akta osobowe — 10 lat (art. 94⁴ KP)
- Listy płac — 10 lat
- Dokumenty do ZUS, US — do upływu terminu przedawnienia

### Co robimy w praktyce
Pracownik żąda usunięcia po ustaniu zatrudnienia:
1. Usuwamy dane z systemów **aktywnych** (HRIS, ATS, maile)
2. **Zachowujemy** akta osobowe w archiwum (z ograniczonym dostępem) — do końca terminu retencji
3. Po upływie terminu retencji — trwałe usunięcie
4. Informujemy pracownika: "Częściowo zrealizowano; archiwalne dokumenty zostaną usunięte do [data]"

### Kandydat (nie zatrudniony)
Tutaj zwykle **usuwamy w pełni** po 6 miesiącach od zakończenia rekrutacji — chyba że wyraził zgodę na przyszłe.

---

## Art. 18 — Prawo do ograniczenia przetwarzania

### Kiedy
- Pracownik kwestionuje prawidłowość danych → na czas weryfikacji
- Przetwarzanie jest niezgodne z prawem, ale osoba nie chce usunięcia
- Pracodawca nie potrzebuje już danych, ale osoba żąda ich do obrony roszczeń
- Pracownik zgłosił sprzeciw → na czas rozstrzygania

### Co robimy
Oznaczamy dane jako **zablokowane** (nie przetwarzamy aktywnie, ale zachowujemy).

---

## Art. 20 — Prawo do przenoszenia danych

### Kiedy
Gdy przetwarzamy dane na podstawie **zgody** (art. 6(1)(a)) lub **umowy** (art. 6(1)(b)), i dane są przetwarzane **w sposób zautomatyzowany**.

### W HR — stosunkowo rzadko
- Przeniesienie danych z ATS jednego pracodawcy do drugiego — nie realne, bo zwykle brak wspólnego formatu
- Przeniesienie danych z karty sportowej (Multisport) — tak

### Forma
- Format strukturalny, powszechnie używany, nadający się do odczytu maszynowego (CSV, JSON, XML)

---

## Art. 21 — Prawo do sprzeciwu

### Kiedy
Przetwarzanie oparte na art. 6(1)(e) lub art. 6(1)(f) — **uzasadnionym interesie administratora**.

### W HR — typowe przypadki
- Sprzeciw wobec monitoringu **jako pracownika** — pracownik ma ograniczone możliwości (monitoring jest dozwolony w KP); sprzeciw może dotyczyć wykorzystania **konkretnego nagrania**
- Sprzeciw wobec rekrutacji pasywnej (zachowania CV na później) — pracodawca USUWA, jeśli nie ma silniejszych podstaw

### Procedura
1. Rozważamy wniosek — czy jest ważna przyczyna związana z szczególną sytuacją
2. Badamy ważenie interesów: interes pracownika vs. uzasadniony interes pracodawcy
3. Jeśli interes pracownika ważniejszy → zaprzestajemy przetwarzania
4. Jeśli nasz → wyjaśniamy na piśmie, dlaczego kontynuujemy

---

## Art. 22 — Brak decyzji opartej wyłącznie na zautomatyzowanym przetwarzaniu

### Co zabrania
**Decyzje wywołujące skutki prawne** lub **istotnie wpływające** na osobę, **oparte wyłącznie na przetwarzaniu automatycznym** (bez znaczącej interwencji człowieka).

### W HR — przykłady ryzykowne
- **AI wstępny screening CV** — OK, o ile ostateczna decyzja o zaproszeniu na rozmowę podejmuje człowiek
- **AI automatyczne wypowiedzenia** — NIEDOZWOLONE (decyzja istotna, musi być człowiek)
- **AI ocena okresowa / awans** — tylko jako wsparcie, nie jako samodzielna decyzja
- **Automatyczne blokady dostępu IT** — OK (nie decyzja kadrowa)

### Wyjątki (art. 22 ust. 2)
- Niezbędne do zawarcia lub wykonania umowy
- Dozwolone prawem
- Oparte na **wyraźnej zgodzie**

### Obowiązki administratora
- Prawo do interwencji człowieka
- Prawo do wyrażenia stanowiska
- Prawo do zakwestionowania decyzji
- **Informacja o stosowaniu** AI — w klauzuli informacyjnej

---

## Procedura obsługi wniosku RODO — krok po kroku

1. **Rejestracja wniosku** (data wpływu, forma, od kogo)
2. **Weryfikacja tożsamości**
3. **Klasyfikacja** (art. 15 / 16 / 17 / ...)
4. **Analiza** — czy zasadny, jakie ograniczenia
5. **Wykonanie** (przygotowanie kopii, usunięcie, sprostowanie)
6. **Odpowiedź** do osoby z potwierdzeniem wykonania lub odmowy z uzasadnieniem
7. **Archiwizacja** wniosku i odpowiedzi (rejestr) — 3 lata
8. **Ew. aktualizacja** procedur firmy, jeśli wniosek ujawnił problem systemowy

---

## Co jeśli odmawiamy?

Odmowa musi być:
- **Uzasadniona** (podstawa prawna, np. art. 17 ust. 3 RODO — obowiązek prawny retencji)
- **Pisemna**
- **Z pouczeniem** o prawie do skargi do UODO i sądu

**Przykład:** "Nie możemy w całości usunąć danych z akt osobowych, ponieważ jesteśmy zobowiązani do ich przechowywania przez 10 lat zgodnie z art. 94⁴ KP. Dane zostały jednak usunięte z aktywnych systemów HRIS. Po 31 grudnia 2036 r. akta zostaną całkowicie zniszczone."

## Źródła
- [RODO art. 15-22](https://eur-lex.europa.eu/legal-content/PL/TXT/?uri=CELEX%3A32016R0679)
- [UODO — poradnik w sprawie praw osób](https://uodo.gov.pl/pl/138/1204)
- [EROD — wytyczne ws. art. 22 (AI)](https://edpb.europa.eu/our-work-tools/general-guidance/guidelines-recommendations-best-practices_pl)
