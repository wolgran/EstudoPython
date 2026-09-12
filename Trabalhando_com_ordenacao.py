# Ordenação

"""A ordenação em estruturas de dados é um processo fundamental que envolve a organização dos elementos 
de uma coleção de dados de forma ascendente ou descendente, de acordo com um critério específico. 
Essa organização torna a recuperação de informações mais eficiente e permite a realização de buscas 
e operações de maneira mais otimizada. Existem várias técnicas de ordenação disponíveis, desde algoritmos 
simples como o Bubble Sort e o Selection Sort até algoritmos mais eficientes como o Quick Sort e o Merge Sort."""

#Bubble sort

""" Definição: O Bubble Sort é um algoritmo de ordenação simples que compara repetidamente pares adjacentes de elementos
em uma lista e os troca se estiverem na ordem errada. Esse processo é repetido até que nenhuma troca seja necessária,
o que indica que a lista está ordenada.

Características: É fácil de implementar, mas não é eficiente em listas muito grandes, pois seu desempenho é O(n^2) no pior caso."""

"""
vetor = [3,8,7,2,6,1]
n=len(vetor)
print(vetor)
for i in range(n):
  print(i,'<-')
  for j in range(0,n-i-1):
    print(j,'*')
    if vetor[j]>vetor[j+1]:
      aux=vetor[j]
      vetor[j]=vetor[j+1]
      vetor[j+1]=aux
print(vetor)
"""

# Selection sort

"""Definição: O Selection Sort é outro algoritmo de ordenação simples que divide a lista em duas partes: 
a parte ordenada e a parte não ordenada. Ele encontra o menor elemento na parte não ordenada e o move para
a parte ordenada. Esse processo é repetido até que a lista esteja completamente ordenada.
Características: O Selection Sort também é simples de implementar, mas, assim como o Bubble Sort, não é eficiente
em listas muito grandes, com desempenho O(n^2) no pior caso."""

"""
vetor = [3,8,7,2,6,1]
n=len(vetor)
print(vetor)
for i in range(n):
  id_min=i
  print(i,'<-')
  for j in range(i+1,n):
    print(j,'*')
    if vetor[id_min]>vetor[j]:
      id_min=j
  aux=vetor[i]
  vetor[i]=vetor[id_min]
  vetor[id_min]=aux
  

print(vetor)"""

# Quick sort

"""Definição: O Quick Sort é um algoritmo de ordenação baseado na estratégia "divide e conquista". 
Ele seleciona um elemento da lista, chamado de "pivô", e divide a lista em duas sub-listas: uma com
elementos menores que o pivô e outra com elementos maiores. Em seguida, o Quick Sort é aplicado
recursivamente a essas sub-listas até que a lista esteja completamente ordenada.

Características: O Quick Sort é geralmente mais eficiente do que o Bubble Sort e o Selection Sort, 
com um desempenho médio de O(n log n). No entanto, pode ser sensível à escolha do pivô e requer uma 
implementação cuidadosa."""

"""
def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quick_sort(left) + middle + quick_sort(right)
"""

# Calculando o tempo de execução

def bubble_sort(vetor):
  n=len(vetor)
  for i in range(n):
    for j in range(0,n-i-1):
      if vetor[j]>vetor[j+1]:
        aux=vetor[j]
        vetor[j]=vetor[j+1]
        vetor[j+1]=aux
  return (vetor)

def select_sort(vetor):
  n=len(vetor)
  for i in range(n):
    id_min=i
    for j in range(i+1,n):
      if vetor[id_min]>vetor[j]:
        id_min=j
    aux=vetor[i]
    vetor[i]=vetor[id_min]
    vetor[id_min]=aux
  return (vetor)

def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quick_sort(left) + middle + quick_sort(right)

