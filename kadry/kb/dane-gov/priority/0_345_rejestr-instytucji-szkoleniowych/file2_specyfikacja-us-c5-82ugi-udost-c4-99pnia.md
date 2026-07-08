---
dataset_id: 345
file: Specyfikacja_us%C5%82ugi_udost%C4%99pniaj%C4%85cej_informacje_o_instytucjach_szkoleniowych_z_RIS_OpenAPI_3_0.json
file_size_mb: 0.08
institution: "Ministerstwo Rodziny, Pracy i Polityki Społecznej"
data_date: 2025-01-03
freshness: fresh
source_url: http://stor.praca.gov.pl/portal/#/ris
---

# Specyfikacja_us%C5%82ugi_udost%C4%99pniaj%C4%85cej_informacje_o_instytucjach_szkoleniowych_z_RIS_OpenAPI_3_0.json

_(z datasetu: Rejestr Instytucji Szkoleniowych)_

```json
{
  "openapi" : "3.0.0",
  "servers" : [ {
    "description" : "Środowisko produkcyjne STOR",
    "url" : "https://storapi.praca.gov.pl/api_ris/v1"
  } ],
  "info" : {
    "version" : "1.3.0",
    "title" : "Interfejs dostępu do danych publicznych z Rejestru Instytucji Szkoleniowych - API_RIS",
    "description" : "API służące do pobierania publicznych danych zgromadzonych w Rejestrze Instytucji Szkoleniowych utrzymywanym przez Ministerstwo Rodziny, Pracy i Polityki Społecznej"
  },
  "paths" : {
    "/instytucje-szkoleniowe" : {
      "get" : {
        "description" : "zwraca dane instytucji szkoleniowych, możliwość sortowania oraz paczkowania pobieranych danych, prosta możliwość filtrowania wyników",
        "operationId" : "instytucjeSzkoleniowe",
        "tags" : [ "instytucje szkoleniowe" ],
        "parameters" : [ {
          "name" : "filter[nazwaInstytucji]",
          "in" : "query",
          "description" : "filtrowanie wyników po polu nazwaInstytucji",
          "required" : false,
          "schema" : {
            "type" : "string"
          }
        }, {
          "name" : "filter[numerWRejestrze]",
          "in" : "query",
          "description" : "filtrowanie wyników po polu numerWRejestrze",
          "required" : false,
          "schema" : {
            "type" : "string"
          }
        }, {
          "name" : "filter[regon]",
          "in" : "query",
          "description" : "filtrowanie wyników po polu regon",
          "required" : false,
          "schema" : {
            "type" : "string"
          }
        }, {
          "name" : "filter[nip]",
          "in" : "query",
          "description" : "filtrowanie wyników po polu nip",
          "required" : false,
          "schema" : {
            "type" : "string"
          }
        }, {
          "name" : "filter[rodzajWyszukiwanegoObiektu]",
          "in" : "query",
          "description" : "filtrowanie wyników po polu rodzajWyszukiwanegoObiektu",
          "required" : false,
          "schema" : {
            "type" : "string"
          }
        }, {
          "name" : "filter[miejsceDzialalnosci.kodWojewodztwa]",
          "in" : "query",
          "description" : "filtrowanie wyników po polu kodWojewodztwa",
          "required" : false,
          "schema" : {
            "type" : "string"
          }
        }, {
          "name" : "filter[miejsceDzialalnosci.kodPowiatu]",
          "in" : "query",
          "description" : "filtrowanie wyników po polu kodPowiatu",
          "required" : false,
          "schema" : {
            "type" : "string"
          }
        }, {
          "name" : "filter[miejsceDzialalnosci.kodGminy]",
          "in" : "query",
          "description" : "filtrowanie wyników po polu kodGminy",
          "required" : false,
          "schema" : {
            "type" : "string"
          }
        }, {
          "name" : "filter[miejsceDzialalnosci.kodMiejscowosci]",
          "in" : "query",
          "description" : "filtrowani
```

---
_Plik źródłowy: `data/raw/345/Specyfikacja_us%C5%82ugi_udost%C4%99pniaj%C4%85cej_informacje_o_instytucjach_szkoleniowych_z_RIS_OpenAPI_3_0.json` (0.08 MB) · Pobrane z http://stor.praca.gov.pl/portal/#/ris_