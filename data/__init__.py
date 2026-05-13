from data.data_manager import (
    get_empleo_data,
    get_sigma_data,
    get_ciudades,
    is_using_real_data,
    get_available_years,
    get_data_source,
)

from data.ciudades import CIUDADES
from data.sectores import SECTOR_DOMINANTE
from data.migracion import MIGRACION_FRONTERIZA, FRONTERIZAS

EMPLEO_BASE = get_empleo_data()
SIGMA_BASE = get_sigma_data()

__all__ = [
    'CIUDADES',
    'EMPLEO_BASE',
    'SIGMA_BASE',
    'SECTOR_DOMINANTE',
    'MIGRACION_FRONTERIZA',
    'FRONTERIZAS',
    'get_ciudades',
    'is_using_real_data',
    'get_available_years',
    'get_data_source',
]