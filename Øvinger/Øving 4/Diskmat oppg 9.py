def algorithm(a, e, p):
    num = a**e % p
    return f'{a}^{e} (mod {p}) = {num}'

print(algorithm(3, 1246, 7))
