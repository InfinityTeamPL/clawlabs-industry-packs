# Sprawdzanie stanu systemu Windows (Health Check)

## Kiedy uruchamiać

1. **Rutyna miesięczna** — pierwszy tydzień miesiąca, część audytu miesięcznego
2. **Po incydencie** — podejrzane logowanie, wirus, coś dziwnego
3. **Na zgłoszenie klienta** — „komputer działa wolno", „coś jest nie tak", „dziwne okienka"

> **Wymagania:** PowerShell 5.1+ (standard na Windows 10/11) **uruchomiony jako Administrator** — komendy 3 i 4 (Event Log Security) bez elevacji zwracają błąd dostępu.

---

## Jak Bogumił wykonuje health check

Gdy klient ma zainstalowaną aplikację **ClawLabs Office** na Windows, Bogumił łączy się z lokalnym mostem MCP pod `http://172.17.0.1:3001/mcp` i wykonuje polecenia przez `shell_ps { cmd }`. Klient nie musi nic wpisywać — Bogumił działa samodzielnie i tłumaczy wyniki w prostym języku.

---

## Sekwencja komend

### 1. Status Windows Defendera

```powershell
Get-MpComputerStatus | Select-Object AMRunningMode, AntivirusEnabled, RealTimeProtectionEnabled, AntivirusSignatureLastUpdated
```

**Co pokazuje:** czy Defender jest aktywny, ochrona w czasie rzeczywistym, wiek definicji wirusów.

**Czerwone flagi:**
- `AntivirusEnabled = False` — antywirus wyłączony
- `RealTimeProtectionEnabled = False` — ochrona w czasie rzeczywistym wyłączona
- `AntivirusSignatureLastUpdated` starsze niż 3 dni — definicje przestarzałe
- `AMRunningMode = Passive` — Defender pasywny (inny AV przejął kontrolę — sprawdź czy legalny)

**Co mówię klientowi:** _„Sprawdziłem antywirusa. [Wszystko OK / Problem: ochrona jest wyłączona — włączymy ją]."_

---

### 2. Ostatnie aktualizacje Windows

```powershell
Get-HotFix | Sort-Object InstalledOn -Descending | Select-Object -First 10
```

**Co pokazuje:** 10 ostatnio zainstalowanych poprawek z datami.

**Czerwone flagi:**
- Brak aktualizacji od ponad 60 dni — niezałatane luki bezpieczeństwa
- Brak czegokolwiek — Windows Update może być wyłączony

**Co mówię klientowi:** _„Ostatnia aktualizacja była [X] dni temu. [OK / To za długo — sprawdzę dlaczego Windows się nie aktualizuje]."_

---

### 3. Nieudane próby logowania (Event ID 4625)

```powershell
Get-EventLog -LogName Security -InstanceId 4625 -Newest 20 2>$null
```

**Co pokazuje:** 20 ostatnich nieudanych logowań.

**Czerwone flagi:**
- Wiele prób w krótkim czasie — możliwy brute-force
- Próby z nieznanych kont (`administrator`, `admin`, `user`)
- Próby ze zdalnych adresów IP — logowanie sieciowe

**Co mówię klientowi:** _„Sprawdziłem próby logowania. [Czysto / Widzę [X] nieudanych prób — wygląda na automatyczny atak, zajmę się tym]."_

---

### 4. Udane logowania sieciowe (Event ID 4624)

```powershell
Get-EventLog -LogName Security -InstanceId 4624 -Newest 10 2>$null | Where-Object {$_.Message -match 'Network Information'}
```

**Co pokazuje:** udane logowania przez sieć (nie lokalnie przy klawiaturze).

**Czerwone flagi:**
- Logowania z nieznanych adresów IP lub w nocy / weekendy
- Konta nierozpoznane przez klienta
- Logowanie przez RDP bez wiedzy klienta

**Co mówię klientowi:** _„Ktoś logował się przez sieć [data, godzina]. Czy to byłeś Ty lub ktoś z firmy? Jeśli nie — musimy działać natychmiast."_

---

### 5. Procesy zużywające CPU

```powershell
Get-Process | Sort-Object CPU -Descending | Select-Object -First 15 Name,Id,CPU,WorkingSet
```

**Co pokazuje:** 15 procesów najbardziej obciążających procesor.

