def ord(a, p):
    for e in range(1, p):
        if pow(a, e, p) == 1:
            return e;

def ords(p):
    print(f"Z*{p}")
    for i in range(1, p):
        print(f"ord({i:02}) = {ord(i, p):02}")

#ords(4969)

def prime_factors(n):
    factors = []
    while n % 2 == 0:
        factors.append(2)
        n = n // 2

    for i in range(3, int(n**0.5) + 1, 2):
        while n % i == 0:
            factors.append(i)
            n = n // i

    if n > 2:
        factors.append(n)

    return factors

def gens(p):
    phi = p - 1
    factors = prime_factors(phi)
    generators = []
    for i in range(1, p):
        congruent_to_one = False
        for factor in factors:
            if pow(i, phi // factor, p) == 1:
                congruent_to_one = True
                break
        if not congruent_to_one:
            generators.append(i)
    return generators

print(gens(2))
print(gens(3))
print(gens(5))
print(gens(7))
print(gens(11))
print(gens(13))
print(gens(17))
print(gens(53))

