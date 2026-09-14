"""
Faça um programa que peça ao usuário para digitar um número inteiro, 
informe se este número é par ou ímpar. Caso o usuário não digite um numero
interiro, informe que não é um numero inteiro.
"""
"""num = input('Digite um numero inteiro: ')
#isdigit() = Metodo que vertifica se todas palavras digitadas são numeros inteiros.
if not num.isdigit():
    print('Você não digitou um numero interiro')
else:
    num = int(num) 
    if num %2 == 0:
        print('Esté numero é par.')
    else:
        print('Este numero é impar')"""
    
"""Faça um programa que pergunte a hora ao usuário e , baseando-se no horário
descrito, exiba a saudação apropriada. Ex.
Bom dia 0-11, Boa tarde 12-17 e Boa noite 18-23.
"""
hora = int(input('Digite a hora: '))

if hora > 0 and hora < 11:
    print("Bom dia") 
elif hora > 12 and hora <17:
    print("Boa tarde")
else:
    print("Boa noite")
    

"""Faça um programa que peça o primeiro nome do usuário. Se o nome tiver 4 letras ou
menos escreva "Seu nome é curto"; se tiver entre 5 e 6 letras, escreva
"Seu nome é normal"; maior que 6 escreva "Seu nome é mui to grande".
"""