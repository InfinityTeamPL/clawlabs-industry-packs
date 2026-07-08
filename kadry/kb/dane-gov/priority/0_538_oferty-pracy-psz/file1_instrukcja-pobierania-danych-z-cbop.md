---
dataset_id: 538
file: instrukcja_pobierania_danych_z_cbop.pdf
file_size_mb: 0.42
institution: "Ministerstwo Rodziny, Pracy i Polityki Społecznej"
data_date: 2024-12-23
freshness: fresh
source_url: https://oferty.praca.gov.pl/portal/index.cbop#/listaOfert
---

# instrukcja_pobierania_danych_z_cbop.pdf

_(z datasetu: Oferty pracy PSZ)_

**Stron:** 24

**Treść PDF (pierwsze 20 stron, max 5000 znaków):**

 
Strona 1 z 24 
 
 
 
 
 
 
 
 
 
 
 
 
Instrukcja pobierania ofert pracy z CBOP 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
Warszawa, 30 listopada 2020 r. 

 
Strona 2 z 24 
 
1. Opis funkcjonalności 
W systemie teleinformatycznym  Centralna Baza Ofert Pracy ( CBOP) dostępna jest usługa 
umożliwiająca pobranie ofert pracy przez systemy zewnętrzne. URL do usługi wygląda 
następująco: 
URL do WebService: http://oferty.praca.gov.pl/integration/services/oferta 
URL do WSDL: http://oferty.praca.gov.pl/integration/services/oferta?wsdl 
 
W nowej wersji usługi, dostępnej od 20 marca 2020  r., która umożliwia pobranie ofert pracy dla 
wybranego języka, URL ma postać: 
URL do WebService: http://oferty.praca.gov.pl/integration/services/v2/oferta 
URL do WSDL: http://oferty.praca.gov.pl/integration/services/v2/oferta?wsdl 
 
Obydwie powyższe usługi są dostępne.  
 
Odpytywanie CBOP przez systemy zewnętrzne  jest możliwe do wykonania  za pośrednictwem 
usługi W ebService. Oferty pracy udostępniane są jako odpowiedź z serwera w postaci 
spakowanych plików JSON.  
Nazwy plików *.zip nie zawierają polskich znaków, znak  '/' jest zamieniany na znak  '_'. W 
przypadku kodów placówek, do nazwy będzie dołączany rok, miesiąc dzień i godzina pobrania 
pliku. Przykładowo: 
• plik pobrany dla placówki 02140 o godzinie 18 :48 dnia 13 .06.2018 r. będzie miał nazwę: 
02140_2018_06_13_18_48.zip 
• plik pobrany  dla województwa dolnośląskiego o kodzie 02 o godzini e 19 :48 dnia 
13.06.2018 r. będzie miał nazwę:  02_2018_06_13_19_48.zip 
• plik pobrany dla wszystkich województw o godzinie 20 :48 dnia 13 .06.2018 r. będzie miał 
nazwę: wszystkie_2018_06_13_20_48.zip i będzie się składał z 1 plik u zip z zawartością 
podzieloną na województwa. 
 
1.1. Przykładowe wywołania 
Pobranie danych województwa opolskiego (kod 16) dla języka angielskiego (kod en) w nowej 
wersji usługi: 
<soapenv:Envelope xmlns:soapenv="http://schemas.xmlsoap.org/soap/envelope/" 
xmlns:ofer="http://oferty.praca.gov.pl/v2/oferta"> 
   <soapenv:Header/> 

 
Strona 3 z 24 
 
   <soapenv:Body> 
      <ofer:Dane> 
         <pytanie> 
            <Partner>test</Partner> 
<Jezyk>en</Jezyk> 
            <Kryterium> 
               <Wojewodztwo>16</Wojewodztwo>   
 </Kryterium> 
         </pytanie> 
      </ofer:Dane> 
   </soapenv:Body> 
</soapenv:Envelope> 
 
Pobranie danych Powiatowego Urzędu Pracy w Puławach (06140) – wersja usługi bez wersji 
językowej: 
<soapenv:Envelope xmlns:soapenv="http://schemas.xmlsoap.org/soap/envelope/" 
xmlns:ofer="http://oferty.praca.gov.pl/oferta"> 
   <soapenv:Header/> 
   <soapenv:Body> 
      <ofer:Dane> 
         <pytanie> 
            <Partner>test</Partner> 
            <Kryterium> 
               <Jednostka>06140</Jednostka>   
 </Kryterium> 
         </pytanie> 
      </ofer:Dane> 
   </soapenv:Body> 
</soapenv:Envelope> 
 
Pobranie wszystkich aktywnych ofert pracy – wersja usługi bez wersji językowej: 
<soapenv:Envelope xmlns:soapenv="http://schemas.xmlsoap.org/soap/envelope/" 
xmlns:ofer="http://oferty.praca.gov.pl/oferta"> 
   <soapenv:Header/> 
   <soapenv:Body> 
      <ofer:Dane> 
         <pytanie> 
            <Partner>test</Partner> 
            <Kryterium> 
               <Wszystkie>true</Wszystkie> 
            </Kryterium> 

 
Strona 4 z 24 
 
         </pytanie> 
      </ofer:Dane> 
   </soapenv:Body> 
</soapenv:Envelope> 
 
W sekcji <Partner> </Partner> należy podać nazwę przypisaną do Podmiotu pobierającego dane 
z CBOP. 
W sekcji <Jezyk> </Jezyk> należy podać kod języka (dotyczy nowej wersji usługi). W artość 'en' 
oznacza, że uprawniony Podmiot  pobiera aktywne oferty przetłumaczone na język angielski z 
CBOP. Kod języka oferty może przyjmować wartości: 
• pl – polski 
• ru – rosyjski 
• by – białoruski 
• en – angielski 
• ua – ukraiński 
 
W kryterium <Wojewodztwo></Wojewodztwo> należy podać kod województwa, dla którego 
pobierane są oferty. Kody województw wykazane są w punkcie 1.2 Lista kodów województw. 
W kryterium <Jednostka></Jednostka> należy podać kod jednostki zasilającej  (tj. urzędu pracy), 
dla której pobierane są oferty. Kody jednostek zasilających wykazane są w punkcie 1.3 Lista 
kodów jednostek zasilających. 
W kryterium <Wszystkie> </Wszystkie> wartość 'true' oznacza, że uprawniony Podmiot pobiera 
wszystkie aktywne oferty z CBOP. 
 
Walidacje: 
• w sekcji <Partner> </Partner> należy wprowadzić nazwę Podmiotu pobierającego dane z 
CBOP zdefiniowaną przez MRPiT, w przeciwnym razie zwrócony zostanie komunikat błędu 
"Niepoprawna autoryzacja", 
• należy uzupełnić jedno z kryteriów : Województwo, Jednostka lub Wszystkie. W przypadku 
niewypełnienia żadnego z ww. kryteriów lub wprowadzenia więcej niż jednej wartości , 
zwrócony zostanie błąd walidacji WSDL. 
• dla nowej wersji usługi można wybrać język, np. ‘<Jezyk>en</Jezyk>’.  
 
W odpowiedzi zwracane są: 
• spakowana zipem lista plików *.json , zawierających listę ofert w paczkach maksymalnie po 
1000 ofert, 
• data wygenerowania pliku, 

 
Strona 5 z 2

---
_Plik źródłowy: `data/raw/538/instrukcja_pobierania_danych_z_cbop.pdf` (0.42 MB) · Pobrane z https://oferty.praca.gov.pl/portal/index.cbop#/listaOfert_