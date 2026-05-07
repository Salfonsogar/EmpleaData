"""
Servicio para análisis de correlación.
Especializado en correlaciones fronterizas y migración.
"""

from typing import Tuple
from scipy import stats

from data import MIGRACION_FRONTERIZA, FRONTERIZAS, SIGMA_BASE


def calcular_correlacion_migracion(año_idx: int = -1) -> Tuple[float, float]:
    """
    Calcula la correlación Pearson entre migración y volatilidad (sigma) 
    para ciudades fronterizas.
    
    Args:
        año_idx: Índice del año a analizar (-1 = último año, 2026).
        
    Returns:
        Tupla (coeficiente_r, p_value).
    """
    sigmas_f = [SIGMA_BASE[c] for c in FRONTERIZAS]
    migr = [MIGRACION_FRONTERIZA[c][año_idx] for c in FRONTERIZAS]
    
    return stats.pearsonr(migr, sigmas_f)


def get_datos_frontera(año_idx: int = -1) -> list[dict]:
    """
    Retorna datos combinados de ciudades fronterizas para un año.
    
    Args:
        año_idx: Índice del año a analizar.
        
    Returns:
        Lista de dicts con keys: ciudad, migracion, sigma.
    """
    return [
        {
            "ciudad": c,
            "migracion": MIGRACION_FRONTERIZA[c][año_idx],
            "sigma": SIGMA_BASE[c],
        }
        for c in FRONTERIZAS
    ]
