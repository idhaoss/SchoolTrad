"""
Authentication views for the Trading Dashboard Pro application.
Includes login screen, profile selection, and related UI components.
"""
import streamlit as st
from models.auth import (
    setup_config, 
    create_profile, 
    verify_admin, 
    set_admin_password, 
    get_profile_list
)
from models.data import load_profile_data
from config.styles import MAIN_CSS

def show_login_screen():
    """
    Display the login/profile selection screen
    
    Returns:
        dict: Session state with login information
    """
    # Apply CSS
    st.markdown(MAIN_CSS, unsafe_allow_html=True)
    
    # Page title
    st.title("📊 Trading Dashboard Pro")
    
    # Container for login components
    with st.container():
        st.markdown('<div class="login-container">', unsafe_allow_html=True)
        st.subheader("Sélection de Profil")
        
        # Get app configuration
        app_config = setup_config()
        
        # Super Admin login section
        with st.expander("Mode Super Admin"):
            admin_password = st.text_input("Mot de passe Super Admin", type="password")
            
            admin_col1, admin_col2 = st.columns(2)
            with admin_col1:
                if st.button("Se connecter Admin"):
                    if verify_admin(admin_password, app_config):
                        st.session_state.is_logged_in = True
                        st.session_state.is_super_admin = True
                        st.session_state.current_profile = app_config["profiles"][0]  # Default profile
                        st.session_state.profile_data = load_profile_data(st.session_state.current_profile)
                        st.rerun()
                    else:
                        st.error("Mot de passe incorrect ou non configuré.")
            
            with admin_col2:
                # Only show the "Configure Admin" button if admin password isn't set
                if not app_config["super_admin_hash"]:
                    if st.button("Configurer Admin"):
                        if admin_password:
                            updated_config = set_admin_password(admin_password, app_config)
                            st.success("Mot de passe Super Admin configuré!")
                            
                            # Log in as admin after setting password
                            st.session_state.is_logged_in = True
                            st.session_state.is_super_admin = True
                            st.session_state.current_profile = updated_config["profiles"][0]
                            st.session_state.profile_data = load_profile_data(st.session_state.current_profile)
                            st.rerun()
                        else:
                            st.error("Veuillez entrer un mot de passe.")
        
        # Regular user login section
        st.subheader("Profils Utilisateurs")
        
        # List existing profiles
        existing_profiles = get_profile_list(app_config)
        if existing_profiles:
            profile_choice = st.radio("Sélectionner un profil existant:", existing_profiles)
            
            if st.button("Se connecter", key="login_existing"):
                st.session_state.is_logged_in = True
                st.session_state.is_super_admin = False
                st.session_state.current_profile = profile_choice
                st.session_state.profile_data = load_profile_data(profile_choice)
                st.rerun()
        else:
            st.info("Aucun profil existant.")
        
        # Create new profile section
        st.subheader("Créer un nouveau profil")
        new_profile_name = st.text_input("Nom du nouveau profil:")
        
        if st.button("Créer et se connecter"):
            if new_profile_name:
                success, message, updated_config = create_profile(new_profile_name, app_config, False)
                
                if success:
                    st.success(message)
                    
                    # Log in with the new profile
                    st.session_state.is_logged_in = True
                    st.session_state.is_super_admin = False
                    st.session_state.current_profile = new_profile_name
                    st.session_state.profile_data = {}
                    st.rerun()
                else:
                    st.error(message)
            else:
                st.error("Veuillez entrer un nom de profil.")
        
        st.markdown('</div>', unsafe_allow_html=True)
