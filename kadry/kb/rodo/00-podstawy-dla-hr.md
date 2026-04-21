# RODO dla HR — przegląd

_Rozporządzenie 2016/679 (RODO / GDPR) + polska Ustawa o ochronie danych osobowych z 10.05.2018._

## Dlaczego HR to obszar szczególnie wrażliwy

Dane kadrowe są **danymi osobowymi** (imię, PESEL, adres), często także **danymi szczególnej kategorii (art. 9 RODO)**: dane dotyczące zdrowia (zwolnienia, badania), przynależność związkowa, dane biometryczne, wyznanie (dla dni wolnych).

Naruszenia kosztują: do **20 mln euro lub 4% globalnego obrotu** (art. 83 RODO).

## Kluczowe role

| Rola | Kto u klienta |
|------|---------------|
| **Administrator danych** | Pracodawca (firma, spółka, JDG) |
| **Inspektor Ochrony Danych (IOD)** | Obowiązkowy gdy: organ publiczny; przetwarzanie na dużą skalę; systematyczny monitoring. **Dla małego pracodawcy zwykle nieobowiązkowy.** |
| **Podmiot przetwarzający** | Biuro rachunkowe, dostawcy ATS/HRIS, platforma ClawLabs (my!) — każdy wymaga **umowy powierzenia** |
| **Osoba, której dane dotyczą** | Pracownik, kandydat, były pracownik |

## 6 zasad przetwarzania (art. 5 RODO)

1. **Legalność, rzetelność, przejrzystość** — mamy podstawę prawną i informujemy o tym osoby
2. **Ograniczenie celu** — tylko do celu, dla którego zebraliśmy
3. **Minimalizacja** — tylko niezbędne dane (np. przy rekrutacji NIE pytamy o stan cywilny, plany rodzinne)
4. **Prawidłowość** — aktualność, sprostowanie błędów
5. **Ograniczenie przechowywania** — terminy retencji (patrz niżej)
6. **Integralność i poufność** — zabezpieczenia techniczne i organizacyjne

## Podstawy prawne w HR (art. 6 i art. 9 RODO)

**Szczegóły:** `rodo/podstawy-prawne-art6-art9.md`

Skrót dla Janiny:
- **Art. 6 lit. b (wykonanie umowy)** — większość czynności po zatrudnieniu (wynagrodzenie, ewidencja)
- **Art. 6 lit. c (obowiązek prawny)** — akta osobowe, ZUS, US, PIP
- **Art. 6 lit. f (uzasadniony interes)** — rekrutacja pasywna, monitoring (z ograniczeniami)
- **Art. 6 lit. a (zgoda)** — TYLKO gdy nic innego nie pasuje; łatwa do wycofania
- **Art. 9 lit. b (prawo pracy)** — dane o zdrowiu do celu oceny zdolności do pracy
- **Art. 9 lit. a (wyraźna zgoda)** — inne dane szczególne (rzadko)

## Prawa osób (art. 15-22 RODO)

**Szczegóły:** `rodo/prawa-pracownika-art15-22.md`

- **Dostęp** (art. 15) — kopia swoich danych
- **Sprostowanie** (art. 16)
- **Usunięcie** / "prawo do bycia zapomnianym" (art. 17) — ograniczone w HR przez obowiązki retencyjne
- **Ograniczenie przetwarzania** (art. 18)
- **Przenoszenie danych** (art. 20)
- **Sprzeciw** (art. 21)
- **Brak zautomatyzowanych decyzji** (art. 22) — istotne przy AI w rekrutacji!

Termin odpowiedzi: **1 miesiąc** (max. 3 mies. przy skomplikowanych sprawach).

## Obowiązki pracodawcy

### Dokumenty RODO w firmie — MUST HAVE
1. **Polityka Ochrony Danych Osobowych** (wewnętrzna)
2. **Rejestr czynności przetwarzania** (art. 30) — `rodo/rejestr-czynnosci.md`
3. **Klauzule informacyjne** (art. 13, 14) — `rodo/klauzula-rekrutacja.md`, `klauzula-zatrudnienie.md`, `klauzula-monitoring.md`
4. **Umowy powierzenia** z kontrahentami (art. 28) — biuro rachunkowe, HRIS, monitoring, etc.
5. **Analiza ryzyka** (i DPIA dla procesów wysokiego ryzyka)
6. **Procedura naruszeń** — `rodo/naruszenia-wyciek.md`
7. **Upoważnienia** do przetwarzania danych — dla pracowników HR, kadry, księgowości
8. **Rejestr upoważnień**

### Okresy retencji danych kadrowych (tryb polski)

**Pracownicy zatrudnieni od 1.01.2019** (po reformie e-akt):
- **10 lat** od końca roku kalendarzowego, w którym ustał stosunek pracy (art. 94⁴ KP)

**Pracownicy zatrudnieni przed 1.01.2019:**
- **50 lat** (stare zasady) — chyba że pracodawca przekazał ZUS kompletne dane o zarobkach i stażu (ZUS-RIA) — wtedy można skrócić do 10 lat

**Inne typy:**
- **Kandydaci** niezatrudnieni — do **6 miesięcy** po zakończeniu rekrutacji (uzasadniony interes przy roszczeniach), chyba że zgoda na rekrutacje przyszłe
- **Faktury / umowy B2B** — 5 lat od roku rozliczenia (ustawa o rachunkowości)
- **Zlecenia i dzieła** — okres przedawnienia + termin retencji podatkowej (5 lat)
- **Monitoring wizyjny** — max. 3 miesiące (chyba że dowód w postępowaniu)

## 10 zasad Janiny (codzienna praktyka)

1. **Zbieram tylko to czego potrzebuję** — CV ma wystarczyć, nie żądam aktów urodzenia bez potrzeby
2. **Pokazuję klauzulę informacyjną** przy każdym zbieraniu danych
3. **Nie wysyłam danych osobowych na prywatne maile** pracowników (@gmail itp.) — tylko firmowe lub pisemnie
4. **Sprawdzam umowy powierzenia** przed udostępnieniem danych kontrahentowi
5. **Ograniczam dostęp** — tylko osoby z upoważnieniem
6. **Anonymizuję wszędzie gdzie mogę** — np. lista urodzin na ścianie tylko imię/miesiąc, nie pełna data
7. **Ninchronizuję usuwanie** — gdy kończy się termin retencji, kasuję
8. **Sygnalizuję naruszenie** w ciągu 24h — do IOD / prawnika / UODO jeśli wysokie ryzyko
9. **Dokumentuję wszystko** — rejestr, audyt, ślad
10. **Aktualizuję się** — wytyczne UODO zmieniają się, orzecznictwo też

## Źródła
- [RODO — pełny tekst PL](https://eur-lex.europa.eu/legal-content/PL/TXT/?uri=CELEX%3A32016R0679)
- [Ustawa o ochronie danych osobowych 10.05.2018](https://isap.sejm.gov.pl/isap.nsf/DocDetails.xsp?id=WDU20180001000)
- [UODO — strona główna](https://uodo.gov.pl)
- [UODO — wytyczne](https://uodo.gov.pl/pl/file/)
