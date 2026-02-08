# Quick Reference — Project One Luna Deployment

## Daily Operations

### Check Agent Status
```bash
# View recent spawns
openclaw sessions list | grep proj-1

# Check logs
tail -f logs/engineer.log

# View GitHub activity
gh pr list
gh issue list --label "agent:engineer"
```

### Manual Agent Spawn
```bash
# Scheduled work pickup
./config/spawn-engineer.sh

# Specific task
./config/spawn-engineer.sh "Fix bug in issue #42"
./config/spawn-engineer.sh "Implement feature X with tests"
```

### Issue Management
```bash
# Create engineer task
gh issue create \
  --title "Feature: <name>" \
  --label "agent:engineer,priority:p1" \
  --body "Implement <feature>\n\nAcceptance Criteria:\n- [ ] AC1\n- [ ] AC2"

# List open issues
gh issue list --label "agent:engineer" --state open

# View issue details
gh issue view 42
```

### PR Management
```bash
# List open PRs
gh pr list --state open

# Review PR
gh pr view 15
gh pr diff 15
gh pr review 15 --approve

# Merge PR
gh pr merge 15 --squash
```

## Cron Schedule

| Agent | Time (ET) | Command |
|-------|-----------|---------|
| Engineer | 9AM, 2PM, 8PM | `0 9,14,20 * * *` |

View crontab: `crontab -l`  
Edit crontab: `crontab -e`

## File Locations

| Purpose | Path |
|---------|------|
| Agent prompts | `/home/admin/projects/project-one/agents/` |
| Spawn scripts | `/home/admin/projects/project-one/config/` |
| Logs | `/home/admin/projects/project-one/logs/` |
| Source code | `/home/admin/projects/project-one/src/` |
| Tests | `/home/admin/projects/project-one/tests/` |
| Docs | `/home/admin/projects/project-one/docs/` |

## Common Tasks

### Add New Agent
```bash
# 1. Copy prompt template
cp agents/engineer.md agents/architect.md

# 2. Edit prompt for new role
nano agents/architect.md

# 3. Create spawn script
cp config/spawn-engineer.sh config/spawn-architect.sh
nano config/spawn-architect.sh  # Update LABEL, MODEL, PROMPT_FILE

# 4. Make executable
chmod +x config/spawn-architect.sh

# 5. Add to cron
crontab -e
# Add: 0 2 * * * /home/admin/projects/project-one/config/spawn-architect.sh >> /home/admin/projects/project-one/logs/architect.log 2>&1
```

### Update Agent Prompt
```bash
# 1. Edit prompt file
nano agents/engineer.md

# 2. Commit change
git add agents/engineer.md
git commit -m "chore(agent): update engineer prompt"
git push

# 3. Test immediately (optional)
./config/spawn-engineer.sh "Test updated prompt"
```

### Emergency Stop
```bash
# List running agents
openclaw sessions list | grep proj-1

# Kill specific session
openclaw sessions kill <session-id>

# Disable cron temporarily
crontab -e
# Comment out the line with #
```

### View Agent Conversation
```bash
# Get session ID
openclaw sessions list | grep proj-1-engineer

# View full session
openclaw sessions show <session-id>
```

## Testing the Agent

### Test Spawn
```bash
# Dry run
./config/spawn-engineer.sh "Test spawn - check skills loaded and GitHub auth works"

# Check it spawned
openclaw sessions list | tail -5

# Watch logs
tail -f logs/engineer.log
```

### Test Full Loop
```bash
# 1. Create test issue
gh issue create --title "Test: Echo hello world" \
  --label "agent:engineer,priority:p3" \
  --body "Create a simple test file that prints hello world"

# 2. Spawn agent
./config/spawn-engineer.sh

# 3. Monitor
gh pr list  # Should see new PR after ~5-10 min
```

## Troubleshooting

### Agent Not Spawning
```bash
# Check cron is running
systemctl status cron

# Check cron logs
journalctl -u cron -n 50

# Test spawn script manually
./config/spawn-engineer.sh "manual test"

# Verify executable
ls -l config/spawn-engineer.sh
```

### Agent Not Picking Up Issues
```bash
# Verify GitHub auth
gh auth status

# Check label exists
gh label list | grep engineer

# Test query manually
gh issue list --label "agent:engineer"

# Check repo name in prompt matches actual repo
grep "GitHub repo:" agents/engineer.md
```

### Agent Quality Issues
```bash
# Update prompt with stricter guidelines
nano agents/engineer.md

# Add architect agent for reviews
# (See "Add New Agent" above)

# Strengthen CI checks
nano .github/workflows/ci.yml
```

## Links

- **GitHub Repo:** https://github.com/robertoronderosjr/project-one
- **GitHub Issues:** https://github.com/robertoronderosjr/project-one/issues
- **GitHub PRs:** https://github.com/robertoronderosjr/project-one/pulls
- **OpenClaw Docs:** https://docs.openclaw.com

## Support

For Luna framework issues: https://github.com/robertoronderosjr/luna-framework  
For OpenClaw issues: https://github.com/openclaw/openclaw
