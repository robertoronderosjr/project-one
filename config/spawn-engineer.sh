#!/bin/bash
#
# Spawn the Engineer agent for Project One
# Called by cron or manually for reactive spawning
#
# Usage:
#   ./config/spawn-engineer.sh                    # Scheduled run
#   ./config/spawn-engineer.sh "Custom message"   # Reactive spawn with custom message
#

set -euo pipefail

PROJECT_DIR="/home/admin/projects/project-one"
PROMPT_FILE="$PROJECT_DIR/agents/engineer.md"
LABEL="proj-1-engineer"
MODEL="openai-codex"  # GPT-5.3 Codex

# Default message for scheduled runs
DEFAULT_MESSAGE="Scheduled engineer run. Check for assigned issues, work on highest priority task."

# Use custom message if provided, otherwise use default
MESSAGE="${1:-$DEFAULT_MESSAGE}"

# Ensure we're in the project directory
cd "$PROJECT_DIR"

# Pull latest changes
git checkout main && git pull --quiet || true

# Spawn the agent
openclaw sessions spawn \
  --label "$LABEL" \
  --model "$MODEL" \
  --prompt "$(cat $PROMPT_FILE)" \
  --message "$MESSAGE"

echo "[$(date +'%Y-%m-%d %H:%M:%S')] Engineer agent spawned: $MESSAGE"
