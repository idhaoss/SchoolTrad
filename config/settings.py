"""
Configuration settings for the Trading Dashboard Pro application.
Contains constants, default values, and configuration parameters.
"""
import os

# Determine the app's base directory (independent of current working directory)
APP_BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Paths (absolute paths based on the app's location)
CONFIG_FILE = os.path.join(APP_BASE_DIR, "app_config.json")
PROFILES_DIR = os.path.join(APP_BASE_DIR, "profiles")
DEFAULT_PROFILE = "default"

# Ensure directories exist
if not os.path.exists(PROFILES_DIR):
    os.makedirs(PROFILES_DIR)
    print(f"Created profiles directory at: {PROFILES_DIR}")

print(f"Using config file: {CONFIG_FILE}")
print(f"Using profiles directory: {PROFILES_DIR}")

# Create a .gitignore to protect sensitive data
GITIGNORE_CONTENT = f"""
{PROFILES_DIR}/
{CONFIG_FILE}
*.json
__pycache__/
.streamlit/
"""

if not os.path.exists(".gitignore"):
    try:
        with open(".gitignore", "a") as f:
            f.write(GITIGNORE_CONTENT)
    except:
        pass  # Silently fail if unable to create .gitignore

# Trading assets
TIMEFRAMES = ["1m", "5m", "15m", "30m", "1h", "4h", "1d", "1w", "1M"]

# Crypto assets
CRYPTOS = [
    "Bitcoin (BTC)", 
    "Ethereum (ETH)", 
    "Binance Coin (BNB)", 
    "Solana (SOL)", 
    "XRP (XRP)", 
    "Cardano (ADA)", 
    "Avalanche (AVAX)", 
    "Polkadot (DOT)",
    "Dogecoin (DOGE)",
    "Shiba Inu (SHIB)",
    "Chainlink (LINK)",
    "Polygon (MATIC)",
    "Litecoin (LTC)",
    "Uniswap (UNI)",
    "Bitcoin Cash (BCH)",
    "Stellar (XLM)",
    "Cosmos (ATOM)",
    "Algorand (ALGO)",
    "VeChain (VET)",
    "Tezos (XTZ)"
]

# Financial assets
FINANCIAL_ASSETS = {
    "Métaux précieux": [
        "Or (GOLD)", 
        "Argent (SILVER)",
        "Platine (PLATINUM)",
        "Palladium (PALLADIUM)",
        "Cuivre (COPPER)"
    ],
    "Indices boursiers": [
        "S&P 500 (SPX)",
        "Nasdaq 100 (NDX)",
        "Dow Jones (DJI)",
        "CAC 40 (CAC)",
        "DAX (DAX)",
        "FTSE 100 (FTSE)",
        "Nikkei 225 (NI225)",
        "Hang Seng (HSI)"
    ],
    "Forex": [
        "EUR/USD",
        "GBP/USD",
        "USD/JPY",
        "USD/CHF",
        "AUD/USD",
        "USD/CAD",
        "EUR/GBP",
        "EUR/JPY"
    ],
    "Matières premières": [
        "Pétrole Brent (BRENT)",
        "Pétrole WTI (WTI)",
        "Gaz naturel (NATGAS)",
        "Blé (WHEAT)",
        "Maïs (CORN)",
        "Soja (SOYBEAN)",
        "Café (COFFEE)",
        "Coton (COTTON)"
    ]
}

# Default strategy parameters
DEFAULT_PARAMS = {
    "Price Change Threshold (%)": "0.11",
    "Kernel Timeframe": "700",
    "ADX Length": "1",
    "ADX Level": "20",
    "Start Regression at Bar": "70",
    "Lookback Window": "5",
    "Relative Weighting": "25",
    "Start Regression at Bar (2)": "0",
    "Lookback Window (2)": "16",
    "Relative Weighting (2)": "1",
    "Smooth Colors": "2",
    "Bullish Color": "#4bd050",
    "Bearish Color": "#ff5252",
    "Inputs in status line": "Yes"
}

# Application configuration default
DEFAULT_APP_CONFIG = {
    "super_admin_hash": "",
    "super_admin_salt": "",
    "profiles": [DEFAULT_PROFILE],
    "current_profile": DEFAULT_PROFILE
}

# Max number of screenshots per configuration
MAX_SCREENSHOTS = 2
