# Maccabee Intelligence Agent Architecture

## Overview
OpenClaw-powered commodities analysis shop using specialized agents for comprehensive market intelligence, strategy development, and portfolio management.

## Agent Ecosystem

### Tier 1: Data Collection Agents

#### 1. Global Events Monitor (`global-events-monitor`)
**Purpose**: Track geopolitical events affecting commodity markets
**Sources**: Reuters, Bloomberg, government sites, trade publications
**Output**: Structured event data with impact scoring
**Schedule**: Every 2 hours
**Key Metrics**:
- Event severity (1-10)
- Affected commodities
- Timeline impact (immediate/short/long-term)

#### 2. Supply Chain Intelligence (`supply-chain-intel`)
**Purpose**: Monitor physical commodity flows and disruptions
**Sources**: Shipping data, port authorities, pipeline operators
**Output**: Supply chain status reports
**Schedule**: Every 4 hours
**Key Metrics**:
- Chokepoint congestion levels
- Inventory changes at key facilities
- Transportation cost indices

#### 3. Demand Signal Analyzer (`demand-signals`)
**Purpose**: Track consumption patterns and demand drivers
**Sources**: Industrial production data, construction permits, EV sales
**Output**: Demand trend analysis
**Schedule**: Daily
**Key Metrics**:
- Sector-specific demand growth
- Leading indicators correlation
- Seasonal adjustment factors

### Tier 2: Analysis Agents

#### 4. Price Pattern Recognition (`price-patterns`)
**Purpose**: Technical analysis and pattern detection
**Sources**: Futures exchanges, spot markets, historical data
**Output**: Technical signals and pattern alerts
**Schedule**: Every 15 minutes during market hours
**Key Metrics**:
- Momentum indicators
- Support/resistance levels
- Volatility regime classification

#### 5. Cross-Asset Correlations (`correlation-analyzer`)
**Purpose**: Identify relationships between commodities, currencies, equities
**Sources**: Multi-asset price feeds
**Output**: Correlation matrices and regime changes
**Schedule**: Daily
**Key Metrics**:
- Rolling correlation coefficients
- Regime change detection
- Diversification opportunities

#### 6. Fundamental Valuation (`fundamental-value`)
**Purpose**: Fair value estimation using supply/demand models
**Sources**: Production costs, inventory data, consumption forecasts
**Output**: Fair value estimates and over/under-valued signals
**Schedule**: Weekly
**Key Metrics**:
- Cost curve analysis
- Inventory-to-consumption ratios
- Price elasticity estimates

### Tier 3: Strategy Agents

#### 7. Strategy Backtester (`strategy-backtest`)
**Purpose**: Test trading strategies against historical data
**Sources**: Historical price data, fundamental data
**Output**: Strategy performance reports
**Schedule**: On-demand
**Key Metrics**:
- Sharpe ratio, Sortino ratio
- Maximum drawdown
- Win rate and profit factor

#### 8. Portfolio Optimizer (`portfolio-optimizer`)
**Purpose**: Construct optimal commodity portfolios
**Sources**: Expected returns, risk models, correlation data
**Output**: Portfolio allocation recommendations
**Schedule**: Weekly
**Key Metrics**:
- Risk-adjusted returns
- Portfolio volatility
- Concentration limits

#### 9. Risk Manager (`risk-manager`)
**Purpose**: Monitor portfolio risk and generate alerts
**Sources**: Position data, market data, volatility models
**Output**: Risk reports and limit breach alerts
**Schedule**: Real-time during market hours
**Key Metrics**:
- Value at Risk (VaR)
- Expected shortfall
- Concentration risk

### Tier 4: Reporting Agents

#### 10. Daily Brief Generator (`daily-brief`)
**Purpose**: Synthesize all agent outputs into actionable intelligence
**Sources**: All other agents
**Output**: Daily commodities intelligence report
**Schedule**: 8:00 AM CT
**Key Sections**:
- Executive summary
- Market movers
- Strategy recommendations
- Risk alerts

#### 11. Weekly Strategy Review (`weekly-strategy`)
**Purpose**: Comprehensive strategy performance and market outlook
**Sources**: Strategy backtester, portfolio optimizer, fundamental valuation
**Output**: Weekly strategy report
**Schedule**: Sunday 6:00 PM CT
**Key Sections**:
- Strategy performance review
- Market outlook
- Portfolio rebalancing recommendations
- New opportunity identification

## Data Flow Architecture

```
Raw Data Sources → Collection Agents → Analysis Agents → Strategy Agents → Reporting Agents → Dashboard
```

## Agent Communication Protocol

### Message Types
- **DATA_UPDATE**: Raw data from collection agents
- **ANALYSIS_RESULT**: Processed insights from analysis agents
- **STRATEGY_SIGNAL**: Trading signals from strategy agents
- **RISK_ALERT**: Risk warnings from risk manager
- **REPORT_READY**: Completed reports from reporting agents

### Data Schema
```json
{
  "timestamp": "ISO8601",
  "agent_id": "string",
  "message_type": "enum",
  "commodity": "string",
  "data": {},
  "confidence": "float",
  "expiry": "ISO8601"
}
```

## Quality Control

### Agent Health Monitoring
- Response time tracking
- Data freshness validation
- Error rate monitoring
- Output quality scoring

### Data Validation
- Source reliability scoring
- Cross-validation between agents
- Anomaly detection
- Historical consistency checks

## Deployment Strategy

### Phase 1: Core Intelligence (Weeks 1-2)
- Deploy collection agents (1-3)
- Basic analysis agents (4-5)
- Daily brief generator (10)

### Phase 2: Strategy Development (Weeks 3-4)
- Strategy backtester (7)
- Portfolio optimizer (8)
- Weekly strategy review (11)

### Phase 3: Risk Management (Weeks 5-6)
- Risk manager (9)
- Advanced analysis agents (6)
- Full integration testing

### Phase 4: Production Hardening (Weeks 7-8)
- Monitoring and alerting
- Disaster recovery
- Performance optimization
