"""Trabalhando com Lista em Python

Bem-vindo ao notebook de exemplos praticos, onde trabalhamos com o recurso de
listas em Python. As listas sao uma das estruturas de dados mais versateis e
amplamente utilizadas em Python. Elas permitem armazenar uma colecao ordenada
de elementos, que podem ser de diferentes tipos, como numeros, strings e ate
mesmo outras listas. Neste notebook, exploraremos diversas operacoes que
podemos realizar com listas, desde a criacao e manipulacao basica ate tecnicas
avancadas, utilizando os principais metodos disponiveis para este tipo de
variavel.

Tutorial on-line do Python:
https://docs.python.org/3/tutorial/datastructures.html
"""

import sys


# ============================================================
# Criando uma Lista e Acessando seus Elementos
# ============================================================

# Criando uma lista
lista = [1, 2, 3, 4, 5]

# Acessando elementos da lista
primeiro_elemento = lista[0]
ultimo_elemento = lista[-1]

print("Lista completa:", lista)
print("Primeiro elemento:", primeiro_elemento)
print("Ultimo elemento:", ultimo_elemento)


# ============================================================
# Adicionando e Removendo Elementos
# ============================================================

# Criando uma lista vazia
lista = []

# Adicionando elementos a lista
lista.append(1)
lista.append(2)
lista.append(3)

print("Lista apos adicionar elementos:", lista)

# Removendo elementos da lista
elemento_removido = lista.pop()
print("Elemento removido:", elemento_removido)
print("Lista apos remover elemento:", lista)


# Juntando duas listas com extend
lista1 = [2, 3, 4, 5]
lista2 = [6, 7, 8, 9]

print(lista1)
lista1.extend(lista2)
print(lista1)


# O mesmo resultado, um elemento por vez
lista1 = [2, 3, 4, 5]
lista2 = [6, 7, 8, 9]

print(lista1)

for i in lista2:
	lista1.append(i)

print(lista1)


# Percorrendo cada letra de cada nome
nomes = ['ana', 'carlos', 'paulo', 'inaldo', 'silva']

for i in nomes:
	for j in i:
		print(j)


# ============================================================
# Ordenando uma lista
# ============================================================

# Criando uma lista desordenada
lista = [5, 2, 4, 1, 3]
print("Lista sem ordenacao:", lista)
# Ordenando a lista
lista.sort()
print("Lista ordenada crescente:", lista)
lista.sort(reverse=True)
print("Lista ordenada decrescente:", lista)


# As tres maiores idades
idade = [19, 20, 18, 27, 25, 40, 22]
idade.sort()
for i in range(-1, -4, -1):
	print(i, ' -> ', idade[i])


for i in range(10, 20, 2):
	print(i)


# Inverte a ordem dos elementos na lista.
lista1 = [5, 2, 4, 1, 3]
print(lista1)
lista1.reverse()
print(lista1)


# ============================================================
# Iterando sobre uma Lista
# ============================================================

# Iterando sobre uma lista e imprimindo cada elemento
lista = ['a', 'b', 'c', 'd', 'e']
for elemento in lista:
	print(elemento)


lista = ['a', 'b', 'c', 'd', 'e']
for elemento in lista:
	if elemento == 'x':
		print('Encontrei a letra...')


lista = ['a', 'b', 'c', 'a', 'e']
print(lista.count('a'))


lista = ['a', 'b', 'c', 'a', 'e']
if (lista.count('c') == 0):
	print('Nao encontrei')
else:
	print('Encontrei')


lista = ['a', 'b', 'c', 'd', 'e']
aux = False
for elemento in lista:
	if elemento == 'r':
		aux = True
if aux == True:
	print('Encontrei')
else:
	print('Nao Encontrei')


lista = ['a', 'b', 'c', 'd', 'e']

if 'x' in lista:
	print('Encontrei')
else:
	print('Nao Encontrei')


