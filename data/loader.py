from typing import Dict, List, Tuple
from core.constants import AÑOS
from data.empleo_base import EMPLEO_BASE as EMPLEO_BASE_FALLBACK, SIGMA_BASE as SIGMA_BASE_FALLBACK
from data.etl_pipeline import run_pipeline

DATASET_PATH = "data/datasets/2026/anex-mar2026.xlsx"

_EMPLEO_BASE: Dict[str, List[float]] = {}
_SIGMA_BASE: Dict[str, float] = {}
_USING_REAL_DATA = False
_VALIDATION_ISSUES: Dict[str, List[str]] = {}


def _load_real() -> bool:
    global _EMPLEO_BASE, _SIGMA_BASE, _VALIDATION_ISSUES, _USING_REAL_DATA
    try:
        empleo, issues, sigmas = run_pipeline(DATASET_PATH)
        missing_years = sum(1 for v in empleo.values() for val in v if val is None)
        if missing_years > len(empleo) * 2:
            return False

        _EMPLEO_BASE = empleo
        _SIGMA_BASE = sigmas
        _VALIDATION_ISSUES = issues
        _USING_REAL_DATA = True
        return True
    except (FileNotFoundError, ValueError, KeyError, Exception):
        return False


def _load_fallback() -> None:
    global _EMPLEO_BASE, _SIGMA_BASE, _USING_REAL_DATA
    _EMPLEO_BASE = dict(EMPLEO_BASE_FALLBACK)
    _SIGMA_BASE = dict(SIGMA_BASE_FALLBACK)
    _USING_REAL_DATA = False


if not _load_real():
    _load_fallback()


def get_empleo_base() -> Dict[str, List[float]]:
    return _EMPLEO_BASE


def get_sigma_base() -> Dict[str, float]:
    return _SIGMA_BASE


def is_using_real_data() -> bool:
    return _USING_REAL_DATA


def get_validation_issues() -> Dict[str, List[str]]:
    return _VALIDATION_ISSUES
