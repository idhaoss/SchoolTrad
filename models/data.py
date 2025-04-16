"""
Data management module for the Trading Dashboard Pro application.
Handles data storage, retrieval, and manipulation for trading configurations,
parameters, notes, and screenshots.
"""
import os
import json
from datetime import datetime
from io import BytesIO
import base64
from PIL import Image
from models.auth import get_profile_path
from config.settings import DEFAULT_PARAMS, MAX_SCREENSHOTS

def load_profile_data(profile_name):
    """
    Load data for a given profile
    
    Args:
        profile_name (str): Name of the profile
        
    Returns:
        dict: Profile data
    """
    profile_path = get_profile_path(profile_name)
    print(f"Loading profile data from: {profile_path}")
    
    if os.path.exists(profile_path):
        try:
            with open(profile_path, 'r') as f:
                data = json.load(f)
            print(f"Successfully loaded profile '{profile_name}' with {len(data)} configurations")
            return data
        except Exception as e:
            print(f"ERROR loading profile '{profile_name}': {e}")
            import traceback
            traceback.print_exc()
            return {}
    else:
        print(f"Profile file not found: {profile_path}")
        return {}

def save_profile_data(profile_name, data):
    """
    Save data for a given profile
    
    Args:
        profile_name (str): Name of the profile
        data (dict): Profile data to save
        
    Returns:
        bool: Success status
    """
    try:
        profile_path = get_profile_path(profile_name)
        print(f"Saving profile data to: {profile_path}")
        
        # Make sure the directory exists
        directory = os.path.dirname(profile_path)
        if not os.path.exists(directory):
            os.makedirs(directory)
            print(f"Created directory: {directory}")
        
        # Save the data
        with open(profile_path, 'w') as f:
            json.dump(data, f, indent=4)
        
        # Verify the file was created
        if os.path.exists(profile_path):
            file_size = os.path.getsize(profile_path)
            print(f"Successfully saved profile data. File size: {file_size} bytes")
            return True
        else:
            print(f"WARNING: File does not exist after writing: {profile_path}")
            return False
    except Exception as e:
        print(f"ERROR saving profile '{profile_name}': {e}")
        import traceback
        traceback.print_exc()
        return False

def get_config_id(asset, timeframe):
    """
    Generate a unique configuration ID for a given asset and timeframe
    
    Args:
        asset (str): Asset name
        timeframe (str): Timeframe
        
    Returns:
        str: Configuration ID
    """
    return f"{asset}_{timeframe}"

def is_tested(asset, timeframe, data=None):
    """
    Check if a configuration is marked as tested
    
    Args:
        asset (str): Asset name
        timeframe (str): Timeframe
        data (dict, optional): Profile data. If None, an empty dict is used.
        
    Returns:
        bool: True if tested, False otherwise
    """
    if data is None:
        data = {}
    
    config_id = get_config_id(asset, timeframe)
    return config_id in data and 'tested' in data[config_id] and data[config_id]['tested']

def is_improved(asset, timeframe, data=None):
    """
    Check if a configuration is marked as improved
    
    Args:
        asset (str): Asset name
        timeframe (str): Timeframe
        data (dict, optional): Profile data. If None, an empty dict is used.
        
    Returns:
        bool: True if improved, False otherwise
    """
    if data is None:
        data = {}
    
    config_id = get_config_id(asset, timeframe)
    return config_id in data and 'improved' in data[config_id] and data[config_id]['improved']

def toggle_tested(asset, timeframe, data):
    """
    Toggle the 'tested' status of a configuration
    
    Args:
        asset (str): Asset name
        timeframe (str): Timeframe
        data (dict): Profile data
        
    Returns:
        tuple: (updated data, new status)
    """
    config_id = get_config_id(asset, timeframe)
    if config_id not in data:
        data[config_id] = {}
    
    current_status = data[config_id].get('tested', False)
    data[config_id]['tested'] = not current_status
    data[config_id]['last_modified'] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    return data, not current_status