# ============================================================
# Lista de string
# ============================================================

lista = ['a', 'b', 'c', 'd', 'e']
ap = 0
for elemento in lista:
	if elemento == 'x':
		ap = 1
if ap == 0:
	print('Nao encontrei')
else:
	print('Encontrei')


lista = ['a', 'b', 'c', 'd', 'e']
elemento = 'x'
if elemento in lista:
	print('Encontrei')
else:
	print('Nao encontrei')


# ============================================================
# Verificando a Existencia de um Elemento
# ============================================================

# Verificando se um elemento esta presente na lista
lista = ['a', 'b', 'a', 'd', 'e']
elemento = 'e'

if elemento in lista:
	print("O elemento", elemento, "esta na lista.")
else:
	print("O elemento", elemento, "nao esta na lista.")


lista = ['a', 'b', 'c', 'd', 'e']
for i in lista:
	if i == 'a':
		print('Encontrei')


# ============================================================
# Retorna o numero de elementos de uma lista
# ============================================================

fruits = ['Orange', 'apple', 'pear', 'orange', 'kiwi', 'apple', 'banana']
print(fruits.count('orange'))


# Contando as vogais de todas as frutas
fruits = ['orange', 'apple', 'pear', 'orange', 'kiwi', 'apple', 'banana']
cv = 0
for i in fruits:
	for j in i:
		if j in ('a', 'e', 'i', 'o', 'u'):
			cv += 1
print(cv)


# Quantas frutas terminam com vogal
fruits = ['orange', 'apple', 'pear', 'orange', 'kiwi', 'apple', 'banana']
cv = 0
for i in fruits:
	if i[-1] in ('a', 'e', 'i', 'o', 'u'):
		cv += 1
print(cv)


# ============================================================
# Trabalhando com string
# ============================================================

fruits = ['orange', 'apple', 'pear', 'orange', 'kiwi', 'apple', 'banana']
cf = 0
cv = 0
for i in fruits:
	if i == 'orange':
		cf += 1
	if i[0] in ('a', 'e', 'i', 'o', 'u'):
		cv += 1

print('Total de palavras........: ', cf)
print('Quantidade inicio vogal..: ', cv)


frutas = ['orange', 'apple', 'pear', 'orange', 'kiwi', 'apple', 'banana']
c = 0
for i in frutas:
	if i[0] == 'e':
		c += 1

print(c)


lista = [5, 2, 4, 2, 2]
print(lista.count(2))


idade = [19, 20, 18, 27, 25, 40, 22]
idade.sort()
print(idade[-1])


# Maior valor e sua posicao, na mao
idade = [19, 20, 18, 27, 25, 40, 22]
maior = 0
aux = 0
for i in range(len(idade)):
	if idade[i] > maior:
		maior = idade[i]
		aux = i
print(aux, ' -> ', maior)


# Devolve o indice base-zero do primeiro item cujo valor e igual a x, levantando
# ValueError se este valor nao existe.
# Os argumentos opcionais start e end sao interpretados como nas notacoes de
# fatiamento e sao usados para limitar a busca para uma subsequencia especifica
# da lista.
# O indice retornado e calculado relativo ao comeco da sequencia inteira e nao
# referente ao argumento start.
lista1 = [5, 3, 4, 3, 7]
print(lista1.index(3))

lista1 = [5, 3, 4, 3, 7]
print(lista1.index(3, 2, 4))


idade = [19, 20, 18, 27, 25, 40, 22]

print(max(idade))
print(idade.index(max(idade)))


# ============================================================
# Copiando elementos de uma lista
# ============================================================

# Devolve uma copia da lista.
lista1 = [5, 3, 4, 6, 7]
lista2 = lista1.copy()
print(lista2)


idade = [15, 35, 72, 62, 32]

maior = 0
for i in idade:
	if i > maior:
		maior = i
print(maior)
print(idade.index(maior))


