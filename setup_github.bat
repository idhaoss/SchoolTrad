@echo off
echo ====================================
echo Configuration de Git pour SchoolTrad
echo ====================================

echo.
echo 1. Verification de Git...
git --version
if %ERRORLEVEL% NEQ 0 (
    echo Git n'est pas installe. Veuillez l'installer depuis https://git-scm.com/downloads
    exit /b
)

echo.
echo 2. Initialisation du depot Git local...
git init
if %ERRORLEVEL% NEQ 0 (
    echo Erreur lors de l'initialisation du depot Git
    exit /b
)

echo.
echo 3. Ajout des fichiers au suivi Git...
git add .
if %ERRORLEVEL% NEQ 0 (
    echo Erreur lors de l'ajout des fichiers
    exit /b
)

echo.
echo 4. Configuration de Git (modifiez ces valeurs si necessaire)...
set /p username="Entrez votre nom d'utilisateur Git: "
set /p email="Entrez votre email Git: "
git config user.name "%username%"
git config user.email "%email%"

echo.
echo 5. Premier commit...
git commit -m "Version initiale de SchoolTrad"
if %ERRORLEVEL% NEQ 0 (
    echo Erreur lors du premier commit
    exit /b
)

echo.
echo ====================================
echo Configuration terminee avec succes!
echo ====================================
echo.
echo Pour publier sur GitHub, suivez ces etapes:
echo 1. Creez un nouveau depot sur GitHub
echo 2. Executez les commandes suivantes:
echo    git remote add origin https://github.com/votre-nom-utilisateur/schooltrad.git
echo    git branch -M main
echo    git push -u origin main
echo.
echo Pour plus de details, consultez INSTALLATION.md
echo.
pause
