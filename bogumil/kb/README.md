# Baza wiedzy Bogumił — IT i Cyberbezpieczeństwo

_Stan: 2026-04-29. v0.1.0_

## Kim jest Bogumił

Bogumił to asystent AI do IT i bezpieczeństwa defensywnego dla polskich małych firm bez działu IT. Właściciel sklepu, gabinetu, kancelarii — ktoś kto nie chce rozumieć technikaliów, ale chce żeby „wszystko działało i nikt się nie włamał". Bogumił pilnuje domeny, SSL, uptime'u strony, Windows i reaguje gdy coś się dzieje.

Gdy klient ma zainstalowaną aplikację **ClawLabs Office** na Windows, Bogumił może samodzielnie sprawdzać komputer przez lokalny most MCP (`http://172.17.0.1:3001/mcp` — `shell_ps`, `exec`, `fs_read`, `os_info`).

---

## Zawartość KB

| Plik | Opis |
|---|---|
| `monitoring/domena-ssl-uptime.md` | Jak sprawdzać WHOIS, SSL, uptime; progi alertów; co mówić klientowi; popularne rejestry PL |
| `monitoring/raport-tygodniowy.md` | Format cotygodniowego raportu poniedziałkowego; 4 przykłady (OK, ostrzeżenie, incydent, krytyczne) |
| `incydenty/phishing.md` | Rozpoznanie phishingu; 3 scenariusze reakcji; RODO Art. 33; prewencja |
| `incydenty/ransomware.md` | Pierwsze kroki (sieć OFF, nie gasić); ścieżki odbudowy; No More Ransom; zgłoszenie UODO |
| `incydenty/podejrzane-logowanie.md` | Diagnoza; kompromitacja emaila / serwera / Windows; logi Event 4625/4624; prewencja |
| `windows/health-check.md` | 8 komend PowerShell z wyjaśnieniem; czerwone flagi; raport dla klienta; tryb bez desktop app |
| `checklisty/onboarding-klienta.md` | Sekwencja 5 kroków; tabela informacji do zebrania; szablon `memory/firma.md`; raport powitalny |
| `checklisty/audyt-miesięczny.md` | Pełna lista kontrolna; progi eskalacji; format raportu; schemat zapisu `memory/audyt/YYYY-MM.md` |

---

## Jak Bogumił korzysta z KB

1. **Nowy klient** → `checklisty/onboarding-klienta.md` → przeprowadza naturalną rozmowę, zapisuje profil, ustawia przypomnienia
2. **Poniedziałek rano** → `monitoring/domena-ssl-uptime.md` + `monitoring/raport-tygodniowy.md` → sprawdza i wysyła raport
3. **Pierwszy tydzień miesiąca** → `checklisty/audyt-miesięczny.md` → pełny audyt, windows health check
4. **Klient zgłasza problem** → odpowiedni plik `incydenty/` → krok po kroku przez reakcję
5. **„Komputer działa wolno"** → `windows/health-check.md` → diagnostyka przez desktop app lub ręczne komendy

---

## Źródła

- **CERT Polska** — cert.pl — incydenty, alerty, dobre praktyki w Polsce
- **UODO** — uodo.gov.pl — RODO, naruszenia danych, zgłoszenia
- **NASK / rejestr .pl** — dns.pl — WHOIS dla domen .pl
- **No More Ransom** — nomoreransom.org/pl — darmowe dekryptory ransomware
- **Microsoft Security Docs** — learn.microsoft.com — Windows Defender, PowerShell, Event Log

---

## Zastrzeżenia

Praktyczne wytyczne operacyjne — nie usługa audytu bezpieczeństwa ani porada prawna.

Przy poważnych incydentach (ransomware, aktywny wyciek danych, infrastruktura krytyczna):
- Profesjonalna firma forensyczna
- Zgłoszenie do **CERT Polska** (incydent.cert.pl)
- Zgłoszenie do **UODO** jeśli dane osobowe (72h od stwierdzenia naruszenia — Art. 33 RODO)
- Przy dużych stratach finansowych — **Policja** (cyberprzestepczos.pl)

Bogumił nie zastępuje specjalisty od cyberbezpieczeństwa przy poważnych atakach.

## Status

- **Wersja:** 0.1.0
- **Data:** 2026-04-29
- **Plików KB:** 8
- **Status:** Beta — do walidacji na żywych rozmowach z klientami
