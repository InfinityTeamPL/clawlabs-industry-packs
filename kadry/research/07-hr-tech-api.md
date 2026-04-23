# HR-tech API — polskie i europejskie systemy (2026-04-22)

## HR / Płace PL

### Enova365 (Soneta)
- Docs: https://dok.enova.pl/ (moduł "API" / "Web Service")
- Auth: Basic Auth + token (REST od 2020+); starszy SOAP
- Scope: read/write — pracownicy, umowy, listy płac, ewidencja czasu; brak natywnego e-sign
- Format: JSON (REST) / XML (SOAP)
- Przykład: `GET /api/Kadry/Pracownicy/{id}`
- Rate limit: nieudokumentowany (on-prem)
- Cena: API w licencji modułu; moduł Kadry ~2000 PLN/stanowisko
- SDK: brak oficjalnego npm; społecznościowe wrappery C#/.NET

### Comarch ERP Optima / XL
- Docs: https://www.erp.comarch.pl/klienci/ (Comarch ERP XL API REST + Optima API)
- Auth: API key + token; OAuth2 w Comarch ERP XT
- Scope: read/write — pracownicy, umowy, kadry, płace
- Format: JSON. `POST /api/Employees` `{"firstName","lastName","pesel","contractType"}`
- Cena: API w licencji partnerskiej
- SDK: .NET only, brak npm

### Sage / Symfonia HR
- Docs: https://developers.symfonia.pl/
- Auth: OAuth2
- Scope: read/write pracownicy, listy płac; ATS brak
- Format: JSON REST
- Rate limit: **60 req/min** per token
- Cena: API w Symfonia Cloud
- SDK: brak npm

### Unit4 Teta / TETA ME
- Docs: https://docs.unit4.com/ (Unit4 ERP API)
- Auth: OAuth2
- Scope: read/write pracownicy, czas pracy, urlopy
- Format: JSON/OData
- SDK: brak npm

### Bez publicznego API
InsERT Gratyfikant, Wapro Gang, Streamsoft Prestiż, Reset2, Asseco SWP — tylko lokalne SDK / CSV/XML integracje plikowe.

## ATS PL

### TeamTailor
- Docs: https://docs.teamtailor.com/
- Auth: API key (X-Api-Key) + JSON:API
- Scope: read/write candidates, jobs, applications
- Format: JSON:API
- `POST /v1/candidates` → `{"data":{"type":"candidates","attributes":{...}}}`
- Rate: **10 req/sec**
- Cena: od **~€299/mies** plan z API
- SDK: nieoficjalne npm wrappery

### Traffit
- Docs: https://developers.traffit.com/
- Auth: API key
- Scope: read/write candidates, vacancies, stages
- Format: JSON REST
- SDK: brak npm

### eRecruiter (Pracuj.pl)
- Docs: https://developers.erecruiter.pl/ (partner portal, po rejestracji)
- Auth: OAuth2 + client credentials
- Scope: read/write candidates, offers, applications
- Format: JSON REST
- Cena: tylko enterprise
- SDK: brak npm

### Bez publicznego API
Elevato, HireYou, RECMAN, HRmaps, Recru.ee — lub tylko na żądanie partnera.

## Benefity

**MyBenefit, Motivizer, Worksmile, Benefit Systems** — brak publicznego API. Integracje per-klient przez SFTP/CSV lub partner program.

## Czas pracy

### Calamari
- Docs: https://apidocs.calamari.io/
- Auth: Basic Auth + API key
- Scope: read/write — timesheets, urlopy, pracownicy
- Format: JSON REST
- `GET /api/timeentries/find` → array `{employeeId,start,end,project}`
- Rate: **100 req/min**
- Cena: API w Enterprise (~€3/user)
- SDK: brak oficjalnego npm

### Kadromierz
- Docs: https://kadromierz.pl/api/ (dostępne po logowaniu)
- Auth: API key
- Scope: read/write grafiki, RCP, pracownicy
- Format: JSON REST
- SDK: brak npm

### Bez API
KadroNet, timesheets.pl

## E-podpis

### Autenti
- Docs: https://developers.autenti.com/
- Auth: OAuth2 + client credentials
- Scope: write — wysyłka dokumentów do podpisu, webhooks status
- Format: JSON REST
- `POST /api/v2/envelopes` `{"title","documents":[...],"signers":[{"email","role"}]}`
- Rate: **300 req/min**
- Cena: od **~200 PLN/mies** + per-podpis
- SDK: brak oficjalnego npm

### SimplySign (KIR)
- Docs: https://www.simplysign.pl/ → SimplySign API (PKCS#11 + REST dla kwalifikowanego)
- Auth: certyfikat + API key
- Scope: write — podpis kwalifikowany
- Format: REST/PKCS
- SDK: Java/.NET (brak npm)

### Signius
- API dla partnerów, brak publicznej dokumentacji

### mObywatel
- **Brak API** dla podpisu (tylko mObywatel Connect do logowania od 2024)

## Płatności / karty

- **Stripe** — https://stripe.com/docs/api, OAuth2/secret, JSON REST, pełne SDK `npm i stripe`, **100 read/s**
- **Tpay** — https://docs.tpay.com/, API key + HMAC, brak oficjalnego npm
- **Payhawk** — https://developers.payhawk.com/, OAuth2, brak npm
- **Spendesk** — https://developer.spendesk.com/, OAuth2, brak npm
