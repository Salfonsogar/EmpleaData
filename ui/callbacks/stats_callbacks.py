"""
Callbacks relacionados con estadísticas, KPIs y gráficos estadísticos.
"""

from dash import Input, Output
from services.estadisticas_service import calcular_estadisticas, calcular_media_nacional
from services.outlier_service import es_outlier
from ui.components.cards import create_kpi_cards
from visualizations.gauss import figura_gauss
from visualizations.tendencias import figura_tendencia
from visualizations.ranking import figura_ranking


def register_stats_callbacks(app):
    """
    Registra callbacks relacionados con estadísticas y KPIs.
    
    Args:
        app: Instancia de la aplicación Dash.
    """
    @app.callback(
        Output("kpi-cards", "children"),
        [Input("slider-año", "value"),
         Input("dropdown-ciudad", "value")]
    )
    def actualizar_kpis(año, ciudad):
        """Actualiza las tarjetas KPI."""
        est = calcular_estadisticas(ciudad, año)
        mu_nac, _ = calcular_media_nacional(año)
        is_outlier = es_outlier(ciudad, año)
        
        return create_kpi_cards(
            ciudad=ciudad,
            año=año,
            media=est["media"],
            mediana=est["mediana"],
            std=est["std"],
            sector=est["moda"],
            mu_nac=mu_nac,
            is_outlier=is_outlier
        )

    @app.callback(
        Output("grafica-gauss", "figure"),
        [Input("slider-año", "value"),
         Input("dropdown-ciudad", "value")]
    )
    def actualizar_gauss(año, ciudad):
        """Actualiza la gráfica de distribución Gauss."""
        return figura_gauss(ciudad, año)

    @app.callback(
        Output("grafica-tendencia", "figure"),
        Input("dropdown-ciudad", "value")
    )
    def actualizar_tendencia(ciudad):
        """Actualiza la gráfica de tendencia temporal."""
        return figura_tendencia(ciudad)

    @app.callback(
        Output("grafica-ranking", "figure"),
        Input("slider-año", "value")
    )
    def actualizar_ranking(año):
        """Actualiza la gráfica de ranking."""
        return figura_ranking(año)
