import csv
from pathlib import Path
from typing import Dict, List, Optional, Tuple
from core.constants import AÑOS

BASE_PATH = Path(__file__).parent
MICRODATOS_GEIH_PATH = BASE_PATH / "microdatos" / "geih"

DPTO_CODES = {
    5: "Medellín",
    8: "Barranquilla",
    11: "Bogotá",
    13: "Cartagena",
    17: "Manizales",
    20: "Bucaramanga",
    23: "Cali",
    44: "Santa Marta",
    47: "Cúcuta",
    50: "Pasto",
    52: "Montería",
    54: "Valledupar",
    63: "Quibdó",
    66: "Riohacha",
    81: "Arauca",
    91: "Leticia",
    73: "Sincelejo",
}

RAMA2_SECTOR = {
    "01": "Agricultura",
    "02": "Agricultura",
    "03": "Agricultura",
    "05": "Minería",
    "06": "Minería",
    "07": "Minería",
    "08": "Minería",
    "09": "Minería",
    "10": "Industria",
    "11": "Industria",
    "12": "Industria",
    "13": "Industria",
    "14": "Industria",
    "15": "Industria",
    "16": "Industria",
    "17": "Industria",
    "18": "Industria",
    "19": "Industria",
    "20": "Industria",
    "21": "Industria",
    "22": "Industria",
    "23": "Industria",
    "24": "Industria",
    "25": "Industria",
    "26": "Industria",
    "27": "Industria",
    "28": "Industria",
    "29": "Industria",
    "30": "Industria",
    "31": "Industria",
    "32": "Industria",
    "33": "Industria",
    "35": "Servicios",
    "36": "Servicios",
    "37": "Servicios",
    "38": "Servicios",
    "39": "Servicios",
    "41": "Construcción",
    "42": "Construcción",
    "43": "Construcción",
    "45": "Comercio",
    "46": "Comercio",
    "47": "Comercio",
    "49": "Transporte",
    "50": "Transporte",
    "51": "Transporte",
    "52": "Servicios",
    "53": "Servicios",
    "55": "Servicios",
    "56": "Servicios",
    "58": "Servicios",
    "59": "Servicios",
    "60": "Servicios",
    "61": "Servicios",
    "62": "Servicios",
    "63": "Servicios",
    "64": "Servicios",
    "65": "Servicios",
    "66": "Servicios",
    "68": "Servicios",
    "69": "Servicios",
    "70": "Servicios",
    "71": "Servicios",
    "72": "Servicios",
    "73": "Servicios",
    "74": "Servicios",
    "75": "Servicios",
    "77": "Servicios",
    "78": "Servicios",
    "79": "Servicios",
    "80": "Servicios",
    "81": "Servicios",
    "82": "Servicios",
    "84": "Servicios",
    "85": "Servicios",
    "86": "Servicios",
    "87": "Servicios",
    "88": "Servicios",
    "90": "Servicios",
    "91": "Servicios",
    "92": "Servicios",
    "93": "Servicios",
    "94": "Servicios",
    "95": "Servicios",
    "96": "Servicios",
    "97": "Servicios",
    "98": "Servicios",
    "99": "Servicios",
}

_EMPLEO_DATA: Optional[Dict[str, List[float]]] = None
_SIGMA_DATA: Optional[Dict[str, float]] = None
_USING_REAL_DATA = False
_LOADED = False


def _find_files(file_pattern: str) -> List[Tuple[int, int, Path]]:
    files = []
    for year_dir in MICRODATOS_GEIH_PATH.iterdir():
        if not year_dir.is_dir() and not year_dir.name.endswith('.csv'):
            continue
        try:
            year = int(year_dir.name.replace('.csv', ''))
        except ValueError:
            continue
        for month_dir in year_dir.iterdir():
            if not month_dir.is_dir() and not month_dir.name.endswith('.csv'):
                continue
            month = _parse_month(month_dir.name.replace('.csv', ''))
            if month is None:
                continue
            for f in month_dir.iterdir():
                if not f.is_file():
                    continue
                name_lower = f.name.lower()
                if file_pattern.lower() in name_lower:
                    if year == 2021:
                        if ("ocupados" in name_lower and "desocupados" not in name_lower) or "fuerza" in name_lower:
                            files.append((year, month, f))
                    else:
                        files.append((year, month, f))
    files.sort(key=lambda x: (x[0], x[1]))
    return files


