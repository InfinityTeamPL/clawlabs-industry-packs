# Raport tygodniowy — format i procedura

_Bogumił wysyła raport każdy poniedziałek rano (między 8:00 a 9:00) przez Telegram._

## Cel raportu

Właściciel firmy widzi w 30 sekund na telefonie: wszystko gra, albo jest coś do zrobienia. Nie musi się zastanawiać "czy moja strona działa" ani "kiedy mi wygasa domena". Bogumił to ogarnia.

---

## Procedura przed wysłaniem

Bogumił wykonuje w tej kolejności przed każdym raportem:

1. **Sprawdź uptime** — czy strona działała przez ostatnie 7 dni (log ostatnich sprawdzeń)
2. **Sprawdź domenę** — WHOIS, ile dni do wygaśnięcia
3. **Sprawdź SSL** — ile dni do wygaśnięcia certyfikatu
4. **Przejrzyj listę przypomnień** — czy są zaległe faktury hostingowe, zbliżające się daty
5. **Sprawdź notatki z ostatniego tygodnia** — czy był jakiś incydent, czy jest follow-up

Dopiero po zebraniu danych — kompiluje i wysyła.

---

## Szablon raportu

```
📋 Raport IT — [nazwa firmy] | [data]

STRONA
[ikona] [domena] — [status]

DOMENA
[ikona] Wygasa: [data] ([X] dni)

CERTYFIKAT SSL
[ikona] Ważny do: [data] ([X] dni)

[sekcja incydentów — tylko jeśli coś się działo]

[sekcja do zrobienia — tylko jeśli jest akcja wymagana]

— Bogumił
```

---

## Przykład 1 — spokojny tydzień (wszystko OK)

```
📋 Raport IT — Meble Kowalski | pon. 28.04.2026

STRONA
✅ meblekowalski.pl — działa bez zarzutu

DOMENA
✅ Wygasa: 14.09.2026 (139 dni)

CERTYFIKAT SSL
✅ Ważny do: 15.07.2026 (78 dni)

Bez incydentów w tym tygodniu. Dobrego początku tygodnia!

— Bogumił
```

---

## Przykład 2 — ostrzeżenie o domenie

```
📋 Raport IT — Kancelaria Nowak | pon. 28.04.2026

STRONA
✅ kancelaria-nowak.pl — działa

DOMENA
⚠️ Wygasa: 21.05.2026 (23 dni)
→ Odnów w panelu nazwa.pl. Polecam od razu na 2 lata.

CERTYFIKAT SSL
✅ Ważny do: 02.08.2026 (96 dni)

— Bogumił
```

---

## Przykład 3 — był incydent w tygodniu

```
📋 Raport IT — Sklep ABC | pon. 28.04.2026

STRONA
⚠️ sklep-abc.pl — był problem w czwartek

DOMENA
✅ Wygasa: 03.11.2026 (189 dni)

CERTYFIKAT SSL
✅ Ważny do: 29.06.2026 (62 dni)

INCYDENT — czwartek 24.04, godz. 14:20–16:45
Strona nie odpowiadała przez ~2,5 godziny. Hosting (LH.pl) potwierdził awarię serwera po stronie ich infrastruktury. Strona wróciła sama po restarcie serwera przez hosting. Bez danych klientów zagrożonych — awaria techniczna, nie atak.
Status: zamknięty ✅

— Bogumił
```

---

## Przykład 4 — sytuacja krytyczna (domena < 7 dni)

```
📋 Raport IT — Auto-Części Wiśniewski | pon. 28.04.2026

STRONA
✅ czesci-wisniewski.pl — działa

DOMENA
🔴 PILNE — Wygasa: 02.05.2026 (4 dni!)
→ Zaloguj się do home.pl TERAZ i odnów. Jeśli wygaśnie, strona przestanie działać.
→ Link: panel.home.pl → Domeny → [twoja domena] → Przedłuż

CERTYFIKAT SSL
✅ Ważny do: 11.09.2026 (136 dni)

— Bogumił

P.S. Napisz mi gdy odnowisz — zaktualizuję datę.
```

---

## Zasady formatowania

- **Krótko** — właściciel czyta na telefonie, w drodze do pracy
- **Ikony** jako szybki sygnał: ✅ OK, ⚠️ uwaga, 🔴 pilne, 🚨 krytyczne
- **Konkretna akcja** gdy coś wymaga działania — nie "powinieneś odnowić domenę" ale "zaloguj się do panel.home.pl i kliknij Przedłuż"
- **Bez żargonu** — "certyfikat SSL" jest OK (wyjaśniony przy onboardingu), ale nie "TLS handshake failure"
- **Podpis** — zawsze `— Bogumił` na końcu

## Kiedy NIE wysyłać standardowego raportu

Jeśli w piątek/sobotę/niedzielę pojawi się problem krytyczny (strona down > 1h, domena wygasła), Bogumił **nie czeka do poniedziałku** — wysyła alert natychmiast.

## Przechowywanie

Po wysłaniu raportu: zapisuję do `memory/audyt/raport-YYYY-MM-DD.md` z pełnymi danymi (żeby mieć historię).
