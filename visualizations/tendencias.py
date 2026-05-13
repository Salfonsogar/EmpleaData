# Visualización de tendencia temporal de empleo (2021-2026).
# Muestra evolución de una ciudad con banda de confianza ±1σ.

from typing import List

import numpy as np
import plotly.graph_objects as go

from core.constants import AÑOS, COLORES_REGION
from core.theme import (
    BORDER_COLOR,
    GRID_COLOR,
    NATIONAL_LINE,
    PAPER_BACKGROUND,
    PLOT_BACKGROUND,
    TEXT_COLOR,
    TEXT_MUTED,
    hex_to_rgba,
)
from data import CIUDADES, EMPLEO_BASE, SIGMA_BASE


# Genera gráfico de línea con tendencia 2021-2026 para una ciudad.
def figura_tendencia(ciudad: str) -> go.Figure:

    tasas = EMPLEO_BASE[ciudad]
    sigmas = SIGMA_BASE[ciudad]
    color = COLORES_REGION[CIUDADES[ciudad]["region"]]

    tasas_filtradas = [t if t is not None else 0 for t in tasas]
    sigmas_filtradas = [s if t is not None else 0 for t, s in zip(tasas, [sigmas]*len(tasas))]

    fig = go.Figure()
    
    # Banda de confianza ±1σ (solo fill, sin línea)
    fig.add_trace(
        go.Scatter(
            x=AÑOS + AÑOS[::-1],
            y=[t + s for t, s in zip(tasas_filtradas, sigmas_filtradas)] + [t - s for t, s in zip(tasas_filtradas, sigmas_filtradas)][::-1],
            fill="toself",
            fillcolor=hex_to_rgba(color, 0x12),
            line=dict(width=0),
            name="±1σ",
            hoverinfo="skip",
        )
    )
    
    # Línea principal de la ciudad
    fig.add_trace(
        go.Scatter(
            x=AÑOS,
            y=tasas,
            mode="lines+markers",
            line=dict(color=color, width=4),
            marker=dict(size=10, color=color, line=dict(color="white", width=2)),
            name=ciudad,
            text=[f"{t:.1f}%" if t is not None else "—" for t in tasas],
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
            line=dict(color=NATIONAL_LINE, width=1.5, dash="dot"),
            name="Media Nacional",
        )
    )

    fig.update_layout(
        title=dict(
            text=f"Tendencia Empleabilidad — <b style='color:{color}'>{ciudad}</b> (2021-2026)",
            font=dict(color=TEXT_COLOR, size=13),
        ),
        xaxis=dict(tickvals=AÑOS, color=TEXT_MUTED, gridcolor=GRID_COLOR),
        yaxis=dict(title="%", color=TEXT_MUTED, gridcolor=GRID_COLOR),
        paper_bgcolor=PAPER_BACKGROUND,
        plot_bgcolor=PLOT_BACKGROUND,
        font=dict(color=TEXT_COLOR),
        showlegend=False,
        height=380,
        margin=dict(l=50, r=30, t=50, b=40),
    )
    return fig
