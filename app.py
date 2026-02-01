#!/usr/bin/env python3
"""
Commodities Dashboard - Materials Markets Intelligence
Serves OpenClaw cron brief summaries and live market data
"""

import json
import os
from datetime import datetime
from pathlib import Path
from flask import Flask, render_template, jsonify
import subprocess

app = Flask(__name__)

# Configuration
OPENCLAW_CRON_DIR = Path.home() / ".openclaw" / "cron" / "runs"
MATERIALS_BRIEF_JOB_ID = "d29191e6-caa3-46cc-825f-f62154338720"

def get_latest_brief():
    """Read the latest materials morning brief from OpenClaw cron runs"""
    brief_file = OPENCLAW_CRON_DIR / f"{MATERIALS_BRIEF_JOB_ID}.jsonl"
    
    if not brief_file.exists():
        return None
    
    briefs = []
    with open(brief_file, 'r') as f:
        for line in f:
            try:
                entry = json.loads(line.strip())
                if entry.get("status") == "ok" and entry.get("summary"):
                    briefs.append(entry)
            except json.JSONDecodeError:
                continue
    
    if not briefs:
        return None
    
    # Return the most recent brief
    latest = max(briefs, key=lambda x: x.get("ts", 0))
    return {
        "content": latest.get("summary", ""),
        "timestamp": datetime.fromtimestamp(latest["ts"] / 1000).strftime("%Y-%m-%d %H:%M:%S %Z"),
        "duration_seconds": latest.get("durationMs", 0) / 1000,
        "run_at": datetime.fromtimestamp(latest["runAtMs"] / 1000).strftime("%Y-%m-%d %H:%M:%S"),
    }

def get_all_briefs():
    """Get all historical briefs"""
    brief_file = OPENCLAW_CRON_DIR / f"{MATERIALS_BRIEF_JOB_ID}.jsonl"
    
    if not brief_file.exists():
        return []
    
    briefs = []
    with open(brief_file, 'r') as f:
        for line in f:
            try:
                entry = json.loads(line.strip())
                if entry.get("status") == "ok" and entry.get("summary"):
                    briefs.append({
                        "content": entry.get("summary", ""),
                        "timestamp": datetime.fromtimestamp(entry["ts"] / 1000).strftime("%Y-%m-%d %H:%M:%S"),
                        "run_at": datetime.fromtimestamp(entry["runAtMs"] / 1000).strftime("%Y-%m-%d %H:%M:%S"),
                    })
            except json.JSONDecodeError:
                continue
    
    return sorted(briefs, key=lambda x: x["timestamp"], reverse=True)

def fetch_live_prices():
    """Fetch current commodity prices using gog or web sources"""
    # This could be expanded to pull from APIs
    # For now, return placeholder that can be updated
    return {
        "copper_hg": {"price": "4.12", "unit": "USD/lb", "change": "+0.8%"},
        "aluminum_lme": {"price": "2,340", "unit": "USD/t", "change": "-0.3%"},
        "wti_crude": {"price": "73.45", "unit": "USD/bbl", "change": "+1.2%"},
        "natural_gas": {"price": "2.89", "unit": "USD/MMBtu", "change": "+3.4%"},
        "uranium_spot": {"price": "106.50", "unit": "USD/lb", "change": "+0.5%"},
        "lithium_carbonate": {"price": "12,800", "unit": "USD/t", "change": "-2.1%"},
        "nickel_lme": {"price": "16,450", "unit": "USD/t", "change": "+0.9%"},
        "iron_ore": {"price": "108.20", "unit": "USD/t", "change": "-0.4%"},
    }

def trigger_brief_refresh():
    """Trigger a new brief generation via OpenClaw cron"""
    try:
        result = subprocess.run(
            ["openclaw", "cron", "run", MATERIALS_BRIEF_JOB_ID, "--force"],
            capture_output=True,
            text=True,
            timeout=5
        )
        return {"status": "triggered", "message": "Brief generation started"}
    except subprocess.TimeoutExpired:
        return {"status": "triggered", "message": "Brief generation started (running in background)"}
    except Exception as e:
        return {"status": "error", "message": str(e)}

@app.route("/")
def index():
    """Main dashboard page"""
    brief = get_latest_brief()
    prices = fetch_live_prices()
    return render_template("dashboard.html", brief=brief, prices=prices)

@app.route("/api/brief")
def api_brief():
    """API endpoint for latest brief"""
    brief = get_latest_brief()
    return jsonify(brief)

@app.route("/api/briefs")
def api_briefs():
    """API endpoint for all briefs"""
    briefs = get_all_briefs()
    return jsonify(briefs)

@app.route("/api/prices")
def api_prices():
    """API endpoint for commodity prices"""
    prices = fetch_live_prices()
    return jsonify(prices)

@app.route("/api/refresh", methods=["POST"])
def api_refresh():
    """Trigger a new brief generation"""
    result = trigger_brief_refresh()
    return jsonify(result)

@app.route("/history")
def history():
    """View all historical briefs"""
    briefs = get_all_briefs()
    return render_template("history.html", briefs=briefs)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5050, debug=True)
