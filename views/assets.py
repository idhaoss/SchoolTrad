"""
Assets view for the Trading Dashboard Pro application.
Displays the main asset × timeframe table and related components.
"""
import streamlit as st
import pandas as pd
from config.settings import ASSET_CATEGORIES, TIMEFRAMES
from models.data import (
    is_tested, is_improved, has_note, has_screenshots, toggle_tested, toggle_improved,
    save_profile_data, get_custom_assets, add_custom_asset
)

def show_asset_category_selector():
    """
    Show the asset category selector (Crypto vs Financial Assets)
    
    Returns:
        tuple: (asset_list, category_type)
    """
    # Category selector
    col1, col2 = st.columns([2, 3])
    
    with col1:
        view_options = st.radio(
            "Catégorie d'actifs",
            ["Crypto-monnaies", "Actifs Financiers"],
            horizontal=True,
            key="view_selector"
        )
    
    # Get current asset list based on selection
    if view_options == "Crypto-monnaies":
        st.session_state.view = "crypto"
        
        # Récupérer la liste des cryptos personnalisées
        custom_assets = get_custom_assets(st.session_state.current_profile, st.session_state.profile_data)
        all_assets = ASSET_CATEGORIES["crypto"]["assets"] + custom_assets
        all_assets = list(set(all_assets))  # Enlever les doublons
        all_assets.sort()  # Trier la liste
        
        # Interface d'ajout de crypto
        with st.expander("➕ Ajouter une crypto personnalisée", expanded=False):
            add_col1, add_col2 = st.columns([3, 1])
            with add_col1:
                new_asset = st.text_input(
                    "Symbole de la crypto (ex: SOL/USD):",
                    key="new_crypto_input"
                )
            with add_col2:
                if st.button("Ajouter", key="add_crypto_btn", type="primary"):
                    if new_asset:
                        # Vérifier le format
                        if "/" not in new_asset:
                            new_asset = f"{new_asset}/USD"
                        
                        success, message, updated_data = add_custom_asset(
                            st.session_state.current_profile,
                            new_asset,
                            st.session_state.profile_data
                        )
                        if success:
                            st.success(message)
                            st.session_state.profile_data = updated_data
                            st.rerun()
                        else:
                            st.error(message)
                    else:
                        st.error("Veuillez entrer un symbole.")
        
        return all_assets, "crypto"
    else:
        st.session_state.view = "finance"
        
        # Financial subcategory selector
        with col2:
            finance_categories = [cat for cat in ASSET_CATEGORIES.keys() if cat != "crypto"]
            if "finance_category" not in st.session_state:
                st.session_state.finance_category = finance_categories[0]
                
            finance_category = st.selectbox(
                "Type d'actifs financiers", 
                finance_categories,
                index=finance_categories.index(st.session_state.finance_category)
            )
            st.session_state.finance_category = finance_category
            
        current_assets = ASSET_CATEGORIES[finance_category]["assets"]
        return current_assets, "finance"

def generate_asset_table(assets, timeframes, profile_data):
    """
    Generate a styled DataFrame with status indicators for each asset × timeframe
    
    Args:
        assets (list): List of assets
        timeframes (list): List of timeframes
        profile_data (dict): User profile data
        
    Returns:
        tuple: (DataFrame, styled DataFrame)
    """
    # Create dataframe
    data = []
    for asset in assets:
        row = {'Asset': asset}
        for tf in timeframes:
            # Build status indicators
            status_parts = []
            
            if is_tested(asset, tf, profile_data):
                status_parts.append("✓")
            
            if is_improved(asset, tf, profile_data):
                status_parts.append("⭐")
            
            if has_note(asset, tf, profile_data):
                status_parts.append("📝")
            
            if has_screenshots(asset, tf, profile_data):
                status_parts.append("📊")
            
            row[tf] = " ".join(status_parts) if status_parts else ""
        data.append(row)
    
    df = pd.DataFrame(data)
    
    # Apply conditional styling
    def highlight_cell(val):
        if "✓" in str(val) and "⭐" in str(val):
            return 'background-color: #d1e7dd; color: #0a3622; font-weight: bold; text-align: center;'
        elif "✓" in str(val):
            return 'background-color: #d4edda; color: #155724; font-weight: bold; text-align: center;'
        elif "⭐" in str(val):
            return 'background-color: #cce5ff; color: #004085; font-weight: bold; text-align: center;'
        elif len(str(val)) > 0:
            return 'background-color: #fff3cd; color: #856404; font-weight: bold; text-align: center;'
        else:
            return 'text-align: center;'
    
    styled_df = df.style.applymap(highlight_cell, subset=timeframes)
    
    return df, styled_df

