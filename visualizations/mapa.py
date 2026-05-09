# Visualización de mapa coroplético de Colombia.

from typing import Optional

import plotly.graph_objects as go

from core.constants import AÑOS, COLORES_REGION
from core.theme import (
    BORDER_COLOR, HIGHLIGHT_COLOR, MAP_CENTER_LAT, MAP_CENTER_LON,
    MAP_STYLE, MAP_ZOOM, PAPER_BACKGROUND, TEXT_COLOR,
)
from data import CIUDADES, EMPLEO_BASE, SECTOR_DOMINANTE, SIGMA_BASE
from services.estadisticas_service import calcular_media_nacional
from services.outlier_service import es_outlier


# Genera el mapa de Colombia con tasas de empleo por ciudad.
def figura_mapa(año: int, ciudad_sel: Optional[str] = None, region_filtro: Optional[str] = "Todas") -> go.Figure:

    idx = AÑOS.index(año)
    mu_nac, _ = calcular_media_nacional(año)

    ciudades_filtradas = {
        c: info for c, info in CIUDADES.items()
        if region_filtro == "Todas" or info["region"] == region_filtro
    }

    lats, lons, nombres, tasas, regiones, textos = [], [], [], [], [], []
    for ciudad, info in ciudades_filtradas.items():
        tasa = EMPLEO_BASE[ciudad][idx]
        sigma = SIGMA_BASE[ciudad]
        outlier = es_outlier(ciudad, año)
        lats.append(info["lat"])
        lons.append(info["lon"])
        nombres.append(ciudad)
        tasas.append(tasa)
        regiones.append(info["region"])
        textos.append(
            f"<b>{ciudad}</b><br>"
            f"Región: {info['region']}<br>"
            f"Tasa Empleo: {tasa:.1f}%<br>"
            f"σ = {sigma}<br>"
            f"Sector: {SECTOR_DOMINANTE[ciudad]}<br>"
            f"{'⚠️ OUTLIER (>2σ)' if outlier else '✓ Dentro rango normal'}"
        )

    fig = go.Figure()
    for region, color in COLORES_REGION.items():
        mask = [r == region for r in regiones]
        fig.add_trace(
            go.Scattermapbox(
                lat=[lats[i] for i in range(len(lats)) if mask[i]],
                lon=[lons[i] for i in range(len(lons)) if mask[i]],
                mode="markers+text",
                marker=dict(
                    size=[max(12, tasas[i] / 4) for i in range(len(tasas)) if mask[i]],
                    color=color,
                    opacity=0.85,
                ),
                text=[nombres[i] for i in range(len(nombres)) if mask[i]],
                textposition="top center",
                textfont=dict(color=TEXT_COLOR, size=10),
                hovertext=[textos[i] for i in range(len(textos)) if mask[i]],
                hoverinfo="text",
                name=region,
            )
        )

    # Resaltar ciudad seleccionada
    if ciudad_sel and ciudad_sel in CIUDADES:
        info = CIUDADES[ciudad_sel]
        fig.add_trace(
            go.Scattermapbox(
                lat=[info["lat"]],
                lon=[info["lon"]],
                mode="markers",
                marker=dict(size=22, color=HIGHLIGHT_COLOR, opacity=1.0, symbol="circle"),
                hoverinfo="skip",
                name="Seleccionada",
                showlegend=False,
            )
        )

    fig.update_layout(
        mapbox=dict(
            style=MAP_STYLE,
            center=dict(lat=MAP_CENTER_LAT, lon=MAP_CENTER_LON),
            zoom=MAP_ZOOM,
        ),
        margin=dict(l=0, r=0, t=0, b=0),
        paper_bgcolor=PAPER_BACKGROUND,
        plot_bgcolor=PAPER_BACKGROUND,
        legend=dict(
            bgcolor="rgba(255,255,255,0.9)",
            font=dict(color=TEXT_COLOR, size=11),
            bordercolor=BORDER_COLOR,
            borderwidth=1,
        ),
        height=440,
    )
    return fig
