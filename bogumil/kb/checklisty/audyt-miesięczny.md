# Audyt miesięczny

## Kiedy i jak

Bogumił uruchamia audyt w **pierwszym tygodniu każdego miesiąca** dla każdego aktywnego klienta. Wyniki zapisuje do `memory/audyt/YYYY-MM.md`. Na końcu każdego audytu Bogumił ustawia przypomnienie na następny miesiąc.

---

## Lista kontrolna

### Domena i SSL

- [ ] **WHOIS domeny** — ile dni do wygaśnięcia, rejestrator, auto-odnowienie aktywne?
  - < 30 dni → informuj klienta
  - < 14 dni → eskalacja, pilne

- [ ] **Certyfikat SSL** — ile dni do wygaśnięcia, wystawca, brak błędów?
  - < 30 dni → poinformuj klienta
  - < 7 dni → pilne odnowienie

- [ ] **Uptime strony** — czy były przestoje w ostatnich 30 dniach?
  - Sprawdź logi z cotygodniowych sprawdzeń
  - Jeśli brak logów: zapytaj klienta czy zauważył przerwy

---

### Bezpieczeństwo Windows *(jeśli dostępna desktop app)*

- [ ] **Windows Defender** — aktywny, RTP włączone, definicje < 3 dni
- [ ] **Aktualizacje Windows** — ostatnia < 60 dni
- [ ] **Nieudane logowania (Event 4625)** — brak anomalii (wiele prób z obcych IP)
- [ ] **Otwarte porty** — brak nieoczekiwanych (szczególnie 3389 RDP na 0.0.0.0)
- [ ] **Autostart i zadania zaplanowane** — brak podejrzanych wpisów

Szczegóły: `kb/windows/health-check.md`

---

### Backup

- [ ] Zapytaj klienta: _„Czy kopia zapasowa z tego tygodnia jest OK? Kiedy ostatnio sprawdzałeś że da się z niej przywrócić dane?"_
  - Brak backupu od > 30 dni → priorytetowa rozmowa tego samego dnia
  - Brak backupu w ogóle → działanie priorytetowe na ten miesiąc

---

### Faktury i płatności

- [ ] Zapytaj klienta: _„Czy dostałeś jakieś faktury za hosting, domenę lub inne usługi IT?"_
  - Cel: brak zaległości które mogłyby spowodować wyłączenie usług
  - Poproś o przesłanie niezapłaconych faktur

---

### CMS / WordPress *(jeśli dotyczy)*

- [ ] Czy są dostępne aktualizacje WordPressa, wtyczek, motywów?
  - Jeśli tak → zaplanuj aktualizację (zawsze po wcześniejszym backupie)
  - Niezaktualizowany WordPress to najczęstszy wektor włamania u polskich SMB

---

### Przegląd incydentów z ostatnich 30 dni

- [ ] Czy były zdarzenia bezpieczeństwa (alerty, dziwne maile, problemy z dostępem)?
- [ ] Czy podjęte działania były skuteczne?
- [ ] Czy coś wymaga dalszego monitorowania?

---

## Sytuacje wymagające natychmiastowego działania *(nie czekamy na audyt)*

| Sytuacja | Działanie |
|---|---|
| Domena wygasa < 14 dni | Natychmiast alert do klienta, asystuj przy odnowieniu |
| SSL wygasa < 7 dni | Pilne — strona może zacząć pokazywać błędy |
| Windows Defender wyłączony | Poinformuj klienta, spróbuj włączyć przez desktop app |
| Brak aktualizacji > 90 dni | Eskaluj do klienta |
| Setki nieudanych logowań z obcych IP | Wyłącz RDP, zmień hasła — natychmiast |
| Klient zgłasza atak / wirusa | Porzuć plan, uruchom health check, eskaluj |
| Brak backupu od > 30 dni | Rozmowa z klientem tego samego dnia |

---

## Format raportu miesięcznego dla klienta

```
Raport miesięczny — [Firma] — [Miesiąc YYYY]

DOMENA I SSL
- Domena [firma.pl]: ważna do [data] ([X] dni)
- SSL: ważny do [data] ([X] dni)
- Uptime: OK / [opis przestojów]

BEZPIECZEŃSTWO WINDOWS
- Antywirus: OK / [problem]
- Aktualizacje: OK / ostatnia [X] dni temu
- Logowania: czysto / [uwagi]

BACKUP
- Status: klient potwierdził OK / do sprawdzenia / BRAK

DZIAŁANIA W TYM MIESIĄCU
- [lista]

DO ZROBIENIA
- [lista]

Pytania? Napisz!
— Bogumił
```

---

## Zapis wyników

Bogumił zapisuje pełne wyniki techniczne do:

```
memory/audyt/YYYY-MM.md
```

Struktura:
```markdown
# Audyt [Firma] — [YYYY-MM]
Data: [YYYY-MM-DD]

## Domena
Domena: [firma.pl] — wygasa [YYYY-MM-DD] ([X] dni) — auto-odnowienie: [tak/nie]

## SSL
Wygasa: [YYYY-MM-DD] ([X] dni) — wystawca: [Let's Encrypt / inne]

## Uptime
Przestoje ostatnie 30 dni: [brak / opis]

## Windows Health Check
Defender: [OK / problem]
Aktualizacje: ostatnia [YYYY-MM-DD]
Nieudane logowania: [X w ostatnich 30 dniach]
Porty: [OK / uwagi]
Autostart: [OK / uwagi]
Zadania: [OK / uwagi]

## Backup
Potwierdzony przez klienta: [tak / nie / brak odpowiedzi]

## Incydenty
[brak / opis]

## Działania
[lista]

## Następny audyt
[YYYY-MM-DD]
```
