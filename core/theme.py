"""
Theme tokens para el estilo visual claro.
Centraliza todos los colores de UI para mantener consistencia visual.
"""

# Fondos
PAPER_BACKGROUND = "#F5F4F0"       # Fondo base
PLOT_BACKGROUND = "#FFFFFF"        # Área de gráfico
CARD_BACKGROUND = "#FFFFFF"        # Tarjetas/paneles
CONTROLS_BACKGROUND = "#EDECEA"    # Navbar/controles
BORDER_COLOR = "#D9D6D0"          # Borde sutil

# Tipografía
TEXT_COLOR = "#1A1814"             # Texto principal
TEXT_MUTED = "#6B6560"            # Texto secundario / labels
TEXT_DISABLED = "#A09B96"         # Texto deshabilitado / subtítulos

# Acento principal — Azul institucional
COLOR_PRIMARY = "#1B4FCC"
COLOR_PRIMARY_HOVER = "#1540A8"
COLOR_PRIMARY_LIGHT = "#E8EDFB"

# Colores semánticos
COLOR_SUCCESS = "#1A7A3C"
COLOR_DANGER = "#B81C2E"
COLOR_SUCCESS_BG = "#E6F4EB"
COLOR_DANGER_BG = "#FBEAEC"

# Gráficas
GRID_COLOR = "#E0DDD8"
NATIONAL_FILL = "rgba(200,94,0,0.13)"     # #C85E00 + 0x22 alpha
NATIONAL_LINE = "#C85E00"                  # Línea de referencia nacional

# Destacado (mapa)
HIGHLIGHT_COLOR = "#FFD700"

# Estilos de mapa (modo claro)
MAP_STYLE = "carto-positron"
MAP_CENTER_LAT = 4.5709
MAP_CENTER_LON = -74.2973
MAP_ZOOM = 4.5


def hex_to_rgba(hex_color: str, alpha_hex: int) -> str:
    """Convierte #RRGGBB a rgba() con opacidad hex (0-255).
    Uso: hex_to_rgba("#B81C2E", 0x18) -> "rgba(184,28,46,24)"
    """
    r = int(hex_color[1:3], 16)
    g = int(hex_color[3:5], 16)
    b = int(hex_color[5:7], 16)
    return f"rgba({r},{g},{b},{alpha_hex})"
