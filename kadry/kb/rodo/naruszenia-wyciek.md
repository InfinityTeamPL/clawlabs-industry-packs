# Naruszenia ochrony danych — wyciek, zaginięcie, nieuprawniony dostęp

_Art. 33 i 34 RODO. Stan: 2026._

## Co to jest naruszenie

**Art. 4 pkt 12 RODO:** Naruszenie prowadzące do **przypadkowego lub niezgodnego z prawem**:
- **Zniszczenia** (np. pożar w archiwum)
- **Utraty** (zgubiony laptop, USB, teczka z aktami)
- **Zmiany** (nieautoryzowana zmiana danych)
- **Nieuprawnionego ujawnienia** (wysłanie maila nie tej osobie, kradzież bazy)
- **Nieuprawnionego dostępu** (logowanie do konta bez zgody, włamanie hackerskie)

**W HR typowe przypadki:**
- Wysłanie listy płac wszystkim zamiast księgowej
- Kradzież / zgubienie laptopa z danymi pracowników
- Włamanie do systemu HRIS
- Ujawnienie CV kandydata osobie trzeciej
- Nieautoryzowany dostęp kadrowca do akt innych pracowników
- Phishing / ransomware

---

## Procedura — w 72 godziny

### Krok 1: Wykrycie i reakcja natychmiastowa (T=0)
1. **Zatrzymaj wyciek** — odłącz system od sieci, cofnij mail (jeśli możliwe), zablokuj konto
2. **Zabezpiecz dowody** — logi, screenshoty, kopia incydentu
3. **Powiadom zespół reagowania** — IT, HR, IOD / prawnik, zarząd
4. **Załóż rejestr incydentu** — data/czas wykrycia, opis, osoby powiadomione

### Krok 2: Ocena (T+1h do T+24h)
1. **Co się wyciekło** — jakie dane, ile osób, jakie kategorie
2. **Jak długo** — kiedy zaczęło się, kiedy wykryto, co w międzyczasie
3. **Skutki** — dla osób (ryzyko kradzieży tożsamości, dyskryminacji, strat finansowych, zdrowotnych)
4. **Klasyfikacja ryzyka** — niskie / wysokie / bardzo wysokie

### Krok 3: Decyzja o zgłoszeniu (T+24h do T+72h)
Zgodnie z art. 33 i 34 RODO:

| Ryzyko dla osób | Zgłoszenie UODO (art. 33) | Informacja osobom (art. 34) |
|-----------------|---------------------------|------------------------------|
| **Brak** (mało prawdopodobne ryzyko) | ❌ NIE zgłaszamy | ❌ NIE informujemy |
| **Niskie** (możliwe drobne problemy) | ✅ TAK — w 72h | ❌ NIE (chyba że UODO nakaże) |
| **Wysokie** (istotne zagrożenie) | ✅ TAK — w 72h | ✅ TAK — bez zbędnej zwłoki |

**Wszystko dokumentujemy** — nawet incydenty niezgłoszone (art. 33 ust. 5).

### Krok 4: Zgłoszenie do UODO (art. 33 RODO)

**Termin:** **72 godziny** od **powzięcia wiadomości**. Przekroczenie → wyjaśnienie opóźnienia.