def _parse_month(month_name: str) -> Optional[int]:
    months = {
        "Enero": 1, "Febrero": 2, "Marzo": 3, "Abril": 4,
        "Mayo": 5, "Junio": 6, "Julio": 7, "Agosto": 8,
        "Septiembre": 9, "Octubre": 10, "Noviembre": 11, "Diciembre": 12,
    }
    return months.get(month_name)


def _load_counts(
    files: List[Tuple[int, int, Path]],
    include_key: str = "OCI",
    include_val: str = "1"
) -> Dict[Tuple[int, int, int], float]:
    counts: Dict[Tuple[int, int, int], float] = {}

    for year, month, filepath in files:
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
                        key = (year, month, dpto)
                        if include_key and include_val:
                            val = row.get(include_key, "")
                            if val != include_val:
                                continue
                        counts[key] = counts.get(key, 0) + fex
                    except (ValueError, KeyError):
                        continue
        except Exception:
            continue

    return counts


def _load_microdatos_tasa() -> Optional[Dict[str, List[float]]]:
    def group_by_year_month(files: List[Tuple[int, int, Path]]) -> Dict[Tuple[int, int], List[Path]]:
        grouped: Dict[Tuple[int, int], List[Path]] = {}
        for year, month, path in files:
            key = (year, month)
            if key not in grouped:
                grouped[key] = []
            grouped[key].append(path)
        return grouped

    ocupados_files = _find_files("Ocupados")
    fuerza_files = _find_files("uerza")

    if not ocupados_files or not fuerza_files:
        return None

    ocupado_counts: Dict[Tuple[int, int, int], float] = {}
    fuerza_counts: Dict[Tuple[int, int, int], float] = {}

    ocup_grouped = group_by_year_month(ocupados_files)
    fuerza_grouped = group_by_year_month(fuerza_files)

    for (year, month), paths in ocup_grouped.items():
        if year == 2021:
            for path in paths:
                counts = _load_counts([(year, month, path)])
                for k, v in counts.items():
                    ocupado_counts[k] = ocupado_counts.get(k, 0) + v
        else:
            file_tuples = [(year, month, p) for p in paths]
            counts = _load_counts(file_tuples)
            for k, v in counts.items():
                ocupado_counts[k] = ocupado_counts.get(k, 0) + v

    for (year, month), paths in fuerza_grouped.items():
        if year == 2021:
            for path in paths:
                counts = _load_counts([(year, month, path)], include_key=None, include_val=None)
                for k, v in counts.items():
                    fuerza_counts[k] = fuerza_counts.get(k, 0) + v
        else:
            file_tuples = [(year, month, p) for p in paths]
            counts = _load_counts(file_tuples, include_key=None, include_val=None)
            for k, v in counts.items():
                fuerza_counts[k] = fuerza_counts.get(k, 0) + v

    tasas: Dict[Tuple[int, int, int], float] = {}
    for key, ocupada in ocupado_counts.items():
        fuerza = fuerza_counts.get(key, 0)
        if fuerza > 0:
            tasas[key] = (ocupada / fuerza) * 100

    if not tasas:
        return None

    city_year_month: Dict[str, Dict[int, List[float]]] = {}
    for (year, month, dpto), tasa in tasas.items():
        city = DPTO_CODES.get(dpto)
        if city:
            if city not in city_year_month:
                city_year_month[city] = {}
            if year not in city_year_month[city]:
                city_year_month[city][year] = []
            city_year_month[city][year].append(tasa)

    result: Dict[str, List[float]] = {}
    for city in sorted(city_year_month.keys()):
        year_data = city_year_month[city]
        annual_rates = []
        for year in AÑOS:
            if year in year_data and year_data[year]:
                annual_rates.append(round(sum(year_data[year]) / len(year_data[year]), 1))
            else:
                annual_rates.append(None)
        result[city] = annual_rates

    return result


