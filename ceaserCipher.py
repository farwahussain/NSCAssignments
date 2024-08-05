def caesar_cipher(text, shift):
    result = ""

    for char in text:
        if char.isalpha():  
            if char.isupper():
                result += chr((ord(char) - 65 + shift) % 26 + 65)  
            else:
                result += chr((ord(char) - 97 + shift) % 26 + 97)  
        else:
            result += char  

    return result

# Example usage:
text = "Farwa Hussain"
shift = 3
encrypted_text = caesar_cipher(text, shift)
print("Original text:", text)
print("Encrypted text:", encrypted_text)
