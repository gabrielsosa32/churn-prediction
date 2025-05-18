import streamlit as st
import pandas as pd
import joblib

# Cargar modelo y columnas
model = joblib.load("modelo_churn.pkl")
columnas = joblib.load("columnas_modelo.pkl")

# Definí qué columnas son numéricas y cuáles categóricas
columnas_numericas = ['AccountWeeks', 'DataUsage', 'DayMins', 'EveMins', 'NightMins', 'CustServCalls', 'MonthlyCharge', 'OverageFee', 'RoamMins']
columnas_binarias = ['ContractRenewal', 'DataPlan', 'InternationalPlan']  # 'Yes'/'No'
columnas_categoricas = ['Gender']  # Ejemplo si tuvieras 'Male', 'Female'

st.title("📊 Predicción de Churn")
st.write("Completá los datos del cliente:")

# Recolectar inputs
input_dict = {}

for col in columnas:
    if col in columnas_numericas:
        input_dict[col] = st.number_input(f"{col}:", step=0.01)
    elif col in columnas_binarias:
        input_dict[col] = st.selectbox(f"{col} (0 = No, 1 = Sí):", [0, 1])
    elif col in columnas_categoricas:
        input_dict[col] = st.selectbox(f"{col}:", ['Male', 'Female'])
    else:
        input_dict[col] = st.text_input(f"{col} (texto):")

# Convertir a DataFrame
input_df = pd.DataFrame([input_dict])

# Opcional: si tu modelo espera dummies (get_dummies), hacelo acá
# input_df = pd.get_dummies(input_df).reindex(columns=columnas, fill_value=0)

# Predicción
if st.button("Predecir"):
    try:
        pred = model.predict(input_df)[0]
        st.success(f"Resultado: {'🚨 Abandona' if pred == 1 else '✅ No abandona'}")
    except Exception as e:
        st.error(f"Error al predecir: {e}")