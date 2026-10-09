#Iram Jimenez NC = 0079
#NL = 32 = datos2
import pandas as pd

print(pd.__version__) # Output: 1.5.2

# 1. Crear un dataset de ejemplo simular a un CSV
# 2.
datos2 = {
    'distancia_km': [1.5, 3.2, 6.0, 2.8, 4.5],
    'trafico_nivel': [2, 1, 3, 2, 1],
    'edad_repartidor': [25, 30, 22, 45, 28],
    'tiempo_entrega_min': [12, 22, 55, 24, 30]
} # Lo que queremos predecir


df = pd.DataFrame(datos2)

# 2. Separar Variables de Entrada (X) y Variable Objetivo (y)
X = df[['distancia_km', 'trafico_nivel', 'edad_repartidor']] # Features / Entradas
y = df['tiempo_entrega_min']                                  # Target / Salida

# 3. Mostrar estructura
print("--- DATOS DE ENTRADA (FEATURES - X) ---")
print(X.head(2))

print("\n--- VARIABLE OBJETIVO (TARGET - y) ---")
print(y.head(2))
print("Iram Jimenez NC = 0079")

