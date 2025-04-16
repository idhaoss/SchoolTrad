"""
Module d'authentification et de gestion des profils.
"""
import os
import json
import hashlib
import secrets
from datetime import datetime

from ..config.settings import CONFIG_FILE, PROFILES_DIR, DEFAULT_PROFILE, DEFAULT_APP_CONFIG

def get_profile_path(profile_name):
    """
    Obtient le chemin du fichier de profil pour un nom donné.
    """
    return os.path.join(PROFILES_DIR, f"{profile_name}.json")

def setup_config():
    """
    Configure l'application en créant les dossiers et fichiers nécessaires.
    """
    # Créer le dossier profiles s'il n'existe pas
    os.makedirs(PROFILES_DIR, exist_ok=True)
    
    # Créer ou charger le fichier de configuration
    if not os.path.exists(CONFIG_FILE):
        with open(CONFIG_FILE, 'w', encoding='utf-8') as f:
            json.dump(DEFAULT_APP_CONFIG, f, indent=4)
        return DEFAULT_APP_CONFIG
    
    try:
        with open(CONFIG_FILE, 'r', encoding='utf-8') as f:
            return json.load(f)
    except:
        return DEFAULT_APP_CONFIG

def hash_password(password):
    """
    Hash un mot de passe avec SHA-256.
    """
    return hashlib.sha256(password.encode()).hexdigest()

def generate_token():
    """
    Génère un token aléatoire pour l'authentification.
    """
    return secrets.token_hex(32)

def create_profile(profile_name, password, is_super_admin=False):
    """
    Crée un nouveau profil avec le mot de passe donné.
    """
    profile_path = get_profile_path(profile_name)
    
    # Vérifier si le profil existe déjà
    if os.path.exists(profile_path):
        return False, "Ce profil existe déjà"
    
    # Créer le profil
    profile_data = {
        "password_hash": hash_password(password),
        "created_at": datetime.now().isoformat(),
        "is_super_admin": is_super_admin,
        "last_login": None,
        "data": {}
    }
    
    # Sauvegarder le profil
    with open(profile_path, 'w', encoding='utf-8') as f:
        json.dump(profile_data, f, indent=4)
    
    return True, "Profil créé avec succès"

def verify_profile(profile_name, password):
    """
    Vérifie les identifiants d'un profil.
    """
    profile_path = get_profile_path(profile_name)
    
    # Vérifier si le profil existe
    if not os.path.exists(profile_path):
        # Si c'est le premier lancement, créer le profil par défaut
        if profile_name == DEFAULT_PROFILE:
            success, message = create_profile(DEFAULT_PROFILE, password, is_super_admin=True)
            if success:
                return True, True  # (success, is_super_admin)
        return False, False
    
    # Charger le profil
    try:
        with open(profile_path, 'r', encoding='utf-8') as f:
            profile_data = json.load(f)
    except:
        return False, False
    
    # Vérifier le mot de passe
    if profile_data["password_hash"] != hash_password(password):
        return False, False
    
    # Mettre à jour la date de dernière connexion
    profile_data["last_login"] = datetime.now().isoformat()
    with open(profile_path, 'w', encoding='utf-8') as f:
        json.dump(profile_data, f, indent=4)
    
    return True, profile_data.get("is_super_admin", False)

def list_profiles():
    """
    Liste tous les profils existants.
    """
    profiles = []
    
    # Créer le dossier profiles s'il n'existe pas
    os.makedirs(PROFILES_DIR, exist_ok=True)
    
    # Lister les fichiers .json dans le dossier profiles
    for filename in os.listdir(PROFILES_DIR):
        if filename.endswith('.json'):
            profile_name = filename[:-5]  # Enlever l'extension .json
            profile_path = os.path.join(PROFILES_DIR, filename)
            
            try:
                with open(profile_path, 'r', encoding='utf-8') as f:
                    profile_data = json.load(f)
                
                profiles.append({
                    "name": profile_name,
                    "created_at": profile_data.get("created_at"),
                    "last_login": profile_data.get("last_login"),
                    "is_super_admin": profile_data.get("is_super_admin", False)
                })
            except:
                continue
    
    return profiles