**Czerwone flagi:**
- Nieznane procesy z losowymi nazwami (`svchost32`, `winlogon64`, `update_helper`)
- 100% CPU bez wyraźnego powodu
- Wiele kopii tego samego procesu (10x `cmd.exe`)
- Procesy koparek kryptowalut (`xmrig`, `minerd`, `nicehash`)

**Co mówię klientowi:** _„Komputer jest [normalnie obciążony / przeciążony — widzę podejrzany proces X, sprawdzę co to]."_

---

### 6. Otwarte porty nasłuchujące

```powershell
netstat -ano | findstr LISTENING
```

*(wykonywane przez `exec { cmd }` w moście MCP)*

**Co pokazuje:** wszystkie porty na których komputer nasłuchuje połączeń.

**Czerwone flagi:**
- Port 3389 (RDP) otwarty na `0.0.0.0` — zdalny pulpit dostępny z internetu
- Port 445 (SMB) widoczny z zewnątrz — wektor ransomware WannaCry/Petya
- Nieznane porty >1024 słuchające na wszystkich interfejsach

**Co mówię klientowi:** _„Sprawdziłem otwarte porty. [OK / Port X jest otwarty i nie powinien być — zamknę go]."_

---

### 7. Programy uruchamiane przy starcie

```powershell
Get-CimInstance Win32_StartupCommand | Select-Object Name,Command,Location
```

**Co pokazuje:** wszystko co uruchamia się automatycznie przy starcie Windows.

**Czerwone flagi:**
- Wpisy wskazujące na pliki w `%TEMP%`, `%APPDATA%\Roaming`, podfolderach użytkownika
- Skrypty PowerShell lub BAT bez uzasadnienia
- Nieznane nazwy programów

**Co mówię klientowi:** _„Sprawdziłem co włącza się przy starcie. [Wygląda normalnie / Widzę podejrzany wpis X — usuniemy go]."_

---

### 8. Zadania zaplanowane spoza Microsoft

```powershell
Get-ScheduledTask | Where-Object {$_.State -eq 'Ready' -and $_.TaskPath -notlike '\Microsoft*'} | Select-Object TaskName,TaskPath
```

**Co pokazuje:** aktywne zadania zaplanowane nienależące do Microsoftu.

**Czerwone flagi:**
- Zadania z losowymi nazwami lub ścieżkami w folderach użytkownika
- Zadania uruchamiające PowerShell z parametrami Base64
- Zadania uruchamiane bardzo często (co minutę) bez uzasadnienia

**Co mówię klientowi:** _„Sprawdziłem zaplanowane zadania. [Czysto / Widzę nieznane zadanie X — sprawdzę co robi]."_

---

## Raport po health check

Bogumił tłumaczy wyniki krótko, bez żargonu:

```
Stan komputera — [Firma] — [data]

✅ Antywirus: aktywny, definicje aktualne
✅ Aktualizacje: ostatnia 8 dni temu (OK)
⚠️  Logowania: 47 nieudanych prób w ciągu 24h z zewnętrznego IP
    → Wyłączyłem zdalny dostęp RDP, zmień hasło do Windows w ciągu 24h
✅ Procesy: bez podejrzanych
✅ Porty: nic niepokojącego po zamknięciu RDP
✅ Autostart: czysto
✅ Zadania: nic podejrzanego
```

---

## Gdy klient nie ma aplikacji desktopowej

Bogumił prosi o ręczne uruchomienie skryptu. Gotowa wiadomość do wysłania:

> Cześć! Poproszę Cię o uruchomienie krótkiego skryptu diagnostycznego (ok. 2 minuty).
>
> 1. Naciśnij **Windows + X** → **Terminal Windows (Administrator)** lub **PowerShell (Administrator)**
> 2. Wklej poniższe i zatwierdź Enterem:
>
> ```powershell
> Get-MpComputerStatus | Select-Object AntivirusEnabled,RealTimeProtectionEnabled,AntivirusSignatureLastUpdated; Get-HotFix | Sort-Object InstalledOn -Descending | Select-Object -First 5; Get-Process | Sort-Object CPU -Descending | Select-Object -First 10 Name,CPU
> ```
>
> 3. Zrób zrzut ekranu (Win+Shift+S) i wyślij mi go.

Jeśli klient nie wie jak otworzyć PowerShell — Bogumił prowadzi go krok po kroku.
