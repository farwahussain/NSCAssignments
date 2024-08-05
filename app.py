from tkinter import *

window = Tk()
window.title("Cryptography")
window.geometry("500x500")

window.configure(bg="grey")

# Create a frame for input
input_frame = Frame(window)
input_frame.pack(pady=10)

# Label for input text
text_label = Label(input_frame, text="Enter text to encrypt/decrypt:")
text_label.pack()

# Text input field
text_entry = Entry(input_frame)
text_entry.pack()

# Create a frame for output
output_frame = Frame(window)
output_frame.pack(pady=10)

# Output area for displaying results
output_label = Label(output_frame, text="Output:")
output_label.pack()

output_text = Label(output_frame, text="")
output_text.pack()

morse_code_dict = {
    'A': 'α', 'B': 'β', 'C': 'γ', 'D': 'δ', 'E': 'ε', 'F': 'ζ', 'G': 'η', 'H': 'θ', 'I': 'ι', 'J': 'κ',
    'K': 'λ', 'L': 'μ', 'M': 'ν', 'N': 'ξ', 'O': 'ο', 'P': 'π', 'Q': 'ρ', 'R': 'σ', 'S': 'τ', 'T': 'υ',
    'U': 'φ', 'V': 'χ', 'W': 'ψ', 'X': 'ω', 'Y': 'ϕ', 'Z': 'Ω',
    '1': 'α.', '2': 'β.', '3': 'γ.', '4': 'δ.', '5': 'ε.', '6': 'ζ.', '7': 'η.', '8': 'θ.', '9': 'ι.', '0': 'κ.',
    '.': 'κ.', ',': 'λ.', '?': 'μ.', "'": 'ν.', '!': 'ξ.', '/': 'ο.', '(': 'π.', ')': 'ρ.', '&': 'σ.', ':': 'τ.',
    ';': 'υ.', '=': 'φ.', '+': 'χ.', '-': 'ψ.', '_': 'ω.', '"': 'ϕ.', '$': 'Ω.', '@': 'αϕ.'
}

def encode_to_morse(text):
    morse_code = ''
    for char in text:
        if char.upper() in morse_code_dict:
            morse_code += morse_code_dict[char.upper()] + '/'
        else:
            morse_code += char + '/'
    return morse_code.strip('/')

def decode_from_morse(code):
    text = ''
    morse_code_reversed = {v: k for k, v in morse_code_dict.items()}  # Reverse the dictionary
    for code_segment in code.split('/'):
        if code_segment in morse_code_reversed:
            text += morse_code_reversed[code_segment]
        else:
            text += code_segment
    return text

def caesar_cipher_encrypt(plaintext, shift):
    result = ""
    for char in plaintext:
        if char.isalpha():
            if char.isupper():
                result += chr((ord(char) + shift - 65) % 26 + 65)
            else:
                result += chr((ord(char) + shift - 97) % 26 + 97)
        else:
            result += char
    return result

def caesar_cipher_decrypt(ciphertext, shift):
    return caesar_cipher_encrypt(ciphertext, -shift)

def double_encrypt(plaintext, caesar_shift):
    caesar_encrypted = caesar_cipher_encrypt(plaintext, caesar_shift)
    morse_encoded = encode_to_morse(caesar_encrypted)
    return morse_encoded

def double_decrypt(ciphertext, caesar_shift):
    morse_decoded = decode_from_morse(ciphertext)
    caesar_decrypted = caesar_cipher_decrypt(morse_decoded, caesar_shift)
    return caesar_decrypted

def button_click():
    user_text = text_entry.get()
    caesar_shift = 3  # You can change this value
    encrypted_text = double_encrypt(user_text, caesar_shift)
    output_text.config(text=encrypted_text)

# Create the button
encrypt_button = Button(window, text="Encrypt/Decrypt", command=button_click)
encrypt_button.pack()

window.mainloop()
