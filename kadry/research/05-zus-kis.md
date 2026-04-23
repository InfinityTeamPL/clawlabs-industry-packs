# ZUS + KIS — zmiany składek i interpretacje (2026-04-22)

## 1. Tabela składek ZUS 2026

- **URL:** https://www.zus.pl/baza-wiedzy/skladki-wskazniki-odsetki/skladki/wysokosc-skladek-na-ubezpieczenia-spoleczne
- **Format:** HTML (tabela), brak JSON/CSV
- ZUS publikuje PDF komunikatów Prezesa ZUS w Monitorze Polskim

**Stawki 2026:**
- Emerytalne 19,52%
- Rentowe 8%
- Chorobowe 2,45%
- Wypadkowe 1,67% (domyślnie)
- Zdrowotne 9%

## 2. API ZUS / PUE

- **Brak publicznego REST API dla 3rd party**
- PUE ZUS — tylko web interface
- Płatnik (desktop) — SOAP via WSDL, tylko dla płatników z certyfikatem kwalifikowanym
- **KSeF** (Krajowy System e-Faktur) ma publiczne API (https://ksef.mf.gov.pl/api) — to MF, nie ZUS
- e-Składka (eskladka.pl) — tylko generator NRS, brak API
- **bip.zus.pl RSS:** https://bip.zus.pl/rss

## 3. Wyszukiwarka interpretacji KIS

- **URL:** https://eureka.mf.gov.pl/ (zastąpiła sip.mf.gov.pl)
- Parametry GET: `?q=<fraza>&dateFrom=YYYY-MM-DD&dateTo=YYYY-MM-DD&signature=<sygnatura>`
- Filtry: data wydania, sygnatura, akt prawny (PIT/CIT/VAT/Ordynacja), organ (KIS/DKIS)
- Export: HTML + PDF pojedynczej interpretacji; brak masowego API
- **RSS nowych interpretacji:** https://eureka.mf.gov.pl/rss

## 4. Kalkulatory wynagrodzeń

- **Brak oficjalnego API gov.pl** do netto/brutto
- i-zus.pl, gofin.pl, wynagrodzenia.pl, money.pl — tylko web, ToS zakazuje scrapingu
- Kalkulator na podatki.gov.pl — JS w przeglądarce, brak endpointu

## 5. Kluczowe interpretacje KIS 2025-2026 dla HR

1. **0114-KDIP3-2.4011.892.2025** — ryczałt za pracę zdalną do 5,21 zł/dzień zwolniony z PIT tylko przy udokumentowanej kalkulacji kosztów
2. **0115-KDIT2.4011.415.2025** — samochód służbowy + prywatne ładowanie EV u pracownika = przychód; pracodawca zwraca koszt prądu
3. **0113-KDIPT2-3.4011.1021.2025** — karty MultiSport z ZFŚS zwolnione z PIT do 1000 zł/rok (art. 21 ust. 1 pkt 67)
4. **0114-KDIP3-1.4011.55.2026** — PIT-0 dla młodych: premia roczna wypłacona po 26 r.ż. opodatkowana mimo że dotyczy okresu zwolnienia
5. **0112-KDIL2-1.4011.789.2025** — PPK: wpłata powitalna 250 zł i dopłaty roczne 240 zł z FP NIE są przychodem pracownika

*(sygnatury weryfikować w eureka.mf.gov.pl)*

## 6. Biblioteki

**npm:**
- `polish-tax-calculator` (unofficial, stawki hardcoded)
- `gus-regon-api` — tylko REGON
- Brak dedykowanych ZUS

**pypi:**
- `zus-api` (nieoficjalna, kalkulator składek)
- `polish-taxes`

## 7. Kalendarz rozporządzeń rocznych

| Akt | Termin | Gdzie |
|-----|--------|-------|
| Płaca minimalna | Rada Ministrów do **15 września**, Dz.U. do końca IX | dziennikustaw.gov.pl |
| Waloryzacja w roku | Druga od 2024 (styczeń + lipiec) gdy inflacja >5% | j.w. |
| Limit 30x podstawy ZUS | obwieszczenie Min. Rodziny w **grudniu** | monitorpolski.gov.pl |
| Prognozowane przeciętne wynagrodzenie | ustawa budżetowa (XI-XII), obwieszczenie GUS | M.P. |
| Min. podstawa wymiaru dla przedsiębiorców | komunikat Prezesa ZUS w **styczniu** | M.P. |
| Stawki PIT / progi | ustawa PIT, Dz.U. XI-XII, vacatio do 1.I | Dz.U. |

**Źródła ogłoszeń:** dziennikustaw.gov.pl (RSS: `/rss`), monitorpolski.gov.pl (`/rss`)
