"""
Details view for the Trading Dashboard Pro application.
Shows detailed information for a selected asset and timeframe, including
parameters, notes, and screenshots.
"""
import streamlit as st
from models.data import (
    is_tested, is_improved, get_params, save_params, 
    get_note, save_note, get_screenshots, save_screenshot, 
    delete_screenshot, process_uploaded_image, save_profile_data,
    toggle_tested, toggle_improved
)
from config.settings import DEFAULT_PARAMS, MAX_SCREENSHOTS

def show_status_indicators(asset, timeframe, profile_data):
    """
    Display status indicators for the selected configuration
    
    Args:
        asset (str): Selected asset
        timeframe (str): Selected timeframe
        profile_data (dict): User profile data
    """
    # Check statuses
    is_already_tested = is_tested(asset, timeframe, profile_data)
    is_already_improved = is_improved(asset, timeframe, profile_data)
    
    # Display status badges
    status_col1, status_col2 = st.columns(2)
    with status_col1:
        test_status = "✅ TESTÉ" if is_already_tested else "❌ NON TESTÉ"
        st.info(f"Statut: {test_status}")
    
    with status_col2:
        improve_status = "✅ AMÉLIORÉ" if is_already_improved else "❌ NON AMÉLIORÉ"
        st.info(f"Statut: {improve_status}")

def show_parameters_tab(asset, timeframe, profile_data):
    """
    Display and manage parameters for the selected configuration
    
    Args:
        asset (str): Selected asset
        timeframe (str): Selected timeframe
        profile_data (dict): User profile data
        
    Returns:
        dict: Updated profile data
    """
    with st.container():
        st.markdown('<div class="section parameter-section">', unsafe_allow_html=True)
        
        # Get current parameters
        params = get_params(asset, timeframe, profile_data)
        new_params = params.copy()
        
        # Parameter form
        st.subheader("Strat TOP VARIATION STRAT 2 TAB (Heikin Ashi)")
        
        # INPUTS section
        st.markdown("### INPUTS")
        
        # Première rangée de paramètres
        col1, col2, col3, col4 = st.columns(4)
        
        with col1:
            new_params["Price Change Threshold (%)"] = st.text_input(
                "Price Change Threshold (%)", 
                params["Price Change Threshold (%)"]
            )
        
        with col2:
            new_params["Kernel Timeframe"] = st.text_input(
                "Kernel Timeframe", 
                params["Kernel Timeframe"]
            )
            
        with col3:
            new_params["ADX Length"] = st.text_input(
                "ADX Length", 
                params["ADX Length"]
            )
            
        with col4:
            new_params["ADX Level"] = st.text_input(
                "ADX Level", 
                params["ADX Level"]
            )
        
        # Deuxième rangée de paramètres
        col1, col2, col3 = st.columns(3)
        
        with col1:
            new_params["Start Regression at Bar"] = st.text_input(
                "Start Regression at Bar", 
                params["Start Regression at Bar"]
            )
            
        with col2:
            new_params["Lookback Window"] = st.text_input(
                "Lookback Window", 
                params["Lookback Window"]
            )
            
        with col3:
            new_params["Relative Weighting"] = st.text_input(
                "Relative Weighting", 
                params["Relative Weighting"]
            )
        
        # Troisième rangée de paramètres
        col1, col2, col3 = st.columns(3)
        
        with col1:
            new_params["Start Regression at Bar (2)"] = st.text_input(
                "Start Regression at Bar (2)", 
                params["Start Regression at Bar (2)"]
            )
            
        with col2:
            new_params["Lookback Window (2)"] = st.text_input(
                "Lookback Window (2)", 
                params["Lookback Window (2)"]
            )
            
        with col3:
            new_params["Relative Weighting (2)"] = st.text_input(
                "Relative Weighting (2)", 
                params["Relative Weighting (2)"]
            )
        
        # COLORS section
        st.markdown("### COLORS")
        
        col1, col2, col3 = st.columns([1, 1, 2])
        
        with col1:
            smooth_checked = st.checkbox(
                "Smooth Colors", 
                value=True
            )
            
        with col2:
            new_params["Smooth Colors"] = st.text_input(
                "Lag", 
                params["Smooth Colors"]
            )
        
        col1, col2 = st.columns(2)
        
        with col1:
            new_params["Bullish Color"] = st.color_picker(
                "Bullish Color", 
                params["Bullish Color"]
            )
            
        with col2:
            new_params["Bearish Color"] = st.color_picker(
                "Bearish Color", 
                params["Bearish Color"]
            )
        
        # INPUT VALUES section
        st.markdown("### INPUT VALUES")
        new_params["Inputs in status line"] = "Yes" if st.checkbox(
            "Inputs in status line", 
            value=params["Inputs in status line"] == "Yes"
        ) else "No"
        
        # Save button
        if st.button("Sauvegarder les paramètres", key="save_params_btn", use_container_width=True):
            updated_data = save_params(asset, timeframe, new_params, profile_data)
            save_profile_data(st.session_state.current_profile, updated_data)
            st.success("Paramètres sauvegardés!")
            return updated_data
        
        st.markdown('</div>', unsafe_allow_html=True)
    
    return profile_data

