# Podejrzane logowanie — diagnoza i reakcja

_Klient mówi „ktoś mi się włamał na email/serwer" albo dostał alert o logowaniu z obcego kraju. Bogumił sprawdza i działa._

## Pytania diagnostyczne

Bogumił zadaje je zanim cokolwiek zrobi:

1. Do czego był dostęp — email, hosting, serwer, panel sklepu, coś innego?
2. Skąd wiesz — dostałeś alert, widzisz nieznane sesje, coś zostało zmienione?
3. Kiedy to się stało (data, godzina jeśli wiadomo)?
4. Czy logowanie wymagało 2FA? Czy 2FA było włączone?
5. Czy hasło do tego konta było używane gdzieś indziej?
6. Czy ostatnio klikałeś w jakiś link lub wpisywałeś to hasło na stronie zewnętrznej?

---

## Scenariusz 1 — kompromitacja emaila firmowego

**Natychmiastowe działania:**

1. **Zmień hasło** — z czystego urządzenia (najlepiej telefon z mobilnym internetem, nie firmowa sieć)
2. **Wyloguj wszystkie aktywne sesje:**
   - Gmail: Konto Google → Bezpieczeństwo → Urządzenia → wyloguj wszystkie
   - Outlook/M365: account.microsoft.com → Bezpieczeństwo → Aktywność logowania → wyloguj
   - home.pl: panel → Poczta → Sesje
3. **Sprawdź reguły mailowe** — to najczęstszy backdoor po włamaniu:
   - Gmail: Ustawienia → Filtry i zablokowane adresy
   - Outlook: Reguły i alerty
   - Szukaj reguł: przekierowanie na zewnętrzny adres, automatyczne usuwanie maili z banku/ZUS/kontrahentów
4. **Sprawdź dane odzyskiwania** — czy nie zmieniono zapasowego emaila lub numeru telefonu
5. **Włącz 2FA** jeśli jeszcze nie było
6. **Powiadom kontrahentów** jeśli mógł być wysłany phishing z Twojego adresu

---

## Scenariusz 2 — kompromitacja serwera / hostingu / cPanela

**Działania:**

1. **Zmień hasło do panelu** (cPanel, DirectAdmin, Plesk) z czystego urządzenia
2. **Sprawdź datę modyfikacji plików** na serwerze — pliki zmienione w nieznanym czasie mogą być webshellami
3. **Wyszukaj webshelle** — pliki PHP z losowymi nazwami w folderze `public_html`, `wp-content/uploads`, `tmp`
4. **Sprawdź logi serwera** — access.log i error.log — nieprawidłowe żądania POST do nieznanych plików
5. **Skontaktuj się z hostingiem** — home.pl, LH.pl, nazwa.pl mają dział bezpieczeństwa, często pomogą przy skanowaniu
6. **Przywróć z backupu** jeśli dostępny i serwer był mocno skompromitowany

Bogumił przez desktop app (jeśli klient ma serwer na Windows) może sprawdzić logi zdarzeń.

---

## Sprawdzenie logów Windows przez desktop app

Gdy klient ma zainstalowaną aplikację ClawLabs Office, Bogumił sprawdza logi przez local MCP bridge:

**Nieudane logowania (EventID 4625):**
```powershell
Get-EventLog -LogName Security -InstanceId 4625 -Newest 50 2>$null | Select-Object TimeGenerated, Message | Format-List
```

**Udane logowania sieciowe (EventID 4624, typ 3 = sieciowe):**
```powershell
Get-WinEvent -FilterHashtable @{LogName='Security'; Id=4624} -MaxEvents 20 | Where-Object {$_.Message -match 'Logon Type:\s+3'} | Select-Object TimeCreated, Message
```

**Co szukam:**
- Logowania z obcych adresów IP w nocy / weekendy
- Nieznane konta użytkownika
- Wiele nieudanych prób z jednego IP (brute force)

**Jeśli brak desktop app:** proszę klienta o uruchomienie poleceń przez PowerShell (Administrator) i przesłanie zrzutu ekranu.

---

## „Logowanie z Ukrainy / Rosji / Chin" — co to znaczy?

Nie zawsze znaczy atak. Częste powody fałszywego alarmu:
- Atakujący używa VPN lub proxy z tamtych krajów — ale logowanie było Twoje
- Bot skanujący internet trafił na formularz logowania — nie przeszedł bo nie znał hasła
- Usługa Google/Microsoft wykrywa logowanie przez serwery CDN które są zlokalizowane inaczej

**Jak odróżnić:**
- Czy logowanie się powiodło (sukces czy porażka)?
- Czy po tym logowaniu coś się zmieniło (reguły, ustawienia, wysłane maile)?
- Czy ta sesja jest nadal aktywna?

Jeśli logowanie zakończone sukcesem i coś zostało zmienione → traktujemy jak prawdziwy incydent.
Jeśli tylko nieudana próba → odnotowujemy, rozważamy wzmocnienie hasła i włączenie 2FA.

---

## Prewencja

- **Menedżer haseł** (Bitwarden) — unikalne hasło do każdego serwisu, bez powtarzania
- **2FA wszędzie** — Google Authenticator, klucz sprzętowy lub SMS (SMS najsłabszy ale lepszy niż brak)
- **Alerty logowania** — Gmail, M365, home.pl pozwalają ustawić powiadomienie email/SMS przy nowym logowaniu
- **Nie używaj haseł firmowych prywatnie** — i odwrotnie
- **Sprawdź haveibeenpwned.com** — czy Twój email/hasło nie wyciekły w znanych atakach

---

## RODO

Jeśli w skompromitowanym emailu lub serwerze były dane osobowe klientów / pracowników — naruszenie danych osobowych. Art. 33 RODO: zgłoszenie do UODO w ciągu **72 godzin**.

Bogumił pomaga ocenić ryzyko i przygotować projekt zgłoszenia.

---

## Źródła

- **CERT Polska** — incydent.cert.pl
- **haveibeenpwned.com** — sprawdź czy email/hasło wyciekły
- **UODO** — uodo.gov.pl/pl/83/191
