# Maccabee Intelligence

**Materials Markets Intelligence Dashboard**

An automated commodities market intelligence system powered by OpenClaw.

## What It Does

### Current System
1. **Daily Materials Morning Brief** at 8:00am CT covering:
   - Top 5 global developments affecting commodity supply/demand
   - Flow signals: sanctions, shipping disruptions, inventory moves
   - Materials watchlist: Defense, EV/Grid, Energy, Construction
   - Price snapshots for key commodities
   - Source links for audit

2. **Gmail Integration** - monitors for unread messages, summarizes them, waits for confirmation before acting

3. **Live Dashboard** - web UI showing latest briefs, price ticker, and history

### Planned Agent-Based Analysis Shop
**11 Specialized OpenClaw Agents** providing comprehensive commodities intelligence:

**Collection Agents:**
- Global Events Monitor - geopolitical events affecting markets
- Supply Chain Intelligence - shipping, inventory, infrastructure disruptions  
- Demand Signal Analyzer - consumption patterns and demand drivers

**Analysis Agents:**
- Price Pattern Recognition - technical analysis and signals
- Cross-Asset Correlations - multi-asset relationship analysis
- Fundamental Valuation - fair value estimation using supply/demand models

**Strategy Agents:**
- Strategy Backtester - rigorous testing of trading strategies
- Portfolio Optimizer - optimal commodity portfolio construction
- Risk Manager - real-time risk monitoring and alerts

**Reporting Agents:**
- Daily Brief Generator - synthesizes all outputs into actionable intelligence
- Weekly Strategy Review - comprehensive strategy performance and outlook

See `AGENT_ARCHITECTURE.md` for complete specifications.

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
