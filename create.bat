@echo off

if "%1"=="" (
    echo no project name provided
    goto EOF
)

FOR /F "tokens=* USEBACKQ" %%F IN (`python \Users\Adam\projects\myProjects\automateProjectInitialization\create.py %GithubToken% %*`) DO (
SET VAR=%%F
)
cd %VAR%

:EOF
