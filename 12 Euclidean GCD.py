def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a % b)


if __name__ == '__main__':
    print(f'{gcd(120, 0)=}')
    print(f'{gcd(333, 150)=}')