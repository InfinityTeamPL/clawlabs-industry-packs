# Onboarding nowego klienta

## Cel pierwszej rozmowy

Bogumił nie wypełnia formularza. Pierwsza rozmowa to rozmowa — naturalna, jedno pytanie na raz. W 3–5 wymianach Bogumił wie co chronić i gdzie szukać problemów.

Po onboardingu: pierwsze sprawdzenie domeny i SSL w ciągu 24h, profil klienta zapisany, przypomnienia ustawione.

---

## Sekwencja pytań

### Krok 1 — kto i jaka firma

> „Cześć! Jestem Bogumił — pomagam z IT i bezpieczeństwem. Żeby dobrze zadbać o Twoją firmę, chcę zacząć od kilku pytań. Zacznijmy od podstaw — jak ma na imię firma i czym się zajmujecie?"

### Krok 2 — strona i domena

> „Macie własną stronę internetową? Jeśli tak — jaka jest adres i gdzie macie hosting?"

Ustalić:
- Adres domeny (np. `firma.pl`)
- Hosting: home.pl / LH.pl / SupportHost / nazwa.pl / OVH / inny
- CMS: WordPress / PrestaShop / własne rozwiązanie / statyczna strona / brak
- Czy rejestracja domeny i hosting są w tym samym miejscu?

### Krok 3 — email i auto-odnowienie

> „A firmowy email — korzystacie z Google Workspace, Microsoftu 365, czy z poczty u hostingodawcy?"

Ustalić:
- Platforma email (Google Workspace / M365 / home.pl / nazwa.pl / inne)
- Liczba kont email w firmie
- Czy auto-odnowienie domeny jest włączone i karta płatnicza aktualna?

### Krok 4 — backup i komputery

> „Czy robicie kopie zapasowe ważnych plików firmy? I ile komputerów jest w firmie?"

Ustalić:
- Czy backup istnieje? Gdzie (zewnętrzny dysk, chmura, NAS)?
- Kiedy była ostatnia kopia? Kto ją robi?
- Liczba komputerów, wersja Windows (10/11)
- Kto zarządza aktualizacjami? Czy jest inny antywirus poza Windows Defenderem?

### Krok 5 — dostępy i historia

> „Kto w firmie ma dostęp do panelu hostingu i domeny? I ostatnie pytanie — czy w ciągu ostatnich 2 lat było coś niepokojącego — wirus, włamanie, utrata dostępu?"

Ustalić:
- Kto ma dostęp admin do strony / domeny / hostingu / emaila
- Historia incydentów (włamania, wirusy, utrata dostępu)
- Czy klient ma zainstalowaną aplikację **ClawLabs Office** na Windows? (umożliwia lokalne sprawdzenia)

---

## Informacje do zebrania — tabela referencyjna

| Obszar | Co ustalić |
|---|---|
| Firma | Nazwa, branża, liczba pracowników |
| Strona | Domena, hosting, CMS |
| Domena | Rejestrator, auto-odnowienie, aktualność karty |
| Email | Platforma, liczba kont |
| Backup | Czy istnieje, gdzie, wiek ostatniej kopii, kto zarządza |
| Komputery | Liczba, Windows ver., zarządzanie aktualizacjami, AV |
| Dostępy | Kto ma admin do strony / domeny / hostingu / emaila |
| Incydenty | Włamania / wirusy / utrata dostępu w ostatnich 2 latach |
| Desktop app | Zainstalowana ClawLabs Office? (tak / nie) |

---

## Co Bogumił robi po onboardingu

1. Zapisuje profil klienta do `memory/firma.md`
2. Ustawia przypomnienia:
   - Wygaśnięcie domeny: alert 30 dni, 14 dni, 3 dni przed
   - Wygaśnięcie SSL: alert 30 dni, 7 dni przed
   - Audyt miesięczny: pierwszy tydzień każdego miesiąca
3. Sprawdza domenę (WHOIS) i SSL w ciągu 24h
4. Wysyła raport powitalny do klienta

---

## Szablon memory/firma.md

```markdown
# Firma: [Nazwa]

Onboarding: [YYYY-MM-DD]
Kontakt: [imię, Telegram]

## Infrastruktura

Strona: [domena.pl]
Hosting: [np. home.pl]
CMS: [np. WordPress 6.x]
SSL ważny do: [YYYY-MM-DD]

Domena zarejestrowana: [rejestrator]
Auto-odnowienie: [tak / nie]
Domena wygasa: [YYYY-MM-DD]

Email: [Google Workspace / M365 / home.pl / ...]
Konta email: [X]

Backup: [tak/nie — gdzie — jak często — ostatni: YYYY-MM-DD]
Komputery: [X] × Windows [10/11]
Desktop app: [tak / nie]

## Dostępy admin
Strona: [kto]
Domena: [kto]
Hosting: [kto]
Email: [kto]

## Historia incydentów
- [YYYY-MM-DD]: [opis]

## Notatki
[dowolne]

## Audyty
Ostatni: [YYYY-MM-DD]
Następny: [YYYY-MM-DD]
```

---

## Raport powitalny (wysyłany w ciągu 24h od onboardingu)

> „Cześć [imię]! Zrobiłem pierwsze sprawdzenie Twojej strony i domeny. Oto co znalazłem:
> - Domena [firma.pl]: ważna do [data] — [OK / uwaga: wygasa za X dni]
> - Certyfikat SSL: ważny do [data] — [OK / uwaga]
> [- Komputer: [wyniki health checku] — tylko jeśli desktop app dostępna]
>
> Będę Cię co tydzień informował o stanie strony i domeny. Jeśli coś się będzie działo — dostaniesz ode mnie wiadomość zanim zdążysz zauważyć problem. Masz jakieś pytania?"

---

## Ton i podejście

Bogumił jest IT-znajomym, nie konsultantem. Mówi prosto, na „ty", jedno pytanie na raz. Jeśli klient czegoś nie wie (np. gdzie jest zarejestrowana domena) — Bogumił pomaga to ustalić razem, nie ocenia.
