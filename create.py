import os
import sys
from github import Github

project_name = str(sys.argv[1])
github_token = str(sys.argv[2])
flag = str(sys.argv[3]).lower()

if flag == "-r":
    github = Github(github_token)
    user = github.get_user()
    login = user.login
    repo = user.create_repo(project_name)

    commands_remote = [f'echo "# {repo.name}" >> README.md',
                       'git init',
                       f'git remote add origin https://github.com/{login}/{project_name}.git',
                       'git add .',
                       'git commit -m "Initial commit"',
                       'git push -u origin master']

    for c in commands_remote:
        os.system(c)

    print(f"Successfully initiated remote project {project_name}")

elif flag == "-l":
    commands_local = [f'echo # {project_name} >> README.md',
                      'git init',
                      'git add .',
                      'git commit -m "Initial commit"']

    for c in commands_local:
        os.system(c)

    print(f"Successfully initiated local project {project_name}")
