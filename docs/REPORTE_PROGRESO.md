# 📓 Reporte de Progreso Técnico: Predicción Futbolística PL

Este documento resume las fases completadas del proyecto de Machine Learning para la predicción de resultados en la Premier League. Su objetivo es proporcionar contexto completo a cualquier miembro del equipo sobre las decisiones técnicas y el estado actual de los modelos.

---

## 1. Configuración de Infraestructura y Entorno

*   **Entorno Virtual:** Se configuró un entorno Python (`.venv`) con las librerías necesarias registradas en `requirements.txt` (Pandas, Scikit-Learn, Mplsoccer, Seaborn, Plotly, Unidecode).
*   **Estrategia de Ramas (Git Flow):**
    *   `main`: Producción/Entregable final.
    *   `develop`: Integración de características.
    *   `feature/xg-model`: Desarrollo del modelo de Goles Esperados (actual).
    *   `feature/match-predictor-dashboard`: Espacio para el modelo de predicción de partidos.

---

## 2. ETL y Procesamiento de Datos (Pipeline)

Se trabajó con tres fuentes principales: `matches.csv`, `players.csv` y `events.csv`.

### Limpieza de Eventos (Opta JSON)
*   Se desarrolló un parser para la columna `qualifiers`.
*   Extraídas variables clave: `is_big_chance` (Ocasión clara), `is_penalty`, `is_header`, `is_counter` (Contraataque).

### Normalización y Cruce de Jugadores
*   Se detectó una discrepancia en los IDs entre tablas.
*   **Solución:** Implementada limpieza de nombres mediante la librería `unidecode` (remoción de tildes y caracteres especiales) para permitir un cruce por nombre corto (`web_name`) de alta efectividad.

---

## 3. Ingeniería de Características (Feature Engineering)

Para el modelo de xG, se crearon las siguientes dimensiones:

1.  **Geometría Espacial:**
    *   `distance`: Distancia euclidiana al centro de la portería.
    *   `angle`: Ángulo de visión hacia el arco.
2.  **Contexto Situacional (Game State):**
    *   `score_diff`: Diferencia de goles en el momento exacto del tiro (calculado cronológicamente).
    *   `is_late_half`: Indicador de fatiga/presión en los últimos 5 min de cada tiempo.
3.  **Perfil del Ejecutor:**
    *   Variables Dummy para posiciones (`pos_FWD`, `pos_MID`, `pos_DEF`).

---

## 4. Modelo 1: Expected Goals (xG)

### Algoritmo y Entrenamiento
*   **Modelo:** Regresión Logística.
*   **Dataset:** 80% Train / 20% Test (Estratificado por clase `is_goal`).
*   **Optimización de Desbalance:** Se aplicó `class_weight='balanced'` para mejorar la detección de goles (Recall), penalizando más los fallos en la clase minoritaria.

### Evaluación de Rendimiento
| Métrica | Resultado |
| :--- | :--- |
| **AUC-ROC** | **0.825** |
| **Recall (Goles)** | ~60% (Tras balanceo) |
| **Accuracy Geral** | ~89% |

### Importancia de Variables
*   **Positivas:** `is_penalty` (máximo peso), `is_big_chance`, `pos_FWD`.
*   **Negativas:** `distance` (fuerte penalización), `is_header`.

---

## 📅 Próximos Pasos

1.  **Modelo 2 (Match Predictor):** Agregación de eventos por partido para calcular fuerza de ataque/defensa.
2.  **Dashboard:** Visualización interactiva de probabilidades de victoria.
3.  **Refinamiento:** Evaluación de modelos no lineales (Random Forest) para capturar interacciones complejas.

---
*Última actualización: 23 de marzo de 2026*
