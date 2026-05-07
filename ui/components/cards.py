"""
Componente de tarjetas KPI (Key Performance Indicators).
Tarjetas con métricas de empleabilidad.
"""

from dash import html
from core.theme import CARD_BACKGROUND, BORDER_COLOR, TEXT_COLOR, TEXT_MUTED


def kpi_card(titulo: str, valor: str, subtexto: str,
             color: str = "#58A6FF") -> html.Div:
    """
    Crea una tarjeta KPI individual.
    
    Args:
        titulo: Título de la métrica.
        valor: Valor a mostrar.
        subtexto: Texto descriptivo secundario.
        color: Color del borde izquierdo y valor.
        
    Returns:
        Componente html.Div con la tarjeta.
    """
    return html.Div(style={
        "backgroundColor": CARD_BACKGROUND,
        "border": f"1px solid {color}33",
        "borderLeft": f"3px solid {color}",
        "borderRadius": "6px",
        "padding": "12px 16px",
        "minWidth": "150px",
    }, children=[
        html.Div(titulo, style={"color": TEXT_MUTED, "fontSize": "10px",
                                 "letterSpacing": "1px", "marginBottom": "4px"}),
        html.Div(valor, style={"color": color, "fontSize": "22px",
                                "fontWeight": "700", "lineHeight": "1"}),
        html.Div(subtexto, style={"color": TEXT_MUTED, "fontSize": "10px",
                                   "marginTop": "4px"}),
    ])


def create_kpi_cards(ciudad: str, año: int, media: float, mediana: float,
                     std: float, sector: str, mu_nac: float, 
                     is_outlier: bool) -> html.Div:
    """
    Crea el conjunto completo de tarjetas KPI.
    
    Args:
        ciudad: Ciudad seleccionada.
        año: Año seleccionado.
        media: Media calculada.
        mediana: Mediana calculada.
        std: Desviación estándar.
        sector: Sector dominante.
        mu_nac: Media nacional.
        is_outlier: Si es outlier.
        
    Returns:
        Componente html.Div con todas las tarjetas.
    """
    from core.theme import COLOR_DANGER, COLOR_SUCCESS, COLOR_PURPLE, COLOR_WARNING, COLOR_INFO
    
    color_outlier = COLOR_DANGER if is_outlier else COLOR_SUCCESS
    outlier_label = "OUTLIER >2σ" if is_outlier else "NORMAL ±2σ"
    
    cards = [
        kpi_card("TASA EMPLEO", f"{media:.1f}%",
                 f"{ciudad} · {año}", COLOR_INFO),
        kpi_card("MEDIANA",     f"{mediana:.1f}%",
                 "Brecha desigualdad", COLOR_PURPLE),
        kpi_card("DESV. STD",   f"±{std:.2f}",
                 "Volatilidad laboral", COLOR_WARNING),
        kpi_card("SECTOR",      sector[:14],
                 "Mayor contratación", COLOR_SUCCESS),
        kpi_card("MED. NAC.",   f"{mu_nac:.1f}%",
                 f"Colombia {año}", TEXT_MUTED),
        kpi_card("ESTADO",      outlier_label,
                 f"vs. ±2σ nacional", color_outlier),
    ]
    
    return html.Div(children=cards, style={
        "display": "flex", "gap": "12px",
        "padding": "16px 32px",
        "flexWrap": "wrap",
    })
