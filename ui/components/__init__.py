"""
Componentes UI reutilizables.
"""

from .navbar import create_navbar
from .cards import kpi_card, create_kpi_cards

__all__ = [
    'create_navbar',
    'kpi_card',
    'create_kpi_cards',
]
