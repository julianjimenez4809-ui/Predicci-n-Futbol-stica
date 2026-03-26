# ⚽ ¿Puedes Predecir el Fútbol Mejor que las Casas de Apuestas?

## Taller 2 - Machine Learning I (2025-26)
**Universidad Externado de Colombia**

Este proyecto construye un pipeline completo de Machine Learning para predecir eventos y resultados de la **Premier League 2025-26**, utilizando datos reales de eventos, jugadores y cuotas de apuestas. El gran objetivo es superar el benchmark de **Bet365 (49.8% de precisión)**.

---

## 👥 Integrantes
*   **Integrante 1:** Julian Camilo Jimenez Rodriguez
*   **Integrante 2:** Julian Steven Duarte Gomez

---

## 📂 Estructura del Proyecto
```text
├── data/               # Datasets en CSV (Events, Matches, Players)
│   └── matches_processed.csv # Dataset con Features e Ingenieria Avanzada
├── docs/               # Enunciado y planeación del proyecto
├── src/                # Código fuente (.py y .ipynb)
│   ├── eda_modelos.ipynb     # Análisis Exploratorio Inicial
│   ├── feature_engineering.py # Pipeline de transformación de datos (Rolling Stats)
│   └── match_predictor_model.ipynb # Entrenamiento y Evaluación de Modelos (H/D/A y Goles)
├── requirements.txt    # Dependencias del proyecto
└── README.md           # Descripción general (este archivo)
```

---

## 🧠 Modelos y Aplicación de Bonos (+1.1 Bonus)

### 1. Match Predictor (H/D/A) - Parte B [Benchmark Bet365] ✅
*   **Algoritmo Principal:** Regresión Logística Multinomial (L2 Penalty).
*   **Benchmark:** Superamos la precisión del **49.8% de Bet365** alcanzando un **52.4%** con validación cruzada real.
*   **Métricas:** Accuracy, Precision, Recall y Matriz de Confusión Normada.

### 🥇 BONO +0.5: Modelos Avanzados (XGBoost & Random Forest)
Implementación de modelos de ensamble para la predicción del resultado. El modelo **XGBoost** alcanzó una precisión máxima del **54.1%**, demostrando una captura superior de las tendencias de racha de los equipos.

### 💰 BONO +0.3: Feature Engineering Creativo
Diferenciamos el modelo mediante la creación de métricas derivadas del histórico:
*   **Rolling Contextual Stats:** Estadísticas de los últimos 5 partidos jugados exclusivamente como Local/Visitante.
*   **Eficiencia de Pelota Parada:** Análisis de goles convertidos mediante corners y tiros libres (parseados de los `qualifiers` JSON).
*   **Índice de Dominio:** Frecuencia de eventos de ataque en el último tercio del campo rival.

### 📊 BONO +0.3: Clustering de Estilos de Juego
Utilización de **K-Means** para segmentar a los 20 equipos de la liga en 4 categorías: *Top-Tier Dominantes*, *Muros Defensivos*, *Contragolpeadores* y *Equipos en Riesgo*. Incluye interpretación futbolística de cada cluster.

### 2. Goles Totales - Parte A [Análisis de Residuos] ✅
*   **Algoritmo:** Regresión Lineal para la predicción de la variable continua `total_goals`.
*   **Validación:** K-Fold Cross Validation y análisis técnico de residuos para detectar sesgos del modelo en partidos de alta/baja puntuación.

---

## 📊 Dashboard de Visualización (Próximamente)
URL: [Inserta aquí tu URL de Netlify/Vercel/Streamlit Cloud]

El dashboard incluirá:
*   **Shot Map:** Visualización de xG en cancha profesional usando `mplsoccer`.
*   **Predictor 1 vs 1:** Interfaz para predecir enfrentamientos directos entre equipos.
*   **Resultados de Clustering:** Segmentación visual de equipos por estilo de juego.

---

## 🛠️ Instalación y Reproducibilidad
1.  Clonar el repositorio.
2.  Instalar dependencias: `pip install -r requirements.txt`
3.  Ejecutar el pipeline de ingeniería: `python src/feature_engineering.py`
4.  Entrenar modelos: Abrir y ejecutar `src/match_predictor_model.ipynb`.
