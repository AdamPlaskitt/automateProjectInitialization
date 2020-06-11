import os
import sys
from github import Github

# Command parameters
remote = True
private = False
description = "."
description_only = False

# Passed arguments
github_token = str(sys.argv[1])
project_name = str(sys.argv[2])
list_all_args = sys.argv[3:]

# Parse commands
while len(list_all_args) > 0:
    command = list_all_args.pop(0)
    if command.lower() == "-r":
        remote = True
    elif command.lower() == "-l":
        remote = False
    elif command.lower() == "-p":
        private = True
    elif command.lower() == "-d" and len(list_all_args) > 0:
        description = list_all_args.pop(0)
    elif command.lower() == "-do" and len(list_all_args) > 0:
        description = list_all_args.pop(0)
        description_only = True

commands = None
location = None

# Initialise remote repo
if remote:
    github = Github(github_token)
    user = github.get_user()
    login = user.login
    repo = user.create_repo(project_name, private=private, description=description)

    commands = [f'echo # {repo.name} >> README.md',
                f'git remote add origin https://github.com/{login}/{project_name}.git',
                'git add .',
                'git commit -m "Initial commit"',
                'git push -u origin master']

    location = "remote"

# Initialise local repo
elif not remote:

    commands = [f'echo # {project_name}>> README.md',
                'git add .',
                'git commit -m "Initial commit"']

    location = "local"

# Add description to readme
if description != "." and not description_only:
    commands.insert(1, f'echo {description}>> README.md')

# Executes commands
for c in commands:
    os.system(c)

print(f"Successfully initiated {location} project {project_name}")
