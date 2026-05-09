from typing import Dict, List, Optional, Tuple
from core.constants import AÑOS
from data.sources.dane_geih import extract_tasa_ocupacion, CIUDAD_REGION


def extract(dataset_path: str) -> Optional[Dict[str, List[float]]]:
    try:
        return extract_tasa_ocupacion(dataset_path)
    except (FileNotFoundError, ValueError, KeyError) as e:
        return None


def transform(data: Dict[str, List[float]]) -> Dict[str, List[float]]:
    result = {}
    region_data: Dict[str, List[List[float]]] = {}

    for city in sorted(data.keys()):
        vals = data[city]
        region = CIUDAD_REGION.get(city, "Fronterizo")
        if region not in region_data:
            region_data[region] = [[] for _ in AÑOS]

        cleaned = []
        for i, v in enumerate(vals):
            if v is not None and isinstance(v, (int, float)):
                cleaned.append(round(float(v), 1))
                region_data[region][i].append(float(v))
            else:
                cleaned.append(None)
        result[city] = cleaned

    for city in sorted(result.keys()):
        region = CIUDAD_REGION.get(city, "Fronterizo")
        cleaned = []
        for i, v in enumerate(result[city]):
            if v is None:
                region_vals = [rv for rv in region_data[region][i] if rv is not None]
                if region_vals:
                    cleaned.append(round(sum(region_vals) / len(region_vals), 1))
                else:
                    cleaned.append(None)
            else:
                cleaned.append(v)
        result[city] = cleaned

    return result


def validate(data: Dict[str, List[float]]) -> Dict[str, List[str]]:
    issues = {city: [] for city in data}

    for city, vals in data.items():
        for i, year in enumerate(AÑOS):
            v = vals[i]
            if v is None:
                issues[city].append(f"{year}: sin dato")
            elif not (20 <= v <= 85):
                issues[city].append(f"{year}: fuera de rango ({v})")

        real_vals = [v for v in vals if v is not None]
        if len(real_vals) < 2:
            issues[city].append("menos de 2 años con datos")
        else:
            for i in range(1, len(real_vals)):
                if abs(real_vals[i] - real_vals[i - 1]) > 15:
                    issues[city].append(
                        f"cambio abrupto {AÑOS[i]}: {real_vals[i-1]}→{real_vals[i]}"
                    )

    return issues


def load(data: Dict[str, List[float]]) -> Dict[str, List[float]]:
    return {
        city: [
            round(v, 1) if v is not None else None
            for v in vals
        ]
        for city, vals in data.items()
    }


def _compute_regional_sigmas(data: Dict[str, List[float]]) -> Dict[str, float]:
    region_volatilities: Dict[str, List[float]] = {}
    for city, vals in data.items():
        region = CIUDAD_REGION.get(city, "Fronterizo")
        real_vals = [v for v in vals if v is not None]
        if len(real_vals) >= 2:
            changes = [abs(real_vals[i] - real_vals[i-1]) for i in range(1, len(real_vals))]
            avg_change = sum(changes) / len(changes)
            if region not in region_volatilities:
                region_volatilities[region] = []
            region_volatilities[region].append(avg_change)

    sigmas = {}
    for city, vals in data.items():
        region = CIUDAD_REGION.get(city, "Fronterizo")
        real_vals = [v for v in vals if v is not None]
        if len(real_vals) >= 2:
            changes = [abs(real_vals[i] - real_vals[i-1]) for i in range(1, len(real_vals))]
            city_volatility = sum(changes) / len(changes)
            sigmas[city] = round(city_volatility * 1.5, 1)
        else:
            region_cities = region_volatilities.get(region, [])
            if region_cities:
                sigmas[city] = round(sum(region_cities) / len(region_cities) * 1.5, 1)
            else:
                sigmas[city] = 3.0

    return sigmas


def run_pipeline(dataset_path: str) -> Tuple[Dict[str, List[float]], Dict[str, List[str]], Dict[str, float]]:
    raw = extract(dataset_path)
    if raw is None:
        raise FileNotFoundError(
            f"No se pudieron extraer datos de '{dataset_path}'. "
            "Verifica que el archivo existe y tiene el formato DANE-GEIH esperado."
        )

    transformed = transform(raw)
    issues = validate(transformed)
    cleaned = load(transformed)
    sigmas = _compute_regional_sigmas(cleaned)

    return cleaned, issues, sigmas
