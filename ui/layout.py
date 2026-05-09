from dash import html, dcc
from core.theme import (
    PAPER_BACKGROUND, CARD_BACKGROUND, BORDER_COLOR,
    TEXT_MUTED, COLOR_PRIMARY,
)
from ui.components.navbar import create_navbar


def _section_container(children, style_extra=None):
    base = {
        "backgroundColor": CARD_BACKGROUND,
        "borderRadius": "8px",
        "border": f"1px solid {BORDER_COLOR}",
        "overflow": "hidden",
    }
    if style_extra:
        base.update(style_extra)
    return html.Div(children=children, style=base)


def create_layout() -> html.Div:
    return html.Div(
        style={
            "backgroundColor": PAPER_BACKGROUND,
            "minHeight": "100vh",
            "fontFamily": "'IBM Plex Mono', 'Courier New', monospace",
        },
        children=[

            html.Div(style={
                "maxWidth": "1200px",
                "margin": "0 auto",
                "padding": "0 24px",
            }, children=[

                # ── TOP BAR (header + controles integrados) ─────────────
                create_navbar(),

                # ── FILA 1: MAPA (60%) + KPIs (40%) ────────────────────
                html.Div(style={
                    "marginTop": "20px",
                    "display": "flex", "gap": "20px",
                    "alignItems": "stretch",
                }, children=[

                    _section_container(
                        dcc.Graph(id="mapa-colombia",
                                  config={"displayModeBar": False}),
                        style_extra={"flex": "3"},
                    ),

                    _section_container(
                        html.Div(id="kpi-cards", style={"height": "100%"}),
                        style_extra={"flex": "2", "height": "440px"},
                    ),
                ]),

                # ── FILA 2: RANKING (full width, standalone) ─────────────
                html.Div(style={
                    "marginTop": "20px",
                }, children=[
                    _section_container(
                        dcc.Graph(id="grafica-ranking",
                                  config={"displayModeBar": False}),
                    ),
                    html.Span(
                        "[Top 5]",
                        id="toggle-ranking",
                        n_clicks=0,
                        style={
                            "color": TEXT_MUTED,
                            "fontSize": "10px",
                            "cursor": "pointer",
                            "textAlign": "right",
                            "padding": "4px 4px 0",
                            "userSelect": "none",
                            "display": "block",
                        },
                    ),
                ]),

                # ── FILA 3: GAUSS (2/3) + TREND (1/3) ─────────────────
                html.Div(style={
                    "marginTop": "20px",
                    "display": "flex", "gap": "16px",
                    "alignItems": "stretch",
                }, children=[

                    _section_container(
                        dcc.Graph(id="grafica-gauss",
                                  config={"displayModeBar": False}),
                        style_extra={"flex": "2"},
                    ),

                    _section_container(
                        dcc.Graph(id="grafica-tendencia",
                                  config={"displayModeBar": False}),
                        style_extra={"flex": "1"},
                    ),
                ]),

                # ── FILA 4: CORRELACIÓN FRONTERIZA (colapsable) ─────────
                html.Div(style={
                    "marginTop": "20px",
                }, children=[

                    html.Div(
                        "▶ Ver an\u00e1lisis de correlaci\u00f3n fronteriza (+0.5)",
                        id="toggle-correlacion",
                        n_clicks=0,
                        style={
                            "color": COLOR_PRIMARY,
                            "fontSize": "11px",
                            "letterSpacing": "0.5px",
                            "cursor": "pointer",
                            "userSelect": "none",
                            "padding": "8px 12px",
                            "backgroundColor": CARD_BACKGROUND,
                            "borderRadius": "6px",
                            "border": f"1px solid {BORDER_COLOR}",
                            "display": "inline-block",
                        },
                    ),

                    html.Div(
                        id="contenido-correlacion",
                        style={"display": "none", "marginTop": "12px"},
                        children=[
                            _section_container(
                                dcc.Graph(id="grafica-correlacion",
                                          config={"displayModeBar": False}),
                            ),
                        ],
                    ),
                ]),

                # ── FOOTER ─────────────────────────────────────────────
                html.Div(style={
                    "borderTop": f"1px solid {BORDER_COLOR}",
                    "padding": "16px 0",
                    "marginTop": "32px",
                    "textAlign": "center",
                }, children=[
                    html.Span(
                        "Modelado y Simulación · Docente: Andrés Perpiñán Reyes · "
                        "Fuentes: DANE-GEIH / Datos Abiertos Colombia / SISRPO-MinSalud",
                        style={"color": TEXT_MUTED, "fontSize": "10px"},
                    ),
                ]),

            ]),
        ]
    )
