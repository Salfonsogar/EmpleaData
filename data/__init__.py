from .ciudades import CIUDADES
from .sectores import SECTOR_DOMINANTE
from .migracion import MIGRACION_FRONTERIZA, FRONTERIZAS

from .loader import get_empleo_base, get_sigma_base, is_using_real_data, get_validation_issues

EMPLEO_BASE = get_empleo_base()
SIGMA_BASE = get_sigma_base()

__all__ = [
    'CIUDADES',
    'EMPLEO_BASE',
    'SIGMA_BASE',
    'SECTOR_DOMINANTE',
    'MIGRACION_FRONTERIZA',
    'FRONTERIZAS',
    'is_using_real_data',
    'get_validation_issues',
]
