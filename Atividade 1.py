def calcular_area_retangulo(base, altura):
    """Calcula a área de um retângulo."""
    area = base * altura
    return area


base_usuario = float(input("Digite o valor da base: "))
altura_usuario = float(input("Digite o valor da altura: "))

resultado = calcular_area_retangulo(base_usuario, altura_usuario)
print(f"A área do retângulo é: {resultado}")