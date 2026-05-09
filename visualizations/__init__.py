"""
Visualizaciones Plotly reutilizables.
"""

from .mapa import figura_mapa
from .gauss import figura_gauss
from .tendencias import figura_tendencia
from .ranking import figura_ranking
from .correlacion import figura_correlacion_frontera

__all__ = [
    'figura_mapa',
    'figura_gauss',
    'figura_tendencia',
    'figura_ranking',
    'figura_correlacion_frontera',
]
