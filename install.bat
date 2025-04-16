@echo off
title Installation de SchoolTrad

echo ============================================
echo    INSTALLATION DE SCHOOLTRAD
echo ============================================
echo.

:: Vérifier si Python est installé
python --version >nul 2>&1
if %errorlevel% neq 0 (
    echo Python n'est pas installe ou n'est pas dans le PATH.
    echo Veuillez installer Python 3.8 ou superieur depuis https://www.python.org/downloads/
    echo Assurez-vous de cocher "Add Python to PATH" lors de l'installation.
    echo.
    echo Appuyez sur une touche pour quitter...
    pause >nul
    exit /b 1
)

:: Afficher la version de Python
echo Verification de Python...
python --version
echo.

:: Créer un environnement virtuel s'il n'existe pas déjà
if not exist "venv" (
    echo Creation de l'environnement virtuel...
    python -m venv venv
    if %errorlevel% neq 0 (
        echo Erreur lors de la creation de l'environnement virtuel.
        pause
        exit /b 1
    )
    echo Environnement virtuel cree avec succes.
) else (
    echo Environnement virtuel existant detecte.
)
echo.

:: Activer l'environnement virtuel et installer les dépendances
echo Installation des dependances...
call venv\Scripts\activate
python -m pip install --upgrade pip
pip install -r requirements.txt
if %errorlevel% neq 0 (
    echo Erreur lors de l'installation des dependances.
    pause
    exit /b 1
)
echo Toutes les dependances ont ete installees avec succes.
echo.

:: Créer le dossier profiles s'il n'existe pas
if not exist "profiles" (
    echo Creation du dossier de donnees...
    mkdir profiles
    echo Dossier 'profiles' cree.
) else (
    echo Le dossier de donnees existe deja.
)
echo.

:: Créer un raccourci bureau
echo Creation du raccourci de lancement...
echo Set oWS = WScript.CreateObject("WScript.Shell") > "%TEMP%\CreateShortcut.vbs"
echo sLinkFile = "%USERPROFILE%\Desktop\SchoolTrad.lnk" >> "%TEMP%\CreateShortcut.vbs"
echo Set oLink = oWS.CreateShortcut(sLinkFile) >> "%TEMP%\CreateShortcut.vbs"
echo oLink.TargetPath = "%~dp0run.bat" >> "%TEMP%\CreateShortcut.vbs"
echo oLink.WorkingDirectory = "%~dp0" >> "%TEMP%\CreateShortcut.vbs"
echo oLink.Description = "SchoolTrad - Trading Dashboard" >> "%TEMP%\CreateShortcut.vbs"
echo oLink.IconLocation = "%SystemRoot%\System32\SHELL32.dll,22" >> "%TEMP%\CreateShortcut.vbs"
echo oLink.Save >> "%TEMP%\CreateShortcut.vbs"
cscript //nologo "%TEMP%\CreateShortcut.vbs"
del "%TEMP%\CreateShortcut.vbs"
echo Raccourci cree sur le Bureau.
echo.

:: Créer le script de lancement
echo @echo off > run.bat
echo title SchoolTrad >> run.bat
echo call "%~dp0venv\Scripts\activate" >> run.bat
echo echo Lancement de SchoolTrad... >> run.bat
echo echo. >> run.bat
echo python -m streamlit run "%~dp0streamlit_app.py" >> run.bat
echo pause >> run.bat
echo.

echo ============================================
echo   INSTALLATION TERMINEE AVEC SUCCES!
echo ============================================
echo.
echo SchoolTrad a ete installe avec succes!
echo.
echo Un raccourci a ete cree sur votre Bureau.
echo Double-cliquez sur ce raccourci pour lancer l'application.
echo.
echo Appuyez sur une touche pour lancer SchoolTrad maintenant...
pause >nul

:: Lancer l'application
call run.bat
