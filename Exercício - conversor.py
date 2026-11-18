def celsius_para_fahrenheit(c):
    """
    Converte uma temperatura de graus Celsius para Fahrenheit.

    Parâmetros:
        c (float): Temperatura em graus Celsius.

    Retorna:
        float: Temperatura equivalente em graus Fahrenheit.
    """
    return (c * 9 / 5) + 32


def km_para_milhas(km):
    """
    Converte uma distância de quilômetros para milhas.

    Parâmetros:
        km (float): Distância em quilômetros.

    Retorna:
        float: Distância equivalente em milhas.
    """
    return km * 0.621371


def kg_para_libras(kg):
    """
    Converte uma massa de quilogramas para libras.

    Parâmetros:
        kg (float): Massa em quilogramas.

    Retorna:
        float: Massa equivalente em libras.
    """
    return kg * 2.20462


def exibir_menu():
    """Exibe as opções disponíveis no menu principal."""
    print("\n" + "=" * 35)
    print("      CONVERSOR DE UNIDADES")
    print("=" * 35)
    print("1. Celsius para Fahrenheit")
    print("2. Quilômetros para Milhas")
    print("3. Quilogramas para Libras")
    print("0. Sair")
    print("=" * 35)


def main():
    """Função principal que gerencia o loop do menu interativo."""
    while True:
        exibir_menu()
        opcao = input("Escolha uma opção: ").strip()

        if opcao == "0":
            print("Encerrando o programa. Até logo!")
            break

        if opcao not in ("1", "2", "3"):
            print("Opção inválida! Digite 1, 2, 3 ou 0 para sair.")
            continue

        try:
            valor = float(input("Digite o valor a ser convertido: ").replace(",", "."))
        except ValueError:
            print("Entrada inválida! Por favor, digite apenas números.")
            continue

        if opcao == "1":
            resultado = celsius_para_fahrenheit(valor)
            print(f"Resultado: {valor:.2f} °C = {resultado:.2f} °F")
        elif opcao == "2":
            resultado = km_para_milhas(valor)
            print(f"Resultado: {valor:.2f} km = {resultado:.2f} mi")
        elif opcao == "3":
            resultado = kg_para_libras(valor)
            print(f"Resultado: {valor:.2f} kg = {resultado:.2f} lb")


if __name__ == "__main__":
    main()