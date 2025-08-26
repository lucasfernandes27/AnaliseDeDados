import pandas as pd

df = pd.read_csv('clientes.csv')

#verificar registros
print(df.head().to_string())

#verificar qtd de linhas
print("qtd: ", df.shape)

#verificar dados
print("Tipos: \n", df.dtypes)

#checar nulos
print("Valores nulos: \n", df.isnull().sum())