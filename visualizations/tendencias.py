# Visualización de tendencia temporal de empleo (2021-2026).
# Muestra evolución de una ciudad con banda de confianza ±1σ.

from typing import List

import numpy as np
import plotly.graph_objects as go

from core.constants import AÑOS, COLORES_REGION
from core.theme import (
    BORDER_COLOR,
    COLOR_WARNING,
    PAPER_BACKGROUND,
    PLOT_BACKGROUND,
    TEXT_COLOR,
)
from data import CIUDADES, EMPLEO_BASE, SIGMA_BASE


# Genera gráfico de línea con tendencia 2021-2026 para una ciudad.
def figura_tendencia(ciudad: str) -> go.Figure:

    tasas = EMPLEO_BASE[ciudad]
    sigmas = SIGMA_BASE[ciudad]
    color = COLORES_REGION[CIUDADES[ciudad]["region"]]

    fig = go.Figure()
    # Banda de confianza ±1σ
    fig.add_trace(
        go.Scatter(
            x=AÑOS + AÑOS[::-1],
            y=[t + sigmas for t in tasas] + [t - sigmas for t in tasas][::-1],
            fill="toself",
            fillcolor=f"rgba{tuple(list(bytes.fromhex(color[1:])) + [40])}",
            line=dict(color="rgba(0,0,0,0)"),
            name="±1σ",
            hoverinfo="skip",
        )
    )
    # Línea principal
    fig.add_trace(
        go.Scatter(
            x=AÑOS,
            y=tasas,
            mode="lines+markers",
            line=dict(color=color, width=3),
            marker=dict(size=9, color=color, line=dict(color="white", width=1.5)),
            name=ciudad,
            text=[f"{t:.1f}%" for t in tasas],
            textposition="top center",
            hovertemplate="%{x}: %{y:.1f}%<extra></extra>",
        )
    )

    # Media nacional por año
    from services.estadisticas_service import calcular_media_nacional

    nac = [calcular_media_nacional(a)[0] for a in AÑOS]
    fig.add_trace(
        go.Scatter(
            x=AÑOS,
            y=nac,
            mode="lines",
            line=dict(color=COLOR_WARNING, width=1.5, dash="dot"),
            name="Media Nacional",
        )
    )

    fig.update_layout(
        title=dict(
            text=f"Tendencia Empleabilidad — {ciudad} (2021-2026)",
            font=dict(color=TEXT_COLOR, size=13),
        ),
        xaxis=dict(tickvals=AÑOS, color="#8B949E", gridcolor="#21262D"),
        yaxis=dict(title="%", color="#8B949E", gridcolor="#21262D"),
        paper_bgcolor=PAPER_BACKGROUND,
        plot_bgcolor=PLOT_BACKGROUND,
        font=dict(color=TEXT_COLOR),
        legend=dict(
            bgcolor=f"rgba(13,17,23,0.85)",
            bordercolor=BORDER_COLOR,
            borderwidth=1,
            font=dict(size=10),
        ),
        showlegend=False,
        height=380,
        margin=dict(l=50, r=30, t=50, b=40),
    )
    return fig
