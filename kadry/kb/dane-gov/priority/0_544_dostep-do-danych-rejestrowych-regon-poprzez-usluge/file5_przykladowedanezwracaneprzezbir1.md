---
dataset_id: 544
file: PrzykladoweDaneZwracanePrzezBIR1.txt
file_size_mb: 0.02
institution: "Główny Urząd Statystyczny"
data_date: 2025-01-02
freshness: fresh
source_url: https://api.stat.gov.pl
---

# PrzykladoweDaneZwracanePrzezBIR1.txt

_(z datasetu: Dostęp do danych rejestrowych REGON poprzez usługę sieciową – interfejsy API)_


Przykładowe dane zwracene przez metodę DaneSzukaj oraz raporty metody DanePobierzPelnyRaport

================================================================================  
Metoda DaneSzukaj - jednorazowo zwraca maks. 100 wpisów (rekordów)

  <dane>
    <Regon>111111111</Regon>
	<!-- UWAGA: prosze ignorowac pole RegonLink; to nie jest pole dla uslugi BIR1 -->
    <RegonLink>&lt;a href='javascript:danePobierzPelnyRaport("11111111100000","DaneRaportFizycznaPubl", 1);'&gt;001331220&lt;/a&gt;</RegonLink>
    <Nazwa>NazwaFirmy</Nazwa>
    <Wojewodztwo>PODKARPACKIE</Wojewodztwo>
    <Powiat>NazwaPowiatu</Powiat>
    <Gmina>NazwaGminy</Gmina>
    <Miejscowosc>NazwaMiejscowosci</Miejscowosc>
    <KodPocztowy>99-999</KodPocztowy>
    <Typ>F</Typ>
    <SilosID>1</SilosID>
  </dane>
  
  <!-- opcjonalnie: dane o kolejnych rodzajach dzialalności gospodarczej podmiotu (tzw. silosach) -->
  <dane>
    <Regon>111111111</Regon>
    <RegonLink>&lt;a href='javascript:danePobierzPelnyRaport("11111111100000","DaneRaportFizycznaPubl", 2);'&gt;001331220&lt;/a&gt;</RegonLink>
    <Nazwa>GOSPODARSTWO ROLNE</Nazwa>
    <Wojewodztwo>PODKARPACKIE</Wojewodztwo>
    <Powiat>NazwaPowiatu</Powiat>
    <Gmina>NazwaGminy</Gmina>
    <Miejscowosc>NazwaMiejscowosci</Miejscowosc>
    <KodPocztowy>99-999</KodPocztowy>
    <Typ>F</Typ>
    <SilosID>2</SilosID>
  </dane>
  
  <!-- opcjonalnie: dane o kolejnych podmiotach -->
  <dane>
    <Regon>222222222</Regon>
    ....
    <SilosID>1</SilosID>
  </dane>
================================================================================  
================================================================================  
================================================================================  

RAPORTY metody DanePobierzPelnyRaport (opis - str.11 "Instrukcji")

PublDaneRaportTypJednostki
  <dane>
    <Typ>P</Typ>
  </dane>
  lub 
  <dane>
    <Typ>F</Typ>
  </dane>
  lub
  <dane>
    <Typ>LP</Typ>
  </dane>
  lub
  <dane>
    <Typ>LF</Typ>
  </dane>  

================================================================================  
PublDaneRaportPrawna

