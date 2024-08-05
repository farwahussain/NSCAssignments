def vigenere_encrypt(message, key):
    encrypted_message = ""
    key_index = 0
    for char in message:
        if char.isalpha():
            # Convert the character to uppercase for consistency
            char = char.upper()
            key_char = key[key_index % len(key)].upper()
            # Convert characters to their respective ASCII values
            char_ascii = ord(char) - ord('A')
            key_ascii = ord(key_char) - ord('A')
            # Perform the Vigenère encryption
            encrypted_char = chr(((char_ascii + key_ascii) % 26) + ord('A'))
            encrypted_message += encrypted_char
            key_index += 1
        else:
            # Non-alphabetic characters remain unchanged
            encrypted_message += char
    return encrypted_message

# Example usage
plaintext = input("Enter the message: ")
key = input("Enter the key: ")
encrypted_text = vigenere_encrypt(plaintext, key)
print("Encrypted message:", encrypted_text)
