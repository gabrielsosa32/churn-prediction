# 📉 Predicción de Abandono de Clientes (Churn Prediction)

Este proyecto implementa distintos modelos de machine learning para predecir la propensión de los clientes a abandonar una empresa. Se trabajó con técnicas de preprocesamiento, balanceo de clases, búsqueda de hiperparámetros y ensambles.

---

## 🧠 Modelos Utilizados

1. **Árbol de Decisión**
   - Entrenado sin y con búsqueda de hiperparámetros (`GridSearchCV`).
   - Evaluado con métricas de desempeño y visualización del árbol.

2. **SMOTE**
   - Aplicado para balancear las clases en el conjunto de entrenamiento.

3. **Bagging**
   - Se aplicó bagging clásico con 200 estimadores.
   - También se implementó un bagging *heterogéneo* con:
     - Regresión Logística
     - Árbol de Decisión
     - SVM con kernel `rbf` y `sigmoid`
   - Se repitió el modelo con mejor f1-score para calibrar su importancia.

4. **Random Forest**
   - Entrenado con `n_estimators=45` y evaluación usando muestra OOB.
   - Se realizó búsqueda de grilla (`GridSearchCV`) con:
     - `n_estimators`: 50 a 200 (paso de 10)
     - `max_features`: `sqrt`, `log2`, `None`

---

## 📊 Métricas Evaluadas

- Accuracy
- f1-score
- ROC AUC
- Matriz de Confusión
- Curvas ROC

---

## 🔍 Resultados y Análisis

- Se identificaron las **variables más importantes** en el modelo final (Random Forest).
- Se mostraron los **15 clientes con mayor propensión a abandonar** según el modelo.
- Se discutió la interpretación de los atributos y su relación con el problema.

---

## 💾 Archivos del Proyecto

- `churn_model.ipynb`: notebook con el desarrollo completo.
- `util_bagging.py`: función para realizar bagging heterogéneo.
- `top_clients.csv`: clientes con mayor probabilidad de abandono.
- `README.md`: este archivo.

---

## 🚀 Cómo Ejecutar

1. Cloná este repositorio:
   ```bash
   git clone https://github.com/tu_usuario/churn-prediction.git
   cd churn-prediction
