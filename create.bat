@ECHO OFF

IF "%~1"=="" (
    ECHO no project name provided
    GOTO EOF
)

SET FILENAME=%1
SET EDITOR=code

:START_LOOP

IF (%1)==() GOTO END_LOOP
IF /I "%~1"=="-h" (START https://github.com/AdamPlaskitt/automateProjectInitialization/blob/master/README.md & ECHO See webpage for help & GOTO EOF) ELSE (
IF /I "%~1"=="--help" START https://github.com/AdamPlaskitt/automateProjectInitialization/blob/master/README.md & ECHO See webpage for help & GOTO EOF
)

IF /I "%~1"=="-e" IF NOT (%2)==() ( SET EDITOR=%2 )

SHIFT
GOTO START_LOOP

:END_LOOP

FOR /F "tokens=* USEBACKQ" %%F IN (`create.py %GithubToken% %DefaultProjectPath% %*`) DO (
SET VAR=%%F
)

IF "%VAR%"=="A project with that name already exists" GOTO PRINT
IF "%VAR%"=="Command parameters not recognised" GOTO PRINT
GOTO END

:PRINT
ECHO %VAR%
GOTO EOF

:END
ECHO Successfully initiated project %FILENAME%
CD %VAR%

%EDITOR% .

:EOF
