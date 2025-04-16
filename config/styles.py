"""
CSS styles for the Trading Dashboard Pro application.
These styles customize the Streamlit interface for a better user experience.
"""

# Theme variables for reference
LIGHT_THEME = {
    "background": "linear-gradient(to bottom right, #f8f9fa, #e9ecef)",
    "text_color": "#1e293b",
    "secondary_text": "#475569",
    "sidebar_bg": "#1e293b",
    "sidebar_text": "#f8fafc",
    "button_bg": "#3b82f6",
    "button_hover": "#2563eb",
    "card_bg": "white",
    "border_color": "#e2e8f0",
    "success_color": "#10b981",
    "info_color": "#3b82f6",
    "warning_color": "#f59e0b",
    "error_color": "#dc2626",
    "table_header_bg": "#f8fafc",
    "table_header_text": "#334155",
    "table_row_alt": "#f8fafc",
    "table_row_hover": "#f1f5f9"
}

DARK_THEME = {
    "background": "linear-gradient(to bottom right, #0f172a, #1e293b)",
    "text_color": "#f8fafc",
    "secondary_text": "#cbd5e1",
    "sidebar_bg": "#0f172a",
    "sidebar_text": "#f8fafc",
    "button_bg": "#2563eb",
    "button_hover": "#3b82f6",
    "card_bg": "#1e293b",
    "border_color": "#334155",
    "success_color": "#10b981",
    "info_color": "#3b82f6",
    "warning_color": "#f59e0b",
    "error_color": "#dc2626",
    "table_header_bg": "#0f172a",
    "table_header_text": "#e2e8f0",
    "table_row_alt": "#1e293b",
    "table_row_hover": "#334155"
}

