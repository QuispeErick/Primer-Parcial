import pandas as pd
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.compose import ColumnTransformer

# Cargar el dataset
df = pd.read_csv('monito.csv')

# Imputación de valores faltantes (SimpleImputer)
print("Imputación de valores faltantes:")
imputer = SimpleImputer(strategy='median')  # Se utiliza la mediana para llenar los valores faltantes
#numeric_cols = ["Number of Test Takers", "Critical Reading Mean", "Mathematics Mean", "Writing Mean"]

numeric_cols1 = ["Number of Test Takers"]
numeric_cols2 = ["Critical Reading Mean"]
numeric_cols3 = ["Mathematics Mean"]
numeric_cols4 = ["Writing Mean"]

df[numeric_cols1] = imputer.fit_transform(df[numeric_cols1])
print(df.head())
print("__________________________________________________________")

# Escalado (StandardScaler)

#La estandarización es útil en muchos algoritmos
# de aprendizaje automático, ya que ayuda a que las
# características estén en la misma escala, lo que puede
# mejorar la convergencia del modelo y evitar que ciertas
# características dominen el proceso de optimización.
print("Escalado (StandardScaler):")
scaler = StandardScaler()  # Se utiliza para estandarizar las características numéricas
df[numeric_cols2] = scaler.fit_transform(df[numeric_cols2])
print(df.head())
print("__________________________________________________________")

# Definir las columnas a transformar y las transformaciones a aplicar
categorical_cols = ['School Name']
preprocessor = ColumnTransformer(
    transformers=[
        ('num', 'passthrough', numeric_cols3),  # Mantener las columnas numéricas sin cambios
        ('cat', OneHotEncoder(), categorical_cols)  # Aplicar OneHotEncoder a las columnas categóricas
    ])

# Codificación One-Hot con get_dummies de Pandas
print("Codificación One-Hot con get_dummies de Pandas:")
df_encoded_pd = pd.get_dummies(df, columns=['School Name'])  # Se utiliza para convertir las variables categóricas en variables binarias
print(df_encoded_pd.head())
print("__________________________________________________________")


# Eliminación de columnas con pocos datos
print("Eliminación de columnas con pocos datos:")
df = df.dropna(thresh=len(df) * 0.7, axis=1)  # Se eliminan las columnas que tienen más del 70% de valores faltantes
print(df.head())
print("__________________________________________________________")

# Binarización de características numéricas
print("Binarización de características numéricas:")
threshold = 400  # Umbral para binarizar las características
df[numeric_cols4] = (df[numeric_cols4] > threshold).astype(int)  # Binarizar las características según el umbral
print(df.head())
print("__________________________________________________________")

# Guardar el dataset preprocesado
df.to_csv('monito_preprocesado.csv', index=False)
