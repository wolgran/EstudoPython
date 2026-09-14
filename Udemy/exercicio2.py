def situacao_aluno(media):
    
    if media >= 7:
        return "Aprovado"
    elif media >=5:
        return "Recuperação"
    else:
        return "Reprovador"

for i in range(8):
    nome = input("|Digite o nome do Aluno: ")
    media = float(input("Digite a média do Aluno: "))
    print(nome, "->", situacao_aluno(media))