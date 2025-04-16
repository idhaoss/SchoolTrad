"""
Admin views for the Trading Dashboard Pro application.
Contains UI components for managing profiles and viewing statistics
when logged in as a Super Admin.
"""
import streamlit as st
import pandas as pd
from models.auth import get_profile_list, delete_profile
from models.data import get_profile_stats, load_profile_data, export_profile_data, import_profile_data, save_profile_data
from config.settings import ASSET_CATEGORIES, TIMEFRAMES
from views.assets import generate_asset_table

def show_profile_management(app_config):
    """
    Display profile management section
    
    Args:
        app_config (dict): Application configuration
        
    Returns:
        dict: Updated app configuration
    """
    with st.expander("Gestion des Profils", expanded=True):
        st.subheader("Profils existants")
        
        profiles = get_profile_list(app_config)
        
        if not profiles:
            st.warning("Aucun profil trouvé.")
            return app_config
        
        # Display all profiles with stats and delete buttons
        for profile in profiles:
            col1, col2, col3 = st.columns([3, 6, 1])
            
            # Profile name
            with col1:
                st.markdown(f"**{profile}**")
            
            # Profile stats
            with col2:
                stats = get_profile_stats(profile)
                st.write(f"Configs: {stats['total_configs']} | "
                         f"Testées: {stats['configs_tested']} | "
                         f"Améliorées: {stats['configs_improved']}")
            
            # Delete button (can't delete default profile)
            with col3:
                # Only show delete button for non-default profiles
                if profile != app_config["profiles"][0]:  # First profile is considered default
                    if st.button("❌", key=f"delete_{profile}"):
                        success, message, updated_config = delete_profile(profile, app_config)
                        if success:
                            st.success(message)
                            return updated_config
                        else:
                            st.error(message)
        
        return app_config

def show_profile_viewer(app_config):
    """
    Display profile viewer to select which profile to view
    
    Args:
        app_config (dict): Application configuration
        
    Returns:
        str: Selected profile name
    """
    st.subheader("Visualiser un profil")
    profiles = get_profile_list(app_config)
    
    if not profiles:
        st.warning("Aucun profil à visualiser.")
        return None
    
    selected_profile = st.selectbox("Sélectionner un profil:", profiles)
    
    if st.button("Charger ce profil", key="load_profile_btn"):
        return selected_profile
    
    return None

def show_profile_stats_dashboard():
    """Display statistics dashboard for all profiles"""
    st.subheader("Statistiques Globales")
    
    # Get all profiles from config
    app_config = st.session_state.app_config
    profiles = get_profile_list(app_config)
    
    # Collect stats for all profiles
    stats_data = []
    for profile in profiles:
        stats = get_profile_stats(profile)
        stats_data.append({
            "Profil": profile,
            "Total": stats["total_configs"],
            "Testés": stats["configs_tested"],
            "Améliorés": stats["configs_improved"],
            "Notes": stats["configs_with_notes"],
            "Screenshots": stats["configs_with_screenshots"],
            "% Testé": stats["percent_tested"],
            "% Amélioré": stats["percent_improved"]
        })
    
    # Display as a table
    if stats_data:
        # Create DataFrame
        df = pd.DataFrame(stats_data)
        
        # Define styler function for percentage columns
        def style_percentage(val):
            color = 'red' if val < 25 else 'orange' if val < 50 else 'green'
            return f'color: {color}; font-weight: bold'
        
        # Apply styling
        styled_df = df.style.format({
            "% Testé": "{:.1f}%",
            "% Amélioré": "{:.1f}%"
        }).map(style_percentage, subset=["% Testé", "% Amélioré"])
        
        # Display the table
        st.dataframe(styled_df, use_container_width=True)
    else:
        st.info("Aucune donnée statistique disponible.")

