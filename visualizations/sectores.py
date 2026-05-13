"""
Visualización de sectores económicos más empleados y distribución de género.
"""

import plotly.graph_objects as go
from plotly.subplots import make_subplots

from core.theme import (
    BORDER_COLOR,
    GRID_COLOR,
    PAPER_BACKGROUND,
    PLOT_BACKGROUND,
    TEXT_COLOR,
    TEXT_MUTED,
    COLOR_PRIMARY,
)
from data.sectores import get_top5_sectores, get_genero_sector


def figura_sectores(ciudad: str, año: int) -> go.Figure:
    top5 = get_top5_sectores(ciudad, año)

    sectores = [s[0] for s in top5]
    empleados = [s[1] for s in top5]
    colores_barras = [
        COLOR_PRIMARY if i == 0 else "#4a6fa5"
        for i in range(len(sectores))
    ]

    sector_principal = sectores[0]
    pct_mujeres, pct_hombres = get_genero_sector(sector_principal)

    fig = make_subplots(
        rows=1, cols=2,
        column_widths=[0.55, 0.45],
        specs=[[{"type": "bar"}, {"type": "pie"}]],
        subplot_titles=(
            f"Top 5 Sectores - {ciudad} ({año})",
            f"Distribución Género - {sector_principal}"
        )
    )

    fig.add_trace(
        go.Bar(
            x=empleados,
            y=sectores,
            orientation="h",
            marker=dict(
                color=colores_barras,
                opacity=0.85,
                line=dict(color="rgba(0,0,0,0.08)", width=0.5),
            ),
            text=[f"{e:.0f}K" for e in empleados],
            textposition="outside",
            textfont=dict(color=TEXT_COLOR, size=10),
            hovertemplate="%{y}: %{x:.0f}K empleos<extra></extra>",
        ),
        row=1, col=1
    )

    fig.add_trace(
        go.Pie(
            labels=["Mujeres", "Hombres"],
            values=[pct_mujeres * 100, pct_hombres * 100],
            marker=dict(
                colors=["#e74c3c", "#3498db"]
            ),
            textinfo="label+percent",
            textfont=dict(color="white", size=11),
            hole=0.5,
            hovertemplate="%{label}: %{percent}<extra></extra>",
        ),
        row=1, col=2
    )

    fig.update_layout(
        paper_bgcolor=PAPER_BACKGROUND,
        plot_bgcolor=PLOT_BACKGROUND,
        font=dict(color=TEXT_COLOR),
        height=320,
        margin=dict(l=20, r=20, t=50, b=40),
        showlegend=False,
    )

    fig.update_xaxes(
        title_text="Miles de empleados",
        color=TEXT_MUTED,
        gridcolor=GRID_COLOR,
        row=1, col=1
    )
    fig.update_yaxes(
        color=TEXT_MUTED,
        row=1, col=1
    )

    return fig