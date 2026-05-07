"""
Utilidades de formateo para valores numéricos y texto.
"""

from typing import Union


def format_pct(value: Union[float, int], decimals: int = 1) -> str:
    """
    Formatea un valor numérico como porcentaje.
    
    Args:
        value: Valor numérico.
        decimals: Número de decimales.
        
    Returns:
        String formateado con símbolo %.
    """
    return f"{value:.{decimals}f}%"


def format_number(value: Union[float, int], decimals: int = 2) -> str:
    """
    Formatea un valor numérico con decimales controlados.
    
    Args:
        value: Valor numérico.
        decimals: Número de decimales.
        
    Returns:
        String formateado.
    """
    return f"{value:.{decimals}f}"
