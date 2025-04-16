#!/bin/bash

# Rendre le script exécutable
chmod +x "$0"

echo "============================================"
echo "    INSTALLATION DE SCHOOLTRAD"
echo "============================================"
echo ""

# Vérifier si Python est installé
if ! command -v python3 &> /dev/null; then
    echo "Python 3 n'est pas installé."
    echo "Veuillez installer Python 3.8 ou supérieur."
    echo "Ubuntu/Debian: sudo apt install python3 python3-venv python3-pip"
    echo "MacOS: brew install python3"
    echo ""
    echo "Appuyez sur Entrée pour quitter..."
    read
    exit 1
fi

# Afficher la version de Python
echo "Vérification de Python..."
python3 --version
echo ""

# Créer un environnement virtuel s'il n'existe pas déjà
if [ ! -d "venv" ]; then
    echo "Création de l'environnement virtuel..."
    python3 -m venv venv
    if [ $? -ne 0 ]; then
        echo "Erreur lors de la création de l'environnement virtuel."
        read
        exit 1
    fi
    echo "Environnement virtuel créé avec succès."
else
    echo "Environnement virtuel existant détecté."
fi
echo ""

# Activer l'environnement virtuel et installer les dépendances
echo "Installation des dépendances..."
source venv/bin/activate
pip install --upgrade pip
pip install -r requirements.txt
if [ $? -ne 0 ]; then
    echo "Erreur lors de l'installation des dépendances."
    read
    exit 1
fi
echo "Toutes les dépendances ont été installées avec succès."
echo ""

# Créer le dossier profiles s'il n'existe pas
if [ ! -d "profiles" ]; then
    echo "Création du dossier de données..."
    mkdir profiles
    echo "Dossier 'profiles' créé."
else
    echo "Le dossier de données existe déjà."
fi
echo ""

# Créer le script de lancement
cat > run.sh << 'EOF'
#!/bin/bash
# Obtenir le chemin absolu du script
SCRIPT_DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" &> /dev/null && pwd )"

# Activer l'environnement virtuel
source "$SCRIPT_DIR/venv/bin/activate"

echo "Lancement de SchoolTrad..."
echo ""
python -m streamlit run "$SCRIPT_DIR/streamlit_app.py"

# Gardez la fenêtre du terminal ouverte si l'application se ferme
echo ""
echo "Appuyez sur Entrée pour quitter..."
read
EOF

# Rendre le script de lancement exécutable
chmod +x run.sh

# Créer un raccourci bureau (méthode dépendant du système)
if [[ "$OSTYPE" == "darwin"* ]]; then
    # macOS
    echo "Création du raccourci de lancement pour macOS..."
    DESKTOP="$HOME/Desktop"
    APP_NAME="SchoolTrad"
    
    cat > "$DESKTOP/$APP_NAME.command" << EOF
#!/bin/bash
cd "$(dirname "$0")"
cd "$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"/../$(basename $(pwd))
./run.sh
EOF
    
    chmod +x "$DESKTOP/$APP_NAME.command"
    echo "Raccourci créé sur le Bureau."
else
    # Linux
    echo "Création du raccourci de lancement pour Linux..."
    DESKTOP="$HOME/Desktop"
    if [ ! -d "$DESKTOP" ]; then
        DESKTOP="$HOME/Bureau"
    fi
    
    if [ -d "$DESKTOP" ]; then
        SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" &> /dev/null && pwd)"
        
        cat > "$DESKTOP/SchoolTrad.desktop" << EOF
[Desktop Entry]
Type=Application
Name=SchoolTrad
Comment=Trading Dashboard Pro
Exec=bash -c "cd '$SCRIPT_DIR' && ./run.sh"
Icon=chart
Terminal=true
Categories=Office;Finance;
EOF
        
        chmod +x "$DESKTOP/SchoolTrad.desktop"
        echo "Raccourci créé sur le Bureau."
    else
        echo "Impossible de créer le raccourci bureau (répertoire Bureau non trouvé)."
        echo "Vous pouvez lancer l'application en exécutant ./run.sh"
    fi
fi
echo ""

echo "============================================"
echo "   INSTALLATION TERMINÉE AVEC SUCCÈS!"
echo "============================================"
echo ""
echo "SchoolTrad a été installé avec succès!"
echo ""
echo "Un raccourci a été créé sur votre Bureau."
echo "Double-cliquez sur ce raccourci pour lancer l'application."
echo ""
echo "Ou lancez l'application depuis le terminal avec la commande:"
echo "  ./run.sh"
echo ""
echo "Appuyez sur Entrée pour lancer SchoolTrad maintenant..."
read

# Lancer l'application
./run.sh
