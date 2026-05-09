"""
Servicio para detección de outliers estadísticos.
Determina si una ciudad está fuera del rango normal nacional.
"""

import numpy as np
from typing import List

from data import CIUDADES, EMPLEO_BASE
from core.constants import AÑOS
from .estadisticas_service import calcular_media_nacional


def es_outlier(ciudad: str, año: int, n_sigma: float = 2.0) -> bool:
    """
    Determina si la tasa de empleo de una ciudad es un outlier.
    
    Un outlier se define como un valor que está a más de n_sigma desviaciones
    estándar de la media nacional.
    
    Args:
        ciudad: Nombre de la ciudad.
        año: Año a analizar.
        n_sigma: Número de desviaciones estándar para el límite (default 2.0).
        
    Returns:
        True si es outlier, False en caso contrario.
    """
    idx = AÑOS.index(año)
    mu_nac, _ = calcular_media_nacional(año)
    vals = [EMPLEO_BASE[c][idx] for c in CIUDADES if EMPLEO_BASE[c][idx] is not None]
    if not vals:
        return False
    sigma_nac = np.std(vals)
    val = EMPLEO_BASE[ciudad][idx]
    if val is None:
        return False
    return bool(abs(val - mu_nac) > n_sigma * sigma_nac)


def get_outliers_por_año(año: int, n_sigma: float = 2.0) -> List[str]:
    """
    Retorna la lista de ciudades outliers para un año específico.
    
    Args:
        año: Año a analizar.
        n_sigma: Número de desviaciones estándar para el límite.
        
    Returns:
        Lista de nombres de ciudades que son outliers.
    """
    return [c for c in CIUDADES if es_outlier(c, año, n_sigma)]
