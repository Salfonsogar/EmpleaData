"""
Fixtures compartidas para tests.
Configuración común para todos los archivos de test.
"""

import pytest
from data import CIUDADES, EMPLEO_BASE, SIGMA_BASE, SECTOR_DOMINANTE
from core.constants import AÑOS


@pytest.fixture
def ciudad_valida():
    """Retorna una ciudad válida para tests."""
    return "Bogotá"


@pytest.fixture
def año_valido():
    """Retorna un año válido para tests."""
    return 2026


@pytest.fixture
def año_idx():
    """Retorna el índice del año 2026."""
    return AÑOS.index(2026)


@pytest.fixture
def muestra_mock():
    """Retorna una muestra simulada para tests."""
    import numpy as np
    return np.array([60.0, 61.0, 59.5, 62.0, 60.5])


@pytest.fixture
def ciudades_fronterizas():
    """Retorna lista de ciudades fronterizas."""
    from data import FRONTERIZAS
    return FRONTERIZAS
