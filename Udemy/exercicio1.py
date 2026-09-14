notas = []
for i in range(10):
    nota = float(input("digite a nota do aluno: "))
    notas.append(nota)  
    
    media = sum(notas) / len(notas)
    acima = 0
    menor5 = 0
    
for nota in notas:
    if nota > media:
        acima += 1
    if nota <= 5:
        menor5 += 1

print("\n")
print(f"A média da turma é: {media}")
print(f"A maior nota é {max(notas)}")
print(f'A menor nota da turma é: {min(notas)}')
print(f"{acima} Alunos estão acima da média")
print(f"{menor5} Alunos estão abaixo de 5")