<dane>
    <praw_regon14>00033150100000</praw_regon14>
    <praw_nip>5261040828</praw_nip>
    <praw_nazwa>GŁÓWNY URZĄD STATYSTYCZNY</praw_nazwa>
    <praw_nazwaSkrocona>GUS</praw_nazwaSkrocona>
    <praw_numerWrejestrzeEwidencji />
	<praw_dataWpisuDoRejestruEwidencji>1975-12-15</praw_dataWpisuDoRejestruEwidencji>
    <praw_dataPowstania>1975-12-15</praw_dataPowstania>
    <praw_dataRozpoczeciaDzialalnosci>1975-12-15</praw_dataRozpoczeciaDzialalnosci>
    <praw_dataWpisuDoREGON />
    <praw_dataZawieszeniaDzialalnosci />
    <praw_dataWznowieniaDzialalnosci />
    <praw_dataZaistnieniaZmiany>2009-02-20</praw_dataZaistnieniaZmiany>
    <praw_dataZakonczeniaDzialalnosci />
    <praw_dataSkresleniazRegon />
    <praw_adSiedzKraj_Symbol>PL</praw_adSiedzKraj_Symbol>
    <praw_adSiedzWojewodztwo_Symbol>14</praw_adSiedzWojewodztwo_Symbol>
    <praw_adSiedzPowiat_Symbol>65</praw_adSiedzPowiat_Symbol>
    <praw_adSiedzGmina_Symbol>108</praw_adSiedzGmina_Symbol>
    <praw_adSiedzKodPocztowy>00925</praw_adSiedzKodPocztowy>
    <praw_adSiedzMiejscowoscPoczty_Symbol>0919810</praw_adSiedzMiejscowoscPoczty_Symbol>
    <praw_adSiedzMiejscowosc_Symbol>0919810</praw_adSiedzMiejscowosc_Symbol>
    <praw_adSiedzUlica_Symbol>14199</praw_adSiedzUlica_Symbol>
    <praw_adSiedzNumerNieruchomosci>208</praw_adSiedzNumerNieruchomosci>
    <praw_adSiedzNumerLokalu />
    <praw_adSiedzNietypoweMiejsceLokalizacji />
    <praw_numerTelefonu>6083000</praw_numerTelefonu>
    <praw_numerWewnetrznyTelefonu />
    <praw_numerFaksu>0226083863</praw_numerFaksu>
    <praw_adresEmail>dgsek@stat.gov.pl</praw_adresEmail>
    <praw_adresStronyinternetowej>www.stat.gov.pl</praw_adresStronyinternetowej>
    <praw_adresEmail2 />
    <praw_adSiedzKraj_Nazwa>POLSKA</praw_adSiedzKraj_Nazwa>
    <praw_adSiedzWojewodztwo_Nazwa>MAZOWIECKIE</praw_adSiedzWojewodztwo_Nazwa>
    <praw_adSiedzPowiat_Nazwa>m. st. Warszawa</praw_adSiedzPowiat_Nazwa>
    <praw_adSiedzGmina_Nazwa>Śródmieście</praw_adSiedzGmina_Nazwa>
    <praw_adSiedzMiejscowosc_Nazwa>Warszawa</praw_adSiedzMiejscowosc_Nazwa>
    <praw_adSiedzMiejscowoscPoczty_Nazwa>Warszawa</praw_adSiedzMiejscowoscPoczty_Nazwa>
    <praw_adSiedzUlica_Nazwa>al.Niepodległości</praw_adSiedzUlica_Nazwa>
    <praw_podstawowaFormaPrawna_Symbol>2</praw_podstawowaFormaPrawna_Symbol>
    <praw_szczegolnaFormaPrawna_Symbol>01</praw_szczegolnaFormaPrawna_Symbol>
    <praw_formaFinansowania_Symbol>2</praw_formaFinansowania_Symbol>
    <praw_formaWlasnosci_Symbol>111</praw_formaWlasnosci_Symbol>
    <praw_organZalozycielski_Symbol>050000000</praw_organZalozycielski_Symbol>
    <praw_organRejestrowy_Symbol />
    <praw_rodzajRejestruEwidencji_Symbol>000</praw_rodzajRejestruEwidencji_Symbol>
    <praw_podstawowaFormaPrawna_Nazwa>JEDNOSTKA ORGANIZACYJNA NIEMAJĄCA OSOBOWOŚCI PRAWNEJ</praw_podstawowaFormaPrawna_Nazwa>
    <praw_szczegolnaFormaPrawna_Nazwa>ORGAN

---
_Plik źródłowy: `data/raw/544/PrzykladoweDaneZwracanePrzezBIR1.txt` (0.02 MB) · Pobrane z https://api.stat.gov.pl_