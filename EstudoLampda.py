import pandas as pd

def eleva_cubo(x):
    return x ** 3

#calcular o cubo do numero
eleva_cubo_lambda = lambda x: x ** 3

print(eleva_cubo(2))
print(eleva_cubo_lampba(2))

df = pd.DataFrame({'numeros ' : [1,2,3,4,5]})

df['cubo da Funcao'] = df['numeros'].apply(eleva_cubo)
df['cubo da Funcao'] = df['numeros'].apply(lambda x: x ** 3)
print(df)