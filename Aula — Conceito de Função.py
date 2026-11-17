def saudar(nome):
    print(f"Olá, {nome}!")

saudar("Ana")
saudar("Bruno")
saudar("Carlos")

def estatisticas(nums):
    total = sum(nums)
    media = total / len(nums)
    return total, media

t, m = estatisticas([8, 9, 7])
print(f"Total: {t}, Média: {m}")