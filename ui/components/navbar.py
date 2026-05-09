from dash import dcc, html
from data import CIUDADES
from core.constants import AÑOS, COLORES_REGION
from core.theme import CARD_BACKGROUND, BORDER_COLOR, TEXT_ACCENT, TEXT_COLOR, TEXT_MUTED, PAPER_BACKGROUND


def create_navbar() -> html.Div:
    opciones_ciudades = [{"label": c, "value": c} for c in sorted(CIUDADES.keys())]

    return html.Div(style={
        "backgroundColor": CARD_BACKGROUND,
        "borderBottom": f"1px solid {BORDER_COLOR}",
        "padding": "10px 0",
    }, children=[
        html.Div(style={
            "display": "flex", "alignItems": "center", "gap": "12px",
        }, children=[

            # ── Título (izquierda) ────────────────────────────────────────
            html.Div([
                html.H1("ANALIZADOR DE EMPLEABILIDAD NACIONAL",
                        style={"color": TEXT_ACCENT, "margin": 0,
                               "fontSize": "15px", "letterSpacing": "1px",
                               "fontWeight": "600"}),
                html.P("Colombia 2021–2026 · Modelado y Simulación Estocástica",
                       style={"color": TEXT_MUTED, "margin": "1px 0 0",
                              "fontSize": "10px", "letterSpacing": "0.3px"}),
            ], style={"flexShrink": 0}),

            # ── Spacer ────────────────────────────────────────────────────
            html.Div(style={"flex": "1", "minWidth": "16px"}),

            # ── AÑO slider (protagonista) ─────────────────────────────────
            html.Div([
                dcc.Slider(
                    id="slider-año",
                    min=2021, max=2026, step=1, value=2026,
                    marks={a: {"label": str(a),
                               "style": {"color": TEXT_MUTED, "fontSize": "9px"}}
                           for a in AÑOS},
                    tooltip={"placement": "top", "always_visible": True},
                ),
            ], style={"flex": "0 0 260px"}),

            # ── CIUDAD dropdown ───────────────────────────────────────────
            html.Div([
                html.Span("CIUDAD", style={
                    "color": TEXT_MUTED, "fontSize": "8px",
                    "letterSpacing": "1px", "display": "block",
                    "marginBottom": "2px",
                }),
                dcc.Dropdown(
                    id="dropdown-ciudad",
                    options=opciones_ciudades,
                    value="Bogotá",
                    clearable=False,
                    style={
                        "backgroundColor": PAPER_BACKGROUND,
                        "color": TEXT_COLOR,
                        "border": f"1px solid {BORDER_COLOR}",
                        "width": "160px",
                        "fontSize": "12px",
                        "minHeight": "30px",
                    },
                ),
            ]),

            # ── REGIÓN dropdown ───────────────────────────────────────────
            html.Div([
                html.Span("REGIÓN", style={
                    "color": TEXT_MUTED, "fontSize": "8px",
                    "letterSpacing": "1px", "display": "block",
                    "marginBottom": "2px",
                }),
                dcc.Dropdown(
                    id="dropdown-region",
                    options=[{"label": "Todas", "value": "Todas"}] +
                            [{"label": r, "value": r} for r in COLORES_REGION.keys()],
                    value="Todas",
                    clearable=False,
                    style={
                        "backgroundColor": PAPER_BACKGROUND,
                        "color": TEXT_COLOR,
                        "border": f"1px solid {BORDER_COLOR}",
                        "width": "160px",
                        "fontSize": "12px",
                        "minHeight": "30px",
                    },
                ),
            ]),

        ]),
    ])
