"""
Loader para datos externos (CSV/Excel) futuros.
Preparado para cargar datos reales del DANE-GEIH.
"""

import pandas as pd
from typing import Dict, List
from core.constants import AÑOS


def load_dane_geih(path: str) -> Dict[str, List[float]]:
    """
    Carga datos del DANE-GEIH desde un archivo CSV/Excel.
    
    El archivo debe tener columnas: ciudad, 2021, 2022, 2023, 2024, 2025, 2026
    
    Args:
        path: Ruta al archivo CSV o Excel.
        
    Returns:
        Dict con formato compatible con EMPLEO_BASE.
        
    Raises:
        FileNotFoundError: Si el archivo no existe.
        ValueError: Si el formato del archivo es incorrecto.
    """
    if path.endswith('.csv'):
        df = pd.read_csv(path)
    elif path.endswith(('.xls', '.xlsx')):
        df = pd.read_excel(path)
    else:
        raise ValueError(f"Formato de archivo no soportado: {path}")
    
    # Validar columnas requeridas
    required_cols = ['ciudad'] + [str(a) for a in AÑOS]
    missing = [c for c in required_cols if c not in df.columns]
    if missing:
        raise ValueError(f"Columnas faltantes: {missing}")
    
    # Convertir a formato EMPLEO_BASE
    result = {}
    for _, row in df.iterrows():
        ciudad = row['ciudad']
        valores = [float(row[str(a)]) for a in AÑOS]
        result[ciudad] = valores
    
    return result
