@echo off

if "%1"=="" (
    echo no project name provided
    goto EOF
)

set filename=%1

mkdir "\Users\Adam\projects\myProjects\%filename%" || ( echo Project name already in use & goto EOF )

cd \Users\Adam\projects\myProjects\%filename%
git init

python \Users\Adam\projects\myProjects\automateProjectInitialization\create.py %GithubToken% %*

code .

:EOF
