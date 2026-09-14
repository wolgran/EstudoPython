"""Lista de exercicios - Lista Sequencial

A classe Listasequencial esta em Trabalhando_Lista_Sequêncial.py.
"""

from Trabalhando_Lista_Sequêncial import Listasequencial


"""
1. Crie uma lista sequencial com capacidade para 5 elementos. Insira as
matriculas dos seguintes alunos: 101, 102, 103, 104.
Depois, imprima a lista para verificar os valores armazenados.
"""

lista1 = Listasequencial(5)

lista1.insere(101)
lista1.insere(102)
lista1.insere(103)
lista1.insere(104)

lista1.imprime()


"""
2. Uma loja deseja registrar os codigos dos produtos em estoque. Insira os
codigos 45, 33, 27, 89, 56 em uma lista sequencial de capacidade 5. Depois,
tente inserir o produto 72 e observe o que acontece.
"""

produtos = Listasequencial(5)

produtos.insere(45)
produtos.insere(33)
produtos.insere(27)
produtos.insere(89)
produtos.insere(56)

produtos.imprime()
produtos.insere(72)


"""
3. Considere que foram cadastrados os clientes com os codigos 11, 22, 33, 44,
55. Pesquise se o cliente com codigo 33 esta presente e informe sua posicao na
lista.
"""

cliente = Listasequencial(5)
cliente.insere(11)
cliente.insere(22)
cliente.insere(33)
cliente.insere(44)
cliente.insere(55)

print(cliente.pesquisar(33))


"""
4. A lista de clientes contem os codigos: 10, 20, 30, 40, 50.
Exclua o cliente com codigo 30 e imprima a lista para verificar se a exclusao
foi realizada corretamente.
"""

cliente = Listasequencial(5)
cliente.insere(10)
cliente.insere(20)
cliente.insere(30)
cliente.insere(40)
cliente.insere(50)

cliente.excluir(30)
cliente.imprime()


"""
5. Pacientes aguardam atendimento e foram cadastrados os numeros de senha:
5, 6, 7, 8, 9. Um paciente desistiu (senha 7).
Faca a exclusao deste paciente e imprima novamente a lista.
"""

pacientes = Listasequencial(5)
pacientes.insere(5)
pacientes.insere(6)
pacientes.insere(7)
pacientes.insere(8)
pacientes.insere(9)

pacientes.excluir(7)
pacientes.imprime()


"""
6. O hotel tem capacidade para 6 reservas. Insira os numeros de reserva:
101, 103, 107, 110, 115.
Depois, pesquise se a reserva 108 ja foi cadastrada e mostre a resposta.
"""

reservas = Listasequencial(6)

reservas.insere(101)
reservas.insere(103)
reservas.insere(107)
reservas.insere(110)
reservas.insere(115)

print(reservas.pesquisar(108))


"""
7. Foram cadastrados os pedidos: 2001, 2002, 2003, 2004, 2005.
O cliente cancelou o pedido 2002. Exclua-o e imprima a lista atualizada.
"""

pedidos = Listasequencial(5)

pedidos.insere(2001)
pedidos.insere(2002)
pedidos.insere(2003)
pedidos.insere(2004)
pedidos.insere(2005)

pedidos.excluir(2002)
pedidos.imprime()


"""
8. Em um estacionamento cabem 4 carros. Insira as placas (numericas ficticias):
1234, 5678, 9101, 1213.
Verifique se a placa 5678 esta estacionada.
Depois, tente inserir a placa 1415. O que acontece?
"""

vagas_placas = Listasequencial(4)

vagas_placas.insere(1234)
vagas_placas.insere(5678)
vagas_placas.insere(9101)
vagas_placas.insere(1213)

print(vagas_placas.pesquisar(5678))

vagas_placas.insere(1415)


"""
9. Considere uma lista com as notas: 70, 85, 90, 75, 60.
Pesquise se o aluno obteve a nota 75 e indique a posicao encontrada.
"""

notas = Listasequencial(5)

notas.insere(70)
notas.insere(85)
notas.insere(90)
notas.insere(75)
notas.insere(60)

print(notas.pesquisar(75))


"""
10. Uma lista contem os valores: 1, 2, 3, 4, 5, 6.
Exclua os valores 3 e 5, um de cada vez, e mostre a lista apos cada exclusao.
"""

valores = Listasequencial(6)

valores.insere(1)
valores.insere(2)
valores.insere(3)
valores.insere(4)
valores.insere(5)
valores.insere(6)

valores.excluir(3)
valores.imprime()
print('--------------------')
valores.excluir(5)
valores.imprime()
