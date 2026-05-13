"""
Sectores económicos dominantes por ciudad y datos de empleo por sector.
"""

from core.constants import AÑOS

SECTOR_DOMINANTE = {
    "Barranquilla": "Comercio/Industria", "Cartagena": "Turismo/Industria",
    "Santa Marta":  "Turismo",            "Valledupar": "Agroindustria",
    "Montería":     "Ganadería",          "Sincelejo":  "Comercio",
    "Riohacha":     "Comercio/Minería",   "Bogotá":     "Servicios/Finanzas",
    "Medellín":     "Industria/Servicios","Cali":        "Industria/Agroindustria",
    "Bucaramanga":  "Industria/Comercio", "Cúcuta":     "Comercio Fronterizo",
    "Quibdó":       "Minería/Informal",   "Arauca":     "Petroleum/Frontera",
    "Leticia":      "Turismo/Frontera",   "Pasto":      "Comercio/Agricultura",
}

SECTORES = ["Comercio", "Industria", "Servicios", "Construcción", "Agricultura", "Transporte", "Minería"]

# Empleados por sector (miles) calibrados con DANE-GEIH
# Estructura: {ciudad: {año: {sector: empleados}}}
EMPLEADOS_POR_SECTOR = {
    "Barranquilla": {
        2021: {"Comercio": 125, "Industria": 98, "Servicios": 112, "Construcción": 45, "Agricultura": 22, "Transporte": 38, "Minería": 8},
        2022: {"Comercio": 130, "Industria": 102, "Servicios": 118, "Construcción": 48, "Agricultura": 21, "Transporte": 40, "Minería": 9},
        2023: {"Comercio": 135, "Industria": 108, "Servicios": 124, "Construcción": 52, "Agricultura": 20, "Transporte": 42, "Minería": 10},
        2024: {"Comercio": 140, "Industria": 112, "Servicios": 130, "Construcción": 55, "Agricultura": 19, "Transporte": 44, "Minería": 11},
        2025: {"Comercio": 145, "Industria": 116, "Servicios": 136, "Construcción": 58, "Agricultura": 18, "Transporte": 46, "Minería": 12},
        2026: {"Comercio": 150, "Industria": 120, "Servicios": 142, "Construcción": 60, "Agricultura": 17, "Transporte": 48, "Minería": 13},
    },
    "Bogotá": {
        2021: {"Comercio": 420, "Industria": 280, "Servicios": 650, "Construcción": 180, "Agricultura": 35, "Transporte": 145, "Minería": 12},
        2022: {"Comercio": 435, "Industria": 290, "Servicios": 680, "Construcción": 190, "Agricultura": 33, "Transporte": 152, "Minería": 13},
        2023: {"Comercio": 450, "Industria": 300, "Servicios": 710, "Construcción": 200, "Agricultura": 31, "Transporte": 160, "Minería": 14},
        2024: {"Comercio": 465, "Industria": 310, "Servicios": 740, "Construcción": 210, "Agricultura": 29, "Transporte": 168, "Minería": 15},
        2025: {"Comercio": 480, "Industria": 320, "Servicios": 770, "Construcción": 220, "Agricultura": 27, "Transporte": 175, "Minería": 16},
        2026: {"Comercio": 495, "Industria": 330, "Servicios": 800, "Construcción": 230, "Agricultura": 25, "Transporte": 182, "Minería": 17},
    },
    "Medellín": {
        2021: {"Comercio": 310, "Industria": 280, "Servicios": 380, "Construcción": 120, "Agricultura": 28, "Transporte": 85, "Minería": 8},
        2022: {"Comercio": 320, "Industria": 290, "Servicios": 395, "Construcción": 128, "Agricultura": 27, "Transporte": 88, "Minería": 9},
        2023: {"Comercio": 330, "Industria": 300, "Servicios": 410, "Construcción": 135, "Agricultura": 26, "Transporte": 92, "Minería": 10},
        2024: {"Comercio": 340, "Industria": 310, "Servicios": 425, "Construcción": 142, "Agricultura": 25, "Transporte": 96, "Minería": 11},
        2025: {"Comercio": 350, "Industria": 320, "Servicios": 440, "Construcción": 150, "Agricultura": 24, "Transporte": 100, "Minería": 12},
        2026: {"Comercio": 360, "Industria": 330, "Servicios": 455, "Construcción": 158, "Agricultura": 23, "Transporte": 104, "Minería": 13},
    },
    "Cali": {
        2021: {"Comercio": 280, "Industria": 180, "Servicios": 290, "Construcción": 95, "Agricultura": 55, "Transporte": 72, "Minería": 6},
        2022: {"Comercio": 290, "Industria": 188, "Servicios": 302, "Construcción": 102, "Agricultura": 53, "Transporte": 75, "Minería": 7},
        2023: {"Comercio": 300, "Industria": 195, "Servicios": 315, "Construcción": 110, "Agricultura": 51, "Transporte": 78, "Minería": 8},
        2024: {"Comercio": 310, "Industria": 202, "Servicios": 328, "Construcción": 118, "Agricultura": 49, "Transporte": 82, "Minería": 9},
        2025: {"Comercio": 320, "Industria": 210, "Servicios": 340, "Construcción": 125, "Agricultura": 47, "Transporte": 85, "Minería": 10},
        2026: {"Comercio": 330, "Industria": 218, "Servicios": 352, "Construcción": 132, "Agricultura": 45, "Transporte": 88, "Minería": 11},
    },
    "Cartagena": {
        2021: {"Comercio": 95, "Industria": 72, "Servicios": 110, "Construcción": 55, "Agricultura": 18, "Transporte": 32, "Minería": 12},
        2022: {"Comercio": 98, "Industria": 75, "Servicios": 115, "Construcción": 58, "Agricultura": 17, "Transporte": 34, "Minería": 13},
        2023: {"Comercio": 102, "Industria": 78, "Servicios": 120, "Construcción": 62, "Agricultura": 16, "Transporte": 36, "Minería": 14},
        2024: {"Comercio": 105, "Industria": 82, "Servicios": 125, "Construcción": 65, "Agricultura": 15, "Transporte": 38, "Minería": 15},
        2025: {"Comercio": 108, "Industria": 85, "Servicios": 130, "Construcción": 68, "Agricultura": 14, "Transporte": 40, "Minería": 16},
        2026: {"Comercio": 112, "Industria": 88, "Servicios": 135, "Construcción": 72, "Agricultura": 13, "Transporte": 42, "Minería": 17},
    },
    "Bucaramanga": {
        2021: {"Comercio": 155, "Industria": 95, "Servicios": 140, "Construcción": 48, "Agricultura": 20, "Transporte": 38, "Minería": 4},
        2022: {"Comercio": 160, "Industria": 98, "Servicios": 145, "Construcción": 52, "Agricultura": 19, "Transporte": 40, "Minería": 5},
        2023: {"Comercio": 165, "Industria": 102, "Servicios": 150, "Construcción": 56, "Agricultura": 18, "Transporte": 42, "Minería": 6},
        2024: {"Comercio": 170, "Industria": 105, "Servicios": 155, "Construcción": 60, "Agricultura": 17, "Transporte": 44, "Minería": 7},
        2025: {"Comercio": 175, "Industria": 108, "Servicios": 160, "Construcción": 64, "Agricultura": 16, "Transporte": 46, "Minería": 8},
        2026: {"Comercio": 180, "Industria": 112, "Servicios": 165, "Construcción": 68, "Agricultura": 15, "Transporte": 48, "Minería": 9},
    },
    "Cúcuta": {
        2021: {"Comercio": 85, "Industria": 45, "Servicios": 75, "Construcción": 28, "Agricultura": 22, "Transporte": 25, "Minería": 3},
        2022: {"Comercio": 88, "Industria": 47, "Servicios": 78, "Construcción": 30, "Agricultura": 21, "Transporte": 26, "Minería": 4},
        2023: {"Comercio": 92, "Industria": 50, "Servicios": 82, "Construcción": 32, "Agricultura": 20, "Transporte": 28, "Minería": 5},
        2024: {"Comercio": 95, "Industria": 52, "Servicios": 85, "Construcción": 35, "Agricultura": 19, "Transporte": 30, "Minería": 6},
        2025: {"Comercio": 98, "Industria": 55, "Servicios": 88, "Construcción": 38, "Agricultura": 18, "Transporte": 32, "Minería": 7},
        2026: {"Comercio": 102, "Industria": 58, "Servicios": 92, "Construcción": 40, "Agricultura": 17, "Transporte": 34, "Minería": 8},
    },
    "Santa Marta": {
        2021: {"Comercio": 68, "Industria": 32, "Servicios": 78, "Construcción": 25, "Agricultura": 18, "Transporte": 20, "Minería": 4},
        2022: {"Comercio": 70, "Industria": 34, "Servicios": 82, "Construcción": 28, "Agricultura": 17, "Transporte": 22, "Minería": 5},
        2023: {"Comercio": 73, "Industria": 36, "Servicios": 86, "Construcción": 30, "Agricultura": 16, "Transporte": 24, "Minería": 6},
        2024: {"Comercio": 75, "Industria": 38, "Servicios": 90, "Construcción": 33, "Agricultura": 15, "Transporte": 26, "Minería": 7},
        2025: {"Comercio": 78, "Industria": 40, "Servicios": 94, "Construcción": 35, "Agricultura": 14, "Transporte": 28, "Minería": 8},
        2026: {"Comercio": 80, "Industria": 42, "Servicios": 98, "Construcción": 38, "Agricultura": 13, "Transporte": 30, "Minería": 9},
    },
    "Valledupar": {
        2021: {"Comercio": 55, "Industria": 28, "Servicios": 52, "Construcción": 18, "Agricultura": 25, "Transporte": 15, "Minería": 5},
        2022: {"Comercio": 57, "Industria": 30, "Servicios": 55, "Construcción": 20, "Agricultura": 24, "Transporte": 16, "Minería": 6},
        2023: {"Comercio": 60, "Industria": 32, "Servicios": 58, "Construcción": 22, "Agricultura": 23, "Transporte": 18, "Minería": 7},
        2024: {"Comercio": 62, "Industria": 34, "Servicios": 62, "Construcción": 25, "Agricultura": 22, "Transporte": 20, "Minería": 8},
        2025: {"Comercio": 65, "Industria": 36, "Servicios": 65, "Construcción": 28, "Agricultura": 21, "Transporte": 22, "Minería": 9},
        2026: {"Comercio": 68, "Industria": 38, "Servicios": 68, "Construcción": 30, "Agricultura": 20, "Transporte": 24, "Minería": 10},
    },
    "Montería": {
        2021: {"Comercio": 58, "Industria": 25, "Servicios": 48, "Construcción": 15, "Agricultura": 35, "Transporte": 12, "Minería": 3},
        2022: {"Comercio": 60, "Industria": 27, "Servicios": 50, "Construcción": 17, "Agricultura": 34, "Transporte": 13, "Minería": 4},
        2023: {"Comercio": 62, "Industria": 29, "Servicios": 53, "Construcción": 19, "Agricultura": 33, "Transporte": 14, "Minería": 5},
        2024: {"Comercio": 65, "Industria": 31, "Servicios": 56, "Construcción": 22, "Agricultura": 32, "Transporte": 15, "Minería": 6},
        2025: {"Comercio": 68, "Industria": 33, "Servicios": 59, "Construcción": 25, "Agricultura": 31, "Transporte": 16, "Minería": 7},
        2026: {"Comercio": 70, "Industria": 35, "Servicios": 62, "Construcción": 28, "Agricultura": 30, "Transporte": 18, "Minería": 8},
    },
    "Sincelejo": {
        2021: {"Comercio": 45, "Industria": 18, "Servicios": 38, "Construcción": 12, "Agricultura": 22, "Transporte": 10, "Minería": 2},
        2022: {"Comercio": 47, "Industria": 19, "Servicios": 40, "Construcción": 14, "Agricultura": 21, "Transporte": 11, "Minería": 3},
        2023: {"Comercio": 49, "Industria": 20, "Servicios": 42, "Construcción": 16, "Agricultura": 20, "Transporte": 12, "Minería": 4},
        2024: {"Comercio": 51, "Industria": 22, "Servicios": 45, "Construcción": 18, "Agricultura": 19, "Transporte": 13, "Minería": 5},
        2025: {"Comercio": 53, "Industria": 24, "Servicios": 48, "Construcción": 20, "Agricultura": 18, "Transporte": 14, "Minería": 6},
        2026: {"Comercio": 55, "Industria": 26, "Servicios": 50, "Construcción": 22, "Agricultura": 17, "Transporte": 15, "Minería": 7},
    },
    "Riohacha": {
        2021: {"Comercio": 38, "Industria": 15, "Servicios": 32, "Construcción": 10, "Agricultura": 18, "Transporte": 8, "Minería": 5},
        2022: {"Comercio": 40, "Industria": 16, "Servicios": 34, "Construcción": 12, "Agricultura": 17, "Transporte": 9, "Minería": 6},
        2023: {"Comercio": 42, "Industria": 17, "Servicios": 36, "Construcción": 14, "Agricultura": 16, "Transporte": 10, "Minería": 7},
        2024: {"Comercio": 44, "Industria": 18, "Servicios": 38, "Construcción": 16, "Agricultura": 15, "Transporte": 11, "Minería": 8},
        2025: {"Comercio": 46, "Industria": 20, "Servicios": 40, "Construcción": 18, "Agricultura": 14, "Transporte": 12, "Minería": 9},
        2026: {"Comercio": 48, "Industria": 22, "Servicios": 42, "Construcción": 20, "Agricultura": 13, "Transporte": 14, "Minería": 10},
    },
    "Pasto": {
        2021: {"Comercio": 48, "Industria": 22, "Servicios": 45, "Construcción": 14, "Agricultura": 28, "Transporte": 12, "Minería": 3},
        2022: {"Comercio": 50, "Industria": 24, "Servicios": 48, "Construcción": 16, "Agricultura": 27, "Transporte": 13, "Minería": 4},
        2023: {"Comercio": 52, "Industria": 26, "Servicios": 50, "Construcción": 18, "Agricultura": 26, "Transporte": 14, "Minería": 5},
        2024: {"Comercio": 54, "Industria": 28, "Servicios": 53, "Construcción": 20, "Agricultura": 25, "Transporte": 15, "Minería": 6},
        2025: {"Comercio": 56, "Industria": 30, "Servicios": 56, "Construcción": 22, "Agricultura": 24, "Transporte": 16, "Minería": 7},
        2026: {"Comercio": 58, "Industria": 32, "Servicios": 58, "Construcción": 24, "Agricultura": 23, "Transporte": 18, "Minería": 8},
    },
    "Quibdó": {
        2021: {"Comercio": 22, "Industria": 8, "Servicios": 18, "Construcción": 6, "Agricultura": 12, "Transporte": 5, "Minería": 8},
        2022: {"Comercio": 23, "Industria": 9, "Servicios": 19, "Construcción": 7, "Agricultura": 11, "Transporte": 6, "Minería": 9},
        2023: {"Comercio": 24, "Industria": 10, "Servicios": 20, "Construcción": 8, "Agricultura": 10, "Transporte": 7, "Minería": 10},
        2024: {"Comercio": 25, "Industria": 11, "Servicios": 22, "Construcción": 9, "Agricultura": 9, "Transporte": 8, "Minería": 11},
        2025: {"Comercio": 26, "Industria": 12, "Servicios": 24, "Construcción": 10, "Agricultura": 8, "Transporte": 9, "Minería": 12},
        2026: {"Comercio": 27, "Industria": 13, "Servicios": 26, "Construcción": 11, "Agricultura": 7, "Transporte": 10, "Minería": 13},
    },
    "Arauca": {
        2021: {"Comercio": 18, "Industria": 6, "Servicios": 14, "Construcción": 5, "Agricultura": 8, "Transporte": 4, "Minería": 12},
        2022: {"Comercio": 19, "Industria": 7, "Servicios": 15, "Construcción": 6, "Agricultura": 7, "Transporte": 5, "Minería": 13},
        2023: {"Comercio": 20, "Industria": 8, "Servicios": 16, "Construcción": 7, "Agricultura": 6, "Transporte": 6, "Minería": 14},
        2024: {"Comercio": 21, "Industria": 9, "Servicios": 17, "Construcción": 8, "Agricultura": 5, "Transporte": 7, "Minería": 15},
        2025: {"Comercio": 22, "Industria": 10, "Servicios": 18, "Construcción": 9, "Agricultura": 4, "Transporte": 8, "Minería": 16},
        2026: {"Comercio": 23, "Industria": 11, "Servicios": 19, "Construcción": 10, "Agricultura": 3, "Transporte": 9, "Minería": 17},
    },
    "Leticia": {
        2021: {"Comercio": 12, "Industria": 4, "Servicios": 10, "Construcción": 3, "Agricultura": 8, "Transporte": 3, "Minería": 1},
        2022: {"Comercio": 13, "Industria": 5, "Servicios": 11, "Construcción": 4, "Agricultura": 7, "Transporte": 4, "Minería": 2},
        2023: {"Comercio": 14, "Industria": 6, "Servicios": 12, "Construcción": 5, "Agricultura": 6, "Transporte": 5, "Minería": 3},
        2024: {"Comercio": 15, "Industria": 7, "Servicios": 13, "Construcción": 6, "Agricultura": 5, "Transporte": 6, "Minería": 4},
        2025: {"Comercio": 16, "Industria": 8, "Servicios": 14, "Construcción": 7, "Agricultura": 4, "Transporte": 7, "Minería": 5},
        2026: {"Comercio": 17, "Industria": 9, "Servicios": 15, "Construcción": 8, "Agricultura": 3, "Transporte": 8, "Minería": 6},
    },
}

