---
dataset_id: 7
file: Specyfikacja_us%C5%82ugi_udost%C4%99pniaj%C4%85cej_informacje_o_podmiotach_prowadz%C4%85cych_agencje_zatrudnienia_z_KRAZ_OpenAPI_3_0.json
file_size_mb: 0.04
institution: "Ministerstwo Rodziny, Pracy i Polityki Społecznej"
data_date: 2025-01-03
freshness: fresh
source_url: http://stor.praca.gov.pl/portal/#/kraz
---

# Specyfikacja_us%C5%82ugi_udost%C4%99pniaj%C4%85cej_informacje_o_podmiotach_prowadz%C4%85cych_agencje_zatrudnienia_z_KRAZ_OpenAPI_3_0.json

_(z datasetu: Rejestr Podmiotów Prowadzących Agencje Zatrudnienia)_

```json
{
  "openapi" : "3.0.0",
  "servers" : [ {
    "description" : "Środowisko produkcyjne STOR",
    "url" : "https://storapi.praca.gov.pl/api_kraz/v1"
  } ],
  "info" : {
    "version" : "1.3.0",
    "title" : "Interfejs dostępu do danych publicznych z Krajowego Rejestru Agencji Zatrudnienia - API_KRAZ",
    "description" : "API służące do pobierania publicznych danych zgromadzonych w Krajowym Rejestrze Agencji Zatrudnienia utrzymywanym przez Ministerstwo Rodziny, Pracy i Polityki Społecznej"
  },
  "paths" : {
    "/agencje-zatrudnienia" : {
      "get" : {
        "description" : "zwraca dane agencji zatrudnienia, możliwość sortowania oraz paczkowania pobieranych danych, prosta możliwość filtrowania wyników",
        "operationId" : "agencjeZatrudnienia",
        "tags" : [ "agencje zatrudnienia" ],
        "parameters" : [ {
          "name" : "filter[nazwaAgencji]",
          "in" : "query",
          "description" : "filtrowanie wyników po polu nazwaAgencji",
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
          "name" : "filter[czyPosrednictwoPracyIInne]",
          "in" : "query",
          "description" : "filtrowanie wyników po polu czyPosrednictwoPracyIInne",
          "required" : false,
          "schema" : {
            "type" : "boolean"
          }
        }, {
          "name" : "filter[czyPracaTymczasowa]",
          "in" : "query",
          "description" : "filtrowanie wyników po polu czyPracaTymczasowa",
          "required" : false,
          "schema" : {
            "type" : "boolean"
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
          "name" : "filter[dataWpisuOd]",
          "in" : "query",
          "description" : "filtrowanie wyników po polu dataWpisuOd",
          "required" : false,
          "schema" : {
            "type" : "string"
          }
        }, {
          "name" : "filter[dataWpisuDo]",
          "in" : "query",
          "description" : "filtrowanie wyników po polu dataWpisuDo",
          "required" : false,
          "schema" : {
            "type" : "string"
          }
        }, {
          "name" : "filter[miejsceSiedzibyAgencji.kodWojewodztwa]",
          "in" : "query",
          "description" : "filtrowanie wyników po polu miejsceSiedzibyAgencji.kodWojewodztwa",
          "required" : false,
          "schema" : {
            "type" : "string"
          }
        }, {
          "name" : "filter[miejsceSiedzibyAgencji.kodPowiatu]",
          "in" : "query",
          "description
```

---
_Plik źródłowy: `data/raw/7/Specyfikacja_us%C5%82ugi_udost%C4%99pniaj%C4%85cej_informacje_o_podmiotach_prowadz%C4%85cych_agencje_zatrudnienia_z_KRAZ_OpenAPI_3_0.json` (0.04 MB) · Pobrane z http://stor.praca.gov.pl/portal/#/kraz_