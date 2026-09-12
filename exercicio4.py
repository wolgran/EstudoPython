soma = 0
quant = 0

for i in range(15):
    n = (int(input("Digite o numero: ")))
    if n % 2 == 0 and n > 10:
        soma += n
        quant +=1

print(f"A soma é: {soma}")
print(f"A quantidade de numeros somados é: {quant}")

if quant > 0:
    media = soma / quant
    print(f"A média de numeros somados é:{media:.1f}")
else:
    print("Nenhum numero foi somado")