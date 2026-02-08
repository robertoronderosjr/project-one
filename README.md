# Project One

> **Bootstrap Status:** ⚠️ Deployment in progress — see `BOOTSTRAP.md` for completion steps

## Overview

[TODO: Add project description]

This project uses Luna-style AI agent deployment for autonomous development.

## Agent Team

| Agent | Model | Schedule | Status |
|-------|-------|----------|--------|
| Engineer | GPT-5.3 Codex | 9AM, 2PM, 8PM ET | ✅ Configured |
| Architect | TBD | TBD | ⏳ Not configured |
| Product Owner | TBD | TBD | ⏳ Not configured |

See `agents/README.md` for full roster and configuration.

## Quick Start

### Prerequisites

- OpenClaw CLI installed
- GitHub CLI authenticated: `gh auth status`
- Python 3.11+ (if applicable)
- Redis (if using Luna framework patterns)

### Setup

```bash
# Clone the repo
git clone git@github.com:robertoronderosjr/project-one.git
cd project-one

# Complete bootstrap (FIRST TIME ONLY)
# Follow steps in BOOTSTRAP.md

# Install dependencies (if Python project)
pip install -e .

# Run tests
pytest tests/
```

### Manual Agent Spawn

```bash
# Spawn the engineer for a specific task
./config/spawn-engineer.sh "Implement feature X from issue #123"

# Monitor agent activity
openclaw sessions list | grep proj-1
```

## Development Workflow

1. **Create Issue:** Use GitHub issues with appropriate labels (`agent:engineer`, `priority:p1`, etc.)
2. **Agent Picks Work:** Scheduled agents pick up labeled issues automatically
3. **Implementation:** Agent creates branch, implements feature, writes tests
4. **PR Review:** Agent opens PR, architect reviews (or manual review)
5. **Merge:** Approved PRs auto-merge via PR Merger agent

## Project Structure

```
project-one/
├── agents/              # Agent prompts and configuration
│   ├── engineer.md
│   └── README.md
├── config/              # Deployment configuration
│   ├── cron-jobs.sh
│   └── spawn-engineer.sh
├── docs/                # Project documentation
│   ├── PRD.md          # Product requirements
│   ├── TRD.md          # Technical requirements
│   └── adr/            # Architectural decisions
├── src/                 # Source code
├── tests/               # Test suite
├── .github/
│   └── workflows/
│       └── ci.yml      # CI/CD pipeline
├── logs/                # Agent activity logs
├── BOOTSTRAP.md         # Deployment completion guide
└── README.md           # This file
```

## Contributing

This project is primarily developed by AI agents. Human contributors should:

1. Create issues with clear acceptance criteria
2. Label issues appropriately for agent routing
3. Review PRs opened by agents
4. Update agent prompts if quality issues emerge

## Agent Monitoring

**View recent agent activity:**
```bash
openclaw sessions list --label proj-1-engineer
tail -f logs/engineer.log
```

**Check GitHub activity:**
```bash
gh pr list --label "agent:engineer"
gh issue list --label "agent:engineer"
```

**Spawn on-demand:**
```bash
./config/spawn-engineer.sh "Emergency fix for production issue"
```

## CI/CD

[TODO: Document CI/CD pipeline once configured]

## Deployment

[TODO: Document deployment process]

## License

[TODO: Add license]

## Changelog

- **2026-02-08:** Initial Luna deployment bootstrap
  - Engineer agent configured
  - Spawn scripts created
  - Cron scheduling ready

---

**Status:** Bootstrap phase — complete `BOOTSTRAP.md` to activate agents
