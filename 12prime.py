import random

def power(x, y, p):
    res = 1
    x = x % p
    while y > 0:
        if y & 1:
            res = (res * x) % p
        y = y >> 1  # y = y // 2
        x = (x * x) % p
    return res

def miillerTest(d, n):
    a = 2 + random.randint(1, n - 4)
    x = power(a, d, n)

    if x == 1 or x == n - 1:
        return True

    while d != n - 1:
        x = (x * x) % n
        d *= 2

        if x == 1:
            return False
        if x == n - 1:
            return True

    return False

def is_prime(n, k):
    if n <= 1 or n == 4:
        return False
    if n <= 3:
        return True

    d = n - 1
    while d % 2 == 0:
        d //= 2

    for _ in range(k):
        if not miillerTest(d, n):
            return False

    return True

# Driver code
k = 4  # Number of iterations for accuracy
n = int(input("Enter a number: "))

if is_prime(n, k):
    print(f"{n} is a prime number.")
else:
    print(f"{n} is not a prime number.")
