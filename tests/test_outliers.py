"""
Tests para servicio de detección de outliers.
"""

import pytest
from services.outlier_service import es_outlier, get_outliers_por_año
from data import CIUDADES, EMPLEO_BASE


class TestEsOutlier:
    """Tests para la función es_outlier."""
    
    def test_retorna_bool(self, ciudad_valida, año_valido):
        """Verifica que retorna un booleano."""
        result = es_outlier(ciudad_valida, año_valido)
        assert isinstance(result, bool)
    
    def test_bogota_no_es_outlier_2026(self):
        """Bogotá con mejores tasas no debería ser outlier en 2026."""
        result = es_outlier("Bogotá", 2026)
        assert result == False
    
    def test_ciudad_extrema_es_outlier(self):
        """Bogotá con tasa alta debería ser outlier con 1.5σ."""
        result = es_outlier("Bogotá", 2026, 1.5)
        assert result == True
    
    def test_get_outliers_retorna_lista(self, año_valido):
        """Verifica que get_outliers_por_año retorna una lista."""
        result = get_outliers_por_año(año_valido)
        assert isinstance(result, list)
    
    def test_get_outliers_solo_ciudades_validas(self, año_valido):
        """Verifica que todos los elementos sean ciudades válidas."""
        result = get_outliers_por_año(año_valido)
        for ciudad in result:
            assert ciudad in CIUDADES
