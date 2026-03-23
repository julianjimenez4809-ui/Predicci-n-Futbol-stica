# ⚽ ¿Puedes Predecir el Fútbol Mejor que las Casas de Apuestas?

## Taller 2 - Machine Learning I (2025-26)
**Universidad Externado de Colombia**

Este proyecto busca construir un pipeline completo de Machine Learning para predecir eventos y resultados de la **Premier League 2025-26**, utilizando datos reales de eventos, jugadores y cuotas de apuestas. El gran objetivo es superar el benchmark de **Bet365 (49.8% de precisión)**.

---

## 👥 Integrantes
*   **Integrante 1:** [Nombre Completo / Código]
*   **Integrante 2:** [Nombre Completo / Código]

---

## 🚀 Dashboard del Proyecto
🔗 **URL del Dashboard:** [Inserta aquí tu URL de Netlify/Vercel/Streamlit]

---

## 📂 Estructura del Proyecto
```text
├── data/               # Datasets en CSV (Events, Matches, Players)
├── docs/               # Enunciado y planeación del proyecto
├── src/                # Código fuente (.py y .ipynb)
│   ├── eda_modelos.ipynb   # Análisis Exploratorio y Entrenamiento
│   └── robust_download.py  # Script de adquisición de datos
├── requirements.txt    # Dependencias del proyecto
└── README.md           # Descripción general (este archivo)
```

---

## 🧠 Modelos Implementados

### 1. Expected Goals (xG) - ¿Gol o No Gol?
*   **Modelo:** Regresión Logística.
*   **Objetivo:** Predecir la probabilidad de que un tiro sea gol basándose en la posición (`x,y`), ángulo, distancia y calificadores (`BigChance`, `Head`, etc.).
*   **Métricas:** Accuracy, Precision, Recall, F1-Score y AUC-ROC.

### 2. Match Predictor - ¿Quién Gana?
*   **Parte A (Regresión Lineal):** Predicción de goles totales por partido.
*   **Parte B (Regresión Logística):** Predicción del resultado (Local, Empate o Visitante).
*   **Benchmark:** Superar el 49.8% de precisión de las casas de apuestas.

---

## 🛠️ Requisitos e Instalación
1. Clonar el repositorio.
2. Crear un entorno virtual: `python -m venv .venv`
3. Instalar dependencias: `pip install -r requirements.txt`
4. Los datos ya se encuentran en la carpeta `data/` listos para procesar.

---

## 📊 Dashboard y Visualizaciones
El dashboard incluye:
*   **Shot Map:** Visualización de tiros según probabilidad xG.
*   **Predictor 1 vs 1:** Interfaz para predecir enfrentamientos entre cualquier pareja de equipos.
*   **EDA:** Insights clave sobre la temporada de la Premier League.
# Predicci-n-Futbol-stica
