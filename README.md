# Maccabee Intelligence

**Materials Markets Intelligence Dashboard**

An automated commodities market intelligence system powered by OpenClaw.

## What It Does

1. **Daily Materials Morning Brief** at 8:00am CT covering:
   - Top 5 global developments affecting commodity supply/demand
   - Flow signals: sanctions, shipping disruptions, inventory moves
   - Materials watchlist: Defense, EV/Grid, Energy, Construction
   - Price snapshots for key commodities
   - Source links for audit

2. **Gmail Integration** - monitors for unread messages, summarizes them, waits for confirmation before acting

3. **Live Dashboard** - web UI showing latest briefs, price ticker, and history

## Components

| Component | Port | Purpose |
|-----------|------|---------|
| OpenClaw Gateway | 18789 (TLS) | Agent orchestration |
| Flask Dashboard | 5050 | Web UI for briefs |

## Setup

```bash
# Create virtual environment
python3 -m venv venv
source venv/bin/activate
pip install flask

# Run dashboard
python3 app.py
```

## Cron Jobs

```bash
# List jobs
openclaw cron list

# Run brief manually
openclaw cron run <job-id> --force
```

## Design Principles

- **Read-only by default** — briefs summarize, they don't act
- **Confirmation required** — no auto-replies or auto-actions
- **Source quality bias** — IEA, EIA, LME, Reuters over blogs
- **No investment advice** — analysis only

## License

Private
