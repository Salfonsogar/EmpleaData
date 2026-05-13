"""
Visualización de sectores económicos DANE-GEIH (datos nacionales oficiales).
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

COLORES_SECTORES = [
    "#2E86AB", "#A23B72", "#F18F01", "#C73E1D", "#3B1F2B",
    "#95C623", "#6B2737", "#1B998B", "#F24C4C", "#5F0F40",
    "#9A031E", "#FB8B24",
]


def figura_dane_sectores(año_seleccionado: int = 2024) -> go.Figure:
    """
    Genera 2 gráficos:
    - Izquierda: participación % por sector (barras horizontales) para año seleccionado
    - Derecha: evolución temporal de participación % por sector (líneas)
    """
    from data.sources.dane_geih_sectores import cargar_ocupados_sector

    df_pct = cargar_ocupados_sector(como_porcentaje=True)
    df_abs = cargar_ocupados_sector(como_porcentaje=False)

    if año_seleccionado not in df_pct.columns:
        año_seleccionado = max(df_pct.columns)

    sector_año = df_pct[año_seleccionado].sort_values(ascending=True)

    fig = make_subplots(
        rows=1, cols=2,
        column_widths=[0.45, 0.55],
        specs=[[{"type": "bar"}, {"type": "scatter"}]],
        subplot_titles=(
            f"Participación por sector - Nacional ({año_seleccionado})",
            "Evolución temporal - Nacional (%)"
        )
    )

    fig.add_trace(
        go.Bar(
            y=sector_año.index,
            x=sector_año.values,
            orientation="h",
            marker=dict(
                color=COLORES_SECTORES[:len(sector_año)],
                opacity=0.85,
            ),
            text=[f"{v:.1f}%" for v in sector_año.values],
            textposition="outside",
            textfont=dict(color=TEXT_COLOR, size=9),
            hovertemplate="%{y}: %{x:.1f}%<extra></extra>",
        ),
        row=1, col=1
    )

    años = [c for c in df_pct.columns if isinstance(c, int)]
    sectores_top = sector_año.tail(5).index.tolist()

    for i, sector in enumerate(sectores_top):
        fig.add_trace(
            go.Scatter(
                x=años,
                y=df_pct.loc[sector, años].values,
                mode="lines+markers",
                name=sector[:20],
                line=dict(width=2, color=COLORES_SECTORES[i % len(COLORES_SECTORES)]),
                marker=dict(size=6),
                hovertemplate=f"{sector}: %{{y:.1f}}%<extra></extra>",
            ),
            row=1, col=2
        )

    fig.update_layout(
        paper_bgcolor=PAPER_BACKGROUND,
        plot_bgcolor=PLOT_BACKGROUND,
        font=dict(color=TEXT_COLOR, size=10),
        height=340,
        margin=dict(l=20, r=20, t=50, b=40),
        showlegend=True,
        legend=dict(
            orientation="h",
            yanchor="bottom",
            y=-0.15,
            xanchor="center",
            x=0.55,
            font=dict(size=9),
        ),
    )

    fig.update_xaxes(title_text="% Participación", color=TEXT_MUTED, gridcolor=GRID_COLOR, row=1, col=1)
    fig.update_yaxes(color=TEXT_MUTED, row=1, col=1)

    fig.update_xaxes(title_text="Año", color=TEXT_MUTED, gridcolor=GRID_COLOR, row=1, col=2)
    fig.update_yaxes(title_text="% Participación", color=TEXT_MUTED, gridcolor=GRID_COLOR, row=1, col=2)

    return fig


def get_tabla_resumen_dane() -> str:
    """Retorna resumen textual de los datos DANE."""
    from data.sources.dane_geih_sectores import cargar_ocupados_sector, total_ocupados_nacional

    df = cargar_ocupados_sector()
    df_pct = cargar_ocupados_sector(como_porcentaje=True)

    lines = ["**Resumen Sectores DANE-GEIH (miles de ocupados)**"]
    lines.append("")

    for año in sorted(df.columns):
        total = total_ocupados_nacional(año)
        if total:
            lines.append(f"**{año}**: {total:,} miles de ocupados")
            top3 = df_pct[año].nlargest(3)
            lines.append(f"   Top 3: {', '.join([f'{s[:15]} ({v:.1f}%)' for s, v in top3.items()])}")
            lines.append("")

    return "\n".join(lines)