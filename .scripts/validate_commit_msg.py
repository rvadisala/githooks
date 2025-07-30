#!/usr/bin/env python3
# scripts/validate_commit_msg.py
import sys
import re
import os

def validate_commit_message(commit_msg_filepath):
    try:
        with open(commit_msg_filepath, 'r') as f:
            commit_msg = f.read().strip()
    except Exception as e:
        print(f"Error reading commit message file: {e}", file=sys.stderr)
        sys.exit(1)

    # Regex for: [JIRA-XXXX] <TYPE>: <Descriptive Message>
    # Example: [JIRA-1234] feat: Add user login functionality
    # Added re.IGNORECASE for type flexibility
    commit_regex = re.compile(r"^\[JIRA-\d+\] (feat|bug|fix|chore|docs|style|refactor|test|ci|build|perf): .+", re.IGNORECASE)

    if not commit_regex.match(commit_msg):
        print("\033[31mERROR: Invalid commit message format!\033[0m", file=sys.stderr)
        print("\033[31mYour commit message must follow the standard:\033[0m", file=sys.stderr)
        print("\033[33m  [JIRA-XXXX] <TYPE>: <Descriptive Message>\033[0m", file=sys.stderr)
        print("\033[33mExamples:\033[0m", file=sys.stderr)
        print("\033[32m  [JIRA-1234] feat: Implement user authentication\033[0m", file=sys.stderr)
        print("\033[32m  [JIRA-5678] bug: Fix critical payment gateway issue\033[0m", file=sys.stderr)
        print("\033[32m  [JIRA-9012] docs: Update README with installation guide\033[0m", file=sys.stderr)
        sys.exit(1) # Exit with a non-zero code to abort the commit

    print("\033[32mCommit message validated successfully!\033[0m")
    sys.exit(0) # Exit with 0 to allow the commit

if __name__ == "__main__":
    # The commit message file path is passed as the first argument by Git/pre-commit
    if len(sys.argv) < 2:
        print("Error: Commit message file path not provided.", file=sys.stderr)
        sys.exit(1)

    commit_msg_file_path = sys.argv[1]
    validate_commit_message(commit_msg_file_path)
