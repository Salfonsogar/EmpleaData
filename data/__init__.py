"""
Facade para el módulo de datos.
Re-exporta todas las constantes para facilitar imports centralizados.
"""

from .ciudades import CIUDADES
from .empleo_base import EMPLEO_BASE, SIGMA_BASE
from .sectores import SECTOR_DOMINANTE
from .migracion import MIGRACION_FRONTERIZA, FRONTERIZAS

__all__ = [
    'CIUDADES',
    'EMPLEO_BASE',
    'SIGMA_BASE',
    'SECTOR_DOMINANTE',
    'MIGRACION_FRONTERIZA',
    'FRONTERIZAS',
]
