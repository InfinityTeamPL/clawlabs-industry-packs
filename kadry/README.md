# Janina Kadrowa — paczka branżowa "kadry"

## Czym jest

Agentka AI specjalizująca się w sprawach kadrowych i płacowych: Kodeks Pracy, umowy, urlopy, BHP, RODO w HR, onboarding, offboarding, rekrutacja. Projektowana jako osoba z 20-letnim stażem w polskich działach HR — ciepła, konkretna, na "ty", ale profesjonalna.

## Status

- **Wersja KB:** 0.1.0 (pierwszy draft, do walidacji)
- **Data utworzenia:** 2026-04-21
- **Status:** ⚠️ **Beta — w trenowaniu.** Janina żyje na VM admina (ClawLabs PRO), iteracje SOUL/IDENTITY/KB po rozmowach testowych. **Nie jest jeszcze dostępna jako produkt** dla użytkowników ClawLabs PRO.
- **Docelowo:** Stripe plan "Kadry", snapshot Hetznera `HETZNER_SNAPSHOT_JANINA`, UI `/kadry` na platformie

## Identyfikator paczki

```
industryPackId: "kadry"
displayName: "Janina — Kadry i Płace"
model: "minimax-m2.7-highspeed" (opcjonalnie BYOK: Claude/GPT/Gemini)
```

Runtime manifest: [`clawlabspro/src/lib/industry-packs/kadry.ts`](../../clawlabspro/src/lib/industry-packs/kadry.ts)

## Zawartość paczki

### Knowledge Base (36 plików, ~230 KB)
- **Kodeks Pracy** — 9 plików: rodzaje umów, rozwiązanie, czas pracy, urlopy, uprawnienia rodzicielskie, BHP, mobbing, jawność płac 2026, staż pracy 2026
- **RODO** — 7 plików: podstawy dla HR, art. 6/9, klauzule (rekrutacja/zatrudnienie/monitoring), prawa osób, rejestr czynności, naruszenia
- **Wzory umów** — 7 plików: UoP (próba/nieokreślona), zlecenie, B2B, wypowiedzenie, porozumienie, świadectwo pracy
- **Wynagrodzenia** — płaca minimalna 2026, składniki/potrącenia
- **BHP** — szkolenia, badania lekarskie
- **Urlopy** — wymiar/naliczanie, rodzaje
- **Checklisty** — onboarding, offboarding, rekrutacja, audyt kadrowy

### Skille (13 planowanych, 8 zainstalowanych)
✅ `calendar`, `note-taker`, `reminder`, `web-search`, `summarizer`, `csv-analyzer`, `file-manager`, `invoice-generator`  
❌ `pdf-reader`, `email-drafter`, `knowledge-base`, `translator`, `url-reader` (brak w ClawHub — do uzupełnienia)

## Jak używać

### Dev (iteracje KB przed snapshotem)
```bash
# z katalogu clawlabspro
npx tsx scripts/push-janina-kb.ts --apply
```
Skrypt wgrywa zawartość `../clawlabs-industry-packs/kadry/kb/` na żywą VM Janiny.

### Prod (po snapshotowaniu — docelowo)
Klient wykupuje subskrypcję "Kadry" → Stripe webhook tworzy agenta → provisioner z `HETZNER_SNAPSHOT_JANINA` → klient dostaje w pełni skonfigurowaną Janinę w < 2 min.

## Aktualizacje prawa 2026

Kluczowe zmiany śledzone w [`kb/aktualizacje-2026.md`](kb/aktualizacje-2026.md):

| Zmiana | Data wejścia | Status KB |
|--------|--------------|-----------|
| Płaca min. 4 806 zł / 31,40 zł/h | 01.01.2026 | ✅ w KB |
| Ekwiwalent urlopowy do 25 maja | 01.01.2026 | ✅ w KB |
| Staż pracy — zlecenia/JDG/zagranica (sektor publiczny) | 01.01.2026 | ✅ w KB |
| Staż pracy — sektor prywatny | 01.05.2026 | ✅ w KB |
| Jawność płac (dyrektywa 2023/970) | 07.06.2026 | ✅ w KB |
| Ustawa antymobbingowa (min. 6× min. wynagrodzenia) | W pracach | ⚠️ śledzić |

## Co sprawdzić przed snapshotem produkcyjnym

- [ ] Czy Janina korzysta z `memory/kadry/` w odpowiedziach (testy rozmowne)
- [ ] Czy ton pasuje do "kadrowej 20 lat" (nie za formalnie, nie za luźno)
- [ ] Czy skieruje do radcy prawnego przy sporach/sądach/mobbingu
- [ ] Czy RODO reakcja na "daj dane X" jest właściwa (pyta o podstawę)
- [ ] Czy `pdf-reader` zastępnik znaleziony dla parsowania CV
- [ ] Czy `BOOTSTRAP.md` jest usuwany po pierwszej rozmowie (design)
- [ ] Czy KB jest aktualna (data sprawdzenia na dziś)

## Disclaimers

> Opracowania praktyczne, **nie porada prawna**. Dla sprawy klienta zawsze weryfikacja w ISAP + radca prawny przy sporach. Księgowa do wyliczeń podatkowo-składkowych.
>
> Prawo zmienia się — każdą kwotę i każdy paragraf Janina sprawdza w dniu użycia.
