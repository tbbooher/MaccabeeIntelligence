#!/bin/bash
# Maccabee Intelligence Agent Deployment Script
# Run this on diomedes after transferring the agent configs

set -e

echo "🚀 Deploying Maccabee Intelligence Agent System"

# Check OpenClaw is available
if ! command -v openclaw &> /dev/null; then
    echo "❌ OpenClaw not found. Please install OpenClaw first."
    exit 1
fi

# Phase 1: Core Intelligence Agents
echo "📡 Phase 1: Deploying Collection Agents..."

# Deploy global events monitor
if [ -d "agents/global-events-monitor" ]; then
    echo "  Deploying global-events-monitor..."
    openclaw agent deploy agents/global-events-monitor/
    openclaw cron enable global-events-monitor
else
    echo "  ⚠️  global-events-monitor config not found"
fi

# Deploy daily brief generator
if [ -d "agents/daily-brief" ]; then
    echo "  Deploying daily-brief..."
    openclaw agent deploy agents/daily-brief/
    openclaw cron enable daily-brief
else
    echo "  ⚠️  daily-brief config not found"
fi

# Check deployment status
echo "📊 Checking agent status..."
openclaw agent status --all

echo "✅ Phase 1 deployment complete!"
echo ""
echo "Next steps:"
echo "1. Monitor logs: openclaw logs --agent=daily-brief --tail=50"
echo "2. Test manual run: openclaw cron run daily-brief --force"
echo "3. Check cron schedule: openclaw cron list"
echo ""
echo "The daily brief will run automatically at 8:00 AM CT"
