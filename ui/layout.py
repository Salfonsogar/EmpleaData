"""
Layout principal de la aplicación Dash.
Ensambla todos los componentes UI en la estructura final.
"""

from dash import html, dcc
from data import CIUDADES
from core.theme import PAPER_BACKGROUND, BORDER_COLOR, TEXT_MUTED
from ui.components.navbar import create_navbar
from ui.components.controls import create_controls
from ui.components.cards import create_kpi_cards


def create_layout() -> html.Div:
    """
    Crea el layout completo de la aplicación.
    
    Returns:
        Componente html.Div con toda la UI ensamblada.
    """
    return html.Div(
        style={"backgroundColor": PAPER_BACKGROUND, "minHeight": "100vh",
               "fontFamily": "'IBM Plex Mono', 'Courier New', monospace"},
        children=[

            # ── HEADER ──────────────────────────────────────────────────────────
            create_navbar(),

            # ── CONTROLES ───────────────────────────────────────────────────────
            create_controls(),

            # ── TARJETAS KPI (se actualizan por callback) ────────────────────
            html.Div(id="kpi-cards", style={
                "display": "flex", "gap": "12px",
                "padding": "16px 32px",
                "flexWrap": "wrap",
            }),

            # ── MAPA + GAUSS ────────────────────────────────────────────────────
            html.Div(style={"display": "flex", "gap": "12px",
                            "padding": "0 32px 12px",
                            "alignItems": "flex-start"}, children=[
                html.Div(
                    dcc.Graph(id="mapa-colombia", config={"displayModeBar": False}),
                    style={"flex": "1", "backgroundColor": "#161B22",
                           "borderRadius": "8px", "border": f"1px solid {BORDER_COLOR}",
                           "overflow": "hidden"},
                ),
                html.Div(style={"flex": "0 0 420px", "display": "flex",
                                "flexDirection": "column", "gap": "12px"}, children=[
                    html.Div(
                        dcc.Graph(id="grafica-gauss", config={"displayModeBar": False}),
                        style={"backgroundColor": "#161B22", "borderRadius": "8px",
                               "border": f"1px solid {BORDER_COLOR}"},
                    ),
                    html.Div(
                        dcc.Graph(id="grafica-tendencia",
                                  config={"displayModeBar": False}),
                        style={"backgroundColor": "#161B22", "borderRadius": "8px",
                               "border": f"1px solid {BORDER_COLOR}"},
                    ),
                ]),
            ]),

            # ── RANKING + CORRELACIÓN ───────────────────────────────────────────
            html.Div(style={"display": "flex", "gap": "12px",
                            "padding": "0 32px 24px",
                            "alignItems": "flex-start"}, children=[
                html.Div(
                    dcc.Graph(id="grafica-ranking", config={"displayModeBar": False}),
                    style={"flex": "1", "backgroundColor": "#161B22",
                           "borderRadius": "8px", "border": f"1px solid {BORDER_COLOR}"},
                ),
                html.Div(
                    dcc.Graph(id="grafica-correlacion",
                              config={"displayModeBar": False}),
                    style={"flex": "2", "backgroundColor": "#161B22",
                           "borderRadius": "8px",
                           "border": f"1px solid {BORDER_COLOR}"},
                ),
            ]),

            # ── FOOTER ──────────────────────────────────────────────────────────
            html.Div(style={
                "borderTop": f"1px solid {BORDER_COLOR}",
                "padding": "12px 32px",
                "display": "flex", "justifyContent": "space-between",
            }, children=[
                html.Span("Modelado y Simulación · Docente: Andrés Perpiñán Reyes",
                          style={"color": TEXT_MUTED, "fontSize": "11px"}),
                html.Span("Fuentes: DANE-GEIH · Datos Abiertos Colombia · SISRPO-MinSalud",
                          style={"color": TEXT_MUTED, "fontSize": "11px"}),
            ]),
        ]
    )
