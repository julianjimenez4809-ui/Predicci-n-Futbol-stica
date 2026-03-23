# 🚜 Planeación del Proyecto: Taller 2 - Premier League Predictor

Este documento detalla la hoja de ruta para el desarrollo del proyecto de Machine Learning I, con un cronograma ajustado para cumplir la fecha de entrega del **29 de marzo de 11:59 PM**.

---

## 🗓️ Cronograma General (10 Días)

| Fase | Tareas | Responsable | Estado | Fecha Límite |
| :--- | :--- | :--- | :--- | :--- |
| **I. Adquisición de Datos** | Descargar CSVs completos, verificar integridad y estructura. | Antigravity | Finalizada ✅ | 20 Mar |
| **II. EDA & Feature Engineering** | Limpieza de datos, cálculo de distancia/ángulos, parseo de JSON `qualifiers`. | Integrante 1 / 2 | En Progreso 🔄 | 22 Mar |
| **III. Modelo 1 (xG)** | Implementar Regresión Logística, evaluar Accuracy, Precision, Recall y AUC. | Integrante 1 | Pendiente 📅 | 24 Mar |
| **IV. Modelo 2 (Match Predictor)** | Regresión Lineal (goles) y Logística (H/D/A) con k-fold CV. Benchmark vs B365. | Integrante 2 | Pendiente 📅 | 24 Mar |
| **V. Dashboard & Frontend** | Construcción de Shot Map, interfaz de predicción y visualizaciones interactivas. | Integrante 2 | Pendiente 📅 | 26 Mar |
| **VI. Integración & Deploy** | Desplegar en Vercel/Netlify, crear README final y `requirements.txt`. | Integrante 1 | Pendiente 📅 | 28 Mar |
| **VII. Revisión Final** | Pruebas de reproducibilidad y envío final de repositorio y formulario. | Integrantes 1 y 2 | Pendiente 📅 | 29 Mar |

---

## 👥 Reparto de Responsabilidades (Equipo de 2)

### **🤝 Responsabilidades Compartidas**
*   **Análisis Exploratorio Inicial (EDA):** Ambos deben entender las variables correlacionadas con goles y victorias.
*   **Feature Engineering Creativo:** Brainstorming para definir qué `qualifiers` aportan más información.

### **👤 Integrante 1: "Especialista en Eventos y Probabilidad"**
*   **Foco Principal:** `events.csv` y **Modelo 1 (xG)**.
*   **Tareas Específicas:**
    *   Cálculo de métricas de tiro (Distancia, Ángulo, parte del cuerpo).
    *   Optimización del modelo de Regresión Logística de goles.
    *   Construcción de la matriz de confusión y curvas ROC para xG.
    *   Apoyo en el Shot Map del Dashboard.

### **👤 Integrante 2: "Especialista en Resultados y Dashboard"**
*   **Foco Principal:** `matches.csv` y **Modelo 2 (Match Predictor)** + **Dashboard**.
*   **Tareas Específicas:**
    *   Manejo de cuotas de apuestas (Odds) y cálculo de promedios móviles (rolling stats).
    *   Implementación de Regresión Lineal y Logística para partidos con Cross-Validation.
    *   Diseño del Dashboard Web (Sección Predictor e Interfaz).
    *   Gestión del Deploy final del sitio web.

---

## 🛠️ Stack Tecnológico
*   **Procesamiento:** `pandas`, `numpy`.
*   **ML:** `scikit-learn` (LogisticRegression, LinearRegression, model_selection).
*   **Visualización:** `matplotlib`, `seaborn`, `mplsoccer`, `plotly`.
*   **Dashboard:** `Streamlit`, `Flask` + `D3.js` o similar.

---

## 🔥 Riesgos & Mitigación
*   **Riesgo:** Inestabilidad de la API -> **Mitigación:** Ya descargamos los CSVs en local para trabajar offline.
*   **Riesgo:** Sesgo hacia "No Gol" en xG -> **Mitigación:** Usar métricas como F1-Score y AUC, no solo Accuracy.
*   **Riesgo:** Data Leakage en Match Predictor -> **Mitigación:** Asegurar que las features del partido se calculen con datos previos al encuentro.
