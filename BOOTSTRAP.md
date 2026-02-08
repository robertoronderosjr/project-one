# Project One — Luna Deployment Bootstrap

This guide walks through completing the Luna agent deployment for Project One.

## What You Have

✅ **Engineer agent prompt** — `agents/engineer.md` (pre-configured)
✅ **Spawn scripts** — `config/spawn-engineer.sh` (executable)
✅ **Agent roster** — `agents/README.md` (documentation)
✅ **Project structure** — Basic directories created

## What You Need to Do

### 1. Initialize the GitHub Repository

```bash
cd /home/admin/projects/project-one

# Initialize git if not already done
git init
git add .
git commit -m "chore: initial Luna agent deployment bootstrap"

# Create GitHub repo (update username if different)
gh repo create robertoronderosjr/project-one --public --source=. --remote=origin --push

# Or connect to existing repo
# git remote add origin git@github.com:robertoronderosjr/project-one.git
# git push -u origin main
```

### 2. Create GitHub Labels

```bash
# Agent labels
gh label create "agent:engineer" --color "0E8A16" --description "Tasks for the Engineer agent"
gh label create "agent:architect" --color "1D76DB" --description "Tasks for the Architect agent"
gh label create "agent:po" --color "5319E7" --description "Tasks for the Product Owner agent"
gh label create "agent:research" --color "D93F0B" --description "Tasks for the Research agent"
gh label create "agent:docs" --color "C5DEF5" --description "Tasks for the Docs Keeper agent"
gh label create "agent:merger" --color "FBCA04" --description "Tasks for the PR Merger agent"

# Priority labels
gh label create "priority:p0" --color "B60205" --description "Critical priority"
gh label create "priority:p1" --color "D93F0B" --description "High priority"
gh label create "priority:p2" --color "FBCA04" --description "Medium priority"
gh label create "priority:p3" --color "0E8A16" --description "Low priority"

# Status labels
gh label create "status:blocked" --color "E99695" --description "Blocked by external dependency"
gh label create "status:in-review" --color "FEF2C0" --description "In code review"
gh label create "status:ready" --color "C2E0C6" --description "Ready to work on"
```

### 3. Set Up GitHub Project Board (Optional but Recommended)

```bash
# Create a project
gh project create --owner robertoronderosjr --title "Project One" --format table

# Get the project number (e.g., 3) from the output above, then add fields:
# Fields are added via GitHub web UI: Status, Priority, Agent, Estimate, etc.
# Visit: https://github.com/users/robertoronderosjr/projects/<number>
```

### 4. Configure Cron Jobs

```bash
# Edit crontab
crontab -e

# Add the Engineer agent schedule (9AM, 2PM, 8PM ET):
0 9,14,20 * * * /home/admin/projects/project-one/config/spawn-engineer.sh >> /home/admin/projects/project-one/logs/engineer.log 2>&1

# Optionally add other agents when ready:
# 0 2 * * * /home/admin/projects/project-one/config/spawn-architect.sh >> /home/admin/projects/project-one/logs/architect.log 2>&1
# 0 7,16,22 * * * /home/admin/projects/project-one/config/spawn-po.sh >> /home/admin/projects/project-one/logs/po.log 2>&1
```

### 5. Test the Engineer Agent Spawn

```bash
# Manual test (no cron)
/home/admin/projects/project-one/config/spawn-engineer.sh "Test spawn - verify setup is working"

# Check the spawn happened
openclaw sessions list | grep "proj-1-engineer"

# Check logs
tail -f /home/admin/projects/project-one/logs/engineer.log
```

### 6. Create Initial Issues

Create a few starter issues to give the engineer something to work on:

```bash
# Example: Setup CI
gh issue create \
  --title "Setup CI/CD pipeline" \
  --label "agent:engineer,priority:p1" \
  --body "Configure GitHub Actions for:\n- Python testing (pytest)\n- Linting (ruff, pyright)\n- Coverage reporting\n- Auto-merge approved PRs"

# Example: Project documentation
gh issue create \
  --title "Write project README and setup guide" \
  --label "agent:docs,priority:p2" \
  --body "Create comprehensive README with:\n- Project overview\n- Setup instructions\n- Development workflow\n- Deployment guide"

# Example: Core feature (customize to your project)
gh issue create \
  --title "Implement <feature name>" \
  --label "agent:engineer,priority:p0" \
  --body "Build <feature description>\n\nAcceptance Criteria:\n- [ ] AC1: <criterion>\n- [ ] AC2: <criterion>\n- [ ] Tests with ≥80% coverage\n- [ ] Documentation updated"
```

