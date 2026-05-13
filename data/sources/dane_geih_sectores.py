"""
data/sources/dane_geih_sectores.py
────────────────────────────────────
ETL: Población ocupada por rama de actividad económica — DANE GEIH
Reemplaza data/sectores.py (sintético) con datos REALES oficiales.

Fuente: Gran Encuesta Integrada de Hogares (GEIH) — DANE Colombia
Boletines técnicos diciembre 2022 y 2024 (tablas anuales "Total nacional año")
Clasificación: CIIU Rev. 4 A.C. (2022)
URL: https://www.dane.gov.co/index.php/estadisticas-por-tema/mercado-laboral/empleo-y-desempleo

Diferencia respecto a data/sectores.py anterior:
  sectores.py   → sintético, "calibrado con DANE-GEIH" (estimaciones)
  este módulo   → REAL, cifras oficiales extraídas de boletines primarios DANE

Uso:
    from data.sources.dane_geih_sectores import cargar_ocupados_sector
    df = cargar_ocupados_sector()                        # miles de personas
    df_pct = cargar_ocupados_sector(como_porcentaje=True) # distribución %
"""

import pathlib
import pandas as pd

XLSX_DEFAULT = pathlib.Path(__file__).parent / "DANE_GEIH_sectores_rama_actividad_2021_2026.xlsx"

# Mapeo: nombre en tu proyecto → clave interna / nombre DANE
# Ajusta las claves izquierdas al nombre exacto que uses en data/sectores.py
MAPEO_SECTOR_PROYECTO = {
    "Comercio"               : "Comercio y reparación de vehículos",
    "Manufactura"            : "Industrias manufactureras",
    "Agricultura"            : "Agricultura, ganadería, caza, silvicultura y pesca",
    "Construcción"           : "Construcción",
    "Transporte"             : "Transporte y almacenamiento",
    "Adm. pública/Educación" : "Administración pública y defensa, educación y atención de la salud humana",
    "Alojamiento/Restaurantes": "Alojamiento y servicios de comida",
    "Servicios profesionales": "Actividades profesionales, científicas, técnicas y servicios administrativos",
    "Arte/Servicios varios"  : "Actividades artísticas, entretenimiento, recreación y otras actividades de servicios",
    "Energía/Minas/Agua"     : "Suministro de electricidad, gas, agua y gestión de desechos (incluye minería)",
    "Finanzas/Seguros"       : "Actividades financieras y de seguros",
    "TIC/Información"        : "Información y comunicaciones",
    "Inmobiliario"           : "Actividades inmobiliarias",
}

# Total nacional oficial por año (miles de personas, promedio Ene-Dic)
TOTAL_OCUPADOS_REAL = {
    2021: 20_655,
    2022: 22_032,
    2023: 22_788,
    2024: 23_036,
    2025: None,   # parcial — pendiente boletín dic-2025
    2026: None,   # parcial — año móvil a mar-2026
}


def cargar_ocupados_sector(
    xlsx_path: str | pathlib.Path = XLSX_DEFAULT,
    como_porcentaje: bool = False,
    anios: list[int] | None = None,
    normalizar_nombres: bool = True,
) -> pd.DataFrame:
    """
    Carga la población ocupada por rama de actividad.

    Retorna DataFrame con:
        - índice: rama (nombre DANE o nombre del proyecto si normalizar_nombres)
        - columnas: años enteros
        - valores: miles de personas (o % si como_porcentaje=True)

    Parámetros
    ----------
    xlsx_path          : ruta al Excel DANE_GEIH_sectores_rama_actividad_2021_2026.xlsx
    como_porcentaje    : si True, retorna distribución porcentual
    anios              : lista de años a incluir; None = todos
    normalizar_nombres : si True, renombra al nombre del proyecto (MAPEO_SECTOR_PROYECTO)
    """
    path = pathlib.Path(xlsx_path)
    if not path.exists():
        raise FileNotFoundError(
            f"No se encontró: {path}\n"
            "Ejecuta build_sectores_xlsx.py para regenerarlo, o descarga\n"
            "el boletín GEIH más reciente desde:\n"
            "  https://www.dane.gov.co/index.php/estadisticas-por-tema/mercado-laboral/empleo-y-desempleo"
        )

    sheet = "Distribucion_pct" if como_porcentaje else "Ocupados_rama (miles)"
    raw = pd.read_excel(path, sheet_name=sheet, header=2, index_col=0)

    # Limpiar: descartar fila "TOTAL" y notas
    raw = raw[raw.index.notna()]
    # Mantener sólo filas de ramas (las que no empiezan con "TOTAL")
    rama_names = [v for _, v in MAPEO_SECTOR_PROYECTO.items()]
    raw = raw[raw.index.isin(rama_names) | raw.index.str.startswith("Agricultura") |
              raw.index.str.startswith("Comercio") | raw.index.str.startswith("Industrias") |
              raw.index.str.startswith("Act") | raw.index.str.startswith("Administración") |
              raw.index.str.startswith("Transporte") | raw.index.str.startswith("Alojamiento") |
              raw.index.str.startswith("Construcción") | raw.index.str.startswith("Suministro") |
              raw.index.str.startswith("Información") | raw.index.str.startswith("Actividades")]

    # Limpiar columnas — extraer año entero
    import re
    def _anio(col):
        m = re.search(r"(\d{4})", str(col))
        return int(m.group(1)) if m else None

    raw = raw.rename(columns=_anio)
    raw = raw[[c for c in raw.columns if isinstance(c, int)]]
    raw.columns = raw.columns.astype(int)

    if anios:
        raw = raw[[a for a in anios if a in raw.columns]]

    if normalizar_nombres:
        nombre_inv = {v: k for k, v in MAPEO_SECTOR_PROYECTO.items()}
        raw.index = raw.index.map(lambda x: nombre_inv.get(x, x))
        raw.index.name = "sector"

    return raw.astype(float)


