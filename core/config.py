"""
Configuration centralizada para la aplicación Dash.
Contiene settings de ejecución y configuraciones globales.
"""

import warnings

# Configuración de la aplicación Dash
APP_HOST = "0.0.0.0"
APP_PORT = 8050
APP_DEBUG = False
APP_TITLE = "Analizador Empleabilidad Nacional"

# Suprimir warnings de numpy/scipy
warnings.filterwarnings("ignore")