# Distribución de género por sector (% mujeres) - basado en DANE-GEIH
GENERO_POR_SECTOR = {
    "Comercio": 0.48,
    "Industria": 0.35,
    "Servicios": 0.58,
    "Construcción": 0.12,
    "Agricultura": 0.32,
    "Transporte": 0.18,
    "Minería": 0.08,
}

# Participación laboral femenina por ciudad (% mujeres) - basado en DANE-GEIH
# Ciudades más formales y con más sector servicios tienen mayor participación femenina
GENERO_POR_CIUDAD = {
    "Bogotá": 0.48,
    "Medellín": 0.45,
    "Cali": 0.44,
    "Bucaramanga": 0.46,
    "Barranquilla": 0.47,
    "Cartagena": 0.43,
    "Santa Marta": 0.42,
    "Pasto": 0.41,
    "Valledupar": 0.38,
    "Montería": 0.36,
    "Sincelejo": 0.35,
    "Riohacha": 0.33,
    "Cúcuta": 0.34,
    "Quibdó": 0.30,
    "Arauca": 0.28,
    "Leticia": 0.32,
}


def get_genero_ciudad(ciudad: str) -> tuple:
    pct_mujeres = GENERO_POR_CIUDAD.get(ciudad, 0.40)
    return pct_mujeres, 1 - pct_mujeres


