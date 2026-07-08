---
dataset_id: 345
file: Instrukcja_pobierania_instytucji_szkoleniowych_z_RIS.pdf
file_size_mb: 0.28
institution: "Ministerstwo Rodziny, Pracy i Polityki Społecznej"
data_date: 2025-01-03
freshness: fresh
source_url: http://stor.praca.gov.pl/portal/#/ris
---

# Instrukcja_pobierania_instytucji_szkoleniowych_z_RIS.pdf

_(z datasetu: Rejestr Instytucji Szkoleniowych)_

**Stron:** 18

**Treść PDF (pierwsze 20 stron, max 5000 znaków):**

 
 
 
 
 
Instrukcja pobierania instytucji 
szkoleniowych z RIS  
 
 
 
 
 
 
 
 
 
 
Data opracowania 24.03.2021  

Spis treści 
1. Podstawowe informacje o API_RIS ................................................................................................. 3 
1.1. Usługa zwracająca dane instytucji szkoleniowych .................................................................. 3 
1.2. Usługa zwracająca dane szkoleń ............................................................................................. 6 
2.3. Usługa zwracająca dane przygotowań zawodowych .............................................................. 8 
2.4. Usługa zwracająca dane słownikowe .................................................................................... 10 
2. Komunikacja z API_RIS .................................................................................................................. 12 
2.1. Mechanizm uwierzytelniania ................................................................................................ 12 
2.2. Limit liczby wywołań usług API_RIS ....................................................................................... 12 
3. Specyfikacja techniczna usług ....................................................................................................... 12 
 
  

1. Podstawowe informacje o API_RIS 
API_RIS służy do pobierania przez zainteresowane podmioty informacji z Rejestru Instytucji 
Szkoleniowych (RIS) utrzymywanego przez Ministerstwo Rozwoju, Pracy i Technologii. Poszczególne 
rejestry prowadzone są przez wojewódzkie urzędy pracy na mocy Rozporządzenie Ministra 
Gospodarki i Pracy z dnia 27 października 2004 r. w sprawie rejestru instytucji szkoleniowych. 
API_RIS umożliwia pobranie informacji publicznych gromadzonych w rejestrze poprzez następujące 
usługi: 
a) usługa zwracająca dane instytucji szkoleniowych wpisanych do Rejestru Instytucji 
Szkoleniowych oraz informacji o świadczonych przez nie usługach, 
b) usługa zwracająca informacje o szkoleniach prowadzonych przez instytucje szkoleniowe i 
ich oddziały, 
c) usługa zwracająca dane o programach przygotowania zawodowego dorosłych 
realizowanych przez instytucje szkoleniowe wpisane do RIS. 
d) usługi zwracające wersję oraz zawartość słowników wykorzystywanych w RIS. 
API_RIS wykonane jest w technologii usług RESTful i jest dostępne pod adresem: 
https://storapi.praca.gov.pl/api_ris. 
 
1.1. Usługa zwracająca dane instytucji szkoleniowych 
Usługa umożliwia pobranie danych instytucji szkoleniowych wpisanych do Rejestru Instytucji 
Szkoleniowych oraz informacji o świadczonych przez nie usługach udostępnia informacje o 
instytucjach aktywnych w rejestrze RIS. W przypadku, gdy w ramach warunków wyszukiwania 
zostanie wysłane zapytanie o instytucję wykreśloną z rejestru, usługa zwróci brak danych. 
Usługa dostępna jest pod adresem https://storapi.praca.gov.pl/api_ris/instytucje-szkoleniowe 
Usługa przyjmuje w ramach parametrów wejściowych następujące dane: 
I) Parametry wyszukiwania danych instytucji szkoleniowych w RIS: 
a. nazwa instytucji szkoleniowej lub oddziału (kryterium: nazwaInstytucji)  
b. numer w rejestrze / numer ewidencyjny instytucji szkoleniowej (kryterium: 
numerWRejestrze) 
c. numer REGON instytucji szkoleniowej (kryterium: regon) 
d. numer NIP instytucji szkoleniowej (kryterium: nip) 
e. informacja o tym, jakiego rodzaju ma być wyszukiwany obiekt (kryterium:    
rodzajWyszukiwanegoObiektu): 
- czy mają być wyszukiwane tylko instytucje szkoleniowe (obejmuje oddziały będące 
siedzibą główną – wartość Instytucja) 
- czy wyszukiwanie ma obejmować tylko filie i oddziały instytucji szkoleniowych (oddziały 
nie będące siedzibą główną instytucji szkoleniowej – wartość Oddzial) 
- czy wyszukiwane mają być wszystkie obiekty – wartość Wszystkie lub brak kryterium 
wyszukiwania 
f. miejsce prowadzonej działalności przez instytucję lub oddział: 
- kod województwa (wartość ze słownika województw) - kryterium: 
miejsceDzialalnosci.kodWojewodztwa 
- kod powiatu (wartość ze słownika powiatów) - kryterium: 
miejsceDzialalnosci.kodPowiatu 

- kod gminy (wartość ze słownika gmin) - kryterium: miejsceDzialalnosci.kodGminy 
- kod miejscowości (wartość ze słownika miejscowości) - kryterium: 
miejsceDzialalnosci.kodMiejscowosci 
g. nazwa szkolenia prowadzonego przez instytucję szkoleniową lub jeden z jej oddziałów 
(kryterium: nazwaSzkolenia) 
h. nazwa programu przygotowania zawodowego dorosłych prowadzonego przez instytucję 
szkoleniową lub jeden z jej oddziałów (kryterium: nazwaPZD) 
i. kod obszaru szkolenia (wartość ze słownika obszarów szkoleń; kryterium: 
kodObszaruSzkolenia) 
j. rok wpisania instytucji szkoleniowej do rejestru (kryterium: rokWpisu) 
k. data wpisu instytucji szkoleniowej do rejestru, w kryterium można podać jedną lub dwie 
daty, wyszukiwane są wpisy które odbyły się w określonym przedziale czasu (kryterium: 
dataWpisuOd, dataWpisuDo) – datę należy wpisać w formacie rrrr-mm-dd 
l. kod pocztowy z adr

---
_Plik źródłowy: `data/raw/345/Instrukcja_pobierania_instytucji_szkoleniowych_z_RIS.pdf` (0.28 MB) · Pobrane z http://stor.praca.gov.pl/portal/#/ris_