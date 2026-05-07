"""
Servicios de lógica de negocio.
"""

from .estadisticas_service import calcular_estadisticas, calcular_media_nacional
from .outlier_service import es_outlier, get_outliers_por_año
from .correlacion_service import calcular_correlacion_migracion, get_datos_frontera

__all__ = [
    'calcular_estadisticas',
    'calcular_media_nacional',
    'es_outlier',
    'get_outliers_por_año',
    'calcular_correlacion_migracion',
    'get_datos_frontera',
]