def show_notes_tab(asset, timeframe, profile_data):
    """
    Display and manage notes for the selected configuration
    
    Args:
        asset (str): Selected asset
        timeframe (str): Selected timeframe
        profile_data (dict): User profile data
        
    Returns:
        dict: Updated profile data
    """
    with st.container():
        st.markdown('<div class="section note-section">', unsafe_allow_html=True)
        
        # Get current note
        current_note = get_note(asset, timeframe, profile_data)
        
        # Note editor
        st.subheader("Notes & Observations")
        new_note = st.text_area(
            "Notes sur cette configuration:", 
            current_note, 
            height=400
        )
        
        # Save button
        if st.button("Sauvegarder la note", key="save_note_btn", use_container_width=True):
            updated_data = save_note(asset, timeframe, new_note, profile_data)
            save_profile_data(st.session_state.current_profile, updated_data)
            st.success("Note sauvegardée!")
            return updated_data
        
        st.markdown('</div>', unsafe_allow_html=True)
    
    return profile_data

def show_screenshots_tab(asset, timeframe, profile_data):
    """
    Display and manage screenshots for the selected configuration
    
    Args:
        asset (str): Selected asset
        timeframe (str): Selected timeframe
        profile_data (dict): User profile data
        
    Returns:
        dict: Updated profile data
    """
    with st.container():
        st.markdown('<div class="section screenshot-section">', unsafe_allow_html=True)
        st.subheader("Captures d'écran")
        
        # Get current screenshots
        screenshots = get_screenshots(asset, timeframe, profile_data)
        
        if screenshots:
            st.markdown(f"**{len(screenshots)} capture(s) d'écran disponible(s)**")
            st.markdown('<div class="thumbnails">', unsafe_allow_html=True)
            
            for i, screenshot in enumerate(screenshots):
                st.markdown(f"##### Capture {i+1} ({screenshot['date']})")
                
                if screenshot['description']:
                    st.markdown(f"*{screenshot['description']}*")
                
                try:
                    # Display the image
                    import base64
                    from io import BytesIO
                    from PIL import Image
                    
                    image_data = base64.b64decode(screenshot['image_data'])
                    image = Image.open(BytesIO(image_data))
                    st.image(image, use_column_width=True)
                    
                    # Delete button
                    if st.button(f"Supprimer", key=f"delete_screenshot_{i}"):
                        updated_data, success = delete_screenshot(asset, timeframe, i, profile_data)
                        if success:
                            save_profile_data(st.session_state.current_profile, updated_data)
                            st.success("Capture d'écran supprimée!")
                            return updated_data  # Force a rerun by returning the updated data
                except Exception as e:
                    st.error(f"Erreur lors de l'affichage: {e}")
                
                st.markdown("---")
            
            st.markdown('</div>', unsafe_allow_html=True)
        else:
            st.info("Aucune capture d'écran pour cette configuration.")
        
        # Upload new screenshot
        if len(screenshots) < MAX_SCREENSHOTS:
            st.markdown("### Ajouter une capture d'écran")
            
            description = st.text_input("Description:", key="new_screenshot_desc")
            uploaded_file = st.file_uploader("Choisir une image...", type=["jpg", "jpeg", "png"])
            
            if uploaded_file is not None:
                # Preview the image
                try:
                    from PIL import Image
                    image = Image.open(uploaded_file)
                    st.image(image, caption="Aperçu", width=300)
                    
                    # Save button
                    if st.button("Sauvegarder cette capture d'écran"):
                        # Process the image
                        img_str = process_uploaded_image(uploaded_file)
                        
                        if img_str:
                            # Save the screenshot
                            updated_data = save_screenshot(asset, timeframe, img_str, description, profile_data)
                            save_profile_data(st.session_state.current_profile, updated_data)
                            st.success("Capture d'écran ajoutée!")
                            return updated_data
                        else:
                            st.error("Erreur lors du traitement de l'image.")
                except Exception as e:
                    st.error(f"Erreur: {e}")
        else:
            st.warning(f"Vous avez atteint la limite de {MAX_SCREENSHOTS} captures d'écran. "
                      "Supprimez-en une pour en ajouter une nouvelle.")
        
        st.markdown('</div>', unsafe_allow_html=True)
    
    return profile_data

