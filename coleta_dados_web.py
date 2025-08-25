
import requests
from bs4 import BeautifulSoup

url = 'http://wiki.python.org.br/AprendaMais'
#faz a requisicao
requisicao = requests.get(url)
#puxa oq vc quer do texto
extracao = BeautifulSoup(requisicao.content, 'lxml')

#exibe o texto
#strip remove os espaços em branco
print(extracao.text.strip())

#filtrar para exibir titulos
for linha_texto in extracao.find_all('h2'):
    #remover os espaços
    titulo = linha_texto.text.strip()
    print( 'Titulo', titulo)

contar_titulos = 0
contar_paragrafos = 0
for linha_texto in extracao.find_all(['h2','p']):
            if linha_texto.name  == 'h2':
                contar_titulos += 1 #contar
            elif linha_texto.name == 'p':
                contar_paragrafos += 1

print(contar_titulos, contar_paragrafos)