import os
import sys
from github import Github

project_name = str(sys.argv[1])
github_token = str(sys.argv[2])

github = Github(github_token)
user = github.get_user()
login = user.login
repo = user.create_repo(project_name)

commands = [f'echo "# {repo.name}" >> README.md',
            'git init',
            f'git remote add origin https://github.com/{login}/{project_name}.git',
            'git add .',
            'git commit -m "Initial commit"',
            'git push -u origin master']

for c in commands:
    os.system(c)

print(f"Successfully initiated project {project_name}")