def generate_interactive_asset_table(assets, timeframes, profile_data):
    """
    Generate an interactive table with clickable cells
    
    Args:
        assets (list): List of assets
        timeframes (list): List of timeframes
        profile_data (dict): User profile data
    """
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
                    key=f"cell_{asset}_{tf}",
                    use_container_width=True,
                    type=button_style
                ):
                    st.session_state.selected_asset = asset
                    st.session_state.selected_timeframe = tf
                    st.session_state.show_detail_view = True

def show_table_legend():
    """Display the legend for table status indicators"""
    with st.expander("Légende du tableau"):
        col1, col2, col3, col4 = st.columns(4)
        with col1:
            st.markdown("**✓** : Configuration testée")
        with col2:
            st.markdown("**⭐** : Configuration améliorée")
        with col3:
            st.markdown("**📝** : Notes disponibles")
        with col4:
            st.markdown("**📊** : Captures d'écran disponibles")

def show_asset_selector(current_assets):
    """
    Show the asset and timeframe selector
    
    Args:
        current_assets (list): List of available assets
        
    Returns:
        tuple: (selected_asset, selected_timeframe)
    """
    st.markdown("## Sélectionner une configuration")
    select_col1, select_col2, select_col3, select_col4 = st.columns([2, 1, 1, 1])
    
    with select_col1:
        selected_asset = st.selectbox("Actif", current_assets)
    with select_col2:
        selected_tf = st.selectbox("Timeframe", TIMEFRAMES)
    
    with select_col3:
        if st.button("Afficher", use_container_width=True):
            st.session_state.selected_asset = selected_asset
            st.session_state.selected_timeframe = selected_tf
            st.rerun()
    
    with select_col4:
        is_already_tested = is_tested(selected_asset, selected_tf, st.session_state.profile_data)
        btn_label = "Marquer Non Testé" if is_already_tested else "Marquer Testé"
        
        if st.button(btn_label, use_container_width=True):
            updated_data, new_status = toggle_tested(selected_asset, selected_tf, st.session_state.profile_data)
            st.session_state.profile_data = updated_data
            save_profile_data(st.session_state.current_profile, updated_data)
            st.success(f"Marqué comme {'testé' if new_status else 'non testé'}")
            st.rerun()
    
    # Add button for improved status
    st.markdown("")  # Add some space
    improve_col1, improve_col2 = st.columns([3, 1])
    
    with improve_col2:
        is_already_improved = is_improved(selected_asset, selected_tf, st.session_state.profile_data)
        improve_btn_label = "Marquer Non Amélioré" if is_already_improved else "Marquer Amélioré"
        
        if st.button(improve_btn_label, use_container_width=True):
            updated_data, new_status = toggle_improved(selected_asset, selected_tf, st.session_state.profile_data)
            st.session_state.profile_data = updated_data
            save_profile_data(st.session_state.current_profile, updated_data)
            st.success(f"Marqué comme {'amélioré' if new_status else 'non amélioré'}")
            st.rerun()
    
    return selected_asset, selected_tf

def show_assets_view(show_selector=True):
    """
    Display the main assets view with table and selectors
    
    Args:
        show_selector (bool): Whether to show the category selector (default: True)
    
    Returns:
        tuple: (current_assets, asset_type) - The assets being displayed
    """
    # Show category selector and get assets to display
    if show_selector:
        st.header("Tableau des Actifs × Timeframes")
        current_assets, asset_type = show_asset_category_selector()
    else:
        # Use the asset category stored in session state
        if "view" not in st.session_state or st.session_state.view == "crypto":
            # Récupérer la liste des cryptos personnalisées
            custom_assets = get_custom_assets(st.session_state.current_profile, st.session_state.profile_data)
            all_assets = ASSET_CATEGORIES["crypto"]["assets"] + custom_assets
            all_assets = list(set(all_assets))  # Enlever les doublons
            all_assets.sort()  # Trier la liste
            current_assets = all_assets
            asset_type = "crypto"
        else:
            finance_categories = [cat for cat in ASSET_CATEGORIES.keys() if cat != "crypto"]
            if "finance_category" not in st.session_state:
                st.session_state.finance_category = finance_categories[0]
            current_assets = ASSET_CATEGORIES[st.session_state.finance_category]["assets"]
            asset_type = "finance"
    
    # Generate and display the interactive asset table
    generate_interactive_asset_table(current_assets, TIMEFRAMES, st.session_state.profile_data)
    
    # Show table legend
    show_table_legend()
    
    return current_assets, asset_type
