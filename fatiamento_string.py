"""
Fatiamento de strings
 012345678
 Olá mundo
-987654321
Fatiamento [i(inicio):f(fim):p(pulo)] [::]
print(variavel.replace(' ', '')) remove os espaços vazios
Obs.: a função len retorna a qtd 
de caracteres da str
"""
"""variavel = 'Olá mundo'
print(variavel[::])"""


""" Exercicio
Peça ao usuário para digitar seu nome
Peça ao usuário para digitar sua idade
Se nome e idade forem digitados:
    Exiba:
        Seu nome é {nome}
        Seu nome invertido é {nome invertido}
        Seu nome contém (ou não) espaços
        Seu nome tem {n} letras
        A primeira letra do seu nome é {letra}
        A última letra do seu nome é {letra}
Se nada for digitado em nome ou idade: 
    exiba "Desculpe, você deixou campos vazios.
"""

nome = input("Digite seu nome: ")
idade = input("Digite sua idade: ")


print(f"Seu nome é:{nome}")
print(f"Seu nome invertido é: {nome[::-1]}")
print(f"Seu nome contém {nome.count(' ')} espaços")
if ' ' in nome:
    print("Seu nome contém espaços.")
else:
    print("Seu nome não contem espaços.")
print(f"Seu nome tem {len(nome.replace(' ', ''))} letras")
print(f" A primeira letra do seu nome é: {nome[0]}")
print(f" A ultima letra do seu nome é: {nome[-1]}")
if not nome.strip() or not idade.strip():
    print("Desculpe, você deixou campos vazios")
else:
   idade = int(idade) 

