numero = []

for i in range(10):
    n = int(input(f"Digite o {i + 1} numero: "))
    numero.append(n)
    
atual = 1
maior = 1

for i in range(1, len(numero)):
    if numero[i] > numero[i - 1]:
        atual += 1
    else:
        atual = 1
    if atual > maior:
        maior = atual
print(f"A maior sequencia é: {maior}")