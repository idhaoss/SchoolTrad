"""
Authentication module for the Trading Dashboard Pro application.
Handles user profiles, password hashing, and related functionality.
"""
import os
import json
import hashlib
import secrets
from datetime import datetime
from trading_dashboard_pro.config.settings import CONFIG_FILE, PROFILES_DIR, DEFAULT_PROFILE, DEFAULT_APP_CONFIG

def get_profile_path(profile_name):
    """
    Get the path to the profile's data file
    
    Args:
        profile_name (str): Name of the profile
        
    Returns:
        str: Path to the profile's data file
    """
    return os.path.join(PROFILES_DIR, f"{profile_name}_data.json")

def hash_password(password, salt=None):
    """
    Create a secure hash for the provided password
    
    Args:
        password (str): Password to hash
        salt (str, optional): Salt for the hash. If None, a new one is generated.
        
    Returns:
        tuple: (hash, salt)
    """
    if salt is None:
        salt = secrets.token_hex(16)
    hash_obj = hashlib.sha256((password + salt).encode())
    return hash_obj.hexdigest(), salt

def verify_password(password, stored_hash, salt):
    """
    Verify a password against a stored hash
    
    Args:
        password (str): Password to verify
        stored_hash (str): The stored password hash
        salt (str): The salt used for hashing
        
    Returns:
        bool: True if password is correct, False otherwise
    """
    hash_obj = hashlib.sha256((password + salt).encode())
    return hash_obj.hexdigest() == stored_hash

def setup_config():
    """
    Set up or load the application configuration
    
    Returns:
        dict: The application configuration
    """
    if not os.path.exists(CONFIG_FILE):
        with open(CONFIG_FILE, 'w') as f:
            json.dump(DEFAULT_APP_CONFIG, f, indent=4)
        return DEFAULT_APP_CONFIG.copy()
    
    try:
        with open(CONFIG_FILE, 'r') as f:
            config = json.load(f)
        
        # Add missing fields if needed
        was_updated = False
        for key, value in DEFAULT_APP_CONFIG.items():
            if key not in config:
                config[key] = value
                was_updated = True
        
        if was_updated:
            with open(CONFIG_FILE, 'w') as f:
                json.dump(config, f, indent=4)
        
        return config
    except Exception as e:
        print(f"Error loading config: {e}")
        return DEFAULT_APP_CONFIG.copy()

def set_admin_password(password, config):
    """
    Set the admin password in the config
    
    Args:
        password (str): Password to set
        config (dict): Application configuration
        
    Returns:
        dict: Updated configuration
    """
    password_hash, salt = hash_password(password)
    config["super_admin_hash"] = password_hash
    config["super_admin_salt"] = salt
    
    with open(CONFIG_FILE, 'w') as f:
        json.dump(config, f, indent=4)
    
    return config

def verify_admin(password, config):
    """
    Verify if the provided password matches the admin password
    
    Args:
        password (str): Password to verify
        config (dict): Application configuration
        
    Returns:
        bool: True if admin password is correct, False otherwise
    """
    if not config["super_admin_hash"] or not config["super_admin_salt"]:
        return False
    
    return verify_password(password, config["super_admin_hash"], config["super_admin_salt"])

def create_profile(profile_name, config):
    """
    Create a new user profile
    
    Args:
        profile_name (str): Name of the profile to create
        config (dict): Application configuration
        
    Returns:
        tuple: (success, message, updated_config)
    """
    if profile_name in config["profiles"]:
        return False, f"Le profil '{profile_name}' existe déjà.", config
    
    if not profile_name:
        return False, "Le nom de profil ne peut pas être vide.", config
    
    # Add to profiles list
    config["profiles"].append(profile_name)
    
    # Save the updated config
    with open(CONFIG_FILE, 'w') as f:
        json.dump(config, f, indent=4)
    
    # Create an empty data file for the profile
    profile_path = get_profile_path(profile_name)
    with open(profile_path, 'w') as f:
        json.dump({}, f, indent=4)
    
    return True, f"Profil '{profile_name}' créé avec succès.", config

def delete_profile(profile_name, config):
    """
    Delete a user profile
    
    Args:
        profile_name (str): Name of the profile to delete
        config (dict): Application configuration
        
    Returns:
        tuple: (success, message, updated_config)
    """
    if profile_name == DEFAULT_PROFILE:
        return False, "Impossible de supprimer le profil par défaut.", config
    
    if profile_name not in config["profiles"]:
        return False, f"Le profil '{profile_name}' n'existe pas.", config
    
    # Remove from profiles list
    config["profiles"].remove(profile_name)
    
    # Save the updated config
    with open(CONFIG_FILE, 'w') as f:
        json.dump(config, f, indent=4)
    
    # Delete the profile's data file
    profile_path = get_profile_path(profile_name)
    if os.path.exists(profile_path):
        os.remove(profile_path)
    
    return True, f"Profil '{profile_name}' supprimé avec succès.", config

def get_profile_list(config):
    """
    Get the list of available profiles
    
    Args:
        config (dict): Application configuration
        
    Returns:
        list: List of profile names
    """
    return config["profiles"]
