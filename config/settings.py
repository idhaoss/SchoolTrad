"""
Configuration globale de l'application.
"""
import os

# Obtenir le chemin du dossier de l'application
APP_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Chemins des dossiers et fichiers
CONFIG_FILE = os.path.join(APP_DIR, "config", "app_config.json")
PROFILES_DIR = os.path.join(APP_DIR, "profiles")

# Configuration par défaut
DEFAULT_PROFILE = "admin"
DEFAULT_APP_CONFIG = {
    "theme": {
        "primaryColor": "#007bff",
        "backgroundColor": "#ffffff",
        "secondaryBackgroundColor": "#f8f9fa",
        "textColor": "#212529",
        "font": "sans serif"
    },
    "layout": {
        "showSidebar": True,
        "sidebarWidth": 300,
        "contentWidth": "wide"
    },
    "features": {
        "enableDarkMode": True,
        "enableNotifications": True,
        "enableAutoSave": True
    }
}

# Catégories d'actifs disponibles
ASSET_CATEGORIES = {
    "crypto": {
        "name": "Crypto-monnaies",
        "assets": [
            "BTC/USD", "ETH/USD", "BNB/USD", "XRP/USD", "ADA/USD",
            "SOL/USD", "DOT/USD", "DOGE/USD", "AVAX/USD", "LINK/USD"
        ]
    },
    "forex": {
        "name": "Forex",
        "assets": [
            "EUR/USD", "GBP/USD", "USD/JPY", "USD/CHF", "USD/CAD",
            "AUD/USD", "NZD/USD", "EUR/GBP", "EUR/JPY", "GBP/JPY"
        ]
    },
    "indices": {
        "name": "Indices",
        "assets": [
            "US500", "NASDAQ", "DJ30", "GER40", "UK100",
            "FRA40", "AUS200", "JP225", "HK50", "CHINA50"
        ]
    }
}

# Timeframes disponibles
TIMEFRAMES = ["1m", "5m", "15m", "30m", "1h", "4h", "1d", "1w", "1M"]

# Configuration des graphiques
CHART_CONFIG = {
    "height": 600,
    "width": "100%",
    "theme": {
        "background": "#ffffff",
        "gridColor": "#f0f0f0",
        "textColor": "#333333"
    }
}
