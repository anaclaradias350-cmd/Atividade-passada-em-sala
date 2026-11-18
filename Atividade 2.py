def maior_de_tres(a, b, c):
    if a >= b and a >= c:
        return a
    elif b >= a and b >= c:
        return b
    else:
        return c

print(maior_de_tres(10, 25, 15))   
print(maior_de_tres(50, 12, 8))   
print(maior_de_tres(7, 7, 3))     