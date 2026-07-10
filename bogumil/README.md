# Bogumił — paczka branżowa "bogumil"

## Czym jest

Agentka AI specjalizująca się w IT i cyberbezpieczeństwie dla małych firm bez działu IT: monitoring domeny/SSL/uptime, cotygodniowy raport statusu, reakcja na incydenty (phishing, ransomware, podejrzane logowania), miesięczny health check Windows. Projektowany jako IT-znajomy z 15-letnim stażem w polskich SMB — mówi po ludzku, nie straszy żargonem, działa konkretnie.

## Status

- **Wersja KB:** 0.1.0 (pierwszy draft, do walidacji)
- **Data utworzenia:** 2026-04-28
- **Status:** ⚠️ **Beta — nie dostępny jeszcze dla klientów ClawLabs PRO**
- **Docelowo:** Stripe plan "IT", snapshot Hetznera `HETZNER_SNAPSHOT_BOGUMIL`, UI `/bogumil` na platformie

## Identyfikator paczki

```
industryPackId: "bogumil"
displayName: "Bogumił — IT i Cyberbezpieczeństwo"
model: "minimax-m2.7-highspeed" (opcjonalnie BYOK: Claude/GPT/Gemini)
```

Runtime manifest: [`clawlabspro/src/lib/industry-packs/bogumil.ts`](../../clawlabspro/src/lib/industry-packs/bogumil.ts)

## Zawartość paczki

### Knowledge Base (8 plików)

- **monitoring/** — 2 pliki: domena/SSL/uptime (progi alertów, WHOIS PL, popularne rejestry), raport tygodniowy (4 przykładowe szablony)
- **incydenty/** — 3 pliki: phishing (3 scenariusze), ransomware (natychmiastowe kroki + No More Ransom), podejrzane logowanie (email/serwer/Windows)
- **windows/** — 1 plik: health check przez PowerShell / desktop bridge (8 komend z wyjaśnieniem)
- **checklisty/** — 2 pliki: onboarding klienta (5 kroków + szablon firma.md), audyt miesięczny (lista kontrolna + format raportu)

### Skille (7 zainstalowanych)
✅ `web-search`, `url-reader`, `reminder`, `note-taker`, `calendar`, `file-manager`, `csv-analyzer`

### Desktop app integration
Bogumił korzysta z lokalnego mostu MCP (`http://172.17.0.1:3001/mcp`) gdy klient ma ClawLabs Office na Windows — umożliwia diagnostykę komputera przez `shell_ps` / `exec` / `fs_read`.

## Jak używać

### Dev (iteracje KB przed snapshotem)
```bash
# z katalogu clawlabspro — gdy będzie gotowy skrypt push dla bogumil
npx tsx scripts/push-bogumil-kb.ts --apply
```

### Prod (po snapshotowaniu — docelowo)
Klient wykupuje subskrypcję "IT" → Stripe webhook tworzy agenta → provisioner z `HETZNER_SNAPSHOT_BOGUMIL` → klient dostaje Bogumił w < 2 min.

## Co sprawdzić przed snapshotem produkcyjnym

- [ ] Czy Bogumił poprawnie robi WHOIS lookup i interpretuje wyniki (testy rozmowne)
- [ ] Czy raport tygodniowy jest krótki i czytelny na telefonie
- [ ] Czy tone pasuje do "IT-znajomy" (nie za technicznie, nie za prosto)
- [ ] Czy odpowiedź na phishing / ransomware jest spokojna i konkretna (nie panikuje)
- [ ] Czy RODO Art. 33 jest flagowane przy incydentach naruszenia danych
- [ ] Czy zastrzeganie PESEL jest sugerowane przy kradzieży tożsamości (kontekst PL od XI.2024)
- [ ] Czy desktop app bridge działa (shell_ps przez 172.17.0.1:3001)
- [ ] Czy bez desktop app poprawnie prosi klienta o ręczne uruchomienie komend
- [ ] Czy zawsze pyta o **zgodę** przed uruchomieniem komend na komputerze klienta (nie wchodzi sam)
- [ ] Czy poprawnie deleguje sprawy kadrowe do Janiny (i odbiera incydenty IT od niej)
- [ ] Czy BOOTSTRAP.md jest usuwany po pierwszej rozmowie
- [ ] Czy KB jest aktualna (data sprawdzenia: 2026-04-29)

## Disclaimery

> Praktyczne wytyczne operacyjne, **nie audyt bezpieczeństwa ani porada prawna**. Przy poważnych incydentach Bogumił kieruje do profesjonalnej firmy forensycznej i CERT Polska. Przy naruszeniu danych — pomaga przygotować zgłoszenie do UODO (Art. 33 RODO), ale finalne zgłoszenie warto skonsultować z prawnikiem.
>
> Bogumił jest agentem AI — mówi to przy pierwszej rozmowie z nowym klientem.
