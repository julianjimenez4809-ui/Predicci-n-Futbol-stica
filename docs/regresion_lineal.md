# Regresión Lineal
**Machine Learning 1 — Universidad Externado de Colombia | Julián Zuluaga**

---

## Slide 2 — Si sé X… ¿puedo predecir Y?
- Horas de estudio → Nota del examen
- Experiencia laboral → Salario mensual
- Shots on target → Goles en un partido

---

## Slide 3 — Clasificación vs Regresión
**Clasificación** — Predice una categoría:
- Spam / No spam
- Victoria / Derrota
- KNN, Naive Bayes

**Regresión** — Predice un número:
- Precio de una casa
- Goles en un partido
- Regresión lineal

---

## Slide 4 — ¿Cómo encontrar la mejor línea?
> Residuos, MSE y Mínimos Cuadrados

---

## Slide 5 — Residuos: el error de cada predicción
- **Residuo** = valor real − valor predicho
- Líneas verticales desde cada punto hasta la recta
- Positivo → el modelo subestimó
- Negativo → el modelo sobreestimó

---

## Slide 6 — MSE: Minimizar el Error Total
- Errores +3 y −3 se cancelan → elevar al cuadrado
- **MSE = (1/n) Σ(yᵢ − ŷᵢ)²**
- OLS: encuentra los β que minimizan esa suma
- Visualmente: minimizar el área total de los cuadrados

---

## Slide 7 — Descenso del Gradiente
1. Empezar en punto aleatorio
2. Calcular la pendiente
3. Dar un paso cuesta abajo
4. Repetir hasta el mínimo
- **Learning rate:** grande = salta, chico = lento

---

## Slide 8 — Más variables, más poder
> Regresión múltiple y polinomial

---

## Slide 9 — De Simple a Múltiple
- Simple: ŷ = β₀ + β₁x (una recta)
- Múltiple: ŷ = β₀ + β₁x₁ + β₂x₂ + … (un plano / hiperplano)
- β = 0 → Sin aporte; β ≠ 0 → Tiene efecto

---

## Slide 10 — Overfitting en Regresión
- Grado 1: recta — underfitting, no captura la curva real
- Grado 3: curva suave — **buen balance**
- Grado 15: pasa por todos los puntos pero oscila salvajemente — overfitting
> Más complejo ≠ mejor modelo

---

## Slide 11 — Multicolinealidad
- Variables que miden lo mismo: Shots y Shots on Target
- Coeficientes inestables: si metes ambas, los β se vuelven inestables
- **VIF > 5** → señal de alerta
- Solución: quedarse con la más informativa

---

## Slide 12 — ¿Es bueno mi modelo? Métricas y Diagnóstico

---

## Slide 13 — Métricas de Regresión
- **MSE** = 78.4 (error² promedio)
- **RMSE** = 12.9 € (en unidades de Y)
- **MAE** = 5.2 (error absoluto)
- **R²** = 0.91 (91% de varianza explicada)

---

## Slide 14 — Los 5 Supuestos
1. **Linealidad** — La relación real es aproximadamente lineal
2. **Independencia** — Los datos no dependen entre sí
3. **Homocedasticidad** — La varianza del error es constante
4. **Normalidad** — Los residuos se distribuyen normal
5. **No multicolinealidad** — Las variables X no son redundantes

---

## Slide 15 — ¿Y si el target no es un número?
**Próximo: Regresión Logística**
- ¿Cómo predecir Victoria / Empate / Derrota?
- La función sigmoide: de números a probabilidades
- Taller 2: Predicción Premier League
