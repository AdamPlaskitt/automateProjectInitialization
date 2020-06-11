import os
import sys
from github import Github

remote = True
private = False

github_token = str(sys.argv[1])
project_name = str(sys.argv[2])
list_all_args = sys.argv[3:]

while len(list_all_args) > 0:
    command = list_all_args.pop(0)
    if command.lower() == "-r":
        remote = True
    elif command.lower() == "-l":
        remote = False
    elif command.lower() == "-p":
        private = True

commands = None
location = None

if remote:
    github = Github(github_token)
    user = github.get_user()
    login = user.login
    repo = user.create_repo(project_name, private=private)

    commands = [f'echo # {repo.name} >> README.md',
                f'git remote add origin https://github.com/{login}/{project_name}.git',
                'git add .',
                'git commit -m "Initial commit"',
                'git push -u origin master']

    location = "remote"

elif not remote:

    commands = [f'echo # {project_name} >> README.md',
                'git add .',
                'git commit -m "Initial commit"']

    location = "local"


for c in commands:
    os.system(c)

print(f"Successfully initiated {location} project {project_name}")
