from dash import html
from core.theme import CARD_BACKGROUND, BORDER_COLOR, TEXT_COLOR, TEXT_MUTED


def kpi_card(titulo: str, valor: str, subtexto: str,
             color: str = "#58A6FF") -> html.Div:
    return html.Div(style={
        "backgroundColor": CARD_BACKGROUND,
        "border": f"1px solid {color}22",
        "borderLeft": f"3px solid {color}",
        "borderRadius": "6px",
        "padding": "16px 20px",
        "display": "flex",
        "flexDirection": "column",
        "justifyContent": "center",
    }, children=[
        html.Div(titulo, style={"color": TEXT_MUTED, "fontSize": "9px",
                                "letterSpacing": "1px", "marginBottom": "6px"}),
        html.Div(valor, style={"color": color, "fontSize": "28px",
                               "fontWeight": "700", "lineHeight": "1.1"}),
        html.Div(subtexto, style={"color": TEXT_MUTED, "fontSize": "9px",
                                  "marginTop": "4px"}),
    ])


def create_kpi_cards(ciudad: str, año: int, media: float, mediana: float,
                     std: float, sector: str, mu_nac: float,
                     is_outlier: bool) -> html.Div:
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
        "display": "grid",
        "gridTemplateColumns": "1fr 1fr",
        "gridTemplateRows": "1fr 1fr 1fr",
        "gap": "10px",
        "padding": "16px",
        "height": "100%",
        "boxSizing": "border-box",
    })
