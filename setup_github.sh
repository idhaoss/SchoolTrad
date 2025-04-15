#!/bin/bash

echo "===================================="
echo "Configuration de Git pour SchoolTrad"
echo "===================================="

echo
echo "1. Vérification de Git..."
if ! command -v git &> /dev/null; then
    echo "Git n'est pas installé. Veuillez l'installer:"
    echo "  - Sur Ubuntu/Debian: sudo apt-get install git"
    echo "  - Sur macOS: brew install git"
    exit 1
fi

echo
echo "2. Initialisation du dépôt Git local..."
git init
if [ $? -ne 0 ]; then
    echo "Erreur lors de l'initialisation du dépôt Git"
    exit 1
fi

echo
echo "3. Ajout des fichiers au suivi Git..."
git add .
if [ $? -ne 0 ]; then
    echo "Erreur lors de l'ajout des fichiers"
    exit 1
fi

echo
echo "4. Configuration de Git (modifiez ces valeurs si nécessaire)..."
read -p "Entrez votre nom d'utilisateur Git: " username
read -p "Entrez votre email Git: " email
git config user.name "$username"
git config user.email "$email"

echo
echo "5. Premier commit..."
git commit -m "Version initiale de SchoolTrad"
if [ $? -ne 0 ]; then
    echo "Erreur lors du premier commit"
    exit 1
fi

echo
echo "===================================="
echo "Configuration terminée avec succès!"
echo "===================================="
echo
echo "Pour publier sur GitHub, suivez ces étapes:"
echo "1. Créez un nouveau dépôt sur GitHub"
echo "2. Exécutez les commandes suivantes:"
echo "   git remote add origin https://github.com/votre-nom-utilisateur/schooltrad.git"
echo "   git branch -M main"
echo "   git push -u origin main"
echo
echo "Pour plus de détails, consultez INSTALLATION.md"
echo

read -p "Appuyez sur Entrée pour continuer..."
