# E-podpis — umowy o pracę PL 2026 + eIDAS 2

## 1. Dostawcy e-podpisu (PL)

### Autenti
- Docs: https://developers.autenti.com/
- Auth: OAuth2 Bearer
- Sandbox: TAK (app-sandbox.autenti.com)
- Cennik: 1,5-3 PLN/podpis + od **29 PLN/mies Start**
- Typy: EPO, ZPE (BROKER), **KPE** (KIR), mObywatel (od 2024)

### SimplySign (KIR / Asseco)
- Docs: https://www.simplysign.pl/developers + https://api.simplysign.pl/
- Auth: REST + SOAP, certyfikat kliencki, OAuth2
- Sandbox: TAK (test.simplysign.pl)
- Cennik: **238-349 PLN/rok** za KPE w chmurze
- Typy: **KPE** (kwalifikowany), pieczęć elektroniczna

### Signius (d. signme.pl)
- Docs: https://developer.signius.pl/
- Auth: API Key + OAuth2
- Sandbox: TAK (sandbox.signius.eu)
- Cennik: od 0,99 PLN/podpis w pakiecie, **49 PLN/mies entry**
- Typy: EPO, ZPE, KPE (przez partnerów), SMS-OTP

### Szafir (KIR)
- Docs: https://www.elektronicznypodpis.pl/informacje/dokumentacja/ — SDK Java/.NET (Szafir Host, applet deprecated)
- Auth: lokalny, karta/token USB
- Sandbox: brak publicznego (certyfikaty testowe od KIR)
- Cennik: zestaw karta+czytnik 200-400 PLN + 200-300 PLN/rok
- Typy: **KPE**

### Certum (Asseco)
- Docs: https://pki.certum.pl/wiki/, SDK proCertum
- Auth: REST + PKCS#11
- Cennik: od 149 PLN/rok (mini) do 500+ PLN (standard)
- Typy: **KPE**, pieczęć, znacznik czasu

### mObywatel Biznes / mPodpis
- Docs: https://info.mobywatel.gov.pl/mobywatel-biznes + https://www.gov.pl/web/mobywatel-w-aplikacji/podpis-zaufany
- Dostęp: wniosek przez ePUAP dla firmy (profil zaufany firmowy)
- Typ: **Podpis Zaufany (ZPE)** w rozumieniu eIDAS art. 26
- Cena: **bezpłatny**
- API: integrator.edu.gov.pl / pz.gov.pl — SAML/REST, wymaga umowy z MC

### ePUAP / Profil Zaufany
- Docs: https://epuap.gov.pl/wps/portal + https://pz.gov.pl/
- Auth: SAML2 PZ, OAuth node.epuap
- **Bezpłatny; ZPE**

## 2. Wymogi prawne — umowa o pracę 2026

- **KP art. 29 § 2** — umowę zawiera się **na piśmie**
- **Forma pisemna w wersji elektronicznej** = **kwalifikowany podpis elektroniczny (KPE)** (art. 781 § 1 KC + art. 25 ust. 2 eIDAS)
- **Profil Zaufany / mObywatel (ZPE)** — **NIE spełnia** formy pisemnej dla umowy o pracę (stanowisko MRiPS 2023)
- ZPE dopuszczalne dla: oświadczeń, wniosków urlopowych, aneksów nieistotnych
- **Praktyka:** umowa o pracę wymaga **KPE po stronie pracodawcy i pracownika** albo klasyczny papier
- **E-teczka pracownicza** (rozp. MRPiPS 10.12.2018) — wymaga KPE/pieczęci kwalifikowanej + znacznika czasu
- **Ustawa o usługach zaufania** (Dz.U. 2016 poz. 1579, tekst jedn. 2024) — art. 3-5 kategorie podpisów

## 3. eIDAS 2 (Rozp. 2024/1183, wszedł 20.05.2024)

- **EUDI Wallet** — obowiązek państw członkowskich do **listopad 2026**
- W PL implementacja przez mObywatel 3.0 (MC, projekt EUDIW-PL)
- QES on-the-fly z walletu — art. 5a (**kwalifikowany podpis bez fizycznego tokena**)
- **QEAA** (Qualified Electronic Attestation of Attributes) — weryfikacja atrybutów HR (wykształcenie, uprawnienia)

## 4. Biblioteki open-source do PDF

| Lib | Licencja | Wsparcie |
|-----|----------|----------|
| **node-signpdf** | MIT | PAdES-B-B (github.com/vbuch/node-signpdf) |
| **@signpdf/signpdf** | MIT | PAdES-B-T z TSA (fork) |
| **pdf-lib** | MIT | Generacja/modyfikacja, bez kryptograficznego podpisu |
| **pyHanko** (Py) | MIT | **PAdES-B-B/T/LT/LTA** — pełne wsparcie |
| **DSS** (Java, LGPL) | LGPL | Komisja Europejska, PAdES/XAdES/CAdES Baseline |
| **digidoc4j / xades4j** (Java) | LGPL | ASiC-E |
| **iText 7** | AGPL/commercial | PAdES + LTV |
| **Apache PDFBox** + **BouncyCastle** | Apache 2.0 | Java, custom implementacja |

## 5. mObywatel Biznes — dostęp

- URL: https://info.mobywatel.gov.pl/mobywatel-biznes
- Wniosek: ePUAP → "Wniosek o udostępnienie usługi mObywatel Biznes" do MC
- Wymaga: KRS, reprezentacja zgodna z wpisem, administrator techniczny
- Docs integracji: https://www.gov.pl/web/mobywatel-w-aplikacji/dla-integratorow
- Techn.: SAML2 + REST `/api/v1/`
- Usługi: mLegitymacja, mPodpis, weryfikacja tożsamości (mWeryfikator)

## 6. Przykład workflow Autenti "generuj → podpisz"

```http
POST /api/documents               # upload PDF (multipart) → documentId
POST /api/envelopes               # {name, documentIds:[]}
POST /api/envelopes/{id}/invitations
  body: [
    {email:"pracodawca@…", role:"SIGNER", signatureType:"QUALIFIED"},
    {email:"kasia@…",      role:"SIGNER", signatureType:"QUALIFIED"}
  ]
POST /api/envelopes/{id}/send
GET  /api/envelopes/{id}          # status: DRAFT|SENT|COMPLETED
# webhook → POST {callbackUrl} event=ENVELOPE_COMPLETED
GET  /api/envelopes/{id}/documents/{docId}/download    # signed PDF
GET  /api/envelopes/{id}/protocol                      # audit trail
```

**Flow Janiny dla umowy:**
1. Render template z KB → HTML
2. `pdf-lib` → PDF
3. `POST /documents` + `POST /envelopes` z `signatureType=QUALIFIED`
4. Webhook zapisuje podpisany PDF do e-teczki z timestampem

## 7. Stan obecny w repo

- Brak integracji e-podpisu
- Brak generowania PDF umów
- Janina KB: `scripts/push-janina-kb.ts` + `scripts/transform-neo-to-janina.ts`
