# (x + n) mod m = 0


def additiveInverse(n, m):
    x = 0
    while (x + n) % m != 0:
        x += 1
    return x


if __name__ == '__main__':
    n, m = 5, 13
    print(f'Additive Inverse of {n} over modulo {m} is {additiveInverse(n, m)}')
    n, m = 7, 26
    print(f'Additive Inverse of {n} over modulo {m} is {additiveInverse(n, m)}')

