---
dataset_id: 7
file: Specyfikacja_us%C5%82ugi_udost%C4%99pniaj%C4%85cej_informacje_ze_S%C5%82ownik%C3%B3w_STOR_dla_API_KRAZ_OpenAPI_3_0.json
file_size_mb: 0.02
institution: "Ministerstwo Rodziny, Pracy i Polityki Społecznej"
data_date: 2025-01-03
freshness: fresh
source_url: http://stor.praca.gov.pl/portal/#/kraz
---

# Specyfikacja_us%C5%82ugi_udost%C4%99pniaj%C4%85cej_informacje_ze_S%C5%82ownik%C3%B3w_STOR_dla_API_KRAZ_OpenAPI_3_0.json

_(z datasetu: Rejestr Podmiotów Prowadzących Agencje Zatrudnienia)_

```json
{
  "openapi" : "3.0.0",
  "servers" : [ {
    "description" : "Środowisko produkcyjne STOR",
    "url" : "https://storapi.praca.gov.pl/api_slowniki/v1"
  } ],
  "info" : {
    "version" : "1.0.0",
    "title" : "Interfejs dostępu do danych publicznych - słowników - używanych w systemie STOR i wykorzystywanych przez API_RIS oraz API_KRAZ",
    "description" : "API służące do pobierania publicznych danych słownikowych systemu STOR utrzymywanym przez Ministerstwo Rodziny, Pracy i Polityki Społecznej"
  },
  "paths" : {
    "/slowniki/version" : {
      "get" : {
        "description" : "zwraca wersję słowników STOR",
        "operationId" : "wersjaSlownikow",
        "tags" : [ "słowniki" ],
        "responses" : {
          "200" : {
            "description" : "Informacje o wersji słowników STOR",
            "content" : {
              "application/json" : {
                "schema" : {
                  "type" : "object",
                  "properties" : {
                    "data" : {
                      "type" : "object",
                      "properties" : {
                        "wersjaSlownikow" : {
                          "type" : "string",
                          "description" : "wersja słowników"
                        }
                      }
                    }
                  }
                }
              }
            }
          },
          "500" : {
            "description" : "Błąd wywołania metody",
            "content" : {
              "application/json" : {
                "schema" : {
                  "$ref" : "#/components/schemas/Errors"
                }
              }
            }
          }
        }
      }
    },
    "/slowniki/wojewodztwa" : {
      "get" : {
        "description" : "zwraca słownik województw",
        "operationId" : "slownikWojewodztwa",
        "tags" : [ "słowniki" ],
        "responses" : {
          "200" : {
            "description" : "Informacje o pozycjach słownika",
            "content" : {
              "application/json" : {
                "schema" : {
                  "type" : "object",
                  "properties" : {
                    "data" : {
                      "type" : "array",
                      "items" : {
                        "$ref" : "#/components/schemas/PozycjaSlownika"
                      }
                    }
                  }
                }
              }
            }
          },
          "429" : {
            "description" : "zbyt dużo zapytań w jednostce czasu  lub przekroczono limit wywołań przez podmiot",
            "content" : {
              "application/json" : {
                "schema" : {
                  "$ref" : "#/components/schemas/Errors"
                }
              }
            }
          },
          "401" : {
            "description" : "brak uprawnień do wywołania usługi (nieprawidłowy adres IP lub brak dostępu do API_SLOWNIKI)",
            "content" : {
              "application/json" : {
```

---
_Plik źródłowy: `data/raw/7/Specyfikacja_us%C5%82ugi_udost%C4%99pniaj%C4%85cej_informacje_ze_S%C5%82ownik%C3%B3w_STOR_dla_API_KRAZ_OpenAPI_3_0.json` (0.02 MB) · Pobrane z http://stor.praca.gov.pl/portal/#/kraz_