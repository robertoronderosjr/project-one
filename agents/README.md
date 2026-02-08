# Project One — Agent Team

## Roster

| Agent | Model | Schedule (ET) | Prompt | Status |
|-------|-------|---------------|--------|--------|
| Engineer | GPT-5.3 Codex | 9AM, 2PM, 8PM | `engineer.md` | ✅ Configured |

## Adding More Agents

To expand the agent team, create additional prompt files in this directory:

### Recommended Agent Roles

**Architect** (code reviewer)
- Model: Claude Opus 4.6
- Schedule: 2AM ET (deep review) + reactive spawns
- Responsibilities: Review PRs, ensure quality standards, architecture decisions

**Product Owner** (project manager)
- Model: Claude Opus 4.6
- Schedule: 7AM, 4PM, 10PM ET
- Responsibilities: Prioritize backlog, refine specs, track progress

**Research** (investigator)
- Model: Claude Opus 4.6
- Schedule: 11AM, 6PM ET + reactive spawns
- Responsibilities: Investigate unknowns, prototype solutions, research libraries

**PR Merger** (automation)
- Model: Claude Sonnet 4.5
- Schedule: Every hour at :30
- Responsibilities: Auto-merge approved PRs, check CI status

**Docs Keeper** (documentation)
- Model: Claude Sonnet 4.5
- Schedule: 3AM ET
- Responsibilities: Update docs, ensure completeness, maintain ADRs

## Reactive Spawning

All agents support reactive spawning via `openclaw sessions spawn` with appropriate labels.

Example from another agent:
```bash
openclaw sessions spawn \
  --label "proj-1-engineer" \
  --model "openai-codex" \
  --prompt "$(cat /home/admin/projects/project-one/agents/engineer.md)" \
  --message "Fix the bug in issue #42 - investigate the Redis connection timeout"
```

## Labels

Create GitHub issue labels to route work:
- `agent:engineer` — Engineer tasks
- `agent:architect` — Architect tasks
- `agent:po` — Product Owner tasks
- `agent:research` — Research tasks
- `agent:docs` — Docs Keeper tasks
- `agent:merger` — PR Merger tasks

## Cron Scheduling

See `../config/cron-jobs.sh` for scheduled agent spawning configuration.

## GitHub Integration

Agents use the `gh` CLI for all GitHub operations:
- List issues: `gh issue list --label "agent:engineer"`
- Create PRs: `gh pr create --fill`
- Review PRs: `gh pr review <number> --approve`
- Manage projects: `gh project item-edit ...`

Ensure the GitHub CLI is authenticated: `gh auth status`