# Main CSS styles for the application (light theme)
MAIN_CSS = """
<style>
    /* CUSTOM FONT IMPORT */
    @import url('https://fonts.googleapis.com/css2?family=Roboto:wght@300;400;500;700&family=Montserrat:wght@500;600;700&display=swap');
    
    /* GLOBAL STYLING */
    html, body, [class*="css"] {
        font-family: 'Roboto', sans-serif;
    }
    
    .main {
        background: linear-gradient(to bottom right, #f8f9fa, #e9ecef);
        padding: 0;
    }
    
    .block-container {
        padding-top: 1rem;
        padding-bottom: 1rem;
    }
    
    .dataframe {
        font-family: 'Roboto', sans-serif;
        font-size: 0.9rem;
    }
    
    /* HEADINGS */
    h1, h2, h3, h4, h5, h6 {
        font-family: 'Montserrat', sans-serif;
        font-weight: 600;
    }
    
    h1 {
        color: #1e293b;
        font-size: 2.2rem;
        font-weight: 700;
        padding-bottom: 1rem;
        border-bottom: 2px solid #e2e8f0;
        margin-bottom: 1.5rem;
    }
    
    h2 {
        color: #334155;
        font-size: 1.6rem;
        margin-top: 1.5rem;
        margin-bottom: 1rem;
    }
    
    h3 {
        color: #475569;
        font-size: 1.3rem;
        margin-top: 1rem;
        margin-bottom: 0.5rem;
    }
    
    /* BUTTON STYLING */
    .stButton>button {
        background-color: #3b82f6;
        color: white;
        border: none;
        border-radius: 0.375rem;
        padding: 0.5rem 1rem;
        font-weight: 500;
        transition: all 0.2s ease;
        box-shadow: 0 2px 4px rgba(59, 130, 246, 0.3);
    }
    
    .stButton>button:hover {
        background-color: #2563eb;
        box-shadow: 0 4px 8px rgba(37, 99, 235, 0.4);
        transform: translateY(-1px);
    }
    
    .stButton>button:active {
        transform: translateY(0);
        box-shadow: 0 1px 2px rgba(37, 99, 235, 0.4);
    }
    
    /* Button variants */
    button[data-baseweb="button"][kind="primary"] {
        background-color: #2563eb !important;
    }
    
    button[data-baseweb="button"][kind="secondary"] {
        background-color: #64748b !important;
    }
    
    /* SIDEBAR STYLING */
    [data-testid="stSidebar"] {
        background-color: #1e293b;
        padding-top: 2rem;
    }
    
    [data-testid="stSidebar"] h1, 
    [data-testid="stSidebar"] h2, 
    [data-testid="stSidebar"] h3, 
    [data-testid="stSidebar"] h4 {
        color: #f8fafc;
    }
    
    [data-testid="stSidebar"] .stButton>button {
        width: 100%;
        background-color: #334155;
        margin-bottom: 0.5rem;
    }
    
    [data-testid="stSidebar"] .stButton>button:hover {
        background-color: #475569;
    }
    
    [data-testid="stSidebar"] hr {
        border-color: #475569;
        margin: 1.5rem 0;
    }
    
    /* PROFILE & ADMIN BADGES */
    .profile-badge {
        background-color: #cbd5e1;
        padding: 0.25rem 0.75rem;
        border-radius: 9999px;
        font-weight: 500;
        font-size: 0.875rem;
        margin-left: 0.5rem;
        display: inline-block;
    }
    
    .admin-badge {
        background-color: #dc2626;
        color: white;
        padding: 0.25rem 0.75rem;
        border-radius: 9999px;
        font-weight: 500;
        font-size: 0.875rem;
        margin-left: 0.5rem;
        display: inline-block;
    }
    
    /* SECTION CONTAINERS */
    .section {
        background-color: white;
        padding: 1.5rem;
        border-radius: 0.5rem;
        box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.1), 0 2px 4px -1px rgba(0, 0, 0, 0.06);
        margin-bottom: 1.5rem;
        transition: transform 0.2s, box-shadow 0.2s;
    }
    
    .section:hover {
        box-shadow: 0 10px 15px -3px rgba(0, 0, 0, 0.1), 0 4px 6px -2px rgba(0, 0, 0, 0.05);
    }
    
    .parameter-section {
        border-left: 4px solid #3b82f6;
        background: linear-gradient(to right, #f0f7ff, white);
    }
    
    .note-section {
        border-left: 4px solid #10b981;
        background: linear-gradient(to right, #f0fff4, white);
    }
    
    .screenshot-section {
        border-left: 4px solid #f59e0b;
        background: linear-gradient(to right, #fffbeb, white);
    }
    
    /* FORMS AND INPUT STYLING */
    input[type="text"], .stTextInput > div > div > input {
        padding: 0.5rem;
        border-radius: 0.375rem;
        border: 1px solid #e2e8f0;
        margin-bottom: 1rem;
        width: 100%;
        transition: all 0.2s;
        background-color: #f8fafc;
    }
    
    input[type="text"]:focus, .stTextInput > div > div > input:focus {
        border-color: #3b82f6;
        box-shadow: 0 0 0 3px rgba(59, 130, 246, 0.3);
        outline: none;
    }
    
    /* Parameter Group Styling */
    .stMarkdown h4 {
        margin-top: 1.5rem;
        padding-bottom: 0.5rem;
        border-bottom: 1px solid #e2e8f0;
        color: #334155;
        font-weight: 600;
    }
    
    /* STATUS INDICATORS IN TABLE */
    .tested-cell {
        background-color: #d1fae5;
        color: #065f46;
        font-weight: 500;
        text-align: center;
        border-radius: 0.25rem;
    }
    
    .improved-cell {
        background-color: #dbeafe;
        color: #1e40af;
        font-weight: 500;
        text-align: center;
        border-radius: 0.25rem;
    }
    
    .cell-centered {
        text-align: center;
    }
    
    /* TABLE STYLING */
    table {
        border-collapse: separate !important;
        border-spacing: 0 !important;
        border-radius: 0.5rem !important;
        overflow: hidden !important;
        box-shadow: 0 1px 3px rgba(0, 0, 0, 0.12) !important;
    }
    
    th {
        background-color: #f8fafc !important;
        padding: 0.75rem 1rem !important;
        font-weight: 600 !important;
        color: #334155 !important;
        text-transform: uppercase !important;
        font-size: 0.75rem !important;
        letter-spacing: 0.05em !important;
    }
    
    td {
        padding: 0.75rem 1rem !important;
        border-top: 1px solid #e2e8f0 !important;
    }
    
    tr:nth-child(even) {
        background-color: #f8fafc !important;
    }
    
    tr:hover {
        background-color: #f1f5f9 !important;
    }
    
    /* LOGIN CONTAINER */
    .login-container {
        max-width: 500px;
        margin: 2rem auto;
        padding: 2rem;
        background-color: white;
        border-radius: 1rem;
        box-shadow: 0 10px 25px -5px rgba(0, 0, 0, 0.1), 0 10px 10px -5px rgba(0, 0, 0, 0.04);
        border-top: 4px solid #3b82f6;
    }
    
    /* STATS AND DASHBOARD */
    .dashboard-stats {
        display: flex;
        justify-content: space-between;
        flex-wrap: wrap;
        gap: 1rem;
    }
    
    .stat-card {
        background-color: white;
        padding: 1.5rem;
        border-radius: 0.5rem;
        box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.1), 0 2px 4px -1px rgba(0, 0, 0, 0.06);
        flex: 1;
        min-width: 200px;
        text-align: center;
        transition: transform 0.2s;
        border-top: 4px solid #3b82f6;
    }
    
    .stat-card:hover {
        transform: translateY(-5px);
        box-shadow: 0 10px 15px -3px rgba(0, 0, 0, 0.1), 0 4px 6px -2px rgba(0, 0, 0, 0.05);
    }
    
    .stat-value {
        font-size: 2rem;
        font-weight: 700;
        margin: 0.5rem 0;
        color: #1e293b;
    }
    
    .stat-label {
        color: #64748b;
        font-size: 0.875rem;
        text-transform: uppercase;
        letter-spacing: 0.05em;
    }
    
    /* COLOR VARIANTS */
    .green-bg { 
        background-color: #d1fae5; 
        border-color: #10b981 !important;
    }
    
    .blue-bg { 
        background-color: #dbeafe; 
        border-color: #3b82f6 !important;
    }
    
    .yellow-bg { 
        background-color: #fef3c7; 
        border-color: #f59e0b !important;
    }
    
    .purple-bg { 
        background-color: #ede9fe; 
        border-color: #8b5cf6 !important;
    }
    
    /* EXPANDER STYLING */
    div[data-testid="stExpander"] {
        border: 1px solid #e2e8f0;
        border-radius: 0.5rem;
        overflow: hidden;
        margin-bottom: 1rem;
    }
    
    div[data-testid="stExpander"] > div:first-child {
        background-color: #f8fafc;
        padding: 1rem;
        cursor: pointer;
    }
    
    div[data-testid="stExpander"] > div:last-child {
        border-top: 1px solid #e2e8f0;
        padding: 1rem;
    }
    
    /* HORIZONTAL RULE */
    hr {
        border: none;
        height: 1px;
        background-color: #e2e8f0;
        margin: 2rem 0;
    }
    
    /* SCREENSHOT GALLERY */
    .thumbnails {
        display: grid;
        grid-template-columns: repeat(auto-fill, minmax(300px, 1fr));
        gap: 1rem;
        margin-top: 1rem;
    }
    
    .thumbnails img {
        width: 100%;
        border-radius: 0.5rem;
        box-shadow: 0 1px 3px rgba(0, 0, 0, 0.12);
        transition: transform 0.3s, box-shadow 0.3s;
    }
    
    .thumbnails img:hover {
        transform: scale(1.02);
        box-shadow: 0 10px 15px -3px rgba(0, 0, 0, 0.1), 0 4px 6px -2px rgba(0, 0, 0, 0.05);
    }
    
    /* PROFILE CARDS */
    .profile-card {
        background-color: white;
        padding: 1.5rem;
        border-radius: 0.5rem;
        box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.1), 0 2px 4px -1px rgba(0, 0, 0, 0.06);
        margin-bottom: 1rem;
        transition: transform 0.3s, box-shadow 0.3s;
        border-left: 4px solid #3b82f6;
    }
    
    .profile-card:hover {
        transform: translateY(-5px);
        box-shadow: 0 20px 25px -5px rgba(0, 0, 0, 0.1), 0 10px 10px -5px rgba(0, 0, 0, 0.04);
    }
    
    /* MOBILE RESPONSIVE ADJUSTMENTS */
    @media (max-width: 768px) {
        .dashboard-stats {
            flex-direction: column;
        }
        
        .stat-card {
            width: 100%;
        }
        
        .thumbnails {
            grid-template-columns: 1fr;
        }
    }
</style>
"""

