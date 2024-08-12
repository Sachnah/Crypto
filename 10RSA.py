import math

# Step 1: Input values for p and q
p = int(input("Enter a prime number p: "))
q = int(input("Enter a prime number q: "))

# Step 2: Calculate n
n = p * q
print("n =", n)

# Step 3: Calculate phi
m = (p - 1) * (q - 1)

# Step 4: Find e
e = 2
while e < m :
    if math.gcd(e, m ) == 1:
        break
    else:
        e += 1

print("e =", e)

# Step 5: Calculate d
k = 2
d = (k * m + 1) // e
print("d =", d)
print(f'Public key: ({e}, {n})')
print(f'Private key: ({d}, {n})')

# Step 6: Input plain text
msg = int(input("Enter a message to encrypt (as an integer): "))
print(f'Original message: {msg}')

# Step 7: Encryption
C = pow(msg, e, n)
print(f'Encrypted message: {C}')

# Step 8: Decryption
M = pow(C, d, n)
print(f'Decrypted message: {M}')