def show_profile_data_view(profile_name):
    """
    Display a specific profile's data
    
    Args:
        profile_name (str): Name of the profile to view
        
    Returns:
        bool: True if returning to admin view, False otherwise
    """
    st.subheader(f"Visualisation du profil: {profile_name}")
    profile_data = load_profile_data(profile_name)
    
    if not profile_data:
        st.info(f"Aucune donnée pour le profil '{profile_name}'.")
        if st.button("Retour au tableau de bord Admin", key="empty_profile_return_btn"):
            return True
        return False
    
    # Initialiser les variables de session temporaires pour cette vue
    if "admin_selected_asset" not in st.session_state:
        st.session_state.admin_selected_asset = None
    if "admin_selected_timeframe" not in st.session_state:
        st.session_state.admin_selected_timeframe = None
    
    # Bouton de retour en haut de page
    if st.button("Retour au tableau de bord Admin", key="profile_data_return_btn_top"):
        st.session_state.admin_selected_asset = None
        st.session_state.admin_selected_timeframe = None
        return True
    
    # Créer un layout à deux colonnes comme dans la vue principale
    col1, col2 = st.columns([1, 1])
    
    with col1:
        # Panneau de gauche : tableau des actifs
        st.subheader("Tableau des actifs × timeframes")
        
        # Asset category selector
        cat_col1, cat_col2 = st.columns([2, 3])
        
        with cat_col1:
            view_options = st.radio(
                "Catégorie d'actifs",
                ["Crypto-monnaies", "Actifs Financiers"],
                horizontal=True,
                key="admin_view_selector"
            )
        
        # Set current assets based on selection
        if view_options == "Crypto-monnaies":
            current_assets = ASSET_CATEGORIES["crypto"]["assets"]
            asset_type = "crypto"
        else:
            with cat_col2:
                finance_categories = [cat for cat in ASSET_CATEGORIES.keys() if cat != "crypto"]
                finance_category = st.selectbox(
                    "Type d'actifs financiers", 
                    finance_categories,
                    key="admin_finance_category"
                )
            current_assets = ASSET_CATEGORIES[finance_category]["assets"]
            asset_type = "finance"
        
        # Utilisez generate_interactive_asset_table au lieu de generate_asset_table
        # Mais stockez les sélections dans des variables spécifiques à l'admin
        from views.assets import generate_interactive_asset_table
        
        # Définir une fonction pour capturer la sélection en mode admin
        def admin_generate_interactive_asset_table(assets, timeframes, profile_data):
            """Génère un tableau interactif pour la vue admin"""
            # Create layout with asset names in leftmost column
            col_widths = [2] + [1] * len(timeframes)
            columns = st.columns(col_widths)
            
            # Header row
            with columns[0]:
                st.markdown("### Actif")
            
            for i, tf in enumerate(timeframes):
                with columns[i+1]:
                    st.markdown(f"### {tf}")
            
            # Generate rows of the table
            for asset in assets:
                cols = st.columns(col_widths)
                
                # Asset name column
                with cols[0]:
                    st.markdown(f"**{asset}**")
                
                # Timeframe columns
                for i, tf in enumerate(timeframes):
                    with cols[i+1]:
                        # Build status indicators
                        from models.data import is_tested, is_improved, has_note, has_screenshots
                        
                        status_parts = []
                        
                        if is_tested(asset, tf, profile_data):
                            status_parts.append("✓")
                        
                        if is_improved(asset, tf, profile_data):
                            status_parts.append("⭐")
                        
                        if has_note(asset, tf, profile_data):
                            status_parts.append("📝")
                        
                        if has_screenshots(asset, tf, profile_data):
                            status_parts.append("📊")
                        
                        status_text = " ".join(status_parts) if status_parts else "◯"
                        
                        # Determine button style based on status
                        if "✓" in status_text and "⭐" in status_text:
                            button_style = "primary"
                        elif "✓" in status_text:
                            button_style = "primary"
                        elif "⭐" in status_text:
                            button_style = "primary"
                        elif len(status_parts) > 0:
                            button_style = "secondary"
                        else:
                            button_style = "secondary"
                        
                        # Button to select this configuration
                        if st.button(
                            status_text, 
                            key=f"admin_cell_{asset}_{tf}",
                            use_container_width=True,
                            type=button_style
                        ):
                            st.session_state.admin_selected_asset = asset
                            st.session_state.admin_selected_timeframe = tf
                            st.rerun()
        
        # Générer le tableau interactif
        admin_generate_interactive_asset_table(current_assets, TIMEFRAMES, profile_data)
        
        # Montrer la légende
        from views.assets import show_table_legend
        show_table_legend()
        
        # Export profile data button
        st.markdown("### Exporter les données")
        if st.button("Exporter le profil", key="profile_export_btn", use_container_width=True):
            data_str = export_profile_data(profile_name)
            
            # Create download link
            import base64
            b64 = base64.b64encode(data_str.encode()).decode()
            download_filename = f"{profile_name}_export.json"
            href = f'<a href="data:file/json;base64,{b64}" download="{download_filename}">Télécharger {download_filename}</a>'
            st.markdown(href, unsafe_allow_html=True)
    
    with col2:
        # Panneau de droite : détails de la configuration sélectionnée
        if st.session_state.admin_selected_asset and st.session_state.admin_selected_timeframe:
            # Vue détaillée d'une configuration
            from views.details import show_details_view
            
            # Créer une copie des données du profil pour cette vue
            admin_view_data = profile_data.copy() if profile_data else {}
            
            # Utiliser les variables admin spécifiques sans modifier les variables de session partagées
            updated_data = show_details_view(
                st.session_state.admin_selected_asset, 
                st.session_state.admin_selected_timeframe,
                data_override=admin_view_data  # Utiliser une copie des données pour cette vue
            )
            
            # Toujours sauvegarder les données même si elles ne semblent pas modifiées
            # Cela assure que les modifications sont persistantes
            if updated_data:
                print(f"Saving admin view updates to profile: {profile_name}")
                save_result = save_profile_data(profile_name, updated_data)
                if save_result:
                    st.success("Modifications sauvegardées avec succès")
                else:
                    st.error("Erreur lors de la sauvegarde des modifications")
        else:
            st.info("Sélectionnez une configuration en cliquant sur une cellule du tableau pour voir les détails.")
    
    # Return button at the bottom
    if st.button("Retour au tableau de bord Admin", key="profile_data_return_btn_bottom"):
        st.session_state.admin_selected_asset = None
        st.session_state.admin_selected_timeframe = None
        return True
    
    return False

