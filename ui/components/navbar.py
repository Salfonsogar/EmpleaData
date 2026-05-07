"""
Componente Navbar (Header) de la aplicación.
Barra superior con título, subtítulo y badges de fuentes de datos.
"""

from dash import html
from core.theme import PAPER_BACKGROUND, BORDER_COLOR, TEXT_ACCENT, COLOR_SUCCESS, COLOR_INFO


def create_navbar() -> html.Div:
    """
    Crea el navbar principal de la aplicación.
    
    Returns:
        Componente html.Div con el header.
    """
    return html.Div(style={
        "background": "linear-gradient(135deg, #161B22 0%, #0D1117 60%)",
        "borderBottom": f"1px solid {BORDER_COLOR}",
        "padding": "20px 32px 16px",
    }, children=[
        html.Div(style={"display": "flex", "alignItems": "center",
                        "gap": "16px"}, children=[
            html.Div("📊", style={"fontSize": "32px"}),
            html.Div([
                html.H1("ANALIZADOR DE EMPLEABILIDAD NACIONAL",
                        style={"color": TEXT_ACCENT, "margin": 0,
                               "fontSize": "20px", "letterSpacing": "2px",
                               "fontWeight": "700"}),
                html.P("Colombia 2021–2026 · Modelado y Simulación Estocástica",
                       style={"color": "#8B949E", "margin": 0,
                              "fontSize": "12px", "letterSpacing": "1px"}),
            ]),
            html.Div(style={"marginLeft": "auto", "textAlign": "right"}, children=[
                html.Span("DANE-GEIH", style={
                    "background": f"{COLOR_INFO}22",
                    "color": COLOR_INFO,
                    "border": f"1px solid {COLOR_INFO}",
                    "borderRadius": "4px",
                    "padding": "3px 8px",
                    "fontSize": "10px",
                    "marginRight": "6px",
                }),
                html.Span("Datos Abiertos CO", style={
                    "background": f"{COLOR_SUCCESS}22",
                    "color": COLOR_SUCCESS,
                    "border": f"1px solid {COLOR_SUCCESS}",
                    "borderRadius": "4px",
                    "padding": "3px 8px",
                    "fontSize": "10px",
                }),
            ]),
        ]),
    ])
