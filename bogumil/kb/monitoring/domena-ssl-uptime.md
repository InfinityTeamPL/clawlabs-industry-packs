# Monitorowanie domeny, SSL i dostępności strony

_Stan: 2026-04-28. Bogumił sprawdza te rzeczy regularnie — zanim klient w ogóle zauważy problem._

## Domena — wygaśnięcie

### Jak sprawdzam

Wyszukuję WHOIS dla domeny klienta. Dla domen `.pl` używam rejestru NASK:
- `https://www.dns.pl/cgi-bin/whois.pl?q=<domena>` — oficjalny WHOIS dla .pl
- `https://who.is/whois/<domena>` — dla .com, .eu, .net i innych

### Co szukam w wynikach WHOIS

```
Expiration Date: 2026-09-14
Registrar: home.pl sp. z o.o.
Name Server: ns1.home.pl
Status: ok
```

Kluczowe pole: `Expiration Date` (albo `expires`, `Registry Expiry Date` — zależy od rejestratora).

### Progi alertów

| Czas do wygaśnięcia | Co robię |
|---|---|
| > 30 dni | ✅ OK, notuję datę |
| 30–14 dni | ⚠️ Wysyłam ostrzeżenie klientowi z linkiem do panelu rejestratora |
| 14–3 dni | 🔴 Pilne — dzwonię (Telegram), daję konkretny link do odnowienia |
| < 3 dni | 🚨 KRYTYCZNE — proszę o natychmiastowe działanie |

### Co mówię klientowi

**30 dni:**
> "Hej, domena [domena.pl] wygasa za 28 dni (14 października). Wejdź do panelu [nazwa rejestratora] i odnów — najlepiej na 2 lata żeby nie wracać do tego tematu. Daj znać jak zrobisz, żebym zaktualizował datę."

**Pilne (< 7 dni):**
> "PILNE: domena [domena.pl] wygasa za 5 dni. Jeśli nie odnowisz, strona przestanie działać i możesz stracić domenę. Zaloguj się teraz: [link]. Jeśli masz problem — napisz, pomogę."

### Popularne rejestry w Polsce i linki do odnowienia

| Rejestrator | Panel klienta |
|---|---|
| home.pl | panel.home.pl |
| nazwa.pl | panel.nazwa.pl |
| OVH | ovh.pl/manager |
| Domeny.pl | panel.domeny.pl |
| LH.pl | panel.lh.pl |
| aftermarket.pl | panel.aftermarket.pl |
| cyber_Folks (cyberfolks.pl) | panel.cyberfolks.pl |

### Jeśli domena już wygasła

1. Sprawdzam czy jest jeszcze w **grace period** (NASK .pl: 30 dni po wygaśnięciu, można odnowić za normalną cenę)
2. Po grace period — **redemption period** (kolejne 30 dni, odnowienie droższe — kilkaset zł)
3. Po redemption — domena **dostępna dla wszystkich** (ryzyko przejęcia przez cybersquattera)

Działam natychmiast: `Twoja domena jest w grace period — możesz ją jeszcze odratować, ale masz max 30 dni. Wejdź do [rejestrator] teraz.`

---

## SSL — certyfikat bezpieczeństwa

### Jak sprawdzam

Pobieram informacje o certyfikacie SSL przez request HTTP do strony i sprawdzam nagłówki / dane certyfikatu. Alternatywnie: `https://www.sslshopper.com/ssl-checker.html#hostname=<domena>` przez URL Reader.

Kluczowe pole w odpowiedzi: `Valid Until` / `Not After`.

### Przykład wyniku

```
Certificate for: firma.pl
Issued by: Let's Encrypt
Valid from: 2026-01-15
Valid until: 2026-04-15  ← to sprawdzam
Days remaining: 12       ← ważne
```

### Progi alertów

| Czas do wygaśnięcia | Co robię |
|---|---|
| > 30 dni | ✅ OK |
| 30–7 dni | ⚠️ Alert do klienta — sprawdź czy auto-odnowienie działa |
| < 7 dni | 🔴 Pilne — prawdopodobnie auto-odnowienie nie zadziałało |
| Wygasł | 🚨 Strona pokazuje błąd "Twoje połączenie nie jest prywatne" — klienci uciekają |

### Skąd certyfikaty w Polsce

- **Let's Encrypt** (bezpłatny, auto-odnowienie co 90 dni) — standard u większości hostingów
- **home.pl, nazwa.pl, LH.pl** — często wystawiają Let's Encrypt automatycznie
- Jeśli SSL wygasł mimo auto-odnowienia: prawdopodobnie problem z konfiguracją serwera lub zmiana DNS — klient musi napisać do hostingu

### Co mówię klientowi gdy SSL wygasł

> "Certyfikat SSL waszej strony wygasł — przeglądarki pokazują teraz ostrzeżenie 'strona niebezpieczna' i klienci mogą uciec. Napisz do [hosting] przez panel lub chat i powiedz: 'Proszę o odnowienie certyfikatu SSL dla domeny [domena.pl]'. Zajmie im to 5 minut."

---

## Dostępność strony (uptime)

### Jak sprawdzam

Robię request HTTP do strony klienta przez URL Reader i sprawdzam:
- Kod odpowiedzi HTTP
- Czy strona ładuje się normalnie
- Czas odpowiedzi (jeśli dostępny)

### Interpretacja kodów HTTP

| Kod | Znaczenie | Co robię |
|---|---|---|
| 200 OK | ✅ Strona działa | Notuję, nic nie robię |
| 301/302 | Przekierowanie | Sprawdzam dokąd — zazwyczaj OK |
| 403 Forbidden | Problem z uprawnieniami | Alert — prawdopodobnie błąd konfiguracji |
| 404 Not Found | Strony nie ma | Alert — błąd lub hack |
| 500/503 | Błąd serwera | Alert — hosting lub CMS nie działa |
| Timeout | Brak odpowiedzi | Alert — serwer może być down |

### Progi alertów

- **Pojedynczy błąd**: czekam 5 minut, sprawdzam ponownie (mogło być chwilowe)
- **Błąd > 5 minut**: wysyłam alert do klienta
- **Błąd > 1 godzina**: dzwonię (Telegram), sugeruję kontakt z hostingiem

### Co mówię gdy strona nie działa

> "Wasza strona [domena.pl] nie odpowiada od ok. 20 minut. Sprawdziłem i pojawia się błąd [kod/komunikat]. Zaloguj się do panelu [hosting] i sprawdź czy serwer działa — zazwyczaj jest tam status i przycisk restartu. Jeśli nie wiesz jak — napisz, przeprowadzę cię krok po kroku."

---

## Częstotliwość sprawdzeń

| Co | Jak często |
|---|---|
| Dostępność strony | Co 30 minut (reminder co 30 min w czasie aktywności) |
| SSL certyfikat | Co 7 dni |
| Domena (WHOIS) | Co 7 dni; codziennie gdy < 14 dni do wygaśnięcia |
| Raport zbiorczy | Co poniedziałek rano |

---

## Źródła

- NASK — rejestr domen .pl: https://www.dns.pl
- ICANN WHOIS: https://lookup.icann.org
- SSL Labs (weryfikacja SSL): https://www.ssllabs.com/ssltest/
- home.pl status: https://status.home.pl
- CERT Polska: https://cert.pl
