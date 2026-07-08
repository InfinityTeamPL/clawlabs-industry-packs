---
dataset_id: 747
file: InstrukcjaTerytWs1.pdf
file_size_mb: 0.95
institution: "Główny Urząd Statystyczny"
data_date: 2024-03-19
freshness: fresh
source_url: https://api.stat.gov.pl/
---

# InstrukcjaTerytWs1.pdf

_(z datasetu: Dostęp do danych rejestrowych TERYT poprzez usługę sieciową - interfejsy API)_

**Stron:** 27

**Treść PDF (pierwsze 20 stron, max 5000 znaków):**

 
1 
 
Instrukcja techniczna usługi TERYT ws1 2015 
 
 
  Usługa TERYT ws1 
udostępniająca dane z rejestru TERYT 
 
Instrukcja techniczna. 
 
2015 
Tomasz Gębka 
Centrum Informatyki Statystycznej 
2014-10-24 

 
2 
 
Instrukcja techniczna usługi TERYT ws1 2015 
Metryka dokumentu 
Nazwa projektu TERYT 
Tytuł dokumentu Instrukcja techniczna usługi TERYT ws1  
Zakres dokumentu  
Data utworzenia dokumentu: 2014-08-19 Liczba stron: 27 
Plik (repozytorium)  
Zespół realizacyjny  
Opis  
 
Historia dokumentu 
Nr wersji Data wersji Zmiany 
wprowadził 
Opis Uwagi 
0.01 19.08.2014 Marcin Piekarek Spis treści  
0.02 18.09.2014 Tomasz Gębka Dodano informacje o metodach usługi ws1, dodano 
uaktualnione informacje o strukturach plików XML. 
 
0.03 24.09.2014 Tomasz Gębka Wprowadzono informacje o podstawie prawnej 
udostępniani danych , uaktualniono zbiór metod oraz 
poprawiono opis.  Dodano informacje o logowaniu i 
uzyskiwaniu dostępu do usługi. 
 
0.04 9.10.2014 Tomasz Gębka Uaktualniono listę i opis metod.   
0.05 21.10.2014 Tomasz Gębka Uaktualniono dokument.  
0.06 24.10.2014 Tomasz Gębka Uaktualniono dokument.  
0.07 09.12.2014 Tomasz Gębka Uaktualniono dokument.  
0.08 22.01.2015 Tomasz Gębka Uaktualniono dokument.  
0.09 02.03.2015 Tomasz Gębka Uaktualniono dokument.  
0.1 22.08.2016 Tomasz Gębka Uaktualniono dokument.  
  

 
3 
 
Instrukcja techniczna usługi TERYT ws1 2015 
1. Podstawowe informacje o usłudze .................................................................................. 4 
2. Komunikacja z usługą ..................................................................................................... 4 
2.1. Interfejs programistyczny usługi Teryt ws1 ................................................................ 4 
3. Procedura integracji z usługą Teryt ws1 ....................................................................... 22 
3.1. Integracja ze środowiskiem testowym ................................................................... 22 
3.2. Integracja ze środowiskiem produkcyjnym ........................................................... 22 
3.3. Mechanizm uwierzytelniania ..................................................................................... 22 
4. Zakres udostępnianych danych i podstawa prawna ...................................................... 23 
5. Regulamin korzystania z usługi .................................................................................... 24 
6. Gwarancja jakości usług ................................................................................................ 26 
  

 
4 
 
Instrukcja techniczna usługi TERYT ws1 2015 
1. Podstawowe informacje o usłudze 
 Rejestr TERYT gromadzi aktualne i archiwalne dane dotyczące obiektów 
terytorialnych takich jak : jednostki podziału terytorialnego, jedno stki podziału 
statystycznego, miejscowości, ulice. Jest on rejestrem re ferencyjnym w zakresie 
identyfikatorów w stosunku do innych rejestrów i ewidencji urzędowych i systemów 
administracji publicznej. Tworzona usługa sieciowa ws1 w prosty sposób zapewni ła twy 
dostęp do danych re jestru użytkownikom systemu. Udostępnia ona interfejs 
programistyczny – zbiór metod, dzięki którym możliwe jest pobieranie danych  z rejestru 
TERYT bezpośrednio do  systemów komunikujących się z rejestrem . Zasadniczą 
funkcjonalnością u sługi jest udostępnianie danych osobom fizycznym, podmiotom 
komercyjnym oraz uprawnionym instytucjom publicznym.  
2. Komunikacja z usługą 
2.1.  Interfejs programistyczny usługi Teryt ws1 
 W serwisie zaimplementowano metody zwracające dane z bazy danych. Poniżej 
przedstawiono listę metod wraz ze ws kazaniem parametrów wejściowych oraz ich 
funkcjonalnościami. 
Metody pobierające datę aktualnych katalogów. 
  Bezparametrowe metody z tej grupy, pobierają z bazy danych datę początkową 
aktualnego stanu wskazanego rejestru. Dzięki temu możliwe jest określenie , czy dane 
posiadane przez użytkowników wymagają zaktualizowania. 
Wynik Metoda Parametry 
Data początkowa bieżącego stanu 
katalogu TERC. 
PobierzDateAktualnegoKatTerc  
Data początkowa bieżącego stanu 
katalogu NTS. 
PobierzDateAktualnegoKatNTS  
Data początkowa bieżącego stanu 
katalogu SIMC. 
PobierzDateAktualnegoKatSimc  
Data początkowa bieżącego stanu 
katalogu ULIC. 
PobierzDateAktualnegoKatUlic  
 
Zwracane wyniki są typu DateTime, data w formacie ‘YYYY-MM-DD’. 

 
5 
 
Instrukcja techniczna usługi TERYT ws1 2015 
Listy danych. 
Metody zwracają pewien podzbiór danych z określonych katalogów. Wspólnym 
parametrem jest DataStanu, czyli data , w którym dany katalog jest aktualny. Zakres dat dla 
poszczególnych wersji katalogów przedstawia poniższa tabela. 
Katalog 
Stan początkowy 
Zbiór Plik zmian 
TERC – wersja urzędowa 01-01-1999 01-01-1999 
TERC_ADR – wersja adresowa 01-01-2006 01-01-2006 
NTS 27-07-2000 27-07-2000 
SIMC – wersja urzędowa 01-01-1999 01-01-1999 
SIMC_ADR – wersja adresowa 01-10-2006 01-10-2006 
SIMC – wersja statystyczna 01-01-1999 01-01-1999 
ULIC – 

---
_Plik źródłowy: `data/raw/747/InstrukcjaTerytWs1.pdf` (0.95 MB) · Pobrane z https://api.stat.gov.pl/_