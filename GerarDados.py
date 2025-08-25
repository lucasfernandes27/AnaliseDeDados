import pandas as pd
import random
from faker import Faker

faker = Faker('pt_BR')

dados_pessoas = []

#cria até 10 dados fake
for _ in range(10):
    nome = faker.name()
    cpf = faker.cpf()
    idade = faker.random_int(min=18, max=60)
    #organização da data
    data = faker.date
    endereco = faker.address()
    estado = faker.city()
    pais = 'Brasil'

    pessoa = {
        'nome': nome,
        'cpf': cpf,
        'idade': idade,
        'endereco': endereco,
        'estado': estado,
        'pais': pais

    }

    #adicionar pessoas a lista
    dados_pessoas.append(pessoa)

#criara data frame
df_pessoas = pd.DataFrame(dados_pessoas)

print(df_pessoas)

print (df_pessoas.to_string())

df_pessoas.to_csv('clientes.csv')
