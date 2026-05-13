"""
================================================================================
ANALIZADOR DINÁMICO DE EMPLEABILIDAD NACIONAL (2021-2026)
Modelado y Simulación - Ingeniería de Sistemas
Docente: Andrés Perpiñán Reyes
================================================================================

Arquitectura modular refactorizada siguiendo buenas prácticas de software.
"""

# Importar pandas primero para evitar problemas de importación circular con plotly
import pandas

from dash import Dash
from core.config import APP_HOST, APP_PORT, APP_DEBUG, APP_TITLE
from ui.layout import create_layout
from ui.callbacks import register_all_callbacks


# ─────────────────────────────────────────────────────────────────────────────
# INICIALIZACIÓN DE LA APLICACIÓN
# ─────────────────────────────────────────────────────────────────────────────

app = Dash(
    __name__,
    title=APP_TITLE,
    suppress_callback_exceptions=True,
)

# Configurar layout
app.layout = create_layout()

# Registrar todos los callbacks
register_all_callbacks(app)


# ─────────────────────────────────────────────────────────────────────────────
# MAIN
# ─────────────────────────────────────────────────────────────────────────────

if __name__ == "__main__":
    print("\n" + "="*60)
    print("  ANALIZADOR DE EMPLEABILIDAD NACIONAL 2021-2026")
    print("  Modelado y Simulación · UniCésar")
    print("="*60)
    print("  ▶  Abre tu navegador en: http://127.0.0.1:8050")
    print("="*60 + "\n")
    
    app.run(debug=APP_DEBUG, host=APP_HOST, port=APP_PORT)
