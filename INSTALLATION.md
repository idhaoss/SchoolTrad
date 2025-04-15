# Instructions d'installation et de déploiement

Ce document fournit les instructions détaillées pour installer l'application SchoolTrad et, si vous le souhaitez, la publier sur GitHub.

## Installation locale

1. Assurez-vous que Python 3.8 ou supérieur est installé sur votre système
2. Clonez ou téléchargez ce dépôt sur votre machine
3. Ouvrez un terminal et naviguez jusqu'au dossier du projet
4. Créez un environnement virtuel pour isoler les dépendances :
   ```bash
   python -m venv venv
   ```
5. Activez l'environnement virtuel :
   - Sur Windows : 
     ```
     venv\Scripts\activate
     ```
   - Sur macOS/Linux : 
     ```
     source venv/bin/activate
     ```
6. Installez les dépendances :
   ```bash
   pip install -r requirements.txt
   ```
7. Lancez l'application :
   ```bash
   python -m streamlit run trading_dashboard_pro/app.py
   ```
8. Ouvrez votre navigateur à l'adresse indiquée (généralement http://localhost:8501)

## Publication sur GitHub

Si vous souhaitez publier ce projet sur GitHub, suivez ces étapes :

### 1. Créer un compte GitHub (si vous n'en avez pas déjà un)
Rendez-vous sur [GitHub](https://github.com/) et créez un compte.

### 2. Installer Git (si ce n'est pas déjà fait)
Téléchargez et installez Git à partir de [git-scm.com](https://git-scm.com/downloads).

### 3. Configurer Git
```bash
git config --global user.name "Votre Nom"
git config --global user.email "votre.email@exemple.com"
```

### 4. Initialiser un dépôt Git local
Dans le dossier racine du projet (`schooltrad`) :
```bash
git init
```

### 5. Ajouter les fichiers au suivi Git
```bash
git add .
```

### 6. Effectuer le premier commit
```bash
git commit -m "Version initiale de SchoolTrad"
```

### 7. Créer un nouveau dépôt sur GitHub
- Connectez-vous à votre compte GitHub
- Cliquez sur le bouton "New" ou "+" en haut à droite
- Nommez votre dépôt "schooltrad"
- Choisissez si le dépôt doit être public ou privé
- Ne cochez PAS "Initialize this repository with a README"
- Cliquez sur "Create repository"

### 8. Lier votre dépôt local à GitHub
GitHub vous affichera des instructions. Utilisez les commandes pour un dépôt existant :
```bash
git remote add origin https://github.com/votre-nom-utilisateur/schooltrad.git
git branch -M main
git push -u origin main
```

### 9. Protéger votre branche principale (optionnel mais recommandé)
- Allez dans "Settings" > "Branches" sur la page de votre dépôt
- Sous "Branch protection rules", cliquez sur "Add rule"
- Dans "Branch name pattern", entrez "main"
- Cochez "Require pull request reviews before merging"
- Cliquez sur "Create"

Votre projet est maintenant sur GitHub ! Vous pouvez partager l'URL avec les collaborateurs ou les utilisateurs.

## Mise à jour du projet

Pour mettre à jour le projet après des modifications :

```bash
git add .
git commit -m "Description des modifications"
git push
```

## Gestion des versions

Lorsque vous publiez une nouvelle version :

1. Mettez à jour le fichier `VERSION`
2. Ajoutez une étiquette (tag) Git :
   ```bash
   git tag -a v1.0.1 -m "Version 1.0.1"
   git push origin v1.0.1
   ```
3. Créez une nouvelle release sur GitHub avec les notes de version
