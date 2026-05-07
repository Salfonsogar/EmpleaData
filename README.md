# Analizador Dinámico de Empleabilidad Nacional (2021-2026)

> Modelado y Simulación Estocástica - Ingeniería de Sistemas  
> Docente: Andrés Perpiñán Reyes

## Descripción

Aplicación web interactiva desarrollada en Python/Dash para el análisis de empleabilidad en Colombia (2021-2026), utilizando datos sintéticos calibrados con fuentes DANE-GEIH. Implementa modelado estadístico, simulación Monte Carlo y visualización interactiva.

## Características

- **Mapa interactivo**: Visualización geográfica de tasas de empleo por ciudad
- **Distribución Normal**: Campana de Gauss comparando ciudad vs media nacional
- **Tendencias temporales**: Evolución 2021-2026 con bandas de confianza
- **Ranking nacional**: Comparación ordenada de ciudades
- **Análisis de correlación**: Relación entre migración y volatilidad laboral en ciudades fronterizas
- **KPIs dinámicos**: Tarjetas con estadísticas en tiempo real
- **Detección de outliers**: Identificación automática de ciudades fuera del rango ±2σ

## Arquitectura

```
proyecto/
├── app.py                          # Entry point
├── requirements.txt                # Dependencias
├── README.md                       # Documentación
│
├── core/                           # Configuración central
│   ├── config.py                   # Settings de ejecución
│   ├── constants.py                # AÑOS, COLORES_REGION
│   ├── theme.py                    # Tokens visuales (dark mode)
│   └── validators.py               # Validadores de entrada
│
├── data/                           # Capa de datos
│   ├── __init__.py                 # Facade re-exportador
│   ├── ciudades.py                # Coordenadas y regiones
│   ├── empleo_base.py             # Tasas y volatilidad
│   ├── sectores.py                # Sectores económicos
│   ├── migracion.py               # Datos migración fronteriza
│   ├── loader.py                   # Carga futura CSV/Excel
│   └── datasets/                  # Directorio para datos reales
│
├── services/                       # Lógica de negocio (Service Layer)
│   ├── estadisticas_service.py    # Cálculos estadísticos
│   ├── outlier_service.py         # Detección de outliers
│   └── correlacion_service.py     # Análisis de correlación
│
├── visualizations/                 # Figuras Plotly reutilizables
│   ├── mapa.py
│   ├── gauss.py
│   ├── tendencias.py
│   ├── ranking.py
│   └── correlacion.py
│
├── ui/                            # Interfaz de usuario
│   ├── layout.py                  # Ensamblaje de UI
│   ├── components/
│   │   ├── cards.py              # KPI cards
│   │   ├── navbar.py             # Header
│   │   └── controls.py          # Sliders y dropdowns
│   └── callbacks/
│       ├── __init__.py           # register_all_callbacks()
│       ├── map_callbacks.py
│       ├── stats_callbacks.py
│       └── extra_callbacks.py
│
├── utils/                         # Utilidades puras
│   ├── formatters.py
│   └── helpers.py
│
└── tests/                         # Suite de tests
    ├── conftest.py                # Fixtures compartidas
    ├── test_estadisticas.py
    ├── test_outliers.py
    └── test_visualizaciones.py
```

## Instalación

```bash
# Clonar el repositorio
git clone <repo-url>
cd EmpleaData

# Crear entorno virtual (opcional pero recomendado)
python -m venv venv
source venv/bin/activate  # Linux/Mac
# o venv\Scripts\activate  # Windows

# Instalar dependencias
pip install -r requirements.txt
```

## Ejecución

```bash
python app.py
```

La aplicación se ejecutará en `http://127.0.0.1:8050`

## Dependencias

- **Dash**: Framework web para aplicaciones analíticas
- **Plotly**: Gráficos interactivos
- **Pandas**: Manipulación de datos
- **NumPy**: Computación numérica
- **SciPy**: Algoritmos estadísticos
- **Pytest**: Framework de testing

## Pruebas

```bash
pytest tests/
```

## Fuentes de Datos

- DANE-GEIH (Gran Encuesta Integrada de Hogares)
- Datos Abiertos Colombia
- SISRPO-MinSalud

## Notas Académicas

- Los datos actuales son **sintéticos** calibrados con fuentes históricas
- El módulo `data/loader.py` está preparado para cargar datos reales CSV/Excel
- La semilla aleatoria es determinista (hash ciudad + año) para reproducibilidad
- La arquitectura sigue principios **SOLID** y patrones **Service Layer**

## Capturas de Pantalla

*[Placeholder: Agregar screenshots de la aplicación ejecutándose]*

## Licencia

Proyecto académico - Universidad Popular del Cesar (UniCésar)

---

**Desarrollado con arquitectura modular profesional para escalabilidad y mantenibilidad.**
