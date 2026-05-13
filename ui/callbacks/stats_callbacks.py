from dash import Input, Output
from services.estadisticas_service import calcular_estadisticas, calcular_media_nacional
from services.outlier_service import es_outlier
from ui.components.cards import create_kpi_cards
from visualizations.gauss import figura_gauss
from visualizations.tendencias import figura_tendencia
from visualizations.ranking import figura_ranking
from visualizations.sectores import figura_sectores
from visualizations.genero import figura_genero
from visualizations.heatmap import figura_heatmap
from visualizations.dane_sectores import figura_dane_sectores


def register_stats_callbacks(app):
    @app.callback(
        Output("kpi-cards", "children"),
        [Input("slider-año", "value"),
         Input("dropdown-ciudad", "value")]
    )
    def actualizar_kpis(año, ciudad):
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
            is_outlier=is_outlier,
        )

    @app.callback(
        Output("grafica-gauss", "figure"),
        [Input("slider-año", "value"),
         Input("dropdown-ciudad", "value")]
    )
    def actualizar_gauss(año, ciudad):
        return figura_gauss(ciudad, año)

    @app.callback(
        Output("grafica-tendencia", "figure"),
        Input("dropdown-ciudad", "value")
    )
    def actualizar_tendencia(ciudad):
        return figura_tendencia(ciudad)

    @app.callback(
        Output("grafica-ranking", "figure"),
        Output("toggle-ranking", "children"),
        [Input("slider-año", "value"),
         Input("toggle-ranking", "n_clicks")]
    )
    def actualizar_ranking(año, n_clicks):
        if n_clicks and n_clicks % 2 == 1:
            return figura_ranking(año, top_n=5), "[Ver todas]"
        return figura_ranking(año), "[Top 5]"

    @app.callback(
        Output("grafica-sectores", "figure"),
        [Input("slider-año", "value"),
         Input("dropdown-ciudad", "value")]
    )
    def actualizar_sectores(año, ciudad):
        return figura_sectores(ciudad, año)

    @app.callback(
        Output("grafica-genero", "figure"),
        Input("dropdown-ciudad", "value")
    )
    def actualizar_genero(ciudad):
        return figura_genero(ciudad)

    @app.callback(
        Output("grafica-heatmap", "figure"),
        Input("dropdown-ciudad", "value")
    )
    def actualizar_heatmap(ciudad):
        return figura_heatmap(ciudad)

    @app.callback(
        Output("grafica-dane-sectores", "figure"),
        Input("slider-año", "value")
    )
    def actualizar_dane_sectores(año):
        return figura_dane_sectores(año)
