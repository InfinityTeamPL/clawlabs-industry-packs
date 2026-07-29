# Changelog — bogumil

Format: [Keep a Changelog](https://keepachangelog.com/pl/1.1.0/). Semver per paczka: `bogumil/X.Y.Z`.

---

## [bogumil/0.1.0] — 2026-04-28

Pierwsze wdrożenie paczki IT i cyberbezpieczeństwa.

### Added

- **8 plików KB, ~60 KB:**
  - `monitoring/domena-ssl-uptime.md` — WHOIS PL (.pl przez NASK, inne przez ICANN), progi alertów (30/14/3 dni domena, 30/7 dni SSL), popularne rejestry PL (home.pl, nazwa.pl, OVH, Domeny.pl), grace period przy wygaśnięciu
  - `monitoring/raport-tygodniowy.md` — format cotygodniowego raportu poniedziałkowego, 4 przykłady (OK / ostrzeżenie / incydent / krytyczne), procedura przed wysłaniem
  - `incydenty/phishing.md` — rozpoznanie phishingu w Polsce (InPost/mBank/ZUS/BEC), 3 scenariusze (klik bez danych / wpisane hasło / dane bankowe), obowiązek UODO Art. 33, prewencja (Bitwarden, 2FA)
  - `incydenty/ransomware.md` — 4 natychmiastowe kroki (sieć off, nie gasić, nie płacić, napisz do Bogumił), 3 ścieżki odbudowy (backup / No More Ransom / forensics), RODO 72h, zgłoszenie CERT PL
  - `incydenty/podejrzane-logowanie.md` — diagnoza (5 pytań), reakcja na kompromitację emaila i serwera, komendy Event 4625/4624 przez desktop bridge, „logowanie z Ukrainy/Chin" — co znaczy
  - `windows/health-check.md` — 8 komend PowerShell (Defender, Updates, Event 4625/4624, procesy CPU, porty, autostart, zadania zaplanowane); czerwone flagi; raport dla klienta; tryb bez desktop app
  - `checklisty/onboarding-klienta.md` — 5-krokowa sekwencja pytań, tabela informacji, szablon `memory/firma.md`, raport powitalny
  - `checklisty/audyt-miesięczny.md` — pełna lista kontrolna (domena, SSL, uptime, Windows, backup, faktury, CMS), progi eskalacji, format raportu, schemat `memory/audyt/YYYY-MM.md`

### Kluczowe decyzje projektowe

- **v1 = monitoring + incydenty defensywne** — bez pentestingu, bez audytu kodu, bez zarządzania siecią
- **Desktop app jako opcjonalne wzmocnienie** — core wartość (monitoring domeny/SSL) działa bez desktop app; Windows health check dostępny tylko z desktop app
- **Ton: IT-znajomy, nie konsultant** — krótkie zdania, brak żargonu bez wyjaśnienia, jedno pytanie na raz
- **RODO Art. 33 flagowany przy każdym incydencie** z potencjalnym naruszeniem danych

### Źródła

- CERT Polska (cert.pl), UODO (uodo.gov.pl), NASK dns.pl, No More Ransom (nomoreransom.org/pl), Microsoft Security Docs