### 7. Project-Specific Configuration

Update these files for your specific project needs:

**`pyproject.toml`** (if Python project):
```bash
# Copy from luna-framework as template
cp ~/projects/luna-framework/pyproject.toml .
# Edit to match your project name, dependencies, etc.
```

**`README.md`**:
- Project description and goals
- Setup instructions
- Architecture overview
- Contributing guidelines

**`.github/workflows/ci.yml`**:
- Test automation
- Linting and type checking
- Deployment pipeline

**`docs/`** directory:
- `PRD.md` — Product Requirements Document
- `TRD.md` — Technical Requirements Document
- `adr/` — Architectural Decision Records

### 8. Add More Agents (When Ready)

To add an architect, product owner, or other agents:

1. **Create the prompt file:**
   ```bash
   # Copy from luna-framework as template
   cp ~/projects/luna-framework/agents/architect.md agents/
   # Edit to match Project One specifics
   ```

2. **Create the spawn script:**
   ```bash
   cp config/spawn-engineer.sh config/spawn-architect.sh
   # Update LABEL, MODEL, PROMPT_FILE variables
   chmod +x config/spawn-architect.sh
   ```

3. **Add cron job:**
   ```bash
   crontab -e
   # Add schedule line for the new agent
   ```

4. **Test it:**
   ```bash
   ./config/spawn-architect.sh "Test architect setup"
   ```

## Verification Checklist

Before considering the bootstrap complete, verify:

- [ ] GitHub repo created and connected
- [ ] All agent labels created
- [ ] Priority and status labels created
- [ ] GitHub Project board created (optional)
- [ ] Engineer spawn script is executable
- [ ] Cron job configured and running
- [ ] Logs directory created
- [ ] Test spawn successful
- [ ] At least 2-3 initial issues created
- [ ] README updated with project-specific info
- [ ] CI/CD workflow configured (if applicable)

## Testing the Full Loop

1. Create a simple issue with `agent:engineer` label
2. Wait for the next scheduled run (or spawn manually)
3. Check that the agent:
   - Picked up the issue
   - Created a feature branch
   - Implemented the feature
   - Opened a PR
4. Review the PR (manually or via architect agent)
5. Merge when approved
6. Verify the PR Merger closes the issue

## Troubleshooting

**Agent not spawning via cron:**
- Check crontab: `crontab -l`
- Check cron logs: `/var/log/syslog` or `journalctl -u cron`
- Verify script is executable: `ls -l config/spawn-engineer.sh`
- Test manually: `./config/spawn-engineer.sh "test"`

**Agent spawns but doesn't pick up issues:**
- Verify GitHub CLI auth: `gh auth status`
- Check repo name in prompt file matches actual repo
- Verify labels exist: `gh label list`
- Check issue query: `gh issue list --label "agent:engineer"`

**Agent hallucinating APIs:**
- Ensure Context7 MCP is configured: `mcporter call context7.resolve-library-id query="test" libraryName="pydantic"`
- Verify agent is reading skills in Step 0
- Check that required skills exist in `~/.openclaw/workspace/skills/`

**Low code quality:**
- Add architect agent for code review
- Strengthen CI checks (ruff, pyright, coverage)
- Update engineer prompt with specific quality standards

## Next Steps

Once bootstrap is complete:
1. Start building features via issues
2. Monitor agent performance and iterate on prompts
3. Add more agents as team grows
4. Set up monitoring/alerts for agent activity
5. Create runbooks for common maintenance tasks

## Support

For issues with the Luna framework itself, see:
- Luna Framework repo: https://github.com/robertoronderosjr/luna-framework
- OpenClaw docs: https://docs.openclaw.com

---

**Bootstrap created:** 2026-02-08  
**Project:** Project One  
**Primary agent:** Engineer (GPT-5.3 Codex)
