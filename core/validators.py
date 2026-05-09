"""
Validadores de entrada para ciudades y años.
Movido desde utils/ para evitar dependencias circulares.
"""

from typing import Optional
from data import CIUDADES
from core.constants import AÑOS

def validate_ciudad(ciudad: str) -> Optional[str]:
    """
    Valida si una ciudad existe en el dataset.
    
    Args:
        ciudad: Nombre de la ciudad a validar.
        
    Returns:
        La ciudad validada o None si no existe.
    """
    return ciudad if ciudad in CIUDADES else None


def validate_año(año: int) -> Optional[int]:
    """
    Valida si un año está en el rango de análisis.
    
    Args:
        año: Año a validar.
        
    Returns:
        El año validado o None si está fuera de rango.
    """
    return año if año in AÑOS else None


def get_default_ciudad() -> str:
    """Retorna la ciudad por defecto (Bogotá)."""
    return "Bogotá"


def get_default_año() -> int:
    """Retorna el año por defecto (2026)."""
    return 2026