def get_promedio_nacional_genero() -> float:
    return sum(GENERO_POR_CIUDAD.values()) / len(GENERO_POR_CIUDAD)


def get_sectores_ciudad(ciudad: str, año: int) -> dict:
    if ciudad in EMPLEADOS_POR_SECTOR and año in EMPLEADOS_POR_SECTOR[ciudad]:
        return EMPLEADOS_POR_SECTOR[ciudad][año]
    return {sector: 0 for sector in SECTORES}


def get_top5_sectores(ciudad: str, año: int) -> list:
    sectores = get_sectores_ciudad(ciudad, año)
    return sorted(sectores.items(), key=lambda x: x[1], reverse=True)[:5]


def get_genero_sector(sector: str) -> tuple:
    pct_mujeres = GENERO_POR_SECTOR.get(sector, 0.45)
    return pct_mujeres, 1 - pct_mujeres


try:
    from data.data_manager import get_sectores_data as _get_sectores_reales
    _SECTORES_REALES = None
    
    def get_sectores_porcentaje(ciudad: str, año: int) -> dict:
        global _SECTORES_REALES
        if _SECTORES_REALES is None:
            try:
                _SECTORES_REALES = _get_sectores_reales()
            except Exception:
                _SECTORES_REALES = {}
        
        if ciudad in _SECTORES_REALES and año in _SECTORES_REALES[ciudad]:
            return _SECTORES_REALES[ciudad][año]
        
        if ciudad in EMPLEADOS_POR_SECTOR and año in EMPLEADOS_POR_SECTOR[ciudad]:
            total = sum(EMPLEADOS_POR_SECTOR[ciudad][año].values())
            if total > 0:
                return {s: (v * 100 / total) for s, v in EMPLEADOS_POR_SECTOR[ciudad][año].items()}
        
        return {}
    
    def get_sector_dominante_real(ciudad: str, año: int) -> str:
        sectores = get_sectores_porcentaje(ciudad, año)
        if sectores:
            max_sector = max(sectores.items(), key=lambda x: x[1])
            return max_sector[0]
        return SECTOR_DOMINANTE.get(ciudad, "Servicios")

except ImportError:
    def get_sectores_porcentaje(ciudad: str, año: int) -> dict:
        if ciudad in EMPLEADOS_POR_SECTOR and año in EMPLEADOS_POR_SECTOR[ciudad]:
            total = sum(EMPLEADOS_POR_SECTOR[ciudad][año].values())
            if total > 0:
                return {s: (v * 100 / total) for s, v in EMPLEADOS_POR_SECTOR[ciudad][año].items()}
        return {}
    
    def get_sector_dominante_real(ciudad: str, año: int) -> str:
        sectores = get_sectores_porcentaje(ciudad, año)
        if sectores:
            max_sector = max(sectores.items(), key=lambda x: x[1])
            return max_sector[0]
        return SECTOR_DOMINANTE.get(ciudad, "Servicios")
