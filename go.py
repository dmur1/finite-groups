def ord(a, p):
    for e in range(1, p):
        if pow(a, e, p) == 1:
            return e;

def ords(p):
    print(f"Z*{p}")
    for i in range(1, p):
        print(f"ord({i:02}) = {ord(i, p):02}")

ords(53)
