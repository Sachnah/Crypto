from Crypto.Cipher import DES
from Crypto.Util.Padding import pad, unpad
from Crypto.Random import get_random_bytes

# Function to perform DES encryption
def des_encrypt(plain_text, key):
    # Ensure key is 8 bytes long
    if len(key) != 8:
        raise ValueError("Key must be 8 bytes long")
    cipher = DES.new(key, DES.MODE_ECB)  # Create a new DES cipher object in ECB mode
    padded_text = pad(plain_text.encode(), DES.block_size)  # Pad the plaintext to be a multiple of the block size
    encrypted_text = cipher.encrypt(padded_text)  # Encrypt the padded plaintext
    return encrypted_text

# Function to perform DES decryption
def des_decrypt(encrypted_text, key):
    # Ensure key is 8 bytes long
    if len(key) != 8:
        raise ValueError("Key must be 8 bytes long")
    cipher = DES.new(key, DES.MODE_ECB)  # Create a new DES cipher object in ECB mode
    decrypted_padded_text = cipher.decrypt(encrypted_text)  # Decrypt the ciphertext
    decrypted_text = unpad(decrypted_padded_text, DES.block_size)  # Remove the padding from the decrypted text
    return decrypted_text.decode()

# Example usage
if __name__ == "__main__":
    key = get_random_bytes(8)  # Generate a random 8-byte key
    plain_text = "Hello, World!"

    print(f"Original text: {plain_text}")
    print(f"Key (hex): {key.hex()}")

    encrypted_text = des_encrypt(plain_text, key)
    print(f"Encrypted text (hex): {encrypted_text.hex()}")

    decrypted_text = des_decrypt(encrypted_text, key)
    print(f"Decrypted text: {decrypted_text}")
