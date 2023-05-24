def euclideanAlgorithm(a, b):
    while b != 0:
        a, b = b, a % b
    return a
    
print(euclideanAlgorithm(12, 18))


def reduceFraction(n, d):
    g = euclideanAlgorithm(n, d)
    return n // g, d // g


print(reduceFraction(12, 18))