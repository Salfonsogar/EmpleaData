"""
Datos sintéticos de empleo calibrados con fuentes DANE-GEIH (2021-2026).
Valores aproximados basados en datos públicos históricos.
"""

# Tasas de empleo por ciudad y año (%) - calibradas con DANE GEIH
EMPLEO_BASE = {
    #                    2021   2022   2023   2024   2025   2026
    "Barranquilla":   [54.2,  55.8,  57.1,  58.3,  59.0,  59.7],
    "Cartagena":      [52.1,  53.4,  54.8,  55.9,  56.4,  57.1],
    "Santa Marta":    [51.8,  52.9,  54.1,  55.3,  56.0,  56.8],
    "Valledupar":     [49.3,  50.7,  52.0,  53.1,  53.9,  54.5],
    "Montería":       [48.5,  49.8,  51.2,  52.4,  53.0,  53.8],
    "Sincelejo":      [47.9,  49.1,  50.5,  51.6,  52.3,  53.0],
    "Riohacha":       [46.2,  47.6,  49.0,  50.2,  51.0,  51.8],
    "Bogotá":         [58.9,  60.5,  61.8,  63.0,  63.7,  64.4],
    "Medellín":       [57.3,  59.0,  60.4,  61.7,  62.5,  63.2],
    "Cali":           [55.1,  56.8,  58.2,  59.5,  60.2,  61.0],
    "Bucaramanga":    [56.8,  58.2,  59.5,  60.7,  61.4,  62.1],
    "Cúcuta":         [43.1,  44.5,  45.8,  46.9,  47.6,  48.3],
    "Quibdó":         [38.4,  39.5,  40.7,  41.6,  42.2,  42.9],
    "Arauca":         [41.2,  42.3,  43.5,  44.5,  45.1,  45.8],
    "Leticia":        [39.7,  40.8,  42.0,  43.0,  43.7,  44.4],
    "Pasto":          [50.2,  51.6,  52.9,  54.0,  54.7,  55.4],
}

# Desviación estándar histórica por ciudad (volatilidad)
SIGMA_BASE = {
    "Barranquilla": 1.8, "Cartagena": 2.1, "Santa Marta": 2.3,
    "Valledupar":   2.5, "Montería":  2.7, "Sincelejo":  2.8,
    "Riohacha":     3.1, "Bogotá":    1.5, "Medellín":   1.7,
    "Cali":         1.9, "Bucaramanga": 1.6, "Cúcuta":   4.2,
    "Quibdó":       4.8, "Arauca":    4.5, "Leticia":    4.6,
    "Pasto":        2.9,
}
