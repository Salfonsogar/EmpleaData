"""
Tests para servicios de estadísticas.
"""

import pytest
from services.estadisticas_service import calcular_estadisticas, calcular_media_nacional


class TestCalcularEstadisticas:
    """Tests para la función calcular_estadisticas."""
    
    def test_retorna_dict(self, ciudad_valida, año_valido):
        """Verifica que retorna un diccionario."""
        result = calcular_estadisticas(ciudad_valida, año_valido)
        assert isinstance(result, dict)
    
    def test_tiene_keys_requeridas(self, ciudad_valida, año_valido):
        """Verifica que el dict tiene todas las keys esperadas."""
        result = calcular_estadisticas(ciudad_valida, año_valido)
        required_keys = ["media", "mediana", "moda", "std", "mu_ref", "sigma_ref"]
        for key in required_keys:
            assert key in result
    
    def test_media_es_float(self, ciudad_valida, año_valido):
        """Verifica que la media es un float."""
        result = calcular_estadisticas(ciudad_valida, año_valido)
        assert isinstance(result["media"], float)
    
    def test_moda_es_string(self, ciudad_valida, año_valido):
        """Verifica que la moda es un string (sector)."""
        result = calcular_estadisticas(ciudad_valida, año_valido)
        assert isinstance(result["moda"], str)
    
    def test_media_nacional_retorna_tupla(self, año_valido):
        """Verifica que calcular_media_nacional retorna una tupla."""
        result = calcular_media_nacional(año_valido)
        assert isinstance(result, tuple)
        assert len(result) == 2
    
    def test_media_nacional_valores_razonables(self, año_valido):
        """Verifica que la media nacional está en un rango razonable."""
        media, sigma = calcular_media_nacional(año_valido)
        assert 40 < media < 70
        assert 0 < sigma < 10
