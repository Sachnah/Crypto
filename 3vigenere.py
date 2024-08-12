def encipher():
    input_text = input("Enter Plain Text: ")
    key = input("Enter Key Value: ")
    print("Resultant Cipher Text:", end=" ")

    key = key.upper()
    j = 0

    for i in range(len(input_text)):
        if j >= len(key):
            j = 0

        char_input = ord(input_text[i].upper()) - 65
        char_key = ord(key[j]) - 65

        cipher_char = chr(65 + ((char_input + char_key) % 26))
        print(cipher_char, end="")

        j += 1

def decipher():
    input_text = input("Enter Cipher Text: ")
    key = input("Enter the key value: ")
    print("Resultant Deciphered Text:", end=" ")

    key = key.upper()
    j = 0

    for i in range(len(input_text)):
        if j >= len(key):
            j = 0

        char_input = ord(input_text[i].upper()) - 65
        char_key = ord(key[j]) - 65

        decipher_char = chr(65 + ((char_input - char_key) % 26))
        print(decipher_char, end="")

        j += 1

def main():
    while True:
        print("1. Encrypt Text")
        print("2. Decrypt Text")
        print("3. Exit")
        choice = int(input("Enter Your Choice: "))

        if choice == 3:
            break
        elif choice == 1:
            encipher()
        elif choice == 2:
            decipher()
        else:
            print("Please Enter a Valid Option.")

if __name__ == "__main__":
    main()