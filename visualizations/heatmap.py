"""
Heatmap de evolución temporal de tasas de empleo por ciudad.
"""

import plotly.graph_objects as go
import numpy as np

from core.constants import AÑOS
from core.theme import (
    COLOR_PRIMARY,
    PAPER_BACKGROUND,
    TEXT_COLOR,
    TEXT_MUTED,
)
from data import CIUDADES, EMPLEO_BASE


def figura_heatmap(ciudad_seleccionada: str) -> go.Figure:
    ciudades_ordenadas = sorted(
        CIUDADES.keys(),
        key=lambda c: np.mean([v for v in EMPLEO_BASE[c] if v is not None]),
        reverse=True
    )

    matrix = []
    for ciudad in ciudades_ordenadas:
        row = [EMPLEO_BASE[ciudad][AÑOS.index(año)] for año in AÑOS]
        matrix.append(row)

    texto_matrix = []
    for i, ciudad in enumerate(ciudades_ordenadas):
        row_text = []
        for j, año in enumerate(AÑOS):
            val = matrix[i][j]
            marker = "★" if ciudad == ciudad_seleccionada else ""
            if val is None:
                row_text.append(f"{marker}—")
            else:
                row_text.append(f"{marker}{val:.1f}%")
        texto_matrix.append(row_text)

    colorscale = [
        [0, "#e74c3c"],
        [0.3, "#f39c12"],
        [0.5, "#f1c40f"],
        [0.7, "#2ecc71"],
        [1, "#27ae60"]
    ]

    fig = go.Figure(
        go.Heatmap(
            z=matrix,
            x=AÑOS,
            y=ciudades_ordenadas,
            text=texto_matrix,
            texttemplate="%{text}",
            textfont=dict(color="black", size=9),
            colorscale=colorscale,
            showscale=True,
            colorbar=dict(
                title=dict(text="Tasa %", side="right", font=dict(color=TEXT_MUTED, size=10)),
                tickfont=dict(color=TEXT_MUTED, size=9),
            ),
            hovertemplate="Ciudad: %{y}<br>Año: %{x}<br>Tasa: %{z:.1f}%<extra></extra>",
            zmin=35,
            zmax=70,
        )
    )

    for i, ciudad in enumerate(ciudades_ordenadas):
        if ciudad == ciudad_seleccionada:
            fig.add_hline(
                y=ciudad,
                line=dict(color=COLOR_PRIMARY, width=3),
                opacity=0.8,
            )

    fig.update_layout(
        title=dict(
            text="Evolución Temporal de Empleo (2021-2026)",
            font=dict(color=TEXT_COLOR, size=13)
        ),
        xaxis=dict(
            color=TEXT_MUTED,
            title="Año",
        ),
        yaxis=dict(
            color=TEXT_MUTED,
            tickmode="linear",
        ),
        paper_bgcolor=PAPER_BACKGROUND,
        font=dict(color=TEXT_COLOR),
        height=400,
        margin=dict(l=100, r=60, t=50, b=40),
    )

    return fig