"""
Componente de controles (sliders y dropdowns).
Permite seleccionar año, ciudad y región.
"""

from dash import dcc, html
from data import CIUDADES
from core.constants import AÑOS, COLORES_REGION
from core.theme import PAPER_BACKGROUND, BORDER_COLOR, TEXT_COLOR, TEXT_MUTED


def create_controls() -> html.Div:
    opciones_ciudades = [{"label": c, "value": c} for c in sorted(CIUDADES.keys())]

    return html.Div(style={
        "display": "flex", "gap": "16px", "padding": "16px 0",
        "alignItems": "center", "flexWrap": "wrap",
        "borderBottom": f"1px solid {BORDER_COLOR}",
    }, children=[
        html.Div([
            html.Label("AÑO", style={"color": TEXT_MUTED, "fontSize": "10px",
                                     "letterSpacing": "1px", "display": "block",
                                     "marginBottom": "4px"}),
            dcc.Slider(
                id="slider-año",
                min=2021, max=2026, step=1,
                value=2026,
                marks={a: {"label": str(a),
                           "style": {"color": TEXT_MUTED, "fontSize": "11px"}}
                       for a in AÑOS},
                tooltip={"placement": "bottom", "always_visible": False},
            ),
        ], style={"flex": "0 0 320px"}),

        html.Div([
            html.Label("CIUDAD", style={"color": TEXT_MUTED, "fontSize": "10px",
                                        "letterSpacing": "1px", "display": "block",
                                        "marginBottom": "4px"}),
            dcc.Dropdown(
                id="dropdown-ciudad",
                options=opciones_ciudades,
                value="Bogotá",
                clearable=False,
                style={"backgroundColor": PAPER_BACKGROUND, "color": TEXT_COLOR,
                       "border": f"1px solid {BORDER_COLOR}", "width": "200px"},
            ),
        ]),

        html.Div([
            html.Label("REGIÓN", style={"color": TEXT_MUTED, "fontSize": "10px",
                                        "letterSpacing": "1px", "display": "block",
                                        "marginBottom": "4px"}),
            dcc.Dropdown(
                id="dropdown-region",
                options=[{"label": "Todas", "value": "Todas"}] +
                        [{"label": r, "value": r}
                         for r in COLORES_REGION.keys()],
                value="Todas",
                clearable=False,
                style={"backgroundColor": PAPER_BACKGROUND, "color": TEXT_COLOR,
                       "border": f"1px solid {BORDER_COLOR}", "width": "200px"},
            ),
        ]),
    ])
