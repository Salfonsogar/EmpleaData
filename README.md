# Analizador Dinámico de Empleabilidad Nacional (2021–2026)
**Modelado y Simulación · Docente: Andrés Perpiñán Reyes**

## Instalación
```bash
pip install -r requirements.txt
```

## Ejecución
```bash
python app.py
```
Abre **http://127.0.0.1:8050** en tu navegador.

---

## Qué incluye el simulador

### Nodos obligatorios (§ 2A)
| Región | Ciudades |
|---|---|
| Caribe | Barranquilla, Cartagena, Santa Marta, Valledupar, Montería, Sincelejo, Riohacha |
| Triángulo de Oro | Bogotá, Medellín, Cali |
| Santanderes | Bucaramanga, Cúcuta |
| Fronterizos | Quibdó, Arauca, Leticia, Pasto |

### Motor estadístico (§ 3I)
- **Media**: tasa promedio de empleabilidad del periodo
- **Mediana**: identifica brechas de desigualdad laboral
- **Moda**: sector económico dominante (Comercio, Minería, Servicios, etc.)
- **Desviación Estándar σ**: mide volatilidad/estabilidad laboral

### Campana de Gauss (§ 3II)
- Curva comparativa: ciudad seleccionada vs. media nacional
- Detección de outliers: ¿Quibdó/Leticia fuera de ±2σ?
- Análisis de kurtosis: fronterizas vs. Triángulo de Oro

### Punto Extra — Correlación Fronteriza (§ 5)
- Correlación de Pearson entre σ laboral y tasa de migración (Cúcuta, Arauca, Pasto)
- Comparación platicúrtica: curvas fronterizas vs. Triángulo de Oro

---

## Fuentes de datos recomendadas
- **DANE - GEIH**: https://www.dane.gov.co/index.php/estadisticas-por-tema/mercado-laboral
- **Datos Abiertos Colombia**: https://www.datos.gov.co
- **SISRPO - MinSalud**: https://www.minsalud.gov.co/salud/publica/pags/sisrpo.aspx
