# Setup Guide - Project One

## Prerequisites

- **Python:** 3.11 or higher
- **OpenClaw CLI:** Installed and authenticated
- **GitHub CLI:** `gh auth status` should show authentication
- **Git:** Version 2.x or higher
- **Redis:** (Optional, if using Luna messaging patterns)

## Development Environment Setup

### 1. Clone the Repository

```bash
git clone git@github.com:robertoronderosjr/project-one.git
cd project-one
```

### 2. Create Virtual Environment

```bash
# Using Python's built-in venv
python3.11 -m venv .venv

# Activate (Linux/macOS)
source .venv/bin/activate

# Activate (Windows)
.venv\Scripts\activate
```

### 3. Install Dependencies

```bash
# Install package in editable mode with dev dependencies
pip install -e ".[dev]"

# Verify installation
python -c "import project_one; print(project_one.__version__)"
```

### 4. Verify Tools

```bash
# Run tests
pytest tests/ -v

# Check code quality
ruff check src/ tests/
pyright src/

# Check coverage
pytest tests/ --cov=src --cov-report=term-missing
```

All checks should pass with no errors.

## AI Agent Configuration

Project One uses Luna-style AI agent deployment. See `BOOTSTRAP.md` for complete setup.

### Agent Spawn Scripts

Located in `config/`:
- `spawn-engineer.sh` - Software Engineer agent

### Manual Agent Spawn

```bash
# Spawn engineer for a specific task
./config/spawn-engineer.sh "Implement feature from issue #123"

# Check active sessions
openclaw sessions list | grep proj-1
```

### Automated Scheduling (Cron)

See `config/cron-jobs.sh` for recommended cron schedule:
- Engineer: 9AM, 2PM, 8PM ET

## Project Structure

```
project-one/
├── src/
│   └── project_one/       # Main package
│       └── __init__.py
├── tests/
│   ├── unit/              # Unit tests
│   ├── integration/       # Integration tests
│   └── conftest.py        # Pytest configuration
├── docs/
│   ├── SETUP.md          # This file
│   ├── ARCHITECTURE.md   # Architecture overview
│   ├── PRD.md            # Product requirements
│   ├── TRD.md            # Technical requirements
│   └── adr/              # Architecture decision records
├── agents/
│   ├── engineer.md       # Engineer agent prompt
│   └── README.md         # Agent roster
├── config/
│   ├── spawn-engineer.sh # Agent spawn scripts
│   └── cron-jobs.sh      # Recommended cron schedule
├── .github/
│   └── workflows/
│       └── ci.yml        # CI/CD pipeline
├── pyproject.toml        # Project metadata & dependencies
├── BOOTSTRAP.md          # Bootstrap completion guide
└── README.md             # Project overview
```

## Running Tests

### All Tests

```bash
pytest tests/ -v
```

### Unit Tests Only

```bash
pytest tests/unit/ -v
```

### Integration Tests Only

```bash
pytest tests/integration/ -v
```

### With Coverage

```bash
pytest tests/ --cov=src --cov-report=html
# Open htmlcov/index.html in browser
```

### Watch Mode (requires pytest-watch)

```bash
pip install pytest-watch
ptw -- tests/ -v
```

## Code Quality

### Linting

```bash
# Check for issues
ruff check src/ tests/

# Auto-fix issues
ruff check --fix src/ tests/
```

### Type Checking

```bash
pyright src/
```

### Dead Code Detection

```bash
vulture src/ --min-confidence 80
```

## Common Tasks

### Add a New Feature

1. Create an issue with `agent:engineer` label
2. Wait for scheduled agent run (or spawn manually)
3. Agent will create branch, implement, test, and open PR
4. Review and merge

### Add a New Dependency

```bash
# Edit pyproject.toml
# Add to dependencies array
# Reinstall
pip install -e ".[dev]"
```

### Update Documentation

Edit relevant file in `docs/` and commit.

### Create an ADR (Architecture Decision Record)

```bash
# Copy template
cp docs/adr/ADR-000-template.md docs/adr/ADR-NNN-<topic>.md

# Edit and commit
```

## Troubleshooting

### Import Errors

```bash
# Ensure package is installed in editable mode
pip install -e .

# Verify PYTHONPATH includes src/
echo $PYTHONPATH
```

### Test Failures

```bash
# Run with verbose output
pytest tests/ -vv

# Run specific test
pytest tests/unit/test_sample.py::test_basic_assertion -vv

# Run with pdb on failure
pytest tests/ --pdb
```

### Agent Not Spawning

```bash
# Check script is executable
ls -l config/spawn-engineer.sh

# Check OpenClaw status
openclaw gateway status

# Test manual spawn
./config/spawn-engineer.sh "test spawn"
```

## Additional Resources

- **Luna Framework:** https://github.com/robertoronderosjr/luna-framework
- **OpenClaw Docs:** https://docs.openclaw.com
- **Project Issues:** https://github.com/robertoronderosjr/project-one/issues

## Getting Help

1. Check existing GitHub issues
2. Review agent logs in `logs/`
3. Consult Luna framework documentation
4. Create new issue with `agent:po` label for questions

---

**Last Updated:** 2026-02-08
