# Taller 2 — Machine Learning I
## Universidad Externado de Colombia · Premier League 2025-26

Este repositorio contiene el Taller 2 de Machine Learning I, en el cual construimos un pipeline completo de predicción deportiva entrenado sobre datos reales de la Premier League 2025-26. La pregunta que guía el trabajo es simple pero difícil de responder: ¿puede un modelo de machine learning predecir el resultado de un partido de fútbol con mayor precisión que una casa de apuestas?

El benchmark concreto es Bet365, que históricamente acierta alrededor del 50.2% de los partidos. Nosotros llegamos a 49.4% con validación cruzada real sobre n=241 partidos, lo que deja claro que el mercado de apuestas ya procesa casi toda la información disponible en sus cuotas. El proyecto documenta esto de forma honesta: no maquillamos los resultados con split simple ni elegimos métricas convenientes.

**Integrantes**
- Julian Camilo Jimenez Rodriguez
- Julian Steven Duarte Gomez

---

### Qué contiene el proyecto

El trabajo se divide en dos modelos principales y una serie de análisis complementarios:

**Modelo A — Regresión Lineal sobre goles totales.** Se predice el número de goles en un partido como variable continua. El R² negativo que obtenemos no es un error: es el resultado académicamente correcto cuando los goles siguen una distribución Poisson y la correlación máxima entre cualquier feature pre-partido y el total de goles es de apenas 0.10. El análisis incluye verificación de los cinco supuestos de regresión lineal (Shapiro-Wilk, Durbin-Watson, VIF) y K-Fold CV cronológico.

**Modelo B — Match Predictor (H/D/A).** Regresión logística One-vs-Rest entrenada con las odds de Bet365 como features principales. Se evaluaron 10 configuraciones de modelos con 5-Fold CV estratificado, incluyendo XGBoost, Random Forest y Gradient Boosting. La logística con C=0.1 fue la más robusta.

**Modelo xG — Expected Goals.** Regresión logística sobre 7.198 tiros con AUC-ROC de 0.774. Predice la probabilidad de gol para cada disparo en función de la distancia, el ángulo, el tipo de tiro y la posición del jugador.

**Bonus — Clustering de estilos de juego.** K-Means con k=4 sobre los 20 equipos de la liga. Los cuatro perfiles resultantes (Top-Tier, Defensivos, Contragolpe, En Riesgo) tienen interpretación futbolística directa.

---

### Dashboard

El proyecto incluye un dashboard interactivo desplegado en Vercel que cubre los ocho módulos del análisis: exploración de datos, modelo xG, shot map, predictor 1 vs 1, regresión lineal, clustering y comparación de modelos.

[Ver dashboard en Vercel](https://predicci-n-futbol-stica-i7ra.vercel.app)

---

### Estructura del repositorio

```
cuadernos/
  eda_modelos.ipynb              # EDA, modelo xG, ROC, clustering
  match_predictor_model.ipynb    # Regresión lineal, logística, comparación de modelos

src/
  feature_engineering_matches.py # Pipeline de features con rolling stats 5 partidos

data/
  matches_processed.csv          # 241 partidos con 22 features procesadas

dashboard/
  index.html                     # SPA del dashboard (dark theme, vanilla JS)
  data/predictions.json          # 380 predicciones pre-computadas

img/
  *.png                          # 14 gráficos para presentación (180 DPI)

docs/
  taller2-ml1-premier-league.md  # Enunciado completo del taller
```

---

### Reproducibilidad

```bash
pip install -r requirements.txt
python src/feature_engineering_matches.py
jupyter notebook cuadernos/match_predictor_model.ipynb
```

Los notebooks están organizados para ejecutarse de arriba a abajo sin configuración adicional. Los paths son relativos al repositorio.
