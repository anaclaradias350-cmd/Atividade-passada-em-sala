def calcular():
	print("Calculadora simples")
	print("Operações disponíveis: + (adição), * (multiplicação), / (divisão)")

	try:
		primeiro = float(input("Digite o primeiro número: "))
		operacao = input("Escolha uma operação (+, *, /): ").strip()
		segundo = float(input("Digite o segundo número: "))

		if operacao == "+":
			resultado = primeiro + segundo
		elif operacao == "*":
			resultado = primeiro * segundo
		elif operacao == "/":
			if segundo == 0:
				print("Erro: não é possível dividir por zero.")
				return
			resultado = primeiro / segundo
		else:
			print("Operação inválida.")
			return

		print(f"Resultado: {resultado}")
	except ValueError:
		print("Erro: digite números válidos.")


if __name__ == "__main__":
	calcular()
