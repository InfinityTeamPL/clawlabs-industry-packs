---
dataset_id: 7
file: Instrukcja_pobierania_podmiot%C3%B3w_prowadz%C4%85cych_agencje_zatrudnienia_z_KRAZ.pdf
file_size_mb: 0.2
institution: "Ministerstwo Rodziny, Pracy i Polityki Społecznej"
data_date: 2025-01-03
freshness: fresh
source_url: http://stor.praca.gov.pl/portal/#/kraz
---

# Instrukcja_pobierania_podmiot%C3%B3w_prowadz%C4%85cych_agencje_zatrudnienia_z_KRAZ.pdf

_(z datasetu: Rejestr Podmiotów Prowadzących Agencje Zatrudnienia)_

**Stron:** 12

**Treść PDF (pierwsze 20 stron, max 5000 znaków):**

 
 
 
 
 
Instrukcja pobierania podmiotów 
prowadzących agencje zatrudnienia 
z KRAZ  
  

Instrukcja pobierania podmiotów prowadzących agencje zatrudnienia z KRAZ 
 __________________________________________________________________________________________________________________  
 
  Strona: 2 z 12 
 
 
Spis treści 
1. Podstawowe informacje o API_KRAZ .............................................................................................. 3 
1.1. Usługa zwracająca dane agencji zatrudnienia ......................................................................... 3 
1.2. Usługa zwracająca dane słownikowe ...................................................................................... 6 
2. Komunikacja z API_KRAZ ................................................................................................................. 8 
2.1. Mechanizm uwierzytelniania .................................................................................................. 8 
2.2. Limit liczby wywołań usług API_KRAZ ..................................................................................... 8 
3. Specyfikacja techniczna usług ......................................................................................................... 8 
 
  

Instrukcja pobierania podmiotów prowadzących agencje zatrudnienia z KRAZ 
 __________________________________________________________________________________________________________________  
 
  Strona: 3 z 12 
 
 
1. Podstawowe informacje o API_KRAZ 
API_KRAZ służy do pobierania przez zainteresowane podmioty informacji z Rejestru Podmiotów 
Prowadzących Agencje Zatrudnienia utrzymywanego przez Ministerstwo Rodziny i Polityki Społecznej. 
Poszczególne rejestry prowadzone są przez wojewódzkie urzędy pracy na mocy  ustawy z dnia 20 
kwietnia 2004r. o promocji zatrudnienia i instytucjach rynku pracy oraz rozporządzenia Ministra 
Rodziny, Pracy i Polityki Społecznej z dnia 25 maja 2017 r. w sprawie wzorów dokumentów dotyczących 
działalności agencji zatrudnienia. 
API_KRAZ umożliwia pobranie informacji publicznych gromadzonych w rejestrze poprzez następujące 
usługi: 
a) usługa pobrania pełnego zakresu aktualnie obowiązujących informacji o agencjach 
zatrudnienia znajdujących się w Rejestrze Podmiotów Prowadzących Agencje Zatrudnienia 
i świadczonych przez nie usługach, 
b) usługi zwracające wersję oraz zawartość słowników wykorzystywanych w KRAZ. 
API_KRAZ wykonane jest w technologii usług RESTful i jest dostępne pod adresem: 
https://storapi.praca.gov.pl/api_kraz. 
 
1.1. Usługa zwracająca dane agencji zatrudnienia 
Usługa umożliwia pobranie danych agencji zatrudnienia wpisanych do Rejestru Podmiotów 
Prowadzących Agencje Zatrudnienia udostępnia informacje o  agencjach aktywnych i zawieszonych 
w rejestrze KRAZ z określonym rodzajem prowadzonej działalności. W przypadku, gdy w ramach 
warunków wyszukiwania zosta nie wysłane zapytanie o agencję niespełniającą tych warunków, np . 
wykreśloną z rejestru, usługa zwróci brak danych. 
 
Usługa dostępna jest pod adresem https://storapi.praca.gov.pl/api_kraz/agencje-zatrudnienia 
Usługa przyjmuje w ramach parametrów wejściowych następujące dane: 
I) Parametry wyszukiwania danych instytucji szkoleniowych w KRAZ: 
a. nazwa agencji (kryterium: nazwaAgencji),  
b. numer w rejestrze (kryterium: numerWRejestrze), 
c. agencja prowadząca działalność z zakresu pośrednictwa pracy, doradztwa personalnego, 
poradnictwa zawodowego (kryterium: czyPosrednictwoPracyIInne), 
d. agencja prowadząca działalność z zakresu pracy tymczasowej (kryterium: 
czyPracaTymczasowa), 
e. NIP agencji (kryterium: nip) 
f. data wpisu agencji do rejestru, w kryterium można podać jedną lub dwie daty, wyszukiwane 
są wpisy które odbyły się w określonym przedziale czasu (kryterium: dataWpisuOd, 
dataWpisuDo), 
g. miejsce siedziby agencji (kryterium: miejsceSiedzibyAgencji): 
− kod województwa (wartość ze słownika województw - kodWojewodztwa) 
− kod powiatu (wartość ze słownika powiatów - kodPowiatu) 
− kod gminy (wartość ze słownika gmin - kodGminy) 

Instrukcja pobierania podmiotów prowadzących agencje zatrudnienia z KRAZ 
 __________________________________________________________________________________________________________________  
 
  Strona: 4 z 12 
 
 
− kod miejscowości (wartość ze słownika miejscowości - kodMiejscowosci) 
− kod kraju (wartość ze słownika krajów - kodKraju) 
h. miejsce prowadzonej działalności przez agencję (kryterium: miejsceProwadzeniaDzialalnosci): 
− kod województwa (wartość ze słownika województw - kodWojewodztwa) 
− kod powiatu (wartość ze słownika powiatów - kodPowiatu) 
− kod gminy (wartość ze słownika gmin - kodGminy) 
− kod miejscowości (wartość ze słownika miejscowości - kodMiejscowosci) 
i. kod pocztowy z adresu siedziby agencji w formacie 99-999 (kryterium: kodPocztowy) 
j. kod formy prawnej agencji (kryterium: kodFormyPrawnej) (wartość ze słownika form 
prawnych) 
k. agencja, która w poprzednim roku świadczyła usługi z zak

---
_Plik źródłowy: `data/raw/7/Instrukcja_pobierania_podmiot%C3%B3w_prowadz%C4%85cych_agencje_zatrudnienia_z_KRAZ.pdf` (0.2 MB) · Pobrane z http://stor.praca.gov.pl/portal/#/kraz_