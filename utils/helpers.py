"""
Utilidades varias y funciones helper puras.
"""

from typing import Optional
from data import CIUDADES
from core.constants import COLORES_REGION


def get_region_color(ciudad: str) -> Optional[str]:
    """
    Obtiene el color de una región para una ciudad dada.
    
    Args:
        ciudad: Nombre de la ciudad.
        
    Returns:
        Color hex de la región o None si no existe.
    """
    if ciudad in CIUDADES:
        region = CIUDADES[ciudad]["region"]
        return COLORES_REGION.get(region)
    return None


def get_cities_by_region(region: str) -> list[str]:
    """
    Retorna lista de ciudades filtradas por región.
    
    Args:
        region: Nombre de la región.
        
    Returns:
        Lista de nombres de ciudades en esa región.
    """
    if region == "Todas":
        return list(CIUDADES.keys())
    return [c for c, info in CIUDADES.items() if info["region"] == region]
