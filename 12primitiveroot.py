def isPrimitive(g, p):
    L = []
    for i in range(1, p):
        L.append(pow(g, i) % p)
    for i in range(1, p):
        if L.count(i) > 1:
            L.clear()
            return False
        return True


if __name__ == '__main__':
    g, p = 3, 7
    print(f'Is {g} a primitive root of {p}? {isPrimitive(g, p)}')
    g, p = 3, 11
    print(f'Is {g} a primitive root of {p}? {isPrimitive(g, p)}')