# Diferenca entre iterar sobre os valores e sobre os indices
idade = [15, 35, 72, 62, 32]
for i in idade:
	print(i)

for i in range(len(idade)):
	print(i)


idade = [15, 35, 72, 62, 32]
maior = 0
pm = 0
for i in range(len(idade)):
	if idade[i] > maior:
		maior = idade[i]
		pm = i
print(maior, 'na posicao ', pm)


idade = [15, 35, 72, 62, 32]
print(max(idade), 'na posicao ', idade.index(max(idade)))


idade = [15, 35, 72, 62, 32]

maior = 0
for i in idade:
	if i > maior:
		maior = i
print(maior)


# ============================================================
# Remove todos os elementos de uma lista
# ============================================================

# Remove o primeiro item encontrado na lista cujo valor e igual a x.
# Se nao existir valor igual, uma excecao ValueError e levantada.
lista1 = [5, 2, 4, 2, 2]

print(lista1)
lista1.remove(2)
print(lista1)


# Remove o item na posicao fornecida na lista e retorna.
# Se nenhum indice for especificado, a.pop() remove e retorna o ultimo item.
lista1 = [5, 2, 4, 2, 2]

print(lista1)
lista1.pop(2)
print(lista1)


# Limpa todos os elementos da lista
lista = [5, 2, 4, 2, 2]
print(lista)
lista.clear()
print(lista)


# Estatisticas sobre listas de pares e impares
listap = []
listai = []

for i in range(210, 512, 2):
	listap.append(i)
	listai.append(i - 1)

print('Lista dos valores pares:')
print(listap)
print('A numero de elementos..: ', len(listap))
print('A soma dos elementos...: ', sum(listap))
print('A media dos elementos..: ', sum(listap) / len(listap))
print('O maior elementos......: ', max(listap))
print('O menor elementos......: ', min(listap))

print('Lista dos valores impares:')
print(listai)
print('A numero de elementos..: ', len(listai))
print('A soma dos elementos...: ', sum(listai))
print('A media dos elementos..: ', sum(listai) / len(listai))
print('O maior elementos......: ', max(listai))
print('O menor elementos......: ', min(listai))


# ============================================================
# Trabalhando com Objeto
# ============================================================

aluno = 'Nisston Moraes Tavares de Melo'
# Qual e o numero de caracteres?
# Qual e o numero de palavras?
# Qual e o numero de vogais?
# Qual e o numero de consoantes?
# Quais os caracteres se repetem?
# Quantos espacos em branco existem?
# Quais as iniciais do nome?
# Qual a palavra mais longa?
# Qual o tamanho das palavras?
# Formato de citacao academica (ABNT): extrair o ultimo sobrenome em caixa alta
# seguido das iniciais.

alunos = []


# ============================================================
# Importando dados de um repositorio
# ============================================================
# ponytail: baixa um csv grande da internet, so roda com "--csv" na linha de
# comando. Tire o if se quiser sempre baixar.

if '--csv' in sys.argv:
	import pandas as pd

	# URL do arquivo csv no GitHub
	url = 'https://raw.githubusercontent.com/nisston/disciplinaestruturadedados/main/datatran2021_Completa.csv'

	# Ler o arquivo CSV usando pandas
	df1 = pd.read_csv(url, encoding='latin-1', sep=';')

	# Verificando o tamanho do DataFrame
	print(df1.shape)

	# Exibi o nome das colunas do dataframe
	print(df1.columns)

	# Exibir a estrutura do DataFrame
	df1.info()

	# Verificando se existe conteudo em branco no dataframe
	print(df1.isnull().sum())

	# Apagando os conteudos em branco no dataframe
	df1.dropna(inplace=True, axis=0)

	# Convertendo uma coluna do DataFrame numa lista
	listaq1 = df1['municipio'].to_list()

	print(listaq1[-5:])

	for i in range(-1, -6, -1):
		print(listaq1[i])
