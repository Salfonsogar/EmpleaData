# Visualización de análisis de correlación fronteriza.
# PUNTO EXTRA: σ vs tasa de migración ciudades fronterizas.

from typing import List

import numpy as np
import plotly.graph_objects as go
from plotly.subplots import make_subplots
from scipy import stats

from core.constants import COLORES_REGION
from core.theme import (
    BORDER_COLOR,
    COLOR_DANGER,
    COLOR_SUCCESS,
    COLOR_WARNING,
    PAPER_BACKGROUND,
    PLOT_BACKGROUND,
    TEXT_COLOR,
)
from data import CIUDADES, EMPLEO_BASE, FRONTERIZAS, MIGRACION_FRONTERIZA, SIGMA_BASE


# Genera análisis de correlación para ciudades fronteriza
def figura_correlacion_frontera() -> go.Figure:
    colores_front = [COLOR_DANGER, COLOR_WARNING, "#7B2D8B", "#00B4D8", COLOR_SUCCESS]

    fig = make_subplots(
        rows=1,
        cols=2,
        subplot_titles=[
            "σ Laboral vs Migración (2026)",
            "Comparación Kurtosis (Platicúrtica)",
        ],
        horizontal_spacing=0.12,
    )

    sigmas_f = [SIGMA_BASE[c] for c in FRONTERIZAS]
    migr_2026 = [MIGRACION_FRONTERIZA[c][-1] for c in FRONTERIZAS]

    # Scatter correlación
    for i, ciudad in enumerate(FRONTERIZAS):
        fig.add_trace(
            go.Scatter(
                x=[MIGRACION_FRONTERIZA[ciudad][-1]],
                y=[SIGMA_BASE[ciudad]],
                mode="markers+text",
                marker=dict(size=14, color=colores_front[i]),
                text=[ciudad],
                textposition="top center",
                textfont=dict(color=TEXT_COLOR, size=10),
                name=ciudad,
                hovertemplate=f"{ciudad}<br>Migración: %{{x}}k<br>σ: %{{y}}<extra></extra>",
            ),
            row=1,
            col=1,
        )

    # Correlación
    corr, pval = stats.pearsonr(migr_2026, sigmas_f)
    fig.add_annotation(
        x=0.28,
        y=0.95,
        xref="paper",
        yref="paper",
        text=f"r = {corr:.3f} | p = {pval:.3f}",
        showarrow=False,
        font=dict(color=COLOR_WARNING, size=12),
        bgcolor=f"rgba(13,17,23,0.8)",
    )

    # Comparación kurtosis (curvas normales)
    x = np.linspace(30, 75, 300)
    triangulo = ["Bogotá", "Medellín", "Cali"]
    for ciudad in FRONTERIZAS[:3]:
        mu = EMPLEO_BASE[ciudad][5]
        sig = SIGMA_BASE[ciudad]
        y = stats.norm.pdf(x, mu, sig)
        fig.add_trace(
            go.Scatter(
                x=x,
                y=y,
                mode="lines",
                line=dict(color=COLOR_DANGER, width=1.5, dash="dot"),
                name=f"{ciudad} (frontera)",
                showlegend=(ciudad == FRONTERIZAS[0]),
            ),
            row=1,
            col=2,
        )

    for ciudad in triangulo:
        mu = EMPLEO_BASE[ciudad][5]
        sig = SIGMA_BASE[ciudad]
        y = stats.norm.pdf(x, mu, sig)
        fig.add_trace(
            go.Scatter(
                x=x,
                y=y,
                mode="lines",
                line=dict(color=COLOR_WARNING, width=2),
                name=f"{ciudad} (triángulo)",
                showlegend=(ciudad == triangulo[0]),
            ),
            row=1,
            col=2,
        )

    fig.update_layout(
        paper_bgcolor=PAPER_BACKGROUND,
        plot_bgcolor=PLOT_BACKGROUND,
        font=dict(color=TEXT_COLOR),
        legend=dict(
            bgcolor=f"rgba(13,17,23,0.8)",
            bordercolor=BORDER_COLOR,
            borderwidth=1,
            font=dict(size=9),
        ),
        height=380,
        margin=dict(l=50, r=30, t=60, b=40),
        title=dict(
            text="Análisis Correlación Fronteriza — Punto Extra",
            font=dict(color=TEXT_COLOR, size=13),
        ),
    )
    fig.update_xaxes(color="#8B949E", gridcolor="#21262D")
    fig.update_yaxes(color="#8B949E", gridcolor="#21262D")
    return fig
