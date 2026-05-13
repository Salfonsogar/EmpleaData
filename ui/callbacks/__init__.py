"""
Callbacks de la aplicación Dash.
Orquestador que registra todos los callbacks en la app.
"""

from dash import Input, Output
from .map_callbacks import register_map_callbacks
from .stats_callbacks import register_stats_callbacks
from .extra_callbacks import register_extra_callbacks


def register_all_callbacks(app):
    register_map_callbacks(app)
    register_extra_callbacks(app)
    register_stats_callbacks(app)
    
    @app.callback(
        [Output("tab-overview", "style"),
         Output("tab-regional", "style"),
         Output("tab-nacional", "style")],
        Input("main-tabs", "value")
    )
    def switch_tabs(tab):
        if tab == "overview":
            return {"display": "block"}, {"display": "none"}, {"display": "none"}
        elif tab == "regional":
            return {"display": "none"}, {"display": "block"}, {"display": "none"}
        else:
            return {"display": "none"}, {"display": "none"}, {"display": "block"}