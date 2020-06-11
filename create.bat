@ECHO OFF

IF "%1"=="" (
    ECHO no project name provided
    GOTO EOF
)

:START_LOOP

IF (%1)==() GOTO END_LOOP
IF "%1"=="-h" (START https://github.com/AdamPlaskitt/automateProjectInitialization/blob/master/README.md & ECHO See webpage for help & GOTO EOF) ELSE (
IF "%1"=="--help" START https://github.com/AdamPlaskitt/automateProjectInitialization/blob/master/README.md & ECHO See webpage for help & GOTO EOF
)

SHIFT
GOTO START_LOOP

:END_LOOP

FOR /F "tokens=* USEBACKQ" %%F IN (`python \Users\Adam\projects\myProjects\automateProjectInitialization\create.py %GithubToken% %DefaultProjectPath% %*`) DO (
SET VAR=%%F
)
IF "%VAR%"=="A project with that name already exists" ( ECHO %VAR% ) else ( CD %VAR% )

:EOF
