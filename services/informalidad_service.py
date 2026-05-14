import csv
from pathlib import Path
from typing import Dict, List, Optional, Tuple
from data.data_manager import _find_files, DPTO_CODES
from core.constants import AÑOS

_INFORMALIDAD_DATA: Optional[Dict[str, List[Optional[float]]]] = None


def _load_informalidad() -> Dict[str, List[Optional[float]]]:
    result: Dict[str, List[Optional[float]]] = {}

    files = _find_files("Ocupados")
    if not files:
        return {}

    city_year_data: Dict[str, Dict[int, Tuple[float, float]]] = {}

    for year, month, filepath in files:
        if year not in AÑOS:
            continue

        try:
            with open(filepath, "r", encoding="utf-8", errors="ignore") as f:
                reader = csv.DictReader(f, delimiter=";")
                fex_col = "FEX_C18" if "FEX_C18" in reader.fieldnames else "fex_c_2011"

                for row in reader:
                    try:
                        dpto = int(row.get("DPTO", 0))
                        fex_str = row.get(fex_col, "0").replace(",", ".")
                        fex = float(fex_str)

                        if dpto == 0 or fex == 0:
                            continue

                        city = DPTO_CODES.get(dpto)
                        if not city:
                            continue

                        contrato = row.get("P6450", "").strip()
                        pension = row.get("P6630", "").strip()

                        es_informal = False
                        if contrato == "2":
                            es_informal = True
                        elif pension not in ("1", "2", "3", "4", "5", "6"):
                            es_informal = True
                        elif pension not in ("1",):
                            es_informal = True

                        if city not in city_year_data:
                            city_year_data[city] = {}
                        if year not in city_year_data[city]:
                            city_year_data[city][year] = (0.0, 0.0)

                        total, informal = city_year_data[city][year]
                        total += fex
                        informal += fex if es_informal else 0.0
                        city_year_data[city][year] = (total, informal)

                    except (ValueError, KeyError):
                        continue
        except Exception:
            continue

    for city in sorted(city_year_data.keys()):
        yearly_rates = []
        for year in AÑOS:
            if year in city_year_data[city]:
                total, informal = city_year_data[city][year]
                if total > 0:
                    rate = (informal / total) * 100
                    yearly_rates.append(round(rate, 1))
                else:
                    yearly_rates.append(None)
            else:
                yearly_rates.append(None)
        result[city] = yearly_rates

    return result


def _ensure_loaded():
    global _INFORMALIDAD_DATA
    if _INFORMALIDAD_DATA is None:
        _INFORMALIDAD_DATA = _load_informalidad()


def get_tasa_informalidad(ciudad: str, año: int) -> Optional[float]:
    _ensure_loaded()
    if ciudad not in _INFORMALIDAD_DATA:
        return None
    idx = AÑOS.index(año)
    return _INFORMALIDAD_DATA[ciudad][idx]


def get_informalidad_todas_ciudades(año: int) -> Dict[str, float]:
    _ensure_loaded()
    result = {}
    idx = AÑOS.index(año)
    for ciudad, tasas in _INFORMALIDAD_DATA.items():
        if idx < len(tasas) and tasas[idx] is not None:
            result[ciudad] = tasas[idx]
    return result


def get_evolucion_informalidad() -> Dict[str, List[Optional[float]]]:
    _ensure_loaded()
    return _INFORMALIDAD_DATA


def get_media_nacional_informalidad(año: int) -> float:
    _ensure_loaded()
    idx = AÑOS.index(año)
    valores = []
    for ciudad, tasas in _INFORMALIDAD_DATA.items():
        if idx < len(tasas) and tasas[idx] is not None:
            valores.append(tasas[idx])
    if valores:
        return round(sum(valores) / len(valores), 1)
    return 0.0