#!/bin/bash
#
# Cron job configuration for Project One agents
#
# Installation:
#   1. Make this file executable: chmod +x config/cron-jobs.sh
#   2. Add to crontab: crontab -e
#   3. Add the following lines (adjust times as needed):
#
# # Project One - Engineer Agent (9AM, 2PM, 8PM ET)
# 0 9,14,20 * * * /home/admin/projects/project-one/config/spawn-engineer.sh >> /home/admin/projects/project-one/logs/engineer.log 2>&1
#
# # Project One - Architect Agent (2AM ET) - UNCOMMENT WHEN READY
# # 0 2 * * * /home/admin/projects/project-one/config/spawn-architect.sh >> /home/admin/projects/project-one/logs/architect.log 2>&1
#
# # Project One - Product Owner (7AM, 4PM, 10PM ET) - UNCOMMENT WHEN READY
# # 0 7,16,22 * * * /home/admin/projects/project-one/config/spawn-po.sh >> /home/admin/projects/project-one/logs/po.log 2>&1
#

# This file serves as documentation. Actual spawn scripts are in this directory.
# Each agent has a dedicated spawn script (spawn-engineer.sh, spawn-architect.sh, etc.)
