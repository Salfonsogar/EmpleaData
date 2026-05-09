import os
from core.constants import AÑOS
from data.sources.dane_geih import (
    CIUDAD_MAP, extract_tasa_ocupacion
)


class TestCiudadMap:
    def test_tiene_16_ciudades(self):
        assert len(CIUDAD_MAP) == 16

    def test_incluye_todas_las_del_proyecto(self):
        from data.ciudades import CIUDADES
        project_cities = set(CIUDADES.keys())
        mapped = set(CIUDAD_MAP.values())
        assert project_cities == mapped, f"Faltan: {project_cities - mapped}"

    def test_dane_names_no_duplicados(self):
        assert len(set(CIUDAD_MAP.keys())) == len(CIUDAD_MAP)


class TestExtractTasaOcupacion:
    DATASET = "data/datasets/2026/anex-mar2026.xlsx"

    @classmethod
    def setup_class(cls):
        if not os.path.exists(cls.DATASET):
            pytest.skip(f"Dataset no encontrado: {cls.DATASET}")
        cls.result = extract_tasa_ocupacion(cls.DATASET)

    def test_retorna_dict_con_16_ciudades(self):
        assert len(self.result) == 16

    def test_cada_ciudad_tiene_6_anios(self):
        for city, vals in self.result.items():
            assert len(vals) == len(AÑOS), f"{city}: esperado {len(AÑOS)}, obtenido {len(vals)}"

    def test_valores_en_rango_razonable(self):
        for city, vals in self.result.items():
            for v in vals:
                if v is not None:
                    assert 20 <= v <= 85, f"{city}: {v} fuera de rango [20, 85]"

    def test_bogota_tiene_datos(self):
        assert self.result["Bogotá"][0] is not None
        assert self.result["Bogotá"][4] is not None

    def test_2026_no_es_none(self):
        for city, vals in self.result.items():
            assert vals[5] is not None, f"{city} no tiene dato 2026"

    def test_ciudades_esperadas_presentes(self):
        esperadas = {"Bogotá", "Medellín", "Cali", "Barranquilla", "Cartagena",
                     "Bucaramanga", "Cúcuta", "Pasto", "Sincelejo", "Santa Marta",
                     "Valledupar", "Montería", "Riohacha", "Quibdó", "Arauca", "Leticia"}
        assert esperadas == set(self.result.keys())