# Dark theme CSS with the same structure but different colors
DARK_CSS = """
<style>
    /* CUSTOM FONT IMPORT */
    @import url('https://fonts.googleapis.com/css2?family=Roboto:wght@300;400;500;700&family=Montserrat:wght@500;600;700&display=swap');
    
    /* GLOBAL STYLING */
    html, body, [class*="css"] {
        font-family: 'Roboto', sans-serif;
    }
    
    .main {
        background: linear-gradient(to bottom right, #0f172a, #1e293b);
        padding: 0;
    }
    
    .block-container {
        padding-top: 1rem;
        padding-bottom: 1rem;
    }
    
    .dataframe {
        font-family: 'Roboto', sans-serif;
        font-size: 0.9rem;
    }
    
    /* HEADINGS */
    h1, h2, h3, h4, h5, h6 {
        font-family: 'Montserrat', sans-serif;
        font-weight: 600;
    }
    
    h1 {
        color: #f8fafc;
        font-size: 2.2rem;
        font-weight: 700;
        padding-bottom: 1rem;
        border-bottom: 2px solid #334155;
        margin-bottom: 1.5rem;
    }
    
    h2 {
        color: #e2e8f0;
        font-size: 1.6rem;
        margin-top: 1.5rem;
        margin-bottom: 1rem;
    }
    
    h3 {
        color: #cbd5e1;
        font-size: 1.3rem;
        margin-top: 1rem;
        margin-bottom: 0.5rem;
    }
    
    /* BUTTON STYLING */
    .stButton>button {
        background-color: #2563eb;
        color: white;
        border: none;
        border-radius: 0.375rem;
        padding: 0.5rem 1rem;
        font-weight: 500;
        transition: all 0.2s ease;
        box-shadow: 0 2px 4px rgba(37, 99, 235, 0.3);
    }
    
    .stButton>button:hover {
        background-color: #3b82f6;
        box-shadow: 0 4px 8px rgba(59, 130, 246, 0.4);
        transform: translateY(-1px);
    }
    
    .stButton>button:active {
        transform: translateY(0);
        box-shadow: 0 1px 2px rgba(59, 130, 246, 0.4);
    }
    
    /* Button variants */
    button[data-baseweb="button"][kind="primary"] {
        background-color: #3b82f6 !important;
    }
    
    button[data-baseweb="button"][kind="secondary"] {
        background-color: #475569 !important;
    }
    
    /* SIDEBAR STYLING */
    [data-testid="stSidebar"] {
        background-color: #0f172a;
        padding-top: 2rem;
    }
    
    [data-testid="stSidebar"] h1, 
    [data-testid="stSidebar"] h2, 
    [data-testid="stSidebar"] h3, 
    [data-testid="stSidebar"] h4 {
        color: #f8fafc;
    }
    
    [data-testid="stSidebar"] .stButton>button {
        width: 100%;
        background-color: #1e293b;
        margin-bottom: 0.5rem;
    }
    
    [data-testid="stSidebar"] .stButton>button:hover {
        background-color: #334155;
    }
    
    [data-testid="stSidebar"] hr {
        border-color: #334155;
        margin: 1.5rem 0;
    }
    
    /* PROFILE & ADMIN BADGES */
    .profile-badge {
        background-color: #475569;
        padding: 0.25rem 0.75rem;
        border-radius: 9999px;
        font-weight: 500;
        font-size: 0.875rem;
        margin-left: 0.5rem;
        display: inline-block;
    }
    
    .admin-badge {
        background-color: #ef4444;
        color: white;
        padding: 0.25rem 0.75rem;
        border-radius: 9999px;
        font-weight: 500;
        font-size: 0.875rem;
        margin-left: 0.5rem;
        display: inline-block;
    }
    
    /* SECTION CONTAINERS */
    .section {
        background-color: #1e293b;
        padding: 1.5rem;
        border-radius: 0.5rem;
        box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.3), 0 2px 4px -1px rgba(0, 0, 0, 0.2);
        margin-bottom: 1.5rem;
        transition: transform 0.2s, box-shadow 0.2s;
    }
    
    .section:hover {
        box-shadow: 0 10px 15px -3px rgba(0, 0, 0, 0.4), 0 4px 6px -2px rgba(0, 0, 0, 0.2);
    }
    
    .parameter-section {
        border-left: 4px solid #3b82f6;
    }
    
    .note-section {
        border-left: 4px solid #10b981;
    }
    
    .screenshot-section {
        border-left: 4px solid #f59e0b;
    }
    
    /* STATUS INDICATORS IN TABLE */
    .tested-cell {
        background-color: #064e3b;
        color: #d1fae5;
        font-weight: 500;
        text-align: center;
        border-radius: 0.25rem;
    }
    
    .improved-cell {
        background-color: #1e3a8a;
        color: #dbeafe;
        font-weight: 500;
        text-align: center;
        border-radius: 0.25rem;
    }
    
    .cell-centered {
        text-align: center;
    }
    
    /* TABLE STYLING */
    table {
        border-collapse: separate !important;
        border-spacing: 0 !important;
        border-radius: 0.5rem !important;
        overflow: hidden !important;
        box-shadow: 0 1px 3px rgba(0, 0, 0, 0.3) !important;
    }
    
    th {
        background-color: #0f172a !important;
        padding: 0.75rem 1rem !important;
        font-weight: 600 !important;
        color: #e2e8f0 !important;
        text-transform: uppercase !important;
        font-size: 0.75rem !important;
        letter-spacing: 0.05em !important;
    }
    
    td {
        padding: 0.75rem 1rem !important;
        border-top: 1px solid #334155 !important;
    }
    
    tr:nth-child(even) {
        background-color: #1e293b !important;
    }
    
    tr:hover {
        background-color: #334155 !important;
    }
    
    /* LOGIN CONTAINER */
    .login-container {
        max-width: 500px;
        margin: 2rem auto;
        padding: 2rem;
        background-color: #1e293b;
        border-radius: 1rem;
        box-shadow: 0 10px 25px -5px rgba(0, 0, 0, 0.3), 0 10px 10px -5px rgba(0, 0, 0, 0.2);
        border-top: 4px solid #3b82f6;
    }
    
    /* STATS AND DASHBOARD */
    .dashboard-stats {
        display: flex;
        justify-content: space-between;
        flex-wrap: wrap;
        gap: 1rem;
    }
    
    .stat-card {
        background-color: #1e293b;
        padding: 1.5rem;
        border-radius: 0.5rem;
        box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.3), 0 2px 4px -1px rgba(0, 0, 0, 0.2);
        flex: 1;
        min-width: 200px;
        text-align: center;
        transition: transform 0.2s;
        border-top: 4px solid #3b82f6;
    }
    
    .stat-card:hover {
        transform: translateY(-5px);
        box-shadow: 0 10px 15px -3px rgba(0, 0, 0, 0.4), 0 4px 6px -2px rgba(0, 0, 0, 0.2);
    }
    
    .stat-value {
        font-size: 2rem;
        font-weight: 700;
        margin: 0.5rem 0;
        color: #f8fafc;
    }
    
    .stat-label {
        color: #cbd5e1;
        font-size: 0.875rem;
        text-transform: uppercase;
        letter-spacing: 0.05em;
    }
    
    /* COLOR VARIANTS */
    .green-bg { 
        background-color: #064e3b; 
        border-color: #10b981 !important;
    }
    
    .blue-bg { 
        background-color: #1e3a8a; 
        border-color: #3b82f6 !important;
    }
    
    .yellow-bg { 
        background-color: #78350f; 
        border-color: #f59e0b !important;
    }
    
    .purple-bg { 
        background-color: #5b21b6; 
        border-color: #8b5cf6 !important;
    }
    
    /* EXPANDER STYLING */
    div[data-testid="stExpander"] {
        border: 1px solid #334155;
        border-radius: 0.5rem;
        overflow: hidden;
        margin-bottom: 1rem;
    }
    
    div[data-testid="stExpander"] > div:first-child {
        background-color: #0f172a;
        padding: 1rem;
        cursor: pointer;
    }
    
    div[data-testid="stExpander"] > div:last-child {
        border-top: 1px solid #334155;
        padding: 1rem;
    }
    
    /* HORIZONTAL RULE */
    hr {
        border: none;
        height: 1px;
        background-color: #334155;
        margin: 2rem 0;
    }
    
    /* SCREENSHOT GALLERY */
    .thumbnails {
        display: grid;
        grid-template-columns: repeat(auto-fill, minmax(300px, 1fr));
        gap: 1rem;
        margin-top: 1rem;
    }
    
    .thumbnails img {
        width: 100%;
        border-radius: 0.5rem;
        box-shadow: 0 1px 3px rgba(0, 0, 0, 0.3);
        transition: transform 0.3s, box-shadow 0.3s;
    }
    
    .thumbnails img:hover {
        transform: scale(1.02);
        box-shadow: 0 10px 15px -3px rgba(0, 0, 0, 0.4), 0 4px 6px -2px rgba(0, 0, 0, 0.2);
    }
    
    /* PROFILE CARDS */
    .profile-card {
        background-color: #1e293b;
        padding: 1.5rem;
        border-radius: 0.5rem;
        box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.3), 0 2px 4px -1px rgba(0, 0, 0, 0.2);
        margin-bottom: 1rem;
        transition: transform 0.3s, box-shadow 0.3s;
        border-left: 4px solid #3b82f6;
    }
    
    .profile-card:hover {
        transform: translateY(-5px);
        box-shadow: 0 20px 25px -5px rgba(0, 0, 0, 0.4), 0 10px 10px -5px rgba(0, 0, 0, 0.2);
    }
    
    /* MOBILE RESPONSIVE ADJUSTMENTS */
    @media (max-width: 768px) {
        .dashboard-stats {
            flex-direction: column;
        }
        
        .stat-card {
            width: 100%;
        }
        
        .thumbnails {
            grid-template-columns: 1fr;
        }
    }
</style>
"""

# Function to get CSS based on theme preference
def get_theme_css(is_dark_theme=False):
    """
    Get the appropriate CSS based on the theme preference
    
    Args:
        is_dark_theme (bool): Whether to use dark theme
        
    Returns:
        str: CSS code
    """
    return DARK_CSS if is_dark_theme else MAIN_CSS
