# Deployment Guide

## Prerequisites

1. **OpenClaw Installation**: Ensure OpenClaw is installed and configured on diomedes
2. **API Keys**: Set up environment variables for required APIs
3. **Database**: Configure data storage for agent outputs
4. **Monitoring**: Set up logging and alerting

## Environment Setup

### Required API Keys
```bash
# Add to ~/.bashrc or OpenClaw secrets
export ALPHA_VANTAGE_API_KEY="your_key_here"
export POLYGON_API_KEY="your_key_here"
export REUTERS_API_KEY="your_key_here"
export BLOOMBERG_API_KEY="your_key_here"
```

### Database Configuration
```bash
# PostgreSQL with TimescaleDB for time-series data
sudo apt install postgresql postgresql-contrib
sudo -u postgres createdb maccabee_intelligence
```

## Agent Deployment

### Phase 1: Core Intelligence (Week 1)
```bash
# Deploy collection agents
openclaw agent deploy agents/global-events-monitor/
openclaw agent deploy agents/supply-chain-intel/
openclaw agent deploy agents/demand-signals/

# Deploy basic analysis
openclaw agent deploy agents/price-patterns/
openclaw agent deploy agents/correlation-analyzer/

# Deploy reporting
openclaw agent deploy agents/daily-brief/

# Enable daily brief schedule
openclaw cron enable daily-brief
```

### Phase 2: Strategy Development (Week 2)
```bash
# Deploy strategy agents
openclaw agent deploy agents/strategy-backtester/
openclaw agent deploy agents/portfolio-optimizer/
openclaw agent deploy agents/weekly-strategy/

# Enable weekly strategy schedule
openclaw cron enable weekly-strategy
```

### Phase 3: Risk Management (Week 3)
```bash
# Deploy risk management
openclaw agent deploy agents/risk-manager/
openclaw agent deploy agents/fundamental-value/

# Enable real-time risk monitoring
openclaw agent start risk-manager --mode=realtime
```

## Monitoring & Maintenance

### Health Checks
```bash
# Check all agent status
openclaw agent status --all

# View recent logs
openclaw logs --agent=daily-brief --tail=100

# Monitor cron jobs
openclaw cron list --status
```

### Performance Monitoring
- Agent response times
- Data freshness
- Error rates
- Output quality scores

### Backup & Recovery
```bash
# Backup agent configurations
tar -czf agents-backup-$(date +%Y%m%d).tar.gz agents/

# Backup data
pg_dump maccabee_intelligence > backup-$(date +%Y%m%d).sql
```

## Troubleshooting

### Common Issues
1. **Agent Not Responding**: Check API rate limits and network connectivity
2. **Stale Data**: Verify data source availability and agent schedules
3. **Memory Issues**: Monitor agent memory usage and adjust limits
4. **Dependency Failures**: Check agent dependency chains

### Debug Commands
```bash
# Test individual agent
openclaw agent test global-events-monitor --dry-run

# Check agent dependencies
openclaw agent deps daily-brief

# View detailed logs
openclaw logs --agent=daily-brief --level=debug
```

## Security Considerations

### API Key Management
- Store keys in OpenClaw secrets, not environment variables
- Rotate keys regularly
- Monitor API usage for anomalies

### Data Protection
- Encrypt sensitive data at rest
- Use TLS for all API communications
- Implement access controls for reports

### Audit Trail
- Log all agent actions and decisions
- Track data lineage and sources
- Maintain configuration version history
