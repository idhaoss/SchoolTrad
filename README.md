# 📊 SchoolTrad

[![Version](https://img.shields.io/badge/version-1.0.0-blue.svg)](https://github.com/idhaoss/SchoolTrad/releases)
[![License](https://img.shields.io/badge/license-MIT-green.svg)](LICENSE.md)
[![Python](https://img.shields.io/badge/python-3.8+-yellow.svg)](https://www.python.org/)
[![Streamlit](https://img.shields.io/badge/streamlit-1.28.0+-red.svg)](https://streamlit.io/)

**SchoolTrad** est une plateforme moderne de suivi et d'analyse de configurations de trading, conçue pour permettre aux traders de tous niveaux de documenter et d'améliorer leurs stratégies de manière collaborative.

![SchoolTrad](https://via.placeholder.com/800x400?text=SchoolTrad+Dashboard)

## ✨ Caractéristiques

- **Design moderne** avec interface utilisateur intuitive et responsive
- **Catalogue étendu d'actifs** comprenant plus de 40 cryptomonnaies, forex, indices, matières premières et actions
- **Suivi des actifs** sur 9 timeframes différentes (1m à 1M)
- **Multi-profils** avec système d'authentification pour différents utilisateurs
- **Mode Super Admin** pour gérer et analyser les données de tous les profils
- **Paramètres de stratégie** personnalisables pour chaque configuration
- **Système de notes** pour conserver vos observations
- **Capture d'écran** pour sauvegarder jusqu'à 2 images par configuration
- **Import/Export** de données pour la sauvegarde et le partage
- **Installation simplifiée** avec scripts automatisés pour Windows et Linux/macOS

## Installation

### Prérequis

- Python 3.8 ou supérieur
- pip (gestionnaire de paquets Python)

### Installation automatique (Recommandé)

#### Windows
1. Téléchargez ou clonez ce dépôt
   ```
   git clone https://github.com/idhaoss/SchoolTrad.git
   cd SchoolTrad
   ```
2. Double-cliquez simplement sur le fichier `install.bat`
3. Suivez les instructions à l'écran
4. Un raccourci sera créé sur votre Bureau pour lancer l'application

#### macOS/Linux
1. Téléchargez ou clonez ce dépôt
   ```
   git clone https://github.com/idhaoss/SchoolTrad.git
   cd SchoolTrad
   ```
2. Rendez le script d'installation exécutable :
   ```bash
   chmod +x install.sh
   ```
3. Exécutez le script d'installation :
   ```bash
   ./install.sh
   ```
4. Suivez les instructions à l'écran
5. Un raccourci sera créé sur votre Bureau pour lancer l'application

### Installation manuelle

Si vous préférez installer l'application manuellement :

1. Clonez ce dépôt:
   ```
   git clone https://github.com/idhaoss/SchoolTrad.git
   cd SchoolTrad
   ```

2. Créez un environnement virtuel (recommandé):
   ```
   python -m venv venv
   source venv/bin/activate  # Sur Windows: venv\Scripts\activate
   ```

3. Installez les dépendances:
   ```
   pip install -r requirements.txt
   ```

4. Lancez l'application:
   ```
   python -m streamlit run streamlit_app.py
   ```

5. Ouvrez votre navigateur à l'adresse indiquée (généralement http://localhost:8501)

## Structure du projet

```
SchoolTrad/
├── streamlit_app.py         # Point d'entrée principal
├── install.bat              # Script d'installation Windows
├── install.sh               # Script d'installation Linux/macOS
├── config/                  # Configuration
│   ├── __init__.py
│   ├── settings.py          # Constantes et paramètres
│   └── styles.py            # Styles CSS avec thèmes
├── models/                  # Gestion des données
│   ├── __init__.py
│   ├── auth.py              # Authentification et profils
│   └── data.py              # Gestion des données trading
├── views/                   # Interface utilisateur
│   ├── __init__.py
│   ├── admin.py             # Vue admin
│   ├── assets.py            # Vue tableau des actifs
│   ├── authentication.py    # Vue login
│   └── details.py           # Vue détails de configuration
├── utils/                   # Utilitaires
│   └── __init__.py
├── profiles/                # Stockage des données (créé automatiquement)
├── .streamlit/              # Configuration Streamlit
│   └── config.toml          # Paramètres de l'interface
├── CONTRIBUTING.md          # Guide pour les contributeurs
├── INSTALLATION.md          # Guide d'installation détaillé
├── LICENSE.md               # Licence du projet
├── README.md                # Ce fichier
└── VERSION                  # Numéro de version
```

## Utilisation

### Premier démarrage

1. Lancez l'application
2. Créez un profil utilisateur ou un compte Super Admin
3. Commencez à enregistrer vos configurations de trading!

### Gestion des profils

- Chaque utilisateur peut créer son propre profil
- Les données sont stockées localement (dossier `profiles/`)
- Possibilité d'exporter vos données pour les sauvegarder

### Mode Super Admin

Le mode Super Admin permet:
- De voir les statistiques de tous les profils
- D'accéder aux données de tous les utilisateurs
- De gérer les profils (création, suppression)
- D'effectuer des imports/exports pour n'importe quel profil

### Partage de données entre utilisateurs

L'application stocke les données localement sur chaque machine. Pour partager des données entre utilisateurs :

1. L'utilisateur A exporte ses données via l'option "Exporter mes données" dans la barre latérale
2. L'utilisateur A envoie le fichier JSON exporté à l'utilisateur B (par email, etc.)
3. L'utilisateur B importe ces données via l'option "Importer des données"

En mode Super Admin, il est possible de:
1. Demander aux utilisateurs d'envoyer leurs fichiers JSON exportés
2. Importer ces fichiers dans différents profils pour les comparer
3. Analyser les différences entre les profils

## Dépannage

### Problèmes courants

**Q: Je ne vois pas les nouveaux profils créés dans le tableau de bord admin.**  
R: Le tableau de bord admin recharge automatiquement la configuration à chaque affichage. Si vous ne voyez pas un nouveau profil, essayez de cliquer sur un autre onglet puis revenir au tableau de bord.

**Q: Mes données ne sont pas sauvegardées entre les sessions.**  
R: Vérifiez que le dossier 'profiles/' a été créé dans le répertoire de l'application. Assurez-vous également d'utiliser le bouton "Se déconnecter" pour sauvegarder vos données avant de quitter.

**Q: Je ne peux pas uploader d'images.**  
R: Vérifiez que vous utilisez des formats d'image supportés (JPG, PNG) et que la taille du fichier n'est pas trop importante.

## Contribuer au projet

Les contributions sont les bienvenues ! Si vous souhaitez contribuer à ce projet, veuillez consulter notre [guide de contribution](CONTRIBUTING.md).

## Versions futures

Nous prévoyons d'ajouter les fonctionnalités suivantes dans les prochaines versions :
- Stockage centralisé des données (base de données)
- Fonctionnalités de collaboration en temps réel
- Tableaux de bord analytiques avancés
- Support mobile

## Support

Pour toute question ou problème, veuillez ouvrir une issue sur GitHub.

## Licence

Ce projet est sous licence MIT. Voir le fichier [LICENSE.md](LICENSE.md) pour plus de détails.
