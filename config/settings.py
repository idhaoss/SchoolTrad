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
    },
    "profiles": [],
    "super_admin_hash": ""
}

# Catégories d'actifs disponibles
ASSET_CATEGORIES = {
    "crypto": {
        "name": "Crypto-monnaies",
        "assets": [
            # Top 40 cryptomonnaies
            "BTC/USD", "ETH/USD", "BNB/USD", "XRP/USD", "ADA/USD",
            "SOL/USD", "DOT/USD", "DOGE/USD", "AVAX/USD", "LINK/USD",
            "MATIC/USD", "ATOM/USD", "LTC/USD", "UNI/USD", "ALGO/USD",
            "SHIB/USD", "XLM/USD", "NEAR/USD", "FTM/USD", "VET/USD",
            "HBAR/USD", "SAND/USD", "MANA/USD", "EGLD/USD", "XTZ/USD",
            "THETA/USD", "EOS/USD", "AAVE/USD", "AXS/USD", "ENJ/USD",
            "FIL/USD", "FLOW/USD", "NEO/USD", "CAKE/USD", "CHZ/USD",
            "BAT/USD", "ONE/USD", "IOTA/USD", "GALA/USD", "GRT/USD"
        ]
    },
    "forex": {
        "name": "Forex",
        "assets": [
            # Paires majeures
            "EUR/USD", "GBP/USD", "USD/JPY", "USD/CHF", "USD/CAD",
            "AUD/USD", "NZD/USD", 
            # Paires croisées populaires
            "EUR/GBP", "EUR/JPY", "GBP/JPY", "EUR/AUD", "GBP/CHF",
            "EUR/CHF", "AUD/JPY", "AUD/CAD", "AUD/NZD", "CAD/JPY",
            "EUR/CAD", "EUR/NZD", "GBP/AUD", "GBP/CAD", "GBP/NZD"
        ]
    },
    "indices": {
        "name": "Indices",
        "assets": [
            # Indices américains
            "US500", "NASDAQ", "DJ30", "Russell2000",
            # Indices européens
            "GER40", "UK100", "FRA40", "ESP35", "ITA40", "EUSTX50",
            # Indices asiatiques
            "AUS200", "JP225", "HK50", "CHINA50", "INDIA50", "NIKKEI",
            # Autres indices mondiaux
            "BRAZIL60", "MSCI_EM", "VIX", "FTSE_MIB"
        ]
    },
    "commodities": {
        "name": "Matières premières",
        "assets": [
            # Énergies
            "CRUDE_OIL", "BRENT_OIL", "NATURAL_GAS", "GASOLINE",
            # Métaux
            "GOLD", "SILVER", "PLATINUM", "PALLADIUM", "COPPER",
            # Agricoles
            "CORN", "WHEAT", "SOYBEANS", "COFFEE", "SUGAR", "COTTON"
        ]
    },
    "stocks": {
        "name": "Actions",
        "assets": [
            # Tech
            "AAPL", "MSFT", "GOOGL", "AMZN", "META", "TSLA", "NVDA", "NFLX",
            # Finance
            "JPM", "BAC", "GS", "MS", "V", "MA",
            # Pharma/Santé
            "JNJ", "PFE", "MRNA", "ABBV",
            # Retail
            "WMT", "TGT", "COST", "HD",
            # Autres secteurs
            "DIS", "SBUX", "MCD", "KO", "PEP", "NKE"
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

# Paramètres par défaut pour les configurations
DEFAULT_PARAMS = {
    "Price Change Threshold (%)": "0.5",
    "Kernel Timeframe": "30",
    "ADX Length": "14",
    "ADX Level": "25",
    "Start Regression at Bar": "10",
    "Lookback Window": "50",
    "Relative Weighting": "0.8",
    "Start Regression at Bar (2)": "5",
    "Lookback Window (2)": "20",
    "Relative Weighting (2)": "0.6",
    "Smooth Colors": "3",
    "Bullish Color": "#00FF00",
    "Bearish Color": "#FF0000",
    "Inputs in status line": "Yes"
}

# Nombre maximum de captures d'écran par configuration
MAX_SCREENSHOTS = 2