def _compute_sigmas(data: Dict[str, List[float]]) -> Dict[str, float]:
    sigmas = {}
    region_volatilities: Dict[str, List[float]] = {}

    CIUDAD_REGION = {
        "Barranquilla": "Caribe", "Cartagena": "Caribe", "Santa Marta": "Caribe",
        "Valledupar": "Caribe", "Montería": "Caribe", "Sincelejo": "Caribe",
        "Riohacha": "Caribe", "Bogotá": "Triángulo de Oro", "Medellín": "Triángulo de Oro",
        "Cali": "Triángulo de Oro", "Bucaramanga": "Santanderes", "Cúcuta": "Santanderes",
        "Quibdó": "Fronterizo", "Arauca": "Fronterizo", "Leticia": "Fronterizo",
        "Pasto": "Fronterizo",
    }

    for city, vals in data.items():
        region = CIUDAD_REGION.get(city, "Fronterizo")
        real_vals = [v for v in vals if v is not None]
        if len(real_vals) >= 2:
            changes = [abs(real_vals[i] - real_vals[i-1]) for i in range(1, len(real_vals))]
            city_vol = sum(changes) / len(changes)
            sigmas[city] = round(city_vol * 1.5, 1)
            if region not in region_volatilities:
                region_volatilities[region] = []
            region_volatilities[region].append(city_vol)
        else:
            region_cities = region_volatilities.get(region, [])
            if region_cities:
                sigmas[city] = round(sum(region_cities) / len(region_cities) * 1.5, 1)
            else:
                sigmas[city] = 3.0

    return sigmas


def _load_fallback():
    from data.empleo_base import EMPLEO_BASE, SIGMA_BASE
    return dict(EMPLEO_BASE), dict(SIGMA_BASE)


def _ensure_loaded():
    global _EMPLEO_DATA, _SIGMA_DATA, _USING_REAL_DATA, _LOADED
    if _LOADED:
        return

    microdatos = _load_microdatos_tasa()
    if microdatos:
        _EMPLEO_DATA = microdatos
        _SIGMA_DATA = _compute_sigmas(_EMPLEO_DATA)
        _USING_REAL_DATA = True
    else:
        _EMPLEO_DATA, _SIGMA_DATA = _load_fallback()
        _USING_REAL_DATA = False

    _LOADED = True


def get_empleo_data() -> Dict[str, List[float]]:
    _ensure_loaded()
    return _EMPLEO_DATA


def get_sigma_data() -> Dict[str, float]:
    _ensure_loaded()
    return _SIGMA_DATA


def is_using_real_data() -> bool:
    _ensure_loaded()
    return _USING_REAL_DATA


def get_ciudades() -> List[str]:
    return sorted(get_empleo_data().keys())


def get_available_years() -> List[int]:
    return list(AÑOS)


def get_data_source() -> str:
    _ensure_loaded()
    return "microdatos_geih" if _USING_REAL_DATA else "fallback_sintetico"


_SECTORES_DATA: Optional[Dict[str, Dict[int, Dict[str, float]]]] = None


def _load_sectores_from_geih() -> Dict[str, Dict[int, Dict[str, float]]]:
    sectores_por_ciudad: Dict[str, Dict[int, Dict[str, float]]] = {}
    
    SECTORES = ["Comercio", "Industria", "Servicios", "Construcción", "Agricultura", "Transporte", "Minería"]
    
    files = _find_files("Ocupados")
    if not files:
        return {}
    
    from collections import defaultdict
    city_year_sector: Dict[str, Dict[int, Dict[str, float]]] = defaultdict(lambda: defaultdict(lambda: defaultdict(float)))
    
    for year, month, filepath in files:
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
                        
                        rama = row.get("RAMA2D_R4", "").strip()
                        if not rama:
                            continue
                        
                        sector = RAMA2_SECTOR.get(rama, "Servicios")
                        if sector not in SECTORES:
                            sector = "Servicios"
                        
                        city_year_sector[city][year][sector] += fex
                    except (ValueError, KeyError):
                        continue
        except Exception:
            continue
    
    for city, years_data in city_year_sector.items():
        sectores_por_ciudad[city] = {}
        for year, sector_data in years_data.items():
            total = sum(sector_data.values())
            if total > 0:
                sectores_por_ciudad[city][year] = {s: (count * 100 / total) for s, count in sector_data.items()}
            else:
                sectores_por_ciudad[city][year] = {s: 0.0 for s in SECTORES}
    
    return sectores_por_ciudad


def get_sectores_data() -> Dict[str, Dict[int, Dict[str, float]]]:
    global _SECTORES_DATA
    if _SECTORES_DATA is None:
        _SECTORES_DATA = _load_sectores_from_geih()
    return _SECTORES_DATA