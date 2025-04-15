# Guide de Contribution

Merci de votre intérêt pour contribuer à SchoolTrad ! Ce document fournit les directives et étapes à suivre pour contribuer efficacement au projet.

## Configuration de l'environnement de développement

1. Clonez le dépôt :
```bash
git clone https://github.com/votre-nom-utilisateur/schooltrad.git
cd schooltrad
```

2. Créez et activez un environnement virtuel :
```bash
python -m venv venv
# Sur Windows
venv\Scripts\activate
# Sur macOS/Linux
source venv/bin/activate
```

3. Installez les dépendances :
```bash
pip install -r requirements.txt
```

4. Lancez l'application :
```bash
python -m streamlit run trading_dashboard_pro/app.py
```

## Structure du projet

L'application suit une architecture MVC (Modèle-Vue-Contrôleur) simplifiée :

- `models/` : Logique métier et gestion des données
- `views/` : Interfaces utilisateur Streamlit
- `config/` : Paramètres de configuration
- `utils/` : Fonctions utilitaires

## Normes de codage

- Suivez la [PEP 8](https://www.python.org/dev/peps/pep-0008/) pour le style de code Python
- Utilisez des docstrings au format Google pour documenter toutes les fonctions et classes
- Limitez la longueur des lignes à 88 caractères
- Utilisez des noms significatifs pour les variables et fonctions

## Procédure de contribution

1. **Créez une branche** pour votre fonctionnalité ou correction :
```bash
git checkout -b feature/nom-de-votre-fonctionnalite
```

2. **Apportez vos modifications** et assurez-vous que le code fonctionne correctement
   - Ajoutez des tests si nécessaire
   - Mettez à jour la documentation si nécessaire

3. **Validez vos modifications** avec des messages descriptifs :
```bash
git commit -m "Description claire de vos modifications"
```

4. **Poussez votre branche** vers votre fork :
```bash
git push origin feature/nom-de-votre-fonctionnalite
```

5. **Créez une Pull Request** vers la branche principale du dépôt original

## Conseils pour les Pull Requests

- Une PR par fonctionnalité/correction
- Incluez une description claire de ce que fait votre PR
- Référencez tout problème (issue) lié à votre PR
- Attendez les commentaires et révisez votre code si nécessaire

## Ajout de nouvelles fonctionnalités

1. **Modules de données** : Étendez les classes dans `models/` pour prendre en charge de nouveaux types de données ou fonctionnalités
2. **Interface utilisateur** : Ajoutez de nouvelles vues dans `views/` et intégrez-les dans la structure existante
3. **Configuration** : Mettez à jour les paramètres dans `config/settings.py` si nécessaire

## Contactez-nous

Si vous avez des questions ou besoin d'aide, n'hésitez pas à :
- Ouvrir une issue sur GitHub
- Contacter directement le mainteneur du projet

Merci de contribuer à améliorer Trading Dashboard Pro !