**Forma:** formularz online na [uodo.gov.pl](https://uodo.gov.pl) — zakładka "Zgłoś naruszenie".

**Zawiera:**
- Charakter naruszenia (kategorie i liczba osób, kategorie danych)
- Dane kontaktowe IOD lub innej osoby w firmie
- Możliwe konsekwencje
- Środki podjęte lub proponowane do podjęcia
- Uzasadnienie ewentualnego opóźnienia

### Krok 5: Informacja dla osób, których dane dotyczą (art. 34 RODO)

**Kiedy:** przy **wysokim ryzyku** dla osób.

**Forma:**
- **Bezpośrednia** — mail / SMS / list (indywidualnie)
- **Publiczna** — ogłoszenie, jeśli koszt niewspółmierny lub niemożliwy indywidualny kontakt

**Zawiera:**
- Charakter naruszenia (język prostym, nie urzędowym)
- Dane kontaktowe IOD
- Możliwe konsekwencje
- Środki podjęte i rekomendacje dla osoby (np. zmiana hasła, kontrola kont bankowych)

### Krok 6: Następstwa (T+72h i dalej)
1. **Analiza przyczyn** (root cause analysis)
2. **Plan naprawczy** — co zmienić w procedurach/systemach
3. **Dokumentacja** w rejestrze naruszeń (art. 33 ust. 5)
4. **Współpraca z UODO** — ewentualne wyjaśnienia, audyt
5. **Ewentualne roszczenia** ze strony osób poszkodowanych

---

## Przykłady klasyfikacji ryzyka

### Niskie ryzyko (zgłaszamy UODO, nie informujemy osób)
- Mail z niepełnymi danymi (tylko imię i adres mail) wysłany pod zły adres
- Kradzież dokumentu który i tak jest publicznie dostępny
- Pomyłka w komunikacji wewnętrznej (imię+nazwisko widziane przez nieuprawnionego kolegę)

### Wysokie ryzyko (pełna procedura z art. 34)
- Wyciek listy płac z PESEL, wysokością wynagrodzeń → kradzież tożsamości, roszczenia
- Wyciek orzeczeń lekarskich → ryzyko dyskryminacji, naruszenia prywatności
- Kradzież całej bazy pracowniczej → bardzo wysokie ryzyko wielokierunkowe
- Ransomware z wyciekiem danych → wymuszanie, kradzież tożsamości

---

## Rejestr naruszeń (art. 33 ust. 5 RODO)

Każda firma prowadzi wewnętrzny rejestr (niezależnie od zgłoszenia do UODO):

| Pole | Wartość |
|------|---------|
| **Numer sprawy** | 001/2026 |
| **Data wykrycia** | 2026-04-15 |
| **Data zdarzenia** | 2026-04-14 (noc) |
| **Opis** | Kradzież laptopa z biura, zawierał dane 42 pracowników |
| **Kategorie danych** | Dane identyfikacyjne, PESEL, wynagrodzenia |
| **Kategorie osób** | Pracownicy (42 osoby) |
| **Ryzyko (niskie/wysokie)** | Wysokie |
| **Zgłoszenie UODO** | Tak, nr 123/2026 z 2026-04-17 |
| **Informacja dla osób** | Tak, mail + rozmowa z każdą osobą |
| **Środki naprawcze** | Pełne szyfrowanie dysków (wdrożone 2026-04-20), polityka zabezpieczania sprzętu, szkolenie |
| **Status** | Zamknięte 2026-05-10 |

**Retencja rejestru:** co najmniej 3 lata, zalecane 5 lat.

---

## Co robimy my (ClawLabs / Janina) przy własnym naruszeniu

Janina jest **podmiotem przetwarzającym** (art. 28 RODO) dla klienta. Jeśli **na naszej stronie** (platforma, VM, systemy) dochodzi do naruszenia:

1. **Powiadamiamy klienta (administratora) bez zbędnej zwłoki** — dyscyplinarnie do 24h (nasza wewnętrzna polityka)
2. **Przekazujemy informacje** potrzebne klientowi do wypełnienia obowiązków z art. 33 i 34
3. **Współpracujemy** przy analizie i usuwaniu skutków

**To klient zgłasza do UODO**, nie my. Ale my dostarczamy mu wszystko co potrzebne.

---

## Najczęstsze błędy pracodawców

1. **Opóźnienie zgłoszenia** — "poczekajmy aż wszystko będzie jasne" → 72h lecą od WYKRYCIA, nie od wyjaśnienia
2. **Nie zgłaszamy bo nie chcemy pokazać wstydu** → **kary wzrastają drastycznie** gdy UODO się dowie z innej drogi
3. **Nie informujemy osób** licząc że się nie dowiedzą → problem wraca z nawiązką
4. **Brak procedur** — cała reakcja ad hoc, bez planu
5. **Brak szkoleń dla pracowników** — kto wie, że trzeba zgłosić? Co zrobić jak znajdzie zgubionego laptopa?
6. **Brak testów** — procedura działa na papierze; w praktyce chaos

---

## Mini-plan komunikacji wewnętrznej

### W regulaminie / polityce bezpieczeństwa
> "Każdy pracownik, który podejrzewa naruszenie ochrony danych (zgubiony dokument, niezabezpieczone dane, dziwne maile, nietypowe zachowanie systemu) ma OBOWIĄZEK niezwłocznie zgłosić to na adres **iod@[firma].pl** lub bezpośrednio do kierownika. Zgłoszenie nie naraża pracownika na negatywne konsekwencje."

### Szkolenie roczne (20 min)
- Przykłady naruszeń (case study)
- Jak zgłosić (kanały, kontakty)
- Co zrobić do czasu reakcji specjalisty (zabezpieczyć, odłączyć, nie kasować)

## Źródła
- [RODO art. 33-34](https://eur-lex.europa.eu/legal-content/PL/TXT/?uri=CELEX%3A32016R0679)
- [UODO — zgłoszenie naruszenia](https://uodo.gov.pl/pl/134/1029)
- [EROD — wytyczne ws. zgłaszania naruszeń](https://edpb.europa.eu/our-work-tools/general-guidance/guidelines-recommendations-best-practices_pl)