def toggle_improved(asset, timeframe, data):
    """
    Toggle the 'improved' status of a configuration
    
    Args:
        asset (str): Asset name
        timeframe (str): Timeframe
        data (dict): Profile data
        
    Returns:
        tuple: (updated data, new status)
    """
    config_id = get_config_id(asset, timeframe)
    if config_id not in data:
        data[config_id] = {}
    
    current_status = data[config_id].get('improved', False)
    data[config_id]['improved'] = not current_status
    data[config_id]['last_modified'] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    return data, not current_status

def get_params(asset, timeframe, data):
    """
    Get parameters for a configuration
    
    Args:
        asset (str): Asset name
        timeframe (str): Timeframe
        data (dict): Profile data
        
    Returns:
        dict: Parameters for the configuration
    """
    config_id = get_config_id(asset, timeframe)
    if config_id in data and 'params' in data[config_id]:
        return data[config_id]['params']
    return DEFAULT_PARAMS.copy()

def save_params(asset, timeframe, params, data):
    """
    Save parameters for a configuration
    
    Args:
        asset (str): Asset name
        timeframe (str): Timeframe
        params (dict): Parameters to save
        data (dict): Profile data
        
    Returns:
        dict: Updated profile data
    """
    config_id = get_config_id(asset, timeframe)
    if config_id not in data:
        data[config_id] = {}
    
    data[config_id]['params'] = params
    data[config_id]['last_modified'] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    return data

def get_note(asset, timeframe, data):
    """
    Get note for a configuration
    
    Args:
        asset (str): Asset name
        timeframe (str): Timeframe
        data (dict): Profile data
        
    Returns:
        str: Note for the configuration
    """
    config_id = get_config_id(asset, timeframe)
    if config_id in data and 'note' in data[config_id]:
        return data[config_id]['note']
    return ""

def save_note(asset, timeframe, note, data):
    """
    Save note for a configuration
    
    Args:
        asset (str): Asset name
        timeframe (str): Timeframe
        note (str): Note to save
        data (dict): Profile data
        
    Returns:
        dict: Updated profile data
    """
    config_id = get_config_id(asset, timeframe)
    if config_id not in data:
        data[config_id] = {}
    
    data[config_id]['note'] = note
    data[config_id]['last_modified'] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    return data

def has_note(asset, timeframe, data=None):
    """
    Check if a configuration has a note
    
    Args:
        asset (str): Asset name
        timeframe (str): Timeframe
        data (dict, optional): Profile data. If None, an empty dict is used.
        
    Returns:
        bool: True if has note, False otherwise
    """
    if data is None:
        data = {}
    
    note = get_note(asset, timeframe, data)
    return note != ""

def get_screenshots(asset, timeframe, data):
    """
    Get screenshots for a configuration
    
    Args:
        asset (str): Asset name
        timeframe (str): Timeframe
        data (dict): Profile data
        
    Returns:
        list: Screenshots for the configuration
    """
    config_id = get_config_id(asset, timeframe)
    if config_id in data and 'screenshots' in data[config_id]:
        return data[config_id]['screenshots']
    return []

def has_screenshots(asset, timeframe, data=None):
    """
    Check if a configuration has screenshots
    
    Args:
        asset (str): Asset name
        timeframe (str): Timeframe
        data (dict, optional): Profile data. If None, an empty dict is used.
        
    Returns:
        bool: True if has screenshots, False otherwise
    """
    if data is None:
        data = {}
    
    screenshots = get_screenshots(asset, timeframe, data)
    return len(screenshots) > 0

def save_screenshot(asset, timeframe, image_data, description, data):
    """
    Save a screenshot for a configuration
    
    Args:
        asset (str): Asset name
        timeframe (str): Timeframe
        image_data (str): Base64-encoded image data
        description (str): Description for the screenshot
        data (dict): Profile data
        
    Returns:
        dict: Updated profile data
    """
    config_id = get_config_id(asset, timeframe)
    if config_id not in data:
        data[config_id] = {}
    
    if 'screenshots' not in data[config_id]:
        data[config_id]['screenshots'] = []
    
    # Limit to MAX_SCREENSHOTS
    if len(data[config_id]['screenshots']) >= MAX_SCREENSHOTS:
        data[config_id]['screenshots'].pop(0)  # Remove the oldest
    
    # Add new screenshot
    screenshot_data = {
        'date': datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        'description': description,
        'image_data': image_data
    }
    
    data[config_id]['screenshots'].append(screenshot_data)
    data[config_id]['last_modified'] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    return data

