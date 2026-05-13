# Visualización de distribución normal (Campana de Gauss).
# Compara la distribución de una ciudad vs la media nacional.

from typing import Tuple

import numpy as np
import plotly.graph_objects as go
from scipy import stats

from core.constants import AÑOS, COLORES_REGION
from core.theme import (
    BORDER_COLOR,
    COLOR_DANGER,
    COLOR_SUCCESS,
    GRID_COLOR,
    NATIONAL_FILL,
    NATIONAL_LINE,
    PAPER_BACKGROUND,
    PLOT_BACKGROUND,
    TEXT_COLOR,
    TEXT_MUTED,
    hex_to_rgba,
)
from data import CIUDADES, EMPLEO_BASE, SIGMA_BASE
from services.estadisticas_service import calcular_media_nacional
from services.outlier_service import es_outlier


# Genera la campana de Gauss para una ciudad vs media nacional.
def figura_gauss(ciudad: str, año: int) -> go.Figure:
    idx = AÑOS.index(año)
    mu_ciudad = EMPLEO_BASE[ciudad][idx]
    if mu_ciudad is None:
        fig = go.Figure()
        fig.add_annotation(text=f"No hay datos disponibles para {ciudad} en {año}", 
                          showarrow=False, font=dict(size=14, color=TEXT_MUTED))
        return fig
    sigma_ciudad = SIGMA_BASE[ciudad]
    mu_nac, _ = calcular_media_nacional(año)
    valores_año = [EMPLEO_BASE[c][idx] for c in CIUDADES if EMPLEO_BASE[c][idx] is not None]
    sigma_nac = np.std(valores_año) if valores_año else 1.0

    x = np.linspace(25, 80, 500)
    y_ciudad = stats.norm.pdf(x, mu_ciudad, sigma_ciudad)
    y_nac = stats.norm.pdf(x, mu_nac, sigma_nac)

    color_ciudad = COLORES_REGION[CIUDADES[ciudad]["region"]]
    outlier = es_outlier(ciudad, año)
    color_sombra = COLOR_DANGER if outlier else COLOR_SUCCESS

    fig = go.Figure()

    # Área nacional
    fig.add_trace(
        go.Scatter(
            x=x,
            y=y_nac,
            fill="tozeroy",
            fillcolor=NATIONAL_FILL,
            line=dict(color=NATIONAL_LINE, width=2, dash="dash"),
            name=f"Nacional μ={mu_nac:.1f}% σ={sigma_nac:.2f}",
        )
    )

    # Área ciudad
    fig.add_trace(
        go.Scatter(
            x=x,
            y=y_ciudad,
            fill="tozeroy",
            fillcolor=hex_to_rgba(color_sombra, 0x18),
            line=dict(color=color_sombra, width=2.5),
            name=f"{ciudad} μ={mu_ciudad:.1f}% σ={sigma_ciudad}",
        )
    )

    # Líneas de 2σ nacional
    for sgn, lbl in [(-2, "−2σ"), (+2, "+2σ")]:
        x_lim = mu_nac + sgn * sigma_nac
        fig.add_vline(
            x=x_lim,
            line=dict(color=TEXT_MUTED, dash="dot", width=1.2),
            annotation_text=lbl,
            annotation_font=dict(color=TEXT_MUTED, size=10),
        )

    # Media ciudad
    fig.add_vline(
        x=mu_ciudad,
        line=dict(color=color_sombra, width=2),
        annotation_text=f"μ {ciudad}",
        annotation_font=dict(color=color_sombra, size=11),
    )

    outlier_txt = (
        "⚠️ OUTLIER: fuera de 2σ nacional"
        if outlier
        else "✓ Dentro del rango normal (±2σ)"
    )
    subtitle_size = 12
    outlier_prefix = "⚠️ " if outlier else ""
    fig.update_layout(
        title=dict(
            text=f"<b>Distribución Normal</b> — {ciudad} vs Colombia ({año})<br>"
            f"<sup><span style='color:{color_sombra}'>{outlier_prefix}{outlier_txt}</span></sup>",
            font=dict(color=TEXT_COLOR, size=16),
        ),
        xaxis=dict(
            title="Tasa de Empleabilidad (%)", color=TEXT_MUTED, gridcolor=GRID_COLOR
        ),
        yaxis=dict(title="Densidad", color=TEXT_MUTED, gridcolor=GRID_COLOR),
        paper_bgcolor=PAPER_BACKGROUND,
        plot_bgcolor=PLOT_BACKGROUND,
        font=dict(color=TEXT_COLOR),
        legend=dict(
            bgcolor="rgba(255,255,255,0.9)",
            bordercolor=BORDER_COLOR,
            borderwidth=1,
            font=dict(size=11),
        ),
        height=380,
        margin=dict(l=50, r=30, t=70, b=50),
    )
    return fig
