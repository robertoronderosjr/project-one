# Project One

**Test project for Luna Framework multi-agent deployment**

## Overview

Project One is a demonstration project showcasing the Luna Framework's self-configuring multi-agent orchestration capabilities. This project serves as a template and reference implementation for deploying Luna-managed agent teams.

## Project Status

**Version:** 0.1.0  
**Created:** 2026-02-08  
**Status:** 🚀 Bootstrap Phase  
**Active Agents:** 1 (Engineer)

## Quick Start

### Prerequisites

- OpenClaw Gateway running at `http://localhost:18789`
- Redis available (for A2A messaging and memory)
- GitHub CLI authenticated (`gh auth status`)
- Luna Framework installed at `/home/admin/projects/luna-framework`

### Deploy the Agent Team

```bash
# Bootstrap the engineer agent (already done if you're reading this)
cd /home/admin/projects/project-one
./bootstrap-engineer.py

# Verify deployment
openclaw sessions list | grep proj-1-engineer

# Manual spawn (reactive)
./config/spawn-engineer.sh "Work on issue #123"

# Scheduled runs (add to crontab)
crontab -e
# Add: 0 9,14,20 * * * /home/admin/projects/project-one/config/spawn-engineer.sh >> /home/admin/projects/project-one/logs/engineer.log 2>&1
```

## Agent Team

| Agent | Model | Schedule | Status |
|-------|-------|----------|--------|
| **Engineer** | GPT-5.3 Codex | 9AM, 2PM, 8PM ET | ✅ Active |

### Planned Agents

- **Architect** - Code review and architecture oversight
- **Product Owner** - Backlog management and prioritization
- **Research** - Investigation and prototyping
- **PR Merger** - Automated PR merging
- **Docs Keeper** - Documentation maintenance

See `agents/README.md` for full roster details.

## Project Structure

```
project-one/
├── agents/              # Agent prompt files
├── config/              # Spawn scripts and configuration
├── docs/                # Project documentation
├── logs/                # Agent activity logs
├── src/                 # Source code (to be created)
├── tests/               # Test suite (to be created)
└── .github/             # CI/CD workflows (to be created)
```

## Luna Framework Integration

This project is managed by Luna Framework v0.1.0, providing:

- ✅ **Self-configuring agents** - Agents design and coordinate their own work
- ✅ **Reactive spawning** - Agents spawn each other on-demand
- ✅ **A2A messaging** - Inter-agent communication via Redis Streams
- ✅ **Agent memory** - Episodic, procedural, and semantic memory
- ✅ **GitHub integration** - Automated issue/PR management
- ✅ **Quality gates** - Automated testing and validation

### Configuration Files

- **`luna-project.json`** - Luna Framework project configuration
- **`config/spawn-*.sh`** - Agent spawn scripts
- **`bootstrap-engineer.py`** - Initial deployment script

## Development Workflow

### For Humans

1. Create issues in GitHub with appropriate labels (`agent:engineer`, etc.)
2. Agents pick up labeled issues automatically
3. Review agent PRs and provide feedback
4. Monitor progress via GitHub Projects or OpenClaw dashboard

### For Agents

1. Check for assigned issues: `gh issue list --label "agent:engineer"`
2. Create feature branch: `git checkout -b feat/<topic>`
3. Implement with tests and documentation
4. Open PR with `gh pr create --fill`
5. Spawn architect for review
6. Iterate based on feedback
7. Merge when approved

See `agents/engineer.md` for detailed agent workflow.

## Monitoring

### Check Agent Status

```bash
# List active sessions
openclaw sessions list | grep proj-1

# View agent logs
tail -f logs/engineer.log

# Check deployment history
cat logs/deployments.log
```

### Dashboard Access

- **OpenClaw Dashboard:** http://localhost:18789
- **GitHub Repository:** github.com/robertoronderosjr/project-one (pending)
- **GitHub Project Board:** (pending configuration)

## Cost & Resource Management

**Daily Budget:** $10.00  
**Max Concurrent Agents:** 3  
**Working Hours:** 07:00-23:00 ET

**Current Cost:** ~$2-4/day (1 agent, 3 runs/day)

## Troubleshooting

### Agent Not Spawning

```bash
# Check OpenClaw gateway
curl http://localhost:18789/health

# Check Redis
redis-cli ping

# Re-run bootstrap
./bootstrap-engineer.py
```

### Agent Stuck or Failing

```bash
# View session logs
openclaw sessions logs <session-id> --tail 100

# Manual respawn
./config/spawn-engineer.sh "Resume previous work"
```

### GitHub Integration Issues

```bash
# Verify GitHub CLI auth
gh auth status

# Test repo access
gh repo view robertoronderosjr/project-one
```

## Contributing

This is an automated project managed primarily by AI agents. Human contributions should:

1. Create well-defined issues with acceptance criteria
2. Review and approve agent PRs
3. Provide feedback on agent work quality
4. Adjust agent prompts/configuration as needed

## Documentation

- **[BOOTSTRAP-REPORT.md](BOOTSTRAP-REPORT.md)** - Deployment bootstrap details
- **[agents/README.md](agents/README.md)** - Agent team roster and configuration
- **[config/cron-jobs.sh](config/cron-jobs.sh)** - Cron scheduling reference

## License

Private - robertoronderosjr

## Links

- **Luna Framework:** github.com/robertoronderosjr/luna-framework
- **OpenClaw:** github.com/OpenClaw/openclaw
- **Documentation:** (to be added)

---

**Bootstrapped:** 2026-02-08 01:51 EST  
**By:** Luna Framework subagent (luna-proj-1-engineer)
