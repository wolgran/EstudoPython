"""Lista de exercicios - Classes"""


"""
1. Crie uma classe chamada "Circulo" que tenha um atributo "raio". Implemente um
metodo chamado "calcular_area" que retorna a area do circulo.
"""


class Circulo:
	def __init__(self, raio):
		self.raio = raio
		self.area = 0

	def calcular_area(self):
		self.area = 3.14 * (self.raio ** 2)
		return f"A area do circulo com raio {self.raio} e: {self.area:.2f}"


meu_circulo = Circulo(5)
print(meu_circulo.calcular_area())


"""
2. Crie uma classe chamada "Livro" que tenha atributos "titulo" e "autor".
Implemente um metodo chamado "detalhes" que retorna uma string com as
informacoes do livro.
"""


class Livro:
	def __init__(self, titulo, autor):
		self.titulo = titulo
		self.autor = autor

	def detalhes(self):
		return f'Titulo: {self.titulo} | Autor: {self.autor}'


meu_livro = Livro("O Alquimista", "Paulo Coelho")
print(meu_livro.detalhes())


"""
3. Crie uma classe chamada "Retangulo" que tenha atributos "base" e "altura".
Implemente um metodo chamado "calcular_area" que retorna a area do retangulo.
"""


class Retangulo:
	def __init__(self, base, altura):
		self.base = base
		self.altura = altura
		self.area = 0

	def calcular_area(self):
		self.area = self.base * self.altura
		return f'A area do retangulo e: {self.area:.2f}'


retangulo1 = Retangulo(7.7, 5.)
print(retangulo1.calcular_area())


"""
4. Crie uma classe chamada "ContaBancaria" que tenha atributos "saldo" e
"titular". Implemente metodos "depositar" e "sacar" para manipular o saldo.
"""


class ContaBancaria:
	def __init__(self, saldo, titular):
		self.saldo = saldo
		self.titular = titular

	def depositar(self, valor):
		if valor > 0:
			self.saldo += valor
			print(self.titular)
			print(f"Seu deposito de R$ {valor} foi realizado com sucesso!")
		else:
			print("O valor do deposito tem que ser maior que zero.")

	def sacar(self, valor):
		if valor <= 0:
			print("O valor do saque deve ser maior que zero.")
		elif valor <= self.saldo:
			self.saldo -= valor
			print(self.titular)
			print(f"Seu saque de R$ {valor} realizado com sucesso!")
		else:
			print("Saldo insuficiente para realizar o saque.")

	def exibir_saldo(self):
		return f'Titular: {self.titular} | Saldo Atual: R$ {self.saldo:.2f}'


conta1 = ContaBancaria(5000, 'Felipe wolgran')
conta1.depositar(1000)
conta1.sacar(0.50)
print(conta1.exibir_saldo())


"""
5. Crie uma classe chamada "Pessoa" com atributos "nome" e "idade". Implemente
um metodo chamado "falar" que imprime uma mensagem com o nome da pessoa.
"""


class Pessoa:
	def __init__(self, nome, idade):
		self.nome = nome
		self.idade = idade

	def falar(self, mensagem):
		return f'{self.nome} diz: {mensagem}'


felipe = Pessoa('Felipe', 32)
print(felipe.falar('Ola esta tudo bem?'))


"""
6. Crie uma classe chamada "Produto" com atributos "nome", "preco" e
"quantidade". Implemente um metodo chamado "calcular_total" que retorna o valor
total do produto (preco * quantidade).
"""


class Produto:
	def __init__(self, nome, preco, quantidade):
		self.nome = nome
		self.preco = preco
		self.quantidade = quantidade
		self.valorTotal = 0

	def calcular_total(self):
		self.valorTotal = self.preco * self.quantidade
		return f'O valor total do {self.nome} e: R$ {self.valorTotal:.2f}'


compra = Produto('Cafe', 14.45, 5)
print(compra.calcular_total())


"""
7. Crie uma classe chamada "Carro" com atributos "marca", "modelo" e "ano".
Implemente um metodo chamado "detalhes" que retorna uma string com as
informacoes do carro.
"""


class Carro:
	def __init__(self, marca, modelo, ano):
		self.marca = marca
		self.modelo = modelo
		self.ano = ano

	def detalhes(self):
		return f'O Carro de modelo {self.modelo} do(a) {self.marca} do ano {self.ano}'


meu_carro = Carro('Chevrolet', 'Corsa', 2000)
print(meu_carro.detalhes())


"""
8. Crie uma classe chamada "Aluno" com atributos "nome" e "notas". Implemente um
metodo chamado "calcular_media" que retorna a media das notas do aluno.
"""


class Aluno:
	def __init__(self, nome, notas):
		self.nome = nome
		self.notas = notas
		self.media = 0

	def calcular_media(self):
		if len(self.notas) == 0:
			return 0.0
		self.media = sum(self.notas) / len(self.notas)
		return f'A media do aluno {self.nome} e: {self.media:.2f}'


aluno_felipe = Aluno('Felipe', [7.0, 10.0, 8.0])
print(aluno_felipe.calcular_media())


"""
9. Crie uma classe chamada "Triangulo" com atributos "lado1", "lado2" e "lado3".
Implemente um metodo chamado "calcular_perimetro" que retorna o perimetro do
triangulo.
"""


class Triangulo:
	def __init__(self, lado1, lado2, lado3):
		self.lado1 = lado1
		self.lado2 = lado2
		self.lado3 = lado3
		self.perimetro = 0

	def calcular_perimetro(self):
		self.perimetro = self.lado1 + self.lado2 + self.lado3
		return f'O perimetro do triangulo e : {self.perimetro:.2f}'


triangulo1 = Triangulo(7, 10, 7.14)
print(triangulo1.calcular_perimetro())


"""
10. Crie uma classe chamada "Funcionario" com atributos "nome", "salario" e
"cargo". Implemente um metodo chamado "aumentar_salario" que recebe um valor
percentual de aumento e atualiza o salario do funcionario.
"""


class Funcionario:
	def __init__(self, nome, salario, cargo):
		self.nome = nome
		self.salario = salario
		self.cargo = cargo
		self.aumento = 0

	def aumentar_salario(self, porcentagem):
		self.aumento = (self.salario * porcentagem) / 100
		self.salario += self.aumento
		print(f'Funcionario: {self.nome} | Cargo: {self.cargo}')
		print(f'recebeu um aumento de {porcentagem}% e passa a ter o salario de: {self.salario:.2f} Reais')


FelipeWolgran = Funcionario('Felipe Wolgran B Oliveira', 3000, 'Aux. Tec. Controle de Qualidade')
FelipeWolgran.aumentar_salario(15)
