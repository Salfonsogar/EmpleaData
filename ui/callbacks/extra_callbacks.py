"""
Callbacks adicionales (correlación fronteriza y otros análisis extras).
"""

from dash import Input, Output
from visualizations.correlacion import figura_correlacion_frontera


def register_extra_callbacks(app):
    """
    Registra callbacks para análisis adicionales.
    
    Args:
        app: Instancia de la aplicación Dash.
    """
    @app.callback(
        Output("grafica-correlacion", "figure"),
        Input("slider-año", "value")  # Trigger dummy para cargar al inicio
    )
    def actualizar_correlacion(año):
        """Actualiza la gráfica de correlación fronteriza."""
        return figura_correlacion_frontera()
