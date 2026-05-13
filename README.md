# 📊 Analizador Dinámico de Empleabilidad Nacional (2021-2026)

> **Modelado y Simulación Estocástica** - Ingeniería de Sistemas  
> **Docente:** Andrés Perpiñán Reyes  
> **Universidad:** UniCésar

## 🎯 Descripción

Aplicación web interactiva desarrollada en **Python/Dash** para el análisis de empleabilidad en Colombia durante el período 2021-2026. Utiliza datos reales del **DANE-GEIH** (Gran Encuesta Integrada de Hogares) con visualización interactiva y análisis estadístico avanzado.

---

## 🚀 Características

### 📱 Interfaz por Pestañas

- **Overview**: Mapa de Colombia, KPIs dinámicos, Ranking de ciudades
- **Regional**: Distribución Gauss, Tendencias temporales, Sectores económicos, Género
- **Nacional**: Correlación fronteriza, Sectores DANE, Heatmap

### 📈 Visualizaciones

| Visualización | Descripción |
|---------------|-------------|
| 🗺️ **Mapa de Colombia** | Mapa coroplético interactivo con tasas por ciudad |
| 📊 **Ranking Nacional** | Comparación ordenada de ciudades (Top 5 o todas) |
| 🔔 **Distribución Normal** | Campana de Gauss comparando ciudad vs media nacional |
| 📉 **Evolución Temporal** | Tendencia 2021-2026 con bandas de confianza ±1σ |
| 🥧 **Sectores Económicos** | Distribución por sectores (Comercio, Industria, Servicios) |
| 👥 **Distribución por Género** | Comparación de participación laboral femenina |
| 🔗 **Correlación Fronteriza** | Relación entre migración y volatilidad laboral |
| 🌡️ **Heatmap** | Matriz de correlación temporal por ciudad |
| 📋 **Sectores DANE** | Análisis de sectores económicos a nivel nacional |

### 📊 Funcionalidades

- **KPIs dinámicos**: Media, mediana, desviación estándar, sector dominante
- **Detección de outliers**: Identificación automática de ciudades fuera de ±2σ
- **Selección por región**: Filtrar por Caribe, Triángulo de Oro, Santanderes, Fronterizo
- **Pre-cálculo de figuras**: Optimizado para respuesta instantánea

---

## 🏗️ Arquitectura

```
EmpleaData/
├── app.py                      # Entry point de la aplicación
├── requirements.txt            # Dependencias del proyecto
├── ANALISIS.md                 # Análisis y conclusiones de datos
│
├── core/                       # Configuración central
│   ├── config.py              # Settings de ejecución
│   ├── constants.py           # AÑOS, COLORES_REGION
│   ├── theme.py               # Tokens visuales
│   └── validators.py          # Validadores
│
├── data/                       # Capa de datos
│   ├── ciudades.py            # Coordenadas y regiones
│   ├── empleo_base.py         # Datos base de empleo
│   ├── sectores.py            # Sectores económicos
│   ├── migracion.py           # Datos migración fronteriza
│   ├── data_manager.py        # Carga de microdatos GEIH
│   └── fuentes/               # Datos DANE-GEIH
│       └── dane_geih*.py      # Extractores de datos oficiales
│
├── services/                   # Lógica de negocio
│   ├── estadisticas_service.py   # Cálculos estadísticos
│   ├── outlier_service.py        # Detección de outliers
│   └── correlacion_service.py    # Análisis de correlación
│
├── visualizations/             # Figuras Plotly
│   ├── mapa.py               # Mapa de Colombia
│   ├── gauss.py              # Distribución normal
│   ├── tendencias.py          # Evolución temporal
│   ├── ranking.py             # Ranking de ciudades
│   ├── correlacion.py         # Correlación fronteriza
│   ├── sectores.py            # Sectores económicos
│   ├── genero.py             # Distribución por género
│   ├── heatmap.py             # Matriz de correlación
│   └── dane_sectores.py       # Sectores DANE nacionales
│
├── ui/                        # Interfaz de usuario
│   ├── layout.py             # Estructura de la UI
│   ├── components/
│   │   ├── navbar.py         # Barra de navegación
│   │   └── cards.py          # Tarjetas KPI
│   └── callbacks/
│       ├── __init__.py       # Registro de callbacks
│       ├── map_callbacks.py
│       ├── stats_callbacks.py
│       └── extra_callbacks.py
│
└── utils/                     # Utilidades
    ├── formatters.py
    └── helpers.py
```

---

## ⚡ Instalación y Ejecución

```bash
# Clonar el repositorio
git clone https://github.com/Salfonsogar/EmpleaData.git
cd EmpleaData

# Crear entorno virtual
python -m venv venv
source venv/bin/activate  # Linux/Mac
# venv\Scripts\activate  # Windows

# Instalar dependencias
pip install -r requirements.txt

# Ejecutar aplicación
python app.py
```

La aplicación estará disponible en: **http://127.0.0.1:8050**

---

## 📚 Dependencias

| Paquete | Propósito |
|---------|-----------|
| **Dash** | Framework web para aplicaciones analíticas |
| **Plotly** | Gráficos interactivos |
| **Pandas** | Manipulación de datos |
| **NumPy** | Computación numérica |
| **SciPy** | Algoritmos estadísticos |

---

## 📊 Datos

### Ciudades Analizadas (16)
- **Triángulo de Oro**: Bogotá, Medellín, Cali
- **Caribe**: Barranquilla, Cartagena, Santa Marta, Valledupar, Montería, Sincelejo, Riohacha
- **Santanderes**: Bucaramanga, Cúcuta
- **Fronterizo**: Quibdó, Arauca, Leticia, Pasto

### Período
- **Rango**: 2021-2026
- **Fuente**: DANE-GEIH (Gran Encuesta Integrada de Hogares)

---

## 🔬 Metodología

1. **Extracción**: Datos crudos del DANE-GEIH (microdatos)
2. **Transformación**: Cálculo de tasas de ocupación (OCI)
3. **Validación**: Verificación de rangos (20%-85%)
4. **Imputación**: Valores faltantes por promedio regional
5. **Simulación**: Generación de muestras usando distribuciones normales
6. **Visualización**: Gráficos interactivos con Plotly

---

## 📈 Resultados Clave (2021-2026)

- **Crecimiento nacional**: +5.3 puntos porcentuales
- **Ciudad líder**: Montería (67.6%)
- **Mayor crecimiento**: Cali (+10.1pp)
- **Promedio nacional 2026**: 56.3%

*Ver `ANALISIS.md` para conclusiones detalladas.*

---

## 📝 Notas Académicas

- La aplicación carga **datos reales** del DANE-GEIH cuando están disponibles
- Como fallback, utiliza datos sintéticos calibrados con fuentes históricas
- La semilla aleatoria es determinista (hash ciudad + año) para reproducibilidad
- Arquitectura basada en patrones **Service Layer** y principios **SOLID**

---

## 📄 Licencia

Proyecto académico - Universidad Popular del Cesar (UniCésar)

---

**Desarrollado con ❤️ para el análisis de empleabilidad en Colombia**  
*Modelado y Simulación Estocástica - 2026*