# Visualización de análisis de correlación fronteriza.
# PUNTO EXTRA: σ vs tasa de migración ciudades fronterizas.

from typing import List

import numpy as np
import plotly.graph_objects as go
from plotly.subplots import make_subplots
from scipy import stats

from core.constants import AÑOS, COLORES_REGION
from core.theme import (
    BORDER_COLOR,
    COLOR_DANGER,
    COLOR_PRIMARY,
    COLOR_SUCCESS,
    GRID_COLOR,
    PAPER_BACKGROUND,
    PLOT_BACKGROUND,
    TEXT_COLOR,
    TEXT_MUTED,
)
from data import CIUDADES, EMPLEO_BASE, FRONTERIZAS, MIGRACION_FRONTERIZA, SIGMA_BASE


# Genera análisis de correlación para ciudades fronteriza
def figura_correlacion_frontera(año: int = 2026) -> go.Figure:
    colores_front = [COLOR_DANGER, COLOR_PRIMARY, COLORES_REGION["Santanderes"], COLORES_REGION["Caribe"], COLOR_SUCCESS]
    año_idx = AÑOS.index(año)

    fig = make_subplots(
        rows=1,
        cols=2,
        subplot_titles=[
            f"σ Laboral vs Migración ({año})",
            "Comparación Kurtosis (Platicúrtica)",
        ],
        horizontal_spacing=0.12,
    )

    sigmas_f = [SIGMA_BASE[c] for c in FRONTERIZAS]
    migr_año = [MIGRACION_FRONTERIZA[c][año_idx] for c in FRONTERIZAS]

    # Scatter correlación
    for i, ciudad in enumerate(FRONTERIZAS):
        fig.add_trace(
            go.Scatter(
                x=[MIGRACION_FRONTERIZA[ciudad][año_idx]],
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
    corr, pval = stats.pearsonr(migr_año, sigmas_f)
    fig.add_annotation(
        x=0.28,
        y=0.95,
        xref="paper",
        yref="paper",
        text=f"r = {corr:.3f} | p = {pval:.3f}",
        showarrow=False,
        font=dict(color=COLOR_PRIMARY, size=12),
        bgcolor="rgba(255,255,255,0.9)",
    )

    # Comparación kurtosis (curvas normales)
    x = np.linspace(30, 75, 300)
    triangulo = ["Bogotá", "Medellín", "Cali"]
    for ciudad in FRONTERIZAS[:3]:
        mu = EMPLEO_BASE[ciudad][año_idx]
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
        mu = EMPLEO_BASE[ciudad][año_idx]
        sig = SIGMA_BASE[ciudad]
        y = stats.norm.pdf(x, mu, sig)
        fig.add_trace(
            go.Scatter(
                x=x,
                y=y,
                mode="lines",
                line=dict(color=COLORES_REGION["Triángulo de Oro"], width=2),
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
            bgcolor="rgba(255,255,255,0.9)",
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
    fig.update_xaxes(color=TEXT_MUTED, gridcolor=GRID_COLOR)
    fig.update_yaxes(color=TEXT_MUTED, gridcolor=GRID_COLOR)
    return fig
