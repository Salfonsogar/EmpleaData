from typing import Dict, List

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
)
from services.informalidad_service import (
    get_informalidad_todas_ciudades,
    get_evolucion_informalidad,
    get_media_nacional_informalidad,
)


def figura_informalidad_barras(año: int) -> go.Figure:
    datos_ciudades = get_informalidad_todas_ciudades(año)
    mu_nac = get_media_nacional_informalidad(año)

    if not datos_ciudades:
        fig = go.Figure()
        fig.update_layout(
            title=dict(text=f"Tasa de Informalidad {año}"),
            paper_bgcolor=PAPER_BACKGROUND,
            plot_bgcolor=PLOT_BACKGROUND,
            font=dict(color=TEXT_COLOR),
            height=340,
        )
        return fig

    datos_ord = sorted(
        [(c, t) for c, t in datos_ciudades.items()],
        key=lambda x: x[1],
        reverse=True,
    )

    ciudades_ord = [d[0] for d in datos_ord]
    tasas_ord = [d[1] for d in datos_ord]

    colors = []
    for c in ciudades_ord:
        if c in COLORES_REGION:
            colors.append(COLORES_REGION[c])
        else:
            colors.append("#888888")

    fig = go.Figure(
        go.Bar(
            x=tasas_ord,
            y=ciudades_ord,
            orientation="h",
            marker=dict(
                color=colors,
                opacity=0.85,
                line=dict(color="rgba(0,0,0,0.08)", width=0.5),
            ),
            text=[f"{t:.1f}%" for t in tasas_ord],
            textposition="outside",
            textfont=dict(color=TEXT_COLOR, size=10),
            hovertemplate="%{y}: %{x:.1f}%<extra></extra>",
        )
    )

    fig.add_vline(
        x=mu_nac,
        line=dict(color=NATIONAL_LINE, dash="dash", width=1.5),
        annotation_text=f"Nacional {mu_nac:.1f}%",
        annotation_font=dict(color=NATIONAL_LINE, size=10),
    )

    fig.update_layout(
        title=dict(
            text=f"Tasa de Informalidad {año}", font=dict(color=TEXT_COLOR, size=13)
        ),
        xaxis=dict(
            range=[0, max(tasas_ord) * 1.2] if tasas_ord else [0, 100],
            color=TEXT_MUTED,
            gridcolor=GRID_COLOR,
            title="Tasa (%)",
        ),
        yaxis=dict(color=TEXT_MUTED),
        paper_bgcolor=PAPER_BACKGROUND,
        plot_bgcolor=PLOT_BACKGROUND,
        font=dict(color=TEXT_COLOR),
        height=340,
        margin=dict(l=120, r=60, t=50, b=40),
    )
    return fig


def figura_informalidad_evolucion() -> go.Figure:
    evolucion = get_evolucion_informalidad()

    if not evolucion:
        fig = go.Figure()
        fig.update_layout(
            title="Evolución de la Informalidad",
            paper_bgcolor=PAPER_BACKGROUND,
            plot_bgcolor=PLOT_BACKGROUND,
            font=dict(color=TEXT_COLOR),
            height=340,
        )
        return fig

    fig = go.Figure()

    for ciudad, tasas in evolucion.items():
        color = COLORES_REGION.get(ciudad, "#888888")
        fig.add_trace(
            go.Scatter(
                x=AÑOS,
                y=tasas,
                mode="lines+markers",
                name=ciudad,
                line=dict(color=color, width=2),
                marker=dict(size=6),
                hovertemplate=f"{ciudad}: %{{y:.1f}}%<extra></extra>",
            )
        )

    fig.update_layout(
        title=dict(
            text="Evolución de la Informalidad por Ciudad",
            font=dict(color=TEXT_COLOR, size=13),
        ),
        xaxis=dict(
            color=TEXT_MUTED,
            gridcolor=GRID_COLOR,
            title="Año",
        ),
        yaxis=dict(
            color=TEXT_MUTED,
            gridcolor=GRID_COLOR,
            title="Tasa (%)",
        ),
        paper_bgcolor=PAPER_BACKGROUND,
        plot_bgcolor=PLOT_BACKGROUND,
        font=dict(color=TEXT_COLOR),
        height=340,
        margin=dict(l=50, r=20, t=50, b=40),
        showlegend=False,
    )
    return fig