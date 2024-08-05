import string

def sanitize_input(text):
    printable_chars = set(string.ascii_letters + string.digits + string.punctuation + ' ')
    sanitized_text = ''.join(char for char in text if char in printable_chars)
    return sanitized_text

def encrypt(plaintext, key):
    ciphertext = ''
    for p, k in zip(plaintext, key):
        encrypted_char = chr((ord(p) + ord(k)) % 95 + 32)  
        ciphertext += encrypted_char
    return ciphertext

def decrypt(ciphertext, key):
    decrypted_text = ''
    for c, k in zip(ciphertext, key):
        decrypted_char = chr((ord(c) - ord(k)) % 95 + 32)
        decrypted_text += decrypted_char
    return decrypted_text


if __name__ == "__main__":
    plaintext = input("Enter the plaintext: ")
    key = input("Enter the key: ")

    plaintext = sanitize_input(plaintext.upper())
    key = sanitize_input(key.upper())

    if not plaintext or not key:
        print("Error: Plaintext and key must contain printable ASCII characters.")
    elif len(plaintext) != len(key):
        print("Error: Length of plaintext and key must be the same.")
    else:
        ciphertext = encrypt(plaintext, key)
        print("Plaintext:", plaintext)
        print("Key:", key)
        print("Ciphertext:", ciphertext)
        
        decrypted_text = decrypt(ciphertext, key)
        print("Decrypted Text:", decrypted_text)
