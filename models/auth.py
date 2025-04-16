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

def create_profile(profile_name, app_config, is_super_admin=False):
    """
    Crée un nouveau profil et met à jour la configuration de l'application.
    
    Args:
        profile_name (str): Nom du profil
        app_config (dict): Configuration actuelle de l'application
        is_super_admin (bool, optional): Si le profil est un super admin
        
    Returns:
        tuple: (success, message, updated_config)
    """
    # Vérifier si le profil existe déjà dans la liste des profils
    if profile_name in app_config.get("profiles", []):
        return False, "Ce profil existe déjà", app_config
    
    # Ajouter le profil à la liste des profils
    if "profiles" not in app_config:
        app_config["profiles"] = []
    
    app_config["profiles"].append(profile_name)
    
    # Sauvegarder la configuration
    with open(CONFIG_FILE, 'w', encoding='utf-8') as f:
        json.dump(app_config, f, indent=4)
    
    # Créer le fichier de profil avec des données vides
    profile_path = get_profile_path(profile_name)
    
    # Créer le dossier profiles s'il n'existe pas
    os.makedirs(os.path.dirname(profile_path), exist_ok=True)
    
    # Structure des données de profil
    profile_data = {}
    
    # Sauvegarder le profil
    with open(profile_path, 'w', encoding='utf-8') as f:
        json.dump(profile_data, f, indent=4)
    
    return True, f"Profil '{profile_name}' créé avec succès", app_config

def verify_admin(password, app_config):
    """
    Vérifie si le mot de passe admin est correct.
    
    Args:
        password (str): Mot de passe admin
        app_config (dict): Configuration de l'application
        
    Returns:
        bool: True si le mot de passe est correct, False sinon
    """
    # Si le mot de passe admin n'est pas configuré, c'est faux
    if "super_admin_hash" not in app_config or not app_config["super_admin_hash"]:
        return False
    
    # Vérifier le hash
    return app_config["super_admin_hash"] == hash_password(password)

def set_admin_password(password, app_config):
    """
    Configure le mot de passe admin.
    
    Args:
        password (str): Nouveau mot de passe admin
        app_config (dict): Configuration de l'application
        
    Returns:
        dict: Configuration mise à jour
    """
    # Hasher le mot de passe
    password_hash = hash_password(password)
    
    # Mettre à jour la configuration
    app_config["super_admin_hash"] = password_hash
    
    # Sauvegarder la configuration
    with open(CONFIG_FILE, 'w', encoding='utf-8') as f:
        json.dump(app_config, f, indent=4)
    
    return app_config

def get_profile_list(app_config):
    """
    Obtient la liste des profils.
    
    Args:
        app_config (dict): Configuration de l'application
        
    Returns:
        list: Liste des noms de profils
    """
    return app_config.get("profiles", [])

def delete_profile(profile_name, app_config):
    """
    Supprime un profil.
    
    Args:
        profile_name (str): Nom du profil à supprimer
        app_config (dict): Configuration de l'application
        
    Returns:
        tuple: (success, message, updated_config)
    """
    # Vérifier si le profil existe dans la configuration
    if profile_name not in app_config.get("profiles", []):
        return False, f"Profil '{profile_name}' introuvable", app_config
    
    # Supprimer le profil de la liste
    app_config["profiles"].remove(profile_name)
    
    # Sauvegarder la configuration
    with open(CONFIG_FILE, 'w', encoding='utf-8') as f:
        json.dump(app_config, f, indent=4)
    
    # Supprimer le fichier de profil s'il existe
    profile_path = get_profile_path(profile_name)
    if os.path.exists(profile_path):
        try:
            os.remove(profile_path)
        except Exception as e:
            return False, f"Erreur lors de la suppression du fichier: {e}", app_config
    
    return True, f"Profil '{profile_name}' supprimé avec succès", app_config

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
