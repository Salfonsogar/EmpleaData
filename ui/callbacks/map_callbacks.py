"""
Callbacks relacionados con el mapa y visualizaciones geográficas.
"""

from dash import Input, Output
from visualizations.mapa import figura_mapa


def register_map_callbacks(app):
    """
    Registra callbacks relacionados con el mapa.
    
    Args:
        app: Instancia de la aplicación Dash.
    """
    @app.callback(
        Output("mapa-colombia", "figure"),
        [Input("slider-año", "value"),
         Input("dropdown-ciudad", "value"),
         Input("dropdown-region", "value")]
    )
    def actualizar_mapa(año, ciudad, region):
        """Actualiza el mapa según año, ciudad y región seleccionada."""
        return figura_mapa(año, ciudad, region).to_dict()
