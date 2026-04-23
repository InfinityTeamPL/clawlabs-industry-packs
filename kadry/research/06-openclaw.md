# OpenClaw 2026 — nowe featury dla HR agenta (2026-04-22)

## 1. Wersja

- Nasza Janina: **2026.4.15**
- Aktualna npm `latest`: **2026.4.20**
- `beta`: **2026.4.20-beta.2**
- Między 4.15 a 4.20: 5 dni release'ów → changelog na GitHub Releases
- Cadence: `YYYY.M.D`, beta-first
- Repo: github.com/openclaw/openclaw (owner: steipete)
- Release notes: https://github.com/openclaw/openclaw/releases

## 2. Nowe featury (2025-2026)

### Active Memory (plugin)
Blokujący sub-agent pamięci odpalany **przed** główną odpowiedzią — recall z memory files/vectora zanim model odpowie.
Config: `plugins.entries.active-memory`
Docs: https://docs.openclaw.ai/concepts/active-memory.md

### Memory Wiki (plugin `memory-wiki`)
Kompiluje `MEMORY.md` w wiki vault z claimami/evidence/contradictions/dashboardami.
Tryby: `isolated` / `bridge` / Obsidian.
Narzędzia: `wiki_search`, `wiki_get`, `wiki_apply`, `wiki_lint`
Docs: https://docs.openclaw.ai/plugins/memory-wiki.md

### Memory backendy
- **Builtin** — SQLite + hybrid search
- **QMD** — local rerank + indeksy katalogów poza workspace (watcher na katalog)
- **Honcho** — cross-session, user modeling
- Auto-detect embedding: OpenAI / Gemini / Voyage / Mistral
- Docs: https://docs.openclaw.ai/concepts/memory.md

### Multi-agent routing
- Każdy agent: osobny `workspace`, `agentDir`, session store, auth profiles
- `agents.defaults.skills` + `agents.list[].skills` allowlist per-agent
- Docs: https://docs.openclaw.ai/concepts/multi-agent.md

### Standing Orders + Hooks
Eventy: `message:received`, `message:preprocessed`, `session:compact:before/after`, `agent:bootstrap`, `gateway:startup`
Docs: `/automation/hooks.md` i `/automation/standing-orders.md`

### Streaming (stan)
- Block streaming (paragrafy)
- Preview streaming (edit-in-place) dla Telegram/Discord/Slack
- **Brak token-delta dla kanałów**
- Docs: https://docs.openclaw.ai/concepts/streaming.md

### MCP (dwukierunkowy)
- `openclaw mcp serve` — OpenClaw jako MCP server po stdio/WS (konsumowany przez Claude Code/Codex)
- `openclaw mcp set/unset/list` — rejestruje outbound MCP servery dla agenta
- Wystawiane tools (outbound): `conversations_list`, `messages_read`, `events_wait`, `messages_send`, `permissions_list_open`
- Docs: https://docs.openclaw.ai/cli/mcp.md

### Inne z 2025-2026
- **Dreaming** (`/concepts/dreaming`)
- **Compaction** (`/concepts/compaction`)
- **Context Engine** (`/concepts/context-engine`)
- **Delegate Architecture** — sub-agents (`/concepts/delegate-architecture`)

## 3. Natywne tools (nie ClawHub)

- **PDF tool** — natywny Anthropic + Google + extraction fallback, multi-PDF do 10
- **Web Fetch** (Brave/Exa/Tavily/Perplexity)
- **Firecrawl**
- **apply_patch**
- **Webhooks plugin**

**Brak natywnie w docs:** OCR (scan), DOCX parser, IMAP/SMTP, iCal, e-podpis → wymagają własnych skilli lub MCP.

## 4. Skille HR (ClawHub)

- ClawHub = rejestr skilli
- Install: `openclaw skills install <slug>`
- Search: `openclaw skills search "calendar"`
- Docs: https://docs.openclaw.ai/tools/clawhub.md

## 5. Document watcher (auto-sync memory)

Brak dedykowanego pluginu. Złożenie:
- **QMD backend** z `extraDirs` (watcher na katalog)
- **Hook `agent:bootstrap`** — custom handler push plików
- **`openclaw cron`** — scheduled sync z Dropbox/SharePoint do MEMORY
- **Memory Wiki bridge mode** — import public artifacts

## 6. Multi-tenant (firma z wieloma pracownikami)

Dwa podejścia:
- **Multi-agent** — osobne workspace/sessions per pracownik
- **Session-level state** — jeden agent + routing per `threadId`/`recipient` w Gateway session metadata
- Pamięć workspace-level jest współdzielona w obrębie agenta

## 7. RAG / KB

- `memory_search` hybrid (vector + keyword)
- Auto-detect embedding provider
- QMD rerank
- Memory Wiki z provenance

## 8. Pamięć per user

- Multi-agent LUB session state keyed `agent:<id>:<mainKey>`
- Sessions: `~/.openclaw/agents/<agentId>/sessions`
- Workspace-level memory współdzielona w agencie

## Odpowiedzi na pytania wiodące (skrót)

| Pytanie | Status |
|---------|--------|
| Natywny document watcher? | NIE (złożenie QMD + hook + cron) |
| PDF/OCR/DOCX/e-sign/IMAP/iCal skille? | Tylko PDF natywnie; reszta custom/MCP |
| Własny MCP server z wiedzą? | TAK (`openclaw mcp set <id>`) |
| Multi-tenant? | Multi-agent albo session routing |
| RAG przeszukiwalny semantycznie? | TAK (memory_search hybrid) |
| Token-delta streaming? | NIE dla kanałów |
| Pamięć per user? | Multi-agent LUB session state |
