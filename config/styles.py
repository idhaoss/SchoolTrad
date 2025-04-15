"""
CSS styles for the Trading Dashboard Pro application.
These styles customize the Streamlit interface for a better user experience.
"""

# Main CSS styles for the application
MAIN_CSS = """
<style>
    /* General styling */
    .main { 
        background-color: #f8f9fa;
    }
    .dataframe { 
        font-family: Arial, sans-serif;
    }
    
    /* Button styling */
    .stButton>button {
        background-color: #4e8df2;
        color: white;
        border: none;
        border-radius: 4px;
        padding: 8px 16px;
        transition: all 0.3s ease;
    }
    .stButton>button:hover {
        background-color: #3a7ad5;
        box-shadow: 0 4px 8px rgba(0,0,0,0.1);
    }
    
    /* Profile & Admin badges */
    .profile-badge {
        background-color: #e9ecef;
        padding: 5px 10px;
        border-radius: 10px;
        font-weight: bold;
        margin-left: 10px;
    }
    .admin-badge {
        background-color: #dc3545;
        color: white;
        padding: 5px 10px;
        border-radius: 10px;
        font-weight: bold;
        margin-left: 10px;
    }
    
    /* Section containers */
    .section {
        background-color: white;
        padding: 15px;
        border-radius: 4px;
        box-shadow: 0 1px 3px rgba(0,0,0,0.12);
        margin-bottom: 10px;
    }
    .parameter-section { 
        border-left: 4px solid #4e8df2;
    }
    .note-section { 
        border-left: 4px solid #28a745;
    }
    .screenshot-section { 
        border-left: 4px solid #ffc107;
    }
    
    /* Status indicators in table */
    .tested-cell {
        background-color: #d4edda;
        color: #155724;
        font-weight: bold;
        text-align: center;
    }
    .improved-cell {
        background-color: #cce5ff;
        color: #004085;
        font-weight: bold;
        text-align: center;
    }
    .cell-centered {
        text-align: center;
    }
    
    /* Login container */
    .login-container {
        max-width: 500px;
        margin: 0 auto;
        padding: 20px;
        background-color: white;
        border-radius: 5px;
        box-shadow: 0 2px 10px rgba(0,0,0,0.1);
    }
    
    /* Stats and dashboard */
    .dashboard-stats {
        display: flex;
        justify-content: space-between;
        flex-wrap: wrap;
    }
    .stat-card {
        background-color: white;
        padding: 20px;
        border-radius: 5px;
        box-shadow: 0 1px 3px rgba(0,0,0,0.12);
        flex: 1;
        margin: 5px;
        text-align: center;
    }
    .stat-value {
        font-size: 24px;
        font-weight: bold;
        margin: 10px 0;
    }
    .stat-label {
        color: #6c757d;
        font-size: 14px;
    }
    
    /* Color variants */
    .green-bg { background-color: #d4edda; }
    .blue-bg { background-color: #cce5ff; }
    .yellow-bg { background-color: #fff3cd; }
    .purple-bg { background-color: #e2d9f3; }
    
    /* Other UI elements */
    div[data-testid="stExpander"] {
        border: 1px solid #e9ecef;
        border-radius: 4px;
    }
    h1, h2, h3 {
        color: #2c3e50;
    }
    hr {
        margin-top: 30px;
        margin-bottom: 30px;
    }
    
    /* Screenshot gallery */
    .thumbnails img {
        border: 1px solid #ddd;
        border-radius: 4px;
        padding: 5px;
        transition: 0.3s;
    }
    .thumbnails img:hover {
        box-shadow: 0 0 10px #ddd;
    }
    
    /* Profile cards */
    .profile-card {
        background-color: white;
        padding: 15px;
        border-radius: 5px;
        box-shadow: 0 1px 3px rgba(0,0,0,0.12);
        margin-bottom: 15px;
        transition: all 0.3s ease;
    }
    .profile-card:hover {
        box-shadow: 0 5px 15px rgba(0,0,0,0.1);
        transform: translateY(-2px);
    }
</style>
"""
