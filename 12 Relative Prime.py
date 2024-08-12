def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a % b)


def is_relative_prime(a, b):
    return gcd(a, b) == 1


if __name__ == '__main__':
    print(f'{is_relative_prime(120, 133)=}')
    print(f'{is_relative_prime(333, 150)=}')