def show_details_view(asset, timeframe, data_override=None):
    """
    Display detailed view for a selected asset and timeframe
    
    Args:
        asset (str): Selected asset
        timeframe (str): Selected timeframe
        data_override (dict, optional): Override session data with this data. Used in admin view.
        
    Returns:
        dict: Updated profile data
    """
    # Utiliser les données spécifiques si fournies, sinon utiliser les données de session
    profile_data = data_override if data_override is not None else st.session_state.profile_data
    
    st.markdown(f"## Configuration: {asset} - {timeframe}")
    
    # Display status indicators
    show_status_indicators(asset, timeframe, profile_data)
    
    # Actions row avec boutons pour marquer testé/amélioré
    col1, col2 = st.columns(2)
    
    with col1:
        is_already_tested = is_tested(asset, timeframe, st.session_state.profile_data)
        btn_label = "Marquer Non Testé" if is_already_tested else "Marquer Testé"
        
        if st.button(btn_label, use_container_width=True, key="detail_test_btn"):
            updated_data, new_status = toggle_tested(asset, timeframe, st.session_state.profile_data)
            st.session_state.profile_data = updated_data
            save_profile_data(st.session_state.current_profile, updated_data)
            st.success(f"Marqué comme {'testé' if new_status else 'non testé'}")
            return updated_data
    
    with col2:
        is_already_improved = is_improved(asset, timeframe, st.session_state.profile_data)
        improve_btn_label = "Marquer Non Amélioré" if is_already_improved else "Marquer Amélioré"
        
        if st.button(improve_btn_label, use_container_width=True, key="detail_improve_btn"):
            updated_data, new_status = toggle_improved(asset, timeframe, st.session_state.profile_data)
            st.session_state.profile_data = updated_data
            save_profile_data(st.session_state.current_profile, updated_data)
            st.success(f"Marqué comme {'amélioré' if new_status else 'non amélioré'}")
            return updated_data
    
    # Sections de détails empilées verticalement
    with st.expander("📊 Paramètres", expanded=True):
        updated_data = show_parameters_tab(asset, timeframe, profile_data)
        if data_override is None and updated_data != st.session_state.profile_data:
            st.session_state.profile_data = updated_data
    
    with st.expander("📝 Notes", expanded=True):  
        updated_data = show_notes_tab(asset, timeframe, profile_data)
        if data_override is None and updated_data != st.session_state.profile_data:
            st.session_state.profile_data = updated_data
    
    with st.expander("🖼️ Captures d'écran", expanded=True):
        updated_data = show_screenshots_tab(asset, timeframe, profile_data)
        if data_override is None and updated_data != st.session_state.profile_data:
            st.session_state.profile_data = updated_data
    
    return st.session_state.profile_data
