# deep_research_cron_setup.sh
# This script sets up a cron job to run Deep Research Assistant daily at 7:00 AM

# You must replace 'macmini' or 'imac' in the path with your actual username if different

(crontab -l 2>/dev/null; echo "0 7 * * * /usr/bin/python3 /Users/macmini/Deep_Research_Workflow/deep_research_runner.py >> /Users/macmini/Deep_Research_Workflow/run_history.log 2>&1") | crontab -
