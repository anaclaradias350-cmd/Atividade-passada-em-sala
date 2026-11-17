import math


def somar(a, b):
	return a + b


def subtrair(a, b):
	return a - b


def multiplicar(a, b):
	return a * b


def dividir(a, b):
	if b == 0:
		raise ValueError("Não é possível dividir por zero.")
	return a / b


def potencia(a, b):
	return a**b


def raiz_quadrada(a):
	if a < 0:
		raise ValueError("Não existe raiz quadrada real de número negativo.")
	return math.sqrt(a)


def calcular():
	operacoes = {
		"1": ("Soma", somar, 2),
		"2": ("Subtração", subtrair, 2),
		"3": ("Multiplicação", multiplicar, 2),
		"4": ("Divisão", dividir, 2),
		"5": ("Potência", potencia, 2),
		"6": ("Raiz quadrada", raiz_quadrada, 1),
	}

	while True:
		print("\n=== Calculadora ===")
		for numero, (nome, _, _) in operacoes.items():
			print(f"{numero} - {nome}")
		print("0 - Sair")

		escolha = input("Escolha uma operação: ").strip()
		if escolha == "0":
			print("Até mais!")
			return
		if escolha not in operacoes:
			print("Opção inválida.")
			continue

		nome, funcao, quantidade = operacoes[escolha]
		try:
			valores = [
				float(input(f"Digite o {i + 1}º número: ").replace(",", "."))
				for i in range(quantidade)
			]
			resultado = funcao(*valores)
			print(f"Resultado de {nome.lower()}: {resultado:g}")
		except ValueError as erro:
			print(f"Erro: {erro}")


if __name__ == "__main__":
	calcular()
