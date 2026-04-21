# ClawLabs Industry Packs

Bazy wiedzy i gotowe paczki branżowe dla agentów ClawLabs PRO. Każda paczka to pełna "osoba" — np. **Janina Kadrowa** — z wiedzą ekspercką, wzorami dokumentów i procedurami specyficznymi dla branży.

## Dlaczego to osobne repo

Platforma ClawLabs PRO ([clawlabspro](../clawlabspro)) trzyma kod aplikacji. Tutaj trzymamy **treści** — bazę wiedzy, wzory, checklisty. Powody:

- Treści mają własny cykl życia (zmiany prawa co kwartał, nowe wzory co rok)
- Paczki branżowe rosną — kadry, medycyna, IT, budownictwo, logistyka, etc.
- Łatwiej PR-ować zmiany prawa bez dotykania kodu platformy
- Eksperci branżowi (prawnicy, HR-specjaliści) mogą contrybuować bez dostępu do platformy

## Struktura repo

```
clawlabs-industry-packs/
├── README.md                  # ten plik
├── CHANGELOG.md               # zmiany per paczka, per release
├── .gitignore
│
├── kadry/                     # Janina Kadrowa — kadry, płace, BHP, RODO
│   ├── README.md              # opis paczki, wersja KB, status
│   └── kb/                    # knowledge base (markdown)
│       ├── kodeks-pracy/
│       ├── rodo/
│       ├── wzory-umow/
│       ├── wynagrodzenia/
│       ├── bhp/
│       ├── urlopy/
│       ├── checklisty/
│       └── aktualizacje-2026.md
│
├── medycyna/                  # (planowane) agentka od gabinetu lekarskiego
├── it/                        # (planowane) agent od devops / support IT
└── ...
```

## Jak to współpracuje z platformą ClawLabs PRO

1. **Runtime manifest paczki** (soul, identity, bootstrap, tools, lista skilli) → w `clawlabspro/src/lib/industry-packs/<id>.ts`
2. **Baza wiedzy** (markdown, wzory) → tutaj w `./<id>/kb/`
3. **Skrypty operacyjne** (push KB na VM, build snapshotu) → w `clawlabspro/scripts/` — czytają KB stąd przez ścieżkę sibling lub env `INDUSTRY_PACKS_PATH`
4. **Snapshot Hetznera** (`HETZNER_SNAPSHOT_*`) — zbudowany raz z określonej wersji KB; przy aktualizacji KB → nowy snapshot albo hot-update przez push

## Konwencja per paczka

Każda paczka ma:

```
<id>/
├── README.md                 # nazwa agenta, wersja KB, ostatnia aktualizacja, planowane zmiany
├── CHANGELOG.md              # zmiany w tej paczce
├── kb/                       # markdown base (struktura dowolna, ale spójna w ramach paczki)
└── plans/                    # opcjonalne — plany rozwoju, wdrożenia
```

## Wersjonowanie

- **Tagi git:** `kadry/v1.0.0`, `kadry/v1.1.0` — semver per paczka
- **Runtime w clawlabspro** pinuje konkretną wersję KB: `kadryPack.kbVersion = "v1.0.0"`
- **Breaking changes** w KB (np. reorganizacja folderów) → major bump + aktualizacja scriptów

## Licencja

Prywatne. Wszystkie paczki są własnością Infinity Tech Group. Treści publiczne (cytaty z Kodeksu Pracy, ustawy, orzecznictwo) pochodzą z oficjalnych źródeł (ISAP, gov.pl, UODO, EUR-Lex) — opracowanie własne.

## Kontakt

contact@infinityteam.io
