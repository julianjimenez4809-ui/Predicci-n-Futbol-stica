# Regresión Logística
**Machine Learning 1 — Universidad Externado de Colombia | Julián Zuluaga**

---

## Slide 2 — El Problema: la recta no sirve para clasificar
- Regresión lineal predice cualquier número (incluso fuera de [0,1])
- Una probabilidad debe estar entre 0 y 1
- Con SDT_diff = 8 → ŷ = 1.3 (¿probabilidad del 130%? ❌)
- Con SDT_diff = −5 → ŷ = −0.6 (¿probabilidad negativa? ❌)

---

## Slide 3 — La Sigmoide: de números a probabilidades
- **σ(z) = 1 / (1 + e⁻ᶻ)**
- z = 0 → P = 0.5 (umbral de decisión)
- z = 6 → P ≈ 1 (sí)
- z = −6 → P ≈ 0 (no)
- Siempre entre 0 y 1
- Forma de S: suave transición de "no" a "sí"

---

## Slide 4 — Lineal vs Logística
| | Lineal | Logística |
|---|---|---|
| Predice | Un número (ŷ ∈ ℝ) | Una probabilidad (P ∈ [0,1]) |
| Función de costo | MSE | Log-Loss |
| Aprende con | OLS | MLE |
| Output | Valor continuo | Probabilidad → clase |
| Ejemplo | Goles en un partido | ¿Gana el local? |

---

## Slide 5 — Odds y Log-Odds
- **Odds = P / (1−P)** — "por cada derrota, ¿cuántas victorias?"
- Si P = 0.75 → Odds = 3:1 → "gana 3 veces por cada vez que pierde"
- **Log-odds = log(P/(1−P)) = β₀ + β₁x** → escala lineal
- β₁ → e^β₁ = 1.49 → los odds se multiplican ×1.49 por unidad de x

---

## Slide 6 — Frontera de Decisión
- Divide la predicción de clases: 0 vs 1
- Una línea recta separa las clases en 2D
- P = 0.5 cuando Log-odds = 0
- La frontera es **lineal** en el espacio de features

---

## Slide 7 — Log-Loss: la función de costo
- **Log-Loss = −[y·log(P) + (1−y)·log(1−P)]**
- OLS minimiza error²; Logística maximiza probabilidad (MLE)
- Castiga más cuando el modelo está muy equivocado y se equivoca
- Clase real = 1: si dice P = 0.95 → penalización pequeña
- Clase real = 0: si dice P = 0.95 → penalización enorme

---

## Slide 8 — Multiclase: cuando hay más de 2 opciones
> H / D / A — Cuando hay más de 2 opciones

---

## Slide 9 — ONE-VS-REST (OvR)
- 3 resultados posibles → entrenar 3 modelos independientes:
  1. **Modelo 1:** Home vs (Draw + Away)
  2. **Modelo 2:** Draw vs (Home + Away)
  3. **Modelo 3:** Away vs (Home + Draw)
- **Predicción = clase con mayor probabilidad**

---

## Slide 10 — Benchmark: ¿Pueden superar a Bet365?
- **H/D/A** — 3 clases
- **50.2% accuracy Bet365** — 291 partidos
- Mejor predictor: shots → SOT diff

---

## Slide 11 — LDA vs QDA vs Logística
- **LDA:** asume distribución gaussiana por clase, frontera lineal
- **QDA:** permite fronteras curvas (más flexible)
- **Logística:** menos supuestos, más robusta
> **Logística + OvR: el estándar para multiclase**

---

## Slide 12 — Taller 2: Predicción Premier League
**Entrega: 17 de abril de 2026**

Next Steps:
1. **Modelo Logístico OvR:** predecir H / D / A
2. **Features:** shots, SOT, corners, odds, possession
3. **Benchmark:** superar el 50.2% de Bet365
4. **Próximo tema:** Regularización (Ridge, Lasso)
