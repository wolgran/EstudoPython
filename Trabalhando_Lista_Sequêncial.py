"""Trabalhando com Lista sequencial

Uma lista sequencial, tambem conhecida como array ou vetor, e uma estrutura de
dados que armazena elementos em posicoes contiguas de memoria. Cada elemento da
lista e identificado por um indice, que representa sua posicao na lista,
comecando normalmente do zero. As listas sequenciais sao fundamentais em varias
aplicacoes de programacao e algoritmos devido a sua eficiencia em acessar
elementos diretamente pelo indice.

Caracteristicas principais:

	Acesso Direto: os elementos podem ser acessados diretamente usando o
	indice, o que permite operacoes de leitura e escrita rapidas.

	Tamanho Fixo ou Dinamico: em algumas linguagens, as listas sequenciais
	tem tamanho fixo, enquanto em outras (como Python), elas podem ser
	redimensionadas dinamicamente.

	Eficiencia: operacoes de leitura (acesso a um elemento especifico) sao
	realizadas em tempo constante O(1), enquanto insercoes ou remocoes de
	elementos podem variar em eficiencia, dependendo da posicao do elemento.

Tutorial on-line do Python:
https://docs.python.org/pt-br/3/library/stdtypes.html#list
Biblioteca Virtual:
https://integrada.minhabiblioteca.com.br/reader/books/9786555584288/pageid/252
"""

import numpy as np


# Exemplo de uma lista sequencial em Python
lista = [10, 20, 30, 40, 50]

# Acessando o terceiro elemento (indice 2)
elemento = lista[2]  # Resultado: 30

# Modificando o valor do primeiro elemento
lista[0] = 5  # Lista se torna: [5, 20, 30, 40, 50]

# Adicionando um novo elemento ao final da lista
lista.append(60)  # Lista se torna: [5, 20, 30, 40, 50, 60]

# Removendo o segundo elemento
del lista[1]  # Lista se torna: [5, 30, 40, 50, 60]


class Listasequencial:

	def __init__(self, capacidade):
		self.capacidade = capacidade
		self.ultima_posicao = -1
		self.valores = np.empty(self.capacidade, dtype=int)

	def imprime(self):
		if self.ultima_posicao == -1:
			print('O vetor esta vazio')
		else:
			for i in range(self.ultima_posicao + 1):
				print(i, ' - ', self.valores[i])

	def insere(self, valor):
		if self.ultima_posicao == self.capacidade - 1:
			print('Capacidade maxima atingida...')
		else:
			self.ultima_posicao += 1
			self.valores[self.ultima_posicao] = valor

	def pesquisar(self, valor):
		for i in range(self.ultima_posicao + 1):
			if (valor == self.valores[i]):
				return i
		return -1

	def excluir(self, valor):
		posicao = self.pesquisar(valor)
		if posicao == -1:
			return -1
		else:
			for i in range(posicao, self.ultima_posicao):
				self.valores[i] = self.valores[i + 1]
		self.ultima_posicao -= 1

	def maiorvalor(self):
		maior = 0
		for i in range(self.ultima_posicao + 1):
			if self.valores[i] > maior:
				maior = self.valores[i]
		return (maior)

	def numerospares(self):
		listapares = []
		for i in range(self.ultima_posicao + 1):
			if self.valores[i] % 2 == 0:
				listapares.append(self.valores[i])
		return (listapares)


# Criando novos metodos para o objeto Listasequencial:
#
# 1. Retornar o maior valor.
# 2. Retornar o menor valor.
# 3. Verificar se um valor se repete. O metodo deve ter um valor como parametro.
# 4. Retornar quais os valores sao pares.
# 5. Retornar quais os valores sao impares.
#
# Seu codigo aqui.


if __name__ == "__main__":
	# Criando um objeto e inserindo valores
	p1 = Listasequencial(5)
	p1.insere(4)
	p1.insere(13)
	p1.insere(5)
	p1.insere(17)
	p1.insere(8)
	print(p1.numerospares())

	# Estourando a capacidade
	p2 = Listasequencial(5)
	for v in [4, 3, 5, 7, 8, 9, 12]:
		p2.insere(v)
	p2.imprime()

	# Pesquisando um valor
	print('Pesquisando valores ...')
	val = 5
	resultado = p2.pesquisar(val)
	if resultado == -1:
		print('O valor informado nao existe')
	else:
		print('A posicao do valor ', val, ' foi de', resultado)

	# Excluindo um valor da minha lista
	print('Excluindo um valores ...')
	p2.imprime()
	p2.excluir(5)
	print('--------------------')
	p2.imprime()

	from random import randint
	for i in range(10):
		print(randint(10, 29))
