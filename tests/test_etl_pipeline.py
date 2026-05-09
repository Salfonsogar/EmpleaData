from core.constants import AÑOS
from data.etl_pipeline import extract, transform, validate, load, _compute_regional_sigmas


class TestTransform:
    def test_limpia_none_sin_romper(self):
        data = {"Bogotá": [55.0, None, 57.0, None, 59.0, 60.0]}
        result = transform(data)
        assert "Bogotá" in result

    def test_rellena_con_media_regional(self):
        data = {
            "Bogotá": [55.0, 56.0, 57.0, 58.0, 59.0, 60.0],
            "Medellín": [54.0, 55.0, 56.0, 57.0, 58.0, 59.0],
            "Cali": [53.0, None, 55.0, 56.0, 57.0, 58.0],
        }
        result = transform(data)
        assert result["Cali"][1] is not None

    def test_todas_las_ciudades_presentes(self):
        data = {"Bogotá": [55.0]*6, "Medellín": [56.0]*6}
        result = transform(data)
        assert set(result.keys()) == {"Bogotá", "Medellín"}


class TestValidate:
    def test_sin_errores_para_datos_normales(self):
        data = {"Bogotá": [55.0, 56.0, 57.0, 58.0, 59.0, 60.0]}
        issues = validate(data)
        assert len(issues["Bogotá"]) == 0

    def test_detecta_fuera_de_rango(self):
        data = {"Bogotá": [10.0, 56.0, 57.0, 58.0, 59.0, 60.0]}
        issues = validate(data)
        assert any("fuera de rango" in i for i in issues["Bogotá"])

    def test_detecta_cambio_abrupto(self):
        data = {"Bogotá": [55.0, 56.0, 57.0, 58.0, 59.0, 80.0]}
        issues = validate(data)
        assert any("cambio abrupto" in i for i in issues["Bogotá"])

    def test_detecta_datos_faltantes(self):
        data = {"Bogotá": [None, 56.0, 57.0, None, 59.0, 60.0]}
        issues = validate(data)
        assert any("sin dato" in i for i in issues["Bogotá"])


class TestLoad:
    def test_redondea_a_un_decimal(self):
        data = {"Bogotá": [55.55, 56.666, 57.111]}
        result = load(data)
        for v in result["Bogotá"]:
            assert v == round(v, 1)

    def test_mantiene_none(self):
        data = {"Bogotá": [55.0, None, 57.0]}
        result = load(data)
        assert result["Bogotá"][1] is None


class TestComputeRegionalSigmas:
    def test_retorna_dict_con_ciudades(self):
        data = {"Bogotá": [55.0, 56.0, 57.0, 58.0, 59.0, 60.0]}
        sigmas = _compute_regional_sigmas(data)
        assert "Bogotá" in sigmas

    def test_sigma_es_positivo(self):
        data = {"Bogotá": [55.0, 56.0, 57.0, 58.0, 59.0, 60.0]}
        sigmas = _compute_regional_sigmas(data)
        assert sigmas["Bogotá"] > 0
