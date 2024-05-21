import csv
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

def read_csv(file_name):
    with open(file_name, 'r') as file:
        reader = csv.DictReader(file)
        data = list(reader)
    return data

def extract_numeric_data(data, key):
    numeric_data = []
    for row in data:
        try:
            value = float(row[key])
            if value:
                numeric_data.append(value)
        except ValueError:
            continue
    return numeric_data

def percentile(data, percent):
    data_sorted = sorted(data)
    k = (len(data_sorted) - 1) * percent
    f = int(k)
    c = k - f
    if f + 1 < len(data_sorted):
        return data_sorted[f] + (data_sorted[f + 1] - data_sorted[f]) * c
    return data_sorted[-1]


def geometric_mean(data):

    data = data.dropna()
    data = data[data > 0]
    if len(data) == 0:
        return np.nan
    log_data = np.log(data)
    return np.exp(log_data.mean())


data = read_csv('monito.csv')

# Inciso A
print("-" * 40)
keys = ["Number of Test Takers", "Critical Reading Mean", "Mathematics Mean", "Writing Mean"]


for key in keys:
    col_data = extract_numeric_data(data, key)
    if col_data:  # Ensure there is data to process
        q3 = percentile(col_data, 0.75)
        p80 = percentile(col_data, 0.80)
        print(f"{key} - Q3: {q3}, Percentil 80: {p80}")
    else:
        print(f"{key} - No valid numeric data available.")

# Inciso B
print("-" * 40)
df = pd.read_csv('monito.csv')


df_numeric = df[["Number of Test Takers", "Critical Reading Mean", "Mathematics Mean", "Writing Mean"]]
df_numeric = df_numeric.apply(pd.to_numeric, errors='coerce')

q3 = df_numeric.quantile(0.75)
p80 = df_numeric.quantile(0.80)

print("Q3:\n", q3)
print("Percentil 80:\n", p80)

# Inciso C
print("-" * 40)

# Calcular media, mediana y moda
mean = df_numeric.mean()
median = df_numeric.median()
mode = df_numeric.mode().iloc[0]

# Calcular la media geométrica
geometric_mean_values = df_numeric.apply(geometric_mean)


print("Media:\n", mean)
print("Mediana:\n", median)
print("Moda:\n", mode)
print("Media Geométrica:\n", geometric_mean_values)

# Inciso D

# Histogramas
df_numeric.hist(bins=50, figsize=(12, 8))
plt.suptitle('Grafico')
plt.show()