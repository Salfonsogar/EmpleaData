import plotly.graph_objects as go
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
from visualizations.informalidad import figura_informalidad_barras, figura_informalidad_evolucion
from core.constants import AÑOS
from data import CIUDADES

# Pre-calcular figuras al inicio
_FIGURES_CACHE = {}

def _init_figures_cache():
    """Pre-calcula todas las figuras al inicio"""
    print("Pre-calculando figuras...")
    
    # Ranking
    for año in AÑOS:
        _FIGURES_CACHE[f"ranking_{año}"] = figura_ranking(año)
        _FIGURES_CACHE[f"ranking_{año}_top5"] = figura_ranking(año, top_n=5)
    
    # Genero y heatmap
    for ciudad in CIUDADES:
        _FIGURES_CACHE[f"genero_{ciudad}"] = figura_genero(ciudad)
        _FIGURES_CACHE[f"heatmap_{ciudad}"] = figura_heatmap(ciudad)
        _FIGURES_CACHE[f"tendencia_{ciudad}"] = figura_tendencia(ciudad)
    
    # Dane sectores
    for año in AÑOS:
        try:
            _FIGURES_CACHE[f"dane_sectores_{año}"] = figura_dane_sectores(año)
        except:
            pass
    
    # Informalidad
    for año in AÑOS:
        try:
            _FIGURES_CACHE[f"informalidad_{año}"] = figura_informalidad_barras(año)
        except:
            pass
    
    try:
        _FIGURES_CACHE["informalidad_evolucion"] = figura_informalidad_evolucion()
    except:
        pass
    
    print(f"Figuras pre-calculadas: {len(_FIGURES_CACHE)}")


def register_stats_callbacks(app):
    # Inicializar caché al registrar callbacks
    if not _FIGURES_CACHE:
        _init_figures_cache()

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
        return figura_gauss(ciudad, año).to_dict()

    @app.callback(
        Output("grafica-tendencia", "figure"),
        Input("dropdown-ciudad", "value")
    )
    def actualizar_tendencia(ciudad):
        return _FIGURES_CACHE.get(f"tendencia_{ciudad}", figura_tendencia(ciudad)).to_dict()

    @app.callback(
        Output("grafica-ranking", "figure"),
        Output("toggle-ranking", "children"),
        [Input("slider-año", "value"),
         Input("toggle-ranking", "n_clicks")]
    )
    def actualizar_ranking(año, n_clicks):
        if n_clicks and n_clicks % 2 == 1:
            return _FIGURES_CACHE.get(f"ranking_{año}_top5", figura_ranking(año, top_n=5)).to_dict(), "[Ver todas]"
        return _FIGURES_CACHE.get(f"ranking_{año}", figura_ranking(año)).to_dict(), "[Top 5]"

    @app.callback(
        Output("grafica-sectores", "figure"),
        [Input("slider-año", "value"),
         Input("dropdown-ciudad", "value")]
    )
    def actualizar_sectores(año, ciudad):
        return figura_sectores(ciudad, año).to_dict()

    @app.callback(
        Output("grafica-genero", "figure"),
        Input("dropdown-ciudad", "value")
    )
    def actualizar_genero(ciudad):
        return _FIGURES_CACHE.get(f"genero_{ciudad}", figura_genero(ciudad)).to_dict()

    @app.callback(
        Output("grafica-heatmap", "figure"),
        Input("dropdown-ciudad", "value")
    )
    def actualizar_heatmap(ciudad):
        return _FIGURES_CACHE.get(f"heatmap_{ciudad}", figura_heatmap(ciudad)).to_dict()

    @app.callback(
        Output("grafica-dane-sectores", "figure"),
        Input("slider-año", "value")
    )
    def actualizar_dane_sectores(año):
        return _FIGURES_CACHE.get(f"dane_sectores_{año}", figura_dane_sectores(año)).to_dict()

    @app.callback(
        Output("grafica-informalidad-barras", "figure"),
        Input("slider-año", "value")
    )
    def actualizar_informalidad_barras(año):
        return _FIGURES_CACHE.get(f"informalidad_{año}", figura_informalidad_barras(año)).to_dict()

    @app.callback(
        Output("grafica-informalidad-evolucion", "figure"),
        Input("dropdown-ciudad", "value")
    )
    def actualizar_informalidad_evolucion(ciudad):
        return _FIGURES_CACHE.get("informalidad_evolucion", figura_informalidad_evolucion()).to_dict()
