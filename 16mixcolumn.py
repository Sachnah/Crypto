def galois_multiply(a, b):
    p = 0
    for i in range(8):
        if b & 1:
            p ^= a
        carry = a & 0x80
        a <<= 1
        if carry:
            a ^= 0x1b
        b >>= 1
    return p % 256

def mix_single_column(a):
    temp = a.copy()
    a[0] = galois_multiply(temp[0], 2) ^ galois_multiply(temp[3], 1) ^ galois_multiply(temp[2], 1) ^ galois_multiply(temp[1], 3)
    a[1] = galois_multiply(temp[1], 2) ^ galois_multiply(temp[0], 1) ^ galois_multiply(temp[3], 1) ^ galois_multiply(temp[2], 3)
    a[2] = galois_multiply(temp[2], 2) ^ galois_multiply(temp[1], 1) ^ galois_multiply(temp[0], 1) ^ galois_multiply(temp[3], 3)
    a[3] = galois_multiply(temp[3], 2) ^ galois_multiply(temp[2], 1) ^ galois_multiply(temp[1], 1) ^ galois_multiply(temp[0], 3)

def mix_columns(state):
    for i in range(4):
        mix_single_column(state[i])
    return state

# Example usage
state = [
    [0xdb, 0x13, 0x53, 0x45],
    [0xf2, 0x0a, 0x22, 0x5c],
    [0x01, 0x01, 0x01, 0x01],
    [0xc6, 0xc6, 0xc6, 0xc6]
]

print("State before MixColumns:")
for row in state:
    print([hex(x) for x in row])

mixed_state = mix_columns(state)

print("\nState after MixColumns:")
for row in mixed_state:
    print([hex(x) for x in row])
