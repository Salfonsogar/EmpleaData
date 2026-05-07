"""
Tests para visualizaciones Plotly.
Verifica que las funciones retornen objetos go.Figure válidos.
"""

import pytest
from visualizations.mapa import figura_mapa
from visualizations.gauss import figura_gauss
from visualizations.tendencias import figura_tendencia
from visualizations.ranking import figura_ranking
from visualizations.correlacion import figura_correlacion_frontera


class TestFiguraMapa:
    """Tests para el mapa."""
    
    def test_retorna_figure(self, año_valido, ciudad_valida):
        """Verifica que retorna un go.Figure."""
        fig = figura_mapa(año_valido, ciudad_valida)
        assert hasattr(fig, 'data')
        assert hasattr(fig, 'layout')
    
    def test_con_ciudad_none(self, año_valido):
        """Verifica que funciona con ciudad_sel=None."""
        fig = figura_mapa(año_valido, None)
        assert hasattr(fig, 'data')


class TestFiguraGauss:
    """Tests para la campana de Gauss."""
    
    def test_retorna_figure(self, ciudad_valida, año_valido):
        """Verifica que retorna un go.Figure."""
        fig = figura_gauss(ciudad_valida, año_valido)
        assert hasattr(fig, 'data')
        assert len(fig.data) > 0


class TestFiguraTendencia:
    """Tests para el gráfico de tendencia."""
    
    def test_retorna_figure(self, ciudad_valida):
        """Verifica que retorna un go.Figure."""
        fig = figura_tendencia(ciudad_valida)
        assert hasattr(fig, 'data')
    
    def test_tiene_3_trazas(self, ciudad_valida):
        """Verifica que tiene las 3 trazas (banda, línea, nacional)."""
        fig = figura_tendencia(ciudad_valida)
        assert len(fig.data) >= 3


class TestFiguraRanking:
    """Tests para el ranking."""
    
    def test_retorna_figure(self, año_valido):
        """Verifica que retorna un go.Figure."""
        fig = figura_ranking(año_valido)
        assert hasattr(fig, 'data')
    
    def test_barras_horizontales(self, año_valido):
        """Verifica que es un gráfico de barras horizontal."""
        fig = figura_ranking(año_valido)
        assert fig.data[0].orientation == 'h'


class TestFiguraCorrelacion:
    """Tests para el análisis de correlación."""
    
    def test_retorna_figure(self):
        """Verifica que retorna un go.Figure."""
        fig = figura_correlacion_frontera()
        assert hasattr(fig, 'data')
        # Verificar que tiene subplots (make_subplots crea múltiples ejes)
        assert len([k for k in fig.layout if 'xaxis' in k]) >= 2
