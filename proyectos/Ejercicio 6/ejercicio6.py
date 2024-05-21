
import pandas as pd
import numpy as np
from sklearn.tree import DecisionTreeClassifier, plot_tree
import matplotlib.pyplot as plt

# Cargar el dataset
df = pd.read_csv('monito.csv')

# Preprocesar el dataset
df = df.replace(np.nan, 0)

# se predice el 'Mathematics Mean'
explicativas = df.drop(columns='Mathematics Mean')
objetivo = df['Mathematics Mean']

# Convertir las variables categóricas a numéricas
explicativas = pd.get_dummies(explicativas)

# Crear y entrenar el modelo
model = DecisionTreeClassifier(max_depth=3)
model.fit(X=explicativas, y=objetivo)

# Visualizar el árbol de decisiones
plt.figure(figsize=(20,10))
plot_tree(decision_tree=model, feature_names=explicativas.columns, filled=True, fontsize=8)
plt.show()
