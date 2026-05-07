"""
Servicio de estadísticas laborales.
Incluye generación de muestras simuladas y cálculo de métricas.
"""

import numpy as np
from typing import Dict, List

from data import CIUDADES, EMPLEO_BASE, SIGMA_BASE, SECTOR_DOMINANTE
from core.constants import AÑOS


def _generar_muestra(ciudad: str, año: int, n: int = 120) -> np.ndarray:
    """
    Genera una muestra simulada mensual usando distribución normal.
    
    Args:
        ciudad: Nombre de la ciudad.
        año: Año de la muestra.
        n: Tamaño de la muestra (default 120 = 10 años de datos mensuales).
        
    Returns:
        Array de numpy con valores de tasa de empleo simulados.
    """
    idx = AÑOS.index(año)
    mu = EMPLEO_BASE[ciudad][idx]
    sigma = SIGMA_BASE[ciudad]
    
    # Seed determinista basado en ciudad y año para reproducibilidad
    np.random.seed(hash(ciudad + str(año)) % 2**31)
    muestra = np.random.normal(mu, sigma, n)
    return np.clip(muestra, 20, 85)


def calcular_estadisticas(ciudad: str, año: int) -> Dict:
    """
    Calcula media, mediana, moda y desviación estándar para una ciudad/año.
    
    Args:
        ciudad: Nombre de la ciudad.
        año: Año a analizar.
        
    Returns:
        Dict con keys: media, mediana, moda, std, mu_ref, sigma_ref.
    """
    idx = AÑOS.index(año)
    mu = EMPLEO_BASE[ciudad][idx]
    sigma = SIGMA_BASE[ciudad]
    
    muestra = _generar_muestra(ciudad, año)
    
    return {
        "media": round(float(np.mean(muestra)), 2),
        "mediana": round(float(np.median(muestra)), 2),
        "moda": SECTOR_DOMINANTE[ciudad],
        "std": round(float(np.std(muestra)), 2),
        "mu_ref": mu,
        "sigma_ref": sigma,
    }


def calcular_media_nacional(año: int) -> tuple[float, float]:
    """
    Calcula la media y desviación estándar nacional para un año dado.
    
    Args:
        año: Año a calcular.
        
    Returns:
        Tupla (media_nacional, sigma_nacional).
    """
    idx = AÑOS.index(año)
    valores = [EMPLEO_BASE[c][idx] for c in CIUDADES]
    sigmas = list(SIGMA_BASE.values())
    return round(np.mean(valores), 2), round(np.std(sigmas), 2)
