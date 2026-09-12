"""Estrutura Pilha

Em Python, uma pilha (ou *stack*) é uma estrutura de dados que segue o princípio LIFO (Last In, First Out), ou seja, o último elemento inserido é o primeiro a ser removido. 
Para implementar uma pilha, pode-se utilizar listas, aproveitando os métodos `append()` para adicionar elementos e `pop()` para removê-los do topo da pilha. 
Isso proporciona uma maneira eficiente de gerenciar dados em cenários que exigem controle de acesso sequencial, como no caso de algoritmos de backtracking ou processamento de expressões.
O uso de pilhas é comum em várias aplicações, como na verificação de parênteses balanceados ou na implementação de chamadas de função recursivas. 
Além disso, a estrutura de pilha é uma solução simples para controlar o fluxo de execução de determinadas operações, pois, ao adicionar e remover
elementos do topo, garante-se uma forma de rastreamento ordenado dos dados. A simplicidade na manipulação dessa estrutura, através de poucos métodos nativos,
facilita o desenvolvimento de soluções com alta eficiência e clareza."""

class Pilha:

    def __init__(self):
        self.items = []

    def empilhar(self, item):
        self.items = self.items + [item]

    def desempilhar(self):
        if not self.is_vazia():
            item_removido = self.items[-1]
            self.items = self.items[:-1]
            return item_removido
        else:
            print("A pilha está vazia. Não é possível desempilhar.")

    def topo(self):
        if not self.is_vazia():
            return self.items[-1]
        else:
            print("A pilha está vazia. Não há topo para visualizar.")

    def is_vazia(self):
        return len(self.items) == 0

    def tamanho(self):
        return len(self.items)

    def imprimir(self):
        if not self.is_vazia():
            print("Itens da pilha:")
            for item in self.items:
                print(item, end=' ')
        else:
            print("A pilha está vazia. Não há itens para imprimir.")
            
# Criando uma pilha e empilhando
p1 = Pilha()

p1.empilhar(8)
p1.empilhar(6)
p1.empilhar(7)
p1.empilhar(2)
p1.empilhar(1)
p1.empilhar(4)

p1.imprimir()

# Criando uma pilha, empilhando e visualizando o topo da pilha
p1 = Pilha()

p1.empilhar(8)
p1.empilhar(6)
p1.empilhar(7)
p1.empilhar(2)
p1.empilhar(1)
p1.empilhar(4)

p1.topo()

# Criando uma pilha, empilhando e desempilhando dados
p1 = Pilha()

p1.empilhar(8)
p1.empilhar(6)
p1.empilhar(7)
p1.empilhar(2)
p1.empilhar(1)
p1.empilhar(4)

p1.desempilhar()
p1.desempilhar()
p1.desempilhar()

p1.topo()

# Tentando desempenhar uma pilha vazia
p1 = Pilha()

p1.empilhar(2)
p1.empilhar(1)
p1.empilhar(4)

p1.desempilhar()
p1.desempilhar()
p1.desempilhar()
p1.desempilhar()

#Questões com aplicação de Pilha

# Questão 01 - Crie uma estrutura de pilha para apresentar todas
# as vogais que encontra-se na lista
nome=['Ana','Pedro']

p1=Pilha()
for i in nome:
  for j in i:
    if j.lower() in ('a','e','i','o','u'):
      p1.empilhar(j)
p1.imprimir()

# Questão 02 - Identificar entre os nome quais apresentam
# um número par de vogais
# Utilize a estrutura de Pilha para encontrar a solução
nomes =['Ana','Paula','Beatriz','Mariana','Luana','Carlos','Helena','Laura','Daniel','Bianca']

for i in nomes:
  p1=Pilha()
  for j in i:
    if j.lower() in ('a','e','i','o','u'):
      p1.empilhar(j)
  if p1.tamanho()%2==0:
    print(i,' tem núm de vogais par...: ', p1.tamanho())
    
# Questão 03 - Identificar entre as expressões quais estão escritas de maneira correta
# Utilize a estrutura de Pilha para encontrar a solução
expressao = ['(a+b)*(a+b)','(((a+b)*a+b*())','((a+b)*(a+b))','(a+b)*)(a+b)']

for e in expressao:
  p1 = Pilha()
  for i in e:
    if i=='(':
      p1.empilhar(i)
    elif i==')':
      if not p1.is_vazia() and p1.topo()=='(':
        p1.desempilhar()
      else:
        p1.empilhar('x')
  if (p1.is_vazia()):
    print('Expressão Correta')
  else:
    print('Expressão Incorreta')

# Questão 04 - Crie uma estrutura de Pilha para guardar apenas os números pares desta lista
# depois desempilhe 5 vezes e me retorne o valor do topo.
valores = [9, 16, 11, 40, 49, 25, 50, 31, 46, 9, 25, 27, 42, 22, 39, 31, 9, 33, 20, 30, 39, 17, 11]

p1=Pilha()
for i in valores:
  if i%2==0:
    p1.empilhar(i)

for i in range(5):
  p1.desempilhar()

p1.topo()




