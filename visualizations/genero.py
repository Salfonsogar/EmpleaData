"""
Visualización de brecha de género por ciudad.
Gráfico de barras horizontales mostrando % de participación femenina.
"""

import plotly.graph_objects as go

from core.theme import (
    BORDER_COLOR,
    GRID_COLOR,
    PAPER_BACKGROUND,
    PLOT_BACKGROUND,
    TEXT_COLOR,
    TEXT_MUTED,
    COLOR_PRIMARY,
)
from data.sectores import GENERO_POR_CIUDAD, get_promedio_nacional_genero


def figura_genero(ciudad_seleccionada: str) -> go.Figure:
    ciudades_ordenadas = sorted(
        GENERO_POR_CIUDAD.items(),
        key=lambda x: x[1],
        reverse=True
    )

    ciudades = [c[0] for c in ciudades_ordenadas]
    pct_mujeres = [c[1] * 100 for c in ciudades_ordenadas]
    promedio_nac = get_promedio_nacional_genero() * 100

    colores = []
    for c in ciudades:
        if c == ciudad_seleccionada:
            colores.append(COLOR_PRIMARY)
        elif c == "Bogotá":
            colores.append("#3498db")
        else:
            colores.append("#7f8c8d")

    fig = go.Figure(
        go.Bar(
            x=pct_mujeres,
            y=ciudades,
            orientation="h",
            marker=dict(
                color=colores,
                opacity=0.85,
                line=dict(color="rgba(0,0,0,0.08)", width=0.5),
            ),
            text=[f"{p:.1f}%" for p in pct_mujeres],
            textposition="outside",
            textfont=dict(color=TEXT_COLOR, size=9),
            hovertemplate="%{y}: %{x:.1f}% mujeres<extra></extra>",
        )
    )

    fig.add_vline(
        x=promedio_nac,
        line=dict(color="#e74c3c", dash="dash", width=2),
        annotation_text=f"Nacional: {promedio_nac:.1f}%",
        annotation_font=dict(color="#e74c3c", size=10),
        annotation_position="top",
    )

    fig.update_layout(
        title=dict(
            text="Participación Laboral Femenina por Ciudad",
            font=dict(color=TEXT_COLOR, size=13)
        ),
        xaxis=dict(
            range=[20, 55],
            color=TEXT_MUTED,
            gridcolor=GRID_COLOR,
            title="% Mujeresempleadas"
        ),
        yaxis=dict(color=TEXT_MUTED),
        paper_bgcolor=PAPER_BACKGROUND,
        plot_bgcolor=PLOT_BACKGROUND,
        font=dict(color=TEXT_COLOR),
        height=360,
        margin=dict(l=100, r=40, t=50, b=40),
        showlegend=False,
    )

    return fig