def show_import_export_panel():
    """Display panel for importing profile data"""
    st.subheader("Import/Export de données")
    
    # Get all profiles
    app_config = st.session_state.app_config
    profiles = get_profile_list(app_config)
    
    # Select target profile
    target_profile = st.selectbox("Profil cible:", profiles)
    
    # Import section
    with st.expander("Importer des données"):
        uploaded_file = st.file_uploader("Choisir un fichier JSON", type=["json"])
        merge_option = st.checkbox("Fusionner avec les données existantes", value=True)
        
        if uploaded_file is not None and st.button("Importer", key="import_data_btn"):
            json_data = uploaded_file.read().decode("utf-8")
            success, message = import_profile_data(target_profile, json_data, merge=merge_option)
            
            if success:
                st.success(message)
            else:
                st.error(message)
    
    # Export section
    with st.expander("Exporter des données"):
        if st.button("Exporter les données du profil", key="export_profile_data_btn"):
            data_str = export_profile_data(target_profile)
            
            # Create download link
            import base64
            b64 = base64.b64encode(data_str.encode()).decode()
            download_filename = f"{target_profile}_export.json"
            href = f'<a href="data:file/json;base64,{b64}" download="{download_filename}">Télécharger {download_filename}</a>'
            st.markdown(href, unsafe_allow_html=True)

def show_admin_view():
    """
    Display the admin interface
    
    Returns:
        tuple: (should_view_profile, profile_to_view)
    """
    st.title("Tableau de Bord Super Admin")
    
    # Toujours recharger la configuration depuis le disque pour voir les nouveaux profils
    from models.auth import setup_config
    st.session_state.app_config = setup_config()
    print("Configuration rechargée pour le tableau de bord admin")
    
    # Create tabs for different admin sections
    tabs = st.tabs(["📊 Tableau de bord", "👥 Gestion des profils", "🔄 Import/Export"])
    
    with tabs[0]:  # Dashboard tab
        show_profile_stats_dashboard()
    
    with tabs[1]:  # Profile management tab
        # Update app_config with any changes
        updated_config = show_profile_management(st.session_state.app_config)
        if updated_config != st.session_state.app_config:
            st.session_state.app_config = updated_config
        
        # Profile viewer
        selected_profile = show_profile_viewer(st.session_state.app_config)
        if selected_profile:
            return True, selected_profile
    
    with tabs[2]:  # Import/Export tab
        show_import_export_panel()
    
    return False, None
