# Visualización de ranking de ciudades por tasa de empleo.
# Gráfico de barras horizontal ordenado de mayor a menor.


from typing import List, Optional, Tuple

import plotly.graph_objects as go

from core.constants import AÑOS, COLORES_REGION
from core.theme import (
    BORDER_COLOR,
    COLOR_WARNING,
    PAPER_BACKGROUND,
    PLOT_BACKGROUND,
    TEXT_COLOR,
)
from data import CIUDADES, EMPLEO_BASE
from services.estadisticas_service import calcular_media_nacional


# Genera gráfico de barras horizontal con ranking de ciudades.
def figura_ranking(año: int, top_n: Optional[int] = None) -> go.Figure:

    idx = AÑOS.index(año)
    datos = sorted(
        [(c, EMPLEO_BASE[c][idx], CIUDADES[c]["region"]) for c in CIUDADES],
        key=lambda x: x[1],
        reverse=True,
    )
    if top_n:
        datos = datos[:top_n]
    ciudades_ord = [d[0] for d in datos]
    tasas_ord = [d[1] for d in datos]
    colores_ord = [COLORES_REGION[d[2]] for d in datos]

    mu_nac, _ = calcular_media_nacional(año)

    fig = go.Figure(
        go.Bar(
            x=tasas_ord,
            y=ciudades_ord,
            orientation="h",
            marker=dict(
                color=colores_ord,
                opacity=0.85,
                line=dict(color="rgba(255,255,255,0.15)", width=0.5),
            ),
            text=[f"{t:.1f}%" for t in tasas_ord],
            textposition="outside",
            textfont=dict(color=TEXT_COLOR, size=10),
            hovertemplate="%{y}: %{x:.1f}%<extra></extra>",
        )
    )
    fig.add_vline(
        x=mu_nac,
        line=dict(color=COLOR_WARNING, dash="dash", width=1.5),
        annotation_text=f"Nacional {mu_nac:.1f}%",
        annotation_font=dict(color=COLOR_WARNING, size=10),
    )

    fig.update_layout(
        title=dict(
            text=f"Ranking Empleabilidad {año}", font=dict(color=TEXT_COLOR, size=13)
        ),
        xaxis=dict(
            range=[30, 75], color="#8B949E", gridcolor="#21262D", title="Tasa (%)"
        ),
        yaxis=dict(color="#8B949E"),
        paper_bgcolor=PAPER_BACKGROUND,
        plot_bgcolor=PLOT_BACKGROUND,
        font=dict(color=TEXT_COLOR),
        height=340,
        margin=dict(l=120, r=60, t=50, b=40),
    )
    return fig
