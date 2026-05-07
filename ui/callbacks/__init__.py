"""
Callbacks de la aplicación Dash.
Orquestador que registra todos los callbacks en la app.
"""

from .map_callbacks import register_map_callbacks
from .stats_callbacks import register_stats_callbacks
from .extra_callbacks import register_extra_callbacks


def register_all_callbacks(app):
    """
    Registra todos los callbacks de la aplicación.
    
    Args:
        app: Instancia de la aplicación Dash.
    """
    register_map_callbacks(app)
    register_stats_callbacks(app)
    register_extra_callbacks(app)
