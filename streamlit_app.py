"""
Point d'entrée principal pour le déploiement Streamlit.
Ce fichier est configuré pour fonctionner sur Streamlit Cloud.
"""
import os
import sys
import streamlit as st

# Ajouter le répertoire courant au PYTHONPATH
current_dir = os.path.dirname(os.path.abspath(__file__))
if current_dir not in sys.path:
    sys.path.append(current_dir)

from trading_dashboard_pro.models.auth import setup_config
from trading_dashboard_pro.models.data import load_profile_data, save_profile_data
from trading_dashboard_pro.views.authentication import show_login_screen
from trading_dashboard_pro.views.assets import show_assets_view
from trading_dashboard_pro.views.details import show_details_view
from trading_dashboard_pro.views.admin import show_admin_view, show_profile_data_view

# Configuration de la page
st.set_page_config(
    page_title="SchoolTrad",
    page_icon="📊",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Initialiser les variables de session
if 'is_logged_in' not in st.session_state:
    st.session_state.is_logged_in = False
if 'is_super_admin' not in st.session_state:
    st.session_state.is_super_admin = False
if 'current_profile' not in st.session_state:
    st.session_state.current_profile = ""
if 'profile_data' not in st.session_state:
    st.session_state.profile_data = {}
if 'selected_asset' not in st.session_state:
    st.session_state.selected_asset = None
if 'selected_timeframe' not in st.session_state:
    st.session_state.selected_timeframe = None
if 'show_detail_view' not in st.session_state:
    st.session_state.show_detail_view = False
if 'view_mode' not in st.session_state:
    st.session_state.view_mode = "assets"
if 'admin_viewing_profile' not in st.session_state:
    st.session_state.admin_viewing_profile = None

# Charger la configuration
app_config = setup_config()

# Interface principale de l'application
if not st.session_state.is_logged_in:
    # Écran de connexion
    show_login_screen()
else:
    # Barre latérale pour la gestion du profil et autres options
    with st.sidebar:
        # En-tête avec info profil
        if st.session_state.is_super_admin:
            st.header(f"Super Admin: {st.session_state.current_profile}")
        else:
            st.header(f"Profil: {st.session_state.current_profile}")
        
        # Boutons de navigation (différents selon le mode admin ou non)
        if st.session_state.is_super_admin:
            # Mode Super Admin
            if st.session_state.view_mode == "admin_view_profile":
                if st.button("Retour au tableau de bord Admin"):
                    # Nettoyer les variables de session liées à la vue profil
                    st.session_state.view_mode = "admin"
                    st.session_state.admin_selected_asset = None
                    st.session_state.admin_selected_timeframe = None
                    st.session_state.admin_viewing_profile = None
                    # Forcer un rechargement complet
                    st.rerun()
            elif st.session_state.view_mode != "admin":
                if st.button("Tableau de bord Admin"):
                    st.session_state.view_mode = "admin"
                    st.rerun()
        
        # Bouton pour revenir au tableau des actifs
        if st.session_state.view_mode != "assets" and st.session_state.view_mode != "admin":
            if st.button("Tableau des actifs"):
                st.session_state.view_mode = "assets"
                st.session_state.selected_asset = None
                st.session_state.selected_timeframe = None
                st.rerun()
        
        # Séparateur
        st.markdown("---")
        
        # Section d'import/export
        if st.session_state.view_mode != "admin" and st.session_state.view_mode != "admin_view_profile":
            st.subheader("Import/Export")
            
            # Bouton d'export
            if st.button("Exporter mes données"):
                from trading_dashboard_pro.models.data import export_profile_data
                
                data_str = export_profile_data(st.session_state.current_profile)
                
                # Créer un lien de téléchargement
                import base64
                b64 = base64.b64encode(data_str.encode()).decode()
                download_filename = f"{st.session_state.current_profile}_export.json"
                href = f'<a href="data:file/json;base64,{b64}" download="{download_filename}">Télécharger {download_filename}</a>'
                st.markdown(href, unsafe_allow_html=True)
            
            # Section d'import
            with st.expander("Importer des données"):
                uploaded_file = st.file_uploader("Choisir un fichier JSON", type=["json"])
                merge_option = st.checkbox("Fusionner avec les données existantes", value=True)
                
                if uploaded_file is not None and st.button("Importer"):
                    from trading_dashboard_pro.models.data import import_profile_data
                    
                    json_data = uploaded_file.read().decode("utf-8")
                    success, message = import_profile_data(
                        st.session_state.current_profile,
                        json_data,
                        merge=merge_option
                    )
                    
                    if success:
                        st.success(message)
                        # Recharger les données
                        st.session_state.profile_data = load_profile_data(st.session_state.current_profile)
                        st.rerun()
                    else:
                        st.error(message)
        
        # Séparateur
        st.markdown("---")
        
        # Bouton de déconnexion
        if st.button("Se déconnecter"):
            # Sauvegarder les données avant déconnexion
            save_profile_data(st.session_state.current_profile, st.session_state.profile_data)
            
            # Réinitialiser les variables de session
            st.session_state.is_logged_in = False
            st.session_state.is_super_admin = False
            st.session_state.current_profile = ""
            st.session_state.profile_data = {}
            st.session_state.selected_asset = None
            st.session_state.selected_timeframe = None
            st.session_state.view_mode = "assets"
            st.session_state.admin_viewing_profile = None
            
            st.rerun()
    
    # Contenu principal selon le mode de vue
    if st.session_state.is_super_admin and st.session_state.view_mode == "admin":
        # Vue du tableau de bord admin
        should_view_profile, profile_to_view = show_admin_view()
        
        if should_view_profile:
            st.session_state.admin_viewing_profile = profile_to_view
            st.session_state.view_mode = "admin_view_profile"
            st.rerun()
    
    elif st.session_state.is_super_admin and st.session_state.view_mode == "admin_view_profile":
        # Vue d'un profil spécifique en mode admin
        if show_profile_data_view(st.session_state.admin_viewing_profile):
            # Retour à la vue admin
            st.session_state.view_mode = "admin"
            st.session_state.admin_viewing_profile = None
            st.rerun()
    
    else:
        # Vue principale unifiée (tout sur une page)
        st.session_state.view_mode = "assets"
        
        # Créer un layout à deux colonnes
        col1, col2 = st.columns([1, 1])
        
        with col1:
            # Panneau de gauche : tableau des actifs
            st.subheader("Tableau des actifs × timeframes")
            
            # Bouton pour réduire/agrandir le sélecteur de catégorie
            if st.button("Changer de catégorie d'actifs", use_container_width=True):
                st.session_state.show_category_selector = not st.session_state.get("show_category_selector", True)
                st.rerun()
            
            # Afficher le tableau des actifs
            show_selector = st.session_state.get("show_category_selector", True)
            current_assets, asset_type = show_assets_view(show_selector=show_selector)
        
        with col2:
            # Panneau de droite : détails de la configuration sélectionnée
            if st.session_state.selected_asset and st.session_state.selected_timeframe:
                # Vue détaillée d'une configuration
                updated_data = show_details_view(st.session_state.selected_asset, st.session_state.selected_timeframe)
                
                # Si les données ont changé, les sauvegarder
                if updated_data != st.session_state.profile_data:
                    st.session_state.profile_data = updated_data
                    save_profile_data(st.session_state.current_profile, updated_data)
            else:
                st.info("Sélectionnez une configuration en cliquant sur une cellule du tableau pour voir les détails.")
