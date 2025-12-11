import pandas as pd       # Para manejar datos en tablas
import numpy as np        # Para operaciones numéricas
import matplotlib.pyplot as plt  # Para gráficos básicos
import seaborn as sns     # Para gráficos más avanzados

# Cargar archivo CSV
df = pd.read_csv("C:/Users/xps/Desktop/Desarrollos_2025/Data Scientist/Analisis exploratorio de datos/data/Titanic-Dataset.csv")

# Ver primeras 5 filas
print("Primeras 5 filas:")
print(df.head())

# Dimensiones de nuestro Dataset
print("\nDimensiones del dataset (filas, columnas):")
print(df.shape)

# Info columnas
print("\nInformación general del dataset:")
df.info()

# Valores nulos
print("\nValores nulos por columna:")
print(df.isnull().sum())

# Resumen estadístico de columnas que sean numericas
print("\nResumen estadístico de variables numéricas:")
print(df.describe())