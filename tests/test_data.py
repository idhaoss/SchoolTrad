"""
Tests unitaires pour le module de données de Trading Dashboard Pro.
"""
import unittest
import json
import os
import tempfile
import shutil
from unittest.mock import patch

# Importation du module à tester
from trading_dashboard_pro.models.data import (
    get_config_id, is_tested, is_improved, has_note, has_screenshots,
    toggle_tested, toggle_improved, get_params, save_params
)

class TestDataFunctions(unittest.TestCase):
    """Tests unitaires pour les fonctions du module data.py"""
    
    def setUp(self):
        """Préparation avant chaque test"""
        # Créer des données de test
        self.test_data = {
            "BTC_1h": {
                "tested": True,
                "improved": False,
                "note": "Test note",
                "params": {
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
                    "Bullish Color": "#00FF00",
                    "Bearish Color": "#FF0000",
                    "Inputs in status line": "Yes"
                },
                "screenshots": [
                    {
                        "date": "2025-04-15 12:00:00",
                        "description": "Test screenshot",
                        "image_data": "base64_string"
                    }
                ]
            },
            "ETH_4h": {
                "tested": False,
                "improved": True,
                "note": "",
                "params": {
                    "Price Change Threshold (%)": "0.15",
                    "Kernel Timeframe": "500",
                    "ADX Length": "2",
                    "ADX Level": "25",
                    "Start Regression at Bar": "60",
                    "Lookback Window": "4",
                    "Relative Weighting": "20",
                    "Start Regression at Bar (2)": "5",
                    "Lookback Window (2)": "10",
                    "Relative Weighting (2)": "2",
                    "Smooth Colors": "3",
                    "Bullish Color": "#00AA00",
                    "Bearish Color": "#AA0000",
                    "Inputs in status line": "No"
                },
                "screenshots": []
            }
        }
    
    def test_get_config_id(self):
        """Test de la fonction get_config_id"""
        self.assertEqual(get_config_id("BTC", "1h"), "BTC_1h")
        self.assertEqual(get_config_id("ETH", "4h"), "ETH_4h")
    
    def test_is_tested(self):
        """Test de la fonction is_tested"""
        self.assertTrue(is_tested("BTC", "1h", self.test_data))
        self.assertFalse(is_tested("ETH", "4h", self.test_data))
        self.assertFalse(is_tested("XRP", "1d", self.test_data))  # Actif non existant
    
    def test_is_improved(self):
        """Test de la fonction is_improved"""
        self.assertFalse(is_improved("BTC", "1h", self.test_data))
        self.assertTrue(is_improved("ETH", "4h", self.test_data))
        self.assertFalse(is_improved("XRP", "1d", self.test_data))  # Actif non existant
    
    def test_has_note(self):
        """Test de la fonction has_note"""
        self.assertTrue(has_note("BTC", "1h", self.test_data))
        self.assertFalse(has_note("ETH", "4h", self.test_data))
        self.assertFalse(has_note("XRP", "1d", self.test_data))  # Actif non existant
    
    def test_has_screenshots(self):
        """Test de la fonction has_screenshots"""
        self.assertTrue(has_screenshots("BTC", "1h", self.test_data))
        self.assertFalse(has_screenshots("ETH", "4h", self.test_data))
        self.assertFalse(has_screenshots("XRP", "1d", self.test_data))  # Actif non existant
    
    def test_toggle_tested(self):
        """Test de la fonction toggle_tested"""
        # Test toggle de False à True
        updated_data, new_status = toggle_tested("ETH", "4h", self.test_data.copy())
        self.assertTrue(new_status)
        self.assertTrue(updated_data["ETH_4h"]["tested"])
        
        # Test toggle de True à False
        updated_data, new_status = toggle_tested("BTC", "1h", self.test_data.copy())
        self.assertFalse(new_status)
        self.assertFalse(updated_data["BTC_1h"]["tested"])
        
        # Test avec un nouvel actif
        updated_data, new_status = toggle_tested("XRP", "1d", self.test_data.copy())
        self.assertTrue(new_status)
        self.assertTrue(updated_data["XRP_1d"]["tested"])
    
    def test_toggle_improved(self):
        """Test de la fonction toggle_improved"""
        # Test toggle de False à True
        updated_data, new_status = toggle_improved("BTC", "1h", self.test_data.copy())
        self.assertTrue(new_status)
        self.assertTrue(updated_data["BTC_1h"]["improved"])
        
        # Test toggle de True à False
        updated_data, new_status = toggle_improved("ETH", "4h", self.test_data.copy())
        self.assertFalse(new_status)
        self.assertFalse(updated_data["ETH_4h"]["improved"])
        
        # Test avec un nouvel actif
        updated_data, new_status = toggle_improved("XRP", "1d", self.test_data.copy())
        self.assertTrue(new_status)
        self.assertTrue(updated_data["XRP_1d"]["improved"])
    
    def test_get_params(self):
        """Test de la fonction get_params"""
        # Test récupération de paramètres existants
        params = get_params("BTC", "1h", self.test_data)
        self.assertEqual(params["Price Change Threshold (%)"], "0.11")
        self.assertEqual(params["Kernel Timeframe"], "700")
        
        # Test récupération de paramètres par défaut
        from trading_dashboard_pro.config.settings import DEFAULT_PARAMS
        params = get_params("XRP", "1d", self.test_data)
        self.assertEqual(params, DEFAULT_PARAMS)
    
    def test_save_params(self):
        """Test de la fonction save_params"""
        new_params = {
            "Price Change Threshold (%)": "0.20",
            "Kernel Timeframe": "800",
            "ADX Length": "3",
            "ADX Level": "30",
            "Start Regression at Bar": "65",
            "Lookback Window": "6",
            "Relative Weighting": "22",
            "Start Regression at Bar (2)": "2",
            "Lookback Window (2)": "12",
            "Relative Weighting (2)": "3",
            "Smooth Colors": "4",
            "Bullish Color": "#00BB00",
            "Bearish Color": "#BB0000",
            "Inputs in status line": "Yes"
        }
        
        # Test mise à jour de paramètres existants
        updated_data = save_params("BTC", "1h", new_params, self.test_data.copy())
        self.assertEqual(updated_data["BTC_1h"]["params"], new_params)
        
        # Test création de nouveaux paramètres
        updated_data = save_params("XRP", "1d", new_params, self.test_data.copy())
        self.assertEqual(updated_data["XRP_1d"]["params"], new_params)

if __name__ == '__main__':
    unittest.main()