def cargar_ocupados_sector_long(
    xlsx_path: str | pathlib.Path = XLSX_DEFAULT,
    **kwargs,
) -> pd.DataFrame:
    """
    Igual que cargar_ocupados_sector() pero en formato largo (tidy):
        sector | año | ocupados_miles   (o  pct  si como_porcentaje=True)
    """
    df_wide = cargar_ocupados_sector(xlsx_path, **kwargs)
    col_val = "pct" if kwargs.get("como_porcentaje") else "ocupados_miles"
    df_long = (
        df_wide.reset_index()
        .melt(id_vars=df_wide.index.name or "sector", var_name="año", value_name=col_val)
    )
    df_long["año"] = df_long["año"].astype(int)
    return df_long.sort_values(["sector", "año"]).reset_index(drop=True)


def total_ocupados_nacional(anio: int) -> int | None:
    """Retorna el total de ocupados (miles) para el año dado. None si no disponible."""
    return TOTAL_OCUPADOS_REAL.get(anio)


# ── Descarga directa del boletín DANE más reciente ────────────────────────

def descargar_boletin_dane(
    mes: str = "dic2024",
    destino_dir: str | pathlib.Path = ".",
) -> pathlib.Path:
    """
    Descarga el boletín técnico GEIH en PDF.
    Los datos de rama de actividad (tabla anual) están en los boletines de diciembre.

    Parámetros
    ----------
    mes : código del mes, ej. "dic2024", "mar2026"
    """
    import urllib.request
    base = "https://www.dane.gov.co/files/operaciones/GEIH/"
    # Para boletines pre-2023 la ruta es diferente:
    if int(mes[-4:]) <= 2022:
        base = "https://www.dane.gov.co/files/investigaciones/boletines/ech/ech/"
        fname = f"bol_empleo_{mes[:3]}_{mes[3:]}.pdf"
    else:
        fname = f"bol-GEIH-{mes}.pdf"
    url = base + fname
    destino = pathlib.Path(destino_dir) / fname
    print(f"Descargando: {url}")
    urllib.request.urlretrieve(url, destino)
    print(f"Guardado en: {destino}")
    return destino


# ── CLI rápido ─────────────────────────────────────────────────────────────
if __name__ == "__main__":
    import sys
    pct = "--pct" in sys.argv

    print(f"\n=== Sectores DANE-GEIH — {'Distribución %' if pct else 'Miles personas'} ===\n")
    df = cargar_ocupados_sector(como_porcentaje=pct)
    print(df.to_string())

    print(f"\n=== Totales nacionales oficiales ===")
    for a, t in TOTAL_OCUPADOS_REAL.items():
        print(f"  {a}: {t:,} miles" if t else f"  {a}: (dato parcial)")

    print(f"\n=== Formato largo (primeras 10 filas) ===")
    df_l = cargar_ocupados_sector_long(como_porcentaje=pct)
    print(df_l.head(10).to_string(index=False))