def delete_screenshot(asset, timeframe, index, data):
    """
    Delete a screenshot for a configuration
    
    Args:
        asset (str): Asset name
        timeframe (str): Timeframe
        index (int): Index of the screenshot to delete
        data (dict): Profile data
        
    Returns:
        tuple: (updated data, success status)
    """
    config_id = get_config_id(asset, timeframe)
    if (config_id in data and 
        'screenshots' in data[config_id] and 
        0 <= index < len(data[config_id]['screenshots'])):
        
        data[config_id]['screenshots'].pop(index)
        data[config_id]['last_modified'] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        return data, True
    
    return data, False

def process_uploaded_image(uploaded_file):
    """
    Process an uploaded image file to base64
    
    Args:
        uploaded_file: Uploaded file object
        
    Returns:
        str: Base64-encoded image data
    """
    try:
        # Open image from uploaded file
        image = Image.open(uploaded_file)
        
        # Convert to base64
        buffered = BytesIO()
        image.save(buffered, format="PNG")
        img_str = base64.b64encode(buffered.getvalue()).decode()
        
        return img_str
    except Exception as e:
        print(f"Error processing image: {e}")
        return None

def export_profile_data(profile_name):
    """
    Export profile data as JSON
    
    Args:
        profile_name (str): Name of the profile
        
    Returns:
        str: JSON string with profile data
    """
    data = load_profile_data(profile_name)
    return json.dumps(data, indent=4)

def import_profile_data(profile_name, json_data, merge=False):
    """
    Import profile data from JSON
    
    Args:
        profile_name (str): Name of the profile
        json_data (str): JSON data to import
        merge (bool, optional): Whether to merge with existing data. Default is False.
        
    Returns:
        tuple: (success, message)
    """
    try:
        import_data = json.loads(json_data)
        
        if merge:
            # Merge with existing data
            current_data = load_profile_data(profile_name)
            for config_id, config_data in import_data.items():
                current_data[config_id] = config_data
            
            save_profile_data(profile_name, current_data)
        else:
            # Replace existing data
            save_profile_data(profile_name, import_data)
        
        return True, f"Données importées avec succès dans '{profile_name}'."
    except Exception as e:
        return False, f"Erreur lors de l'importation: {e}"

def get_profile_stats(profile_name):
    """
    Get statistics for a profile
    
    Args:
        profile_name (str): Name of the profile
        
    Returns:
        dict: Profile statistics
    """
    data = load_profile_data(profile_name)
    
    if not data:
        return {
            "total_configs": 0,
            "configs_tested": 0,
            "configs_improved": 0,
            "configs_with_notes": 0,
            "configs_with_screenshots": 0,
            "percent_tested": 0,
            "percent_improved": 0
        }
    
    total_configs = len(data)
    configs_tested = sum(1 for config_id in data if 'tested' in data[config_id] and data[config_id]['tested'])
    configs_improved = sum(1 for config_id in data if 'improved' in data[config_id] and data[config_id]['improved'])
    configs_with_notes = sum(1 for config_id in data if 'note' in data[config_id] and data[config_id]['note'])
    configs_with_screenshots = sum(1 for config_id in data if 'screenshots' in data[config_id] and data[config_id]['screenshots'])
    
    return {
        "total_configs": total_configs,
        "configs_tested": configs_tested,
        "configs_improved": configs_improved,
        "configs_with_notes": configs_with_notes,
        "configs_with_screenshots": configs_with_screenshots,
        "percent_tested": round(configs_tested / max(1, total_configs) * 100, 1),
        "percent_improved": round(configs_improved / max(1, total_configs) * 100, 1)
    }
