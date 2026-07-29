# Phishing — rozpoznanie i reagowanie

_Phishing to najpopularniejszy atak na polskie małe firmy. Bogumił pomaga rozpoznać, zatrzymać i naprawić._

## Jak rozpoznać phishing

Typowe scenariusze w Polsce (2026):

| Nadawca (fałszywy) | Treść przynęty |
|---|---|
| InPost / DPD / DHL | „Twoja paczka czeka — dopłać 1,29 zł" |
| mBank / PKO / ING | „Twoje konto zostało zablokowane — zaloguj się" |
| ZUS / US / UODO | „Masz zaległość — sprawdź dokument" |
| home.pl / nazwa.pl | „Twoja domena wygasa — odnów teraz" |
| Microsoft / Google | „Twoje konto wymaga weryfikacji" |
| Kontrahent (BEC) | „Zmieniliśmy numer konta bankowego — przelej na nowe" |

**Sygnały ostrzegawcze:**
- Adres nadawcy wygląda podejrzanie (`mbank-bezpieczenstwo@gmail.com` zamiast `@mbank.pl`)
- Presja czasowa: „musisz działać teraz", „konto zostanie zablokowane za 24h"
- Prośba o dane logowania, PESEL, numer karty
- Link prowadzi na adres inny niż oficjalna strona (sprawdź przed kliknięciem — najedź kursorem)
- Załącznik `.exe`, `.zip`, `.doc` z prośbą o włączenie makr

---

## Scenariusz 1 — pracownik kliknął link ale nie wpisał danych

**Pytania diagnostyczne Bogumił zadaje:**
1. Czy strona się otworzyła? Jak wyglądała?
2. Czy wpisałeś tam jakieś dane (hasło, PESEL, numer karty)?
3. Na jakim urządzeniu to się stało (komputer w pracy, telefon)?
4. Czy pobierał się jakiś plik?
5. Kiedy dokładnie to się stało?

**Jeśli tylko kliknął link bez wpisywania danych:**
1. Zamknij kartę przeglądarki
2. Odśwież stronę antywirusową Windows Defender — wymuś skan
3. Obserwuj komputer przez 24h — czy coś dziwnego się dzieje
4. Jeśli był pobrany plik — **nie otwieraj go**, prześlij Bogumił do analizy (lub usuń)

---

## Scenariusz 2 — pracownik wpisał hasło na fałszywej stronie

**Działania natychmiast (kolejność ma znaczenie):**

1. **Zmień hasło** do przejętego konta — z innego, czystego urządzenia (nie tego samego komputera)
2. **Wyloguj wszystkie sesje** — w Google: Bezpieczeństwo → Urządzenia; w Microsoft: konto → Aktywność; w home.pl: panel → sesje
3. **Włącz 2FA** jeśli jeszcze nie było włączone
4. **Sprawdź reguły mailowe** — atakujący często dodają regułę przekierowującą maile do siebie (Gmail: Ustawienia → Filtry; Outlook: Reguły)
5. **Sprawdź dane kontaktowe konta** — czy nie zmieniono telefonu odzyskiwania lub zapasowego emaila
6. **Poinformuj innych** w firmie — jeśli email był firmowy, atakujący mógł wysłać phishing do kontrahentów z Twojego adresu
7. **Zastrzeż PESEL** jeśli atakujący mógł zdobyć Twój PESEL (np. przez dokumenty w mailu) — od listopada 2024 obowiązkowe przy podejrzeniu kradzieży tożsamości. Najszybciej przez aplikację **mObywatel** (zakładka „Zastrzeż PESEL") lub na bezpiecznypesel.pl. Bezpłatne, zdejmuje się tak samo łatwo.

**Bogumił pomaga:** przechodzi przez każdy krok razem z klientem przez Telegram.

---

## Scenariusz 3 — skompromitowane dane bankowe lub karta

**Działaj w ciągu minut:**
1. **Zadzwoń na infolinię banku** i zablokuj kartę / konto (numer na odwrocie karty lub na stronie banku)
2. Zgłoś incydent w aplikacji bankowej
3. Zmień hasło do bankowości internetowej z czystego urządzenia
4. Sprawdź ostatnie transakcje — czy nie ma nieautoryzowanych

Bogumił **nie przetwarza danych bankowych** — przy tym scenariuszu natychmiast kieruje do banku.

---

## RODO — czy trzeba zgłaszać do UODO?

Jeśli w skrzynce email, do której uzyskał dostęp atakujący, były dane osobowe klientów lub pracowników (imiona, PESEL, adresy, numery dowodów) — jest to naruszenie danych osobowych w rozumieniu Art. 33 RODO.

**Obowiązki:**
- Zgłoszenie do UODO w ciągu **72 godzin** od stwierdzenia naruszenia
- Jeśli naruszenie może powodować wysokie ryzyko dla osób — też powiadomienie tych osób (Art. 34)

Bogumił pomaga ocenić ryzyko i przygotować projekt zgłoszenia. Finalne zgłoszenie — warto skonsultować z prawnikiem.

Formularz UODO: https://uodo.gov.pl/pl/83/191

---

## Prewencja — co zmniejsza ryzyko

- **Menedżer haseł** (Bitwarden — bezpłatny dla firm) — każde konto ma unikalne hasło
- **2FA wszędzie** — Google Authenticator lub klucz sprzętowy (YubiKey)
- **Weryfikacja nadawcy** — przy zmianie numeru konta kontrahenta zawsze dzwoń i potwierdź głosowo
- **Szkolenie pracowników** — Bogumił może przeprowadzić krótkie szkolenie przez Telegram (przykłady, quiz)
- **Filtr antyspamowy** — Google Workspace i M365 mają wbudowany, wystarczy go skonfigurować

---

## Źródła i zgłaszanie

- **CERT Polska** — zgłoś phishing: https://incydent.cert.pl (przesłanie podejrzanego SMS-a na numer **8080** — bezpłatne, bramka CERT Polska)
- **UODO** — naruszenie danych: https://uodo.gov.pl/pl/83/191
- **Lista ostrzeżeń CERT**: https://cert.pl/posts/ (bieżące kampanie phishingowe w Polsce)
- **Zastrzeganie PESEL** (od XI.2024): aplikacja mObywatel lub bezpiecznypesel.pl
