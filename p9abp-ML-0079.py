#Iram Jimenez NC = 0079
import pandas as pd
print(pd.__version__) # Output: 1.5.2
# 1. Crear un dataset de ejemplo similar a un CSV
datos = {
    'id_paciente': [101, 102, 103, 104, 105],
    'edad': [45, 62, 29, 54, 38],
    'nivel_glucosa': [110, 180, 85, 210, 95],
    'presion_arterial': [80, 95, 70, 100, 75],
    'indice_masa_corporal': [24.5, 31.2, 21.0, 34.8, 26.1],
    'diagnostico_diabetes': [0, 1, 0, 1, 0] # 0: No tiene riesgo / 1: Tiene riesgo (Lo que queremos predecir)
}

df = pd.DataFrame(datos)

# 2. Separar Variables de Entrada (X) y Variable Objetivo (y)
# Excluimos 'id_paciente' de las características porque no aporta información predictiva
X = df[['edad', 'nivel_glucosa', 'presion_arterial', 'indice_masa_corporal']] # Features / Entradas
y = df['diagnostico_diabetes']                                            # Target / Salida

# 3. Mostrar estructura
print("--- DATOS DE ENTRADA (FEATURES - X) ---")
print(X.head(2))

print("\n--- VARIABLE OBJETIVO (TARGET - y) ---")
print(y.head(2))
print("Iram Jimenez NC = 0079")