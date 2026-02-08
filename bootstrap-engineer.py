#!/home/admin/projects/luna-framework/.venv/bin/python
"""Bootstrap script for deploying the Engineer agent in Project One.

This script:
1. Verifies Luna Framework is available
2. Checks Redis connectivity
3. Deploys the Engineer agent via Luna's wake_agent()
4. Logs the deployment status

Usage:
    python bootstrap-engineer.py
"""

import sys
from pathlib import Path

# Add Luna Framework to Python path
luna_path = Path("/home/admin/projects/luna-framework/src")
if luna_path.exists():
    sys.path.insert(0, str(luna_path))
else:
    print(f"❌ Luna Framework not found at {luna_path}")
    sys.exit(1)

try:
    from luna.a2a import wake_agent
    print("✅ Luna Framework imported successfully")
except ImportError as e:
    print(f"❌ Failed to import Luna Framework: {e}")
    sys.exit(1)

# Verify project structure
project_dir = Path("/home/admin/projects/project-one")
prompt_file = project_dir / "agents" / "engineer.md"
config_file = project_dir / "luna-project.json"

if not prompt_file.exists():
    print(f"❌ Engineer prompt file not found: {prompt_file}")
    sys.exit(1)

if not config_file.exists():
    print(f"⚠️  Warning: Luna project config not found: {config_file}")
else:
    print(f"✅ Project config found: {config_file}")

print(f"✅ Engineer prompt found: {prompt_file}")

# Define the initial task for the engineer
initial_task = """**Project One - Initial Setup and Deployment**

You are the first agent deployed in Project One.

**Immediate tasks:**

1. **Verify project structure:**
   - Check that the project directory exists and has proper structure
   - Verify GitHub repo access
   - Check available tools and skills

2. **Initialize the repository (if needed):**
   - Check if GitHub repo exists: `gh repo view robertoronderosjr/project-one`
   - If not, create it or coordinate with the human
   - Initialize git if needed

3. **Set up project scaffolding:**
   - Create basic Python project structure (src/, tests/, docs/)
   - Add pyproject.toml with dependencies
   - Set up CI/CD pipeline (.github/workflows/)
   - Configure quality tools (ruff, pyright, pytest)

4. **Create initial documentation:**
   - README.md with project overview
   - docs/SETUP.md with development setup instructions
   - docs/ARCHITECTURE.md with initial design notes

5. **Report back:**
   - Document what you've accomplished
   - Note any blockers or issues
   - Suggest next steps

**Working directory:** /home/admin/projects/project-one
**Prompt file:** /home/admin/projects/project-one/agents/engineer.md

**Remember to follow Step 0** (load skills, initialize tools) before starting work.
"""

# Deploy the engineer agent
print("\n🚀 Deploying Engineer agent for Project One...")
print(f"   Label: proj-1-engineer-bootstrap")
print(f"   Working dir: {project_dir}")
print(f"   Prompt: {prompt_file}")

try:
    result = wake_agent(
        agent_name="engineer",
        task=initial_task,
        label="proj-1-engineer-bootstrap",
        spawned_by="bootstrap-script",
    )
    
    print("\n✅ Engineer agent deployment initiated!")
    print(f"\nDeployment result:")
    print(f"  Status: {result.get('status')}")
    print(f"  Reason: {result.get('reason')}")
    
    if result.get('session_id'):
        print(f"  Session ID: {result.get('session_id')}")
    
    if result.get('similarity') is not None:
        print(f"  Similarity: {result.get('similarity')}")
    
    print("\n📋 Next steps:")
    print("  1. Monitor the agent's progress in OpenClaw dashboard")
    print("  2. Check logs: tail -f /home/admin/projects/project-one/logs/engineer.log")
    print("  3. Review any GitHub activity in robertoronderosjr/project-one")
    print("  4. Once setup is complete, configure cron jobs for scheduled runs")
    
    # Write deployment record
    deployment_log = project_dir / "logs" / "deployments.log"
    deployment_log.parent.mkdir(exist_ok=True)
    
    from datetime import datetime
    with open(deployment_log, "a") as f:
        f.write(f"\n[{datetime.now().isoformat()}] Engineer agent deployed\n")
        f.write(f"  Label: proj-1-engineer-bootstrap\n")
        f.write(f"  Status: {result.get('status')}\n")
        f.write(f"  Session ID: {result.get('session_id', 'N/A')}\n")
        f.write(f"  Spawned by: bootstrap-script\n")
    
    print(f"\n📝 Deployment logged to: {deployment_log}")

except Exception as e:
    print(f"\n❌ Failed to deploy Engineer agent: {e}")
    import traceback
    traceback.print_exc()
    sys.exit(1)
