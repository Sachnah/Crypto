def gcd(a, b):
    return a if b == 0 else gcd(b, a % b)

def power(x, y, m):
    if y == 0:
        return 1
    p = power(x, y // 2, m) % m
    p = (p * p) % m
    return p if y % 2 == 0 else (x * p) % m

def mod_inverse(a, m):
    if gcd(a, m) != 1:
        print("Inverse doesn't exist")
    else:
        print("Modular multiplicative inverse of", a, "is", power(a, m - 2, m))


a = 3
m = 11
mod_inverse(a, m)
