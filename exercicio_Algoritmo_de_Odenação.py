"""Lista de exercicios - Algoritmo de Ordenacao

1. Escreva uma funcao em Python para ordenar um vetor de inteiros em ordem
crescente usando o algoritmo de Selection Sort.
"""


def select_sort(vetor):
	tamanho = len(vetor)

	for i in range(tamanho - 1):
		posicao_menor = i

		for j in range(i + 1, tamanho):
			if vetor[j] < vetor[posicao_menor]:
				posicao_menor = j

		temp = vetor[i]
		vetor[i] = vetor[posicao_menor]
		vetor[posicao_menor] = temp

	return vetor


"""
2. Escreva uma funcao em Python para ordenar um vetor de inteiros, ele deve
receber um parametro que serve como chave para realizar a ordenacao crescente
ou decrescente.
"""


def ordenar_vetor(vetor, ordem="crescente"):
	tamanho = len(vetor)
	for i in range(tamanho - 1):
		posicao = i
		for j in range(i + 1, tamanho):
			if ordem == "crescente":
				if vetor[j] < vetor[posicao]:
					posicao = j
			elif ordem == "decrescente":
				if vetor[j] > vetor[posicao]:
					posicao = j
		temp = vetor[i]
		vetor[i] = vetor[posicao]
		vetor[posicao] = temp
	return vetor


"""
3. Escreva um programa que encontre o elemento de maior valor em um vetor de
inteiros nao ordenado sem usar a funcao max(). Em seguida, encontre o elemento
minimo sem usar a funcao min().
"""

vetor = [42, 15, 88, 3, 27, 91, 12]

maior = vetor[0]
for i in range(len(vetor)):
	if vetor[i] > maior:
		maior = vetor[i]

menor = vetor[0]
for i in range(len(vetor)):
	if vetor[i] < menor:
		menor = vetor[i]

print("Maior:", maior)
print("Menor:", menor)


"""
4. Crie uma funcao que recebe um vetor de numeros inteiros e retorna o segundo
menor numero. Certifique-se de que sua funcao funcione mesmo se houver numeros
duplicados no vetor.
"""


def segundo_menor(vetor):
	unicos = []
	for i in range(len(vetor)):
		ja_existe = False
		for j in range(len(unicos)):
			if vetor[i] == unicos[j]:
				ja_existe = True
		if ja_existe == False:
			unicos.append(vetor[i])

	unicos.sort()

	return unicos[1]


"""
5. Implemente uma funcao que aceite um vetor de numeros inteiros e remova todos
os elementos duplicados, retornando o vetor resultante sem duplicatas. Nao e
permitido utilizar a funcao set().
"""


def remover_duplicatas(vetor):
	sem_duplicatas = []
	for i in range(len(vetor)):
		ja_existe = False
		for j in range(len(sem_duplicatas)):
			if vetor[i] == sem_duplicatas[j]:
				ja_existe = True
		if ja_existe == False:
			sem_duplicatas.append(vetor[i])

	return sem_duplicatas


"""
6. Escreva um programa que ordene um vetor de inteiros em ordem decrescente e,
em seguida, conte quantos numeros pares e quantos numeros impares existem no
vetor ordenado.
"""

vetor = [15, 8, 42, 4, 23, 16, 7]

vetor.sort(reverse=True)

pares = 0
impares = 0

for i in range(len(vetor)):
	if vetor[i] % 2 == 0:
		pares = pares + 1
	else:
		impares = impares + 1

print("Vetor ordenado:", vetor)
print("Pares:", pares)
print("Impares:", impares)


"""
7. Crie uma funcao que aceite um vetor de numeros inteiros e retorne o terceiro
maior numero. Certifique-se de que sua funcao funcione mesmo se houver numeros
duplicados no vetor.
"""


def terceiro_maior(vetor):
	unicos = []
	for i in range(len(vetor)):
		ja_existe = False
		for j in range(len(unicos)):
			if vetor[i] == unicos[j]:
				ja_existe = True
		if ja_existe == False:
			unicos.append(vetor[i])

	unicos.sort(reverse=True)

	return unicos[2]


"""
8. Crie uma funcao que receba um vetor de numeros inteiros e retorne a mediana,
ou seja, o valor do meio quando o vetor e ordenado. Certifique-se de que sua
funcao funcione para vetores com quantidade de elementos impares.
"""


def calcular_mediana(vetor):
	v = vetor.copy()
	v.sort()

	meio = len(v) // 2
	return v[meio]


if __name__ == "__main__":
	assert select_sort([5, 2, 9, 1]) == [1, 2, 5, 9]
	assert ordenar_vetor([5, 2, 9, 1], "decrescente") == [9, 5, 2, 1]
	assert segundo_menor([3, 1, 1, 2]) == 2
	assert remover_duplicatas([1, 2, 2, 3, 1]) == [1, 2, 3]
	assert terceiro_maior([9, 9, 7, 5, 5, 1]) == 5
	assert calcular_mediana([7, 1, 3]) == 3
	print("ok")
