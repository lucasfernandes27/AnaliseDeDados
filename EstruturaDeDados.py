import pandas as pd

lista_nomes = ['caue', 'lucas', 'clara']
print(lista_nomes)
print("Primeiro da lista: ", lista_nomes[0])

dicionario = {
    #cada pedaço desse é uma chave
        'nome': 'Lucas',
        'idade': 22,
        'Cidade': 'Recife'
}
# \n pular linha
print('Dicionario de pessoa: \n ',dicionario)
#pegar apenas uma coisa
print('Atributo: \n', dicionario.get('nome'))

dados = [
    {'nome': 'Lucas', 'Idade': 22 ,'Cidade':'Recife',},
    {'nome': 'Ana', 'Idade': 28, 'Cidade': 'São Paulo'},
    {'nome': 'Marcos', 'Idade': 35, 'Cidade': 'Belo Horizonte'},
    {'nome': 'Juliana', 'Idade': 19, 'Cidade': 'Curitiba'}
]
#tabela bem certinha
df = pd.DataFrame(dados)
print('Data Frame \n',df)

#selecionar coluna
print(df['nome'])

#selecionar linha
print(df[['nome','Idade']])

#slecionar linha por indice
print('Primeira linha \n', df.loc[0])

#adicionar
#df['Salario'] = [4100, 3200, 2400]

#remover
#df.drop('Salario', axis=1, inplace=True)

#filtro
filtro_idade = df[df['Idade'] >= 30]