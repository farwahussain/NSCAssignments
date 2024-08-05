def text_to_morse(text):
    morse_code_dict = {
        'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.', 'G': '--.', 'H': '....',
        'I': '..', 'J': '.---', 'K': '-.-', 'L': '.-..', 'M': '--', 'N': '-.', 'O': '---', 'P': '.--.',
        'Q': '--.-', 'R': '.-.', 'S': '...', 'T': '-', 'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-',
        'Y': '-.--', 'Z': '--..', ' ': '/', '1': '.----', '2': '..---', '3': '...--', '4': '....-', 
        '5': '.....', '6': '-....', '7': '--...', '8': '---..', '9': '----.', '0': '-----'
    }
    
    morse_code = ''
    for char in text.upper():
        if char in morse_code_dict:
            morse_code += morse_code_dict[char] + ' '
        else:
            morse_code += char  # Keep non-alphabetic characters as they are
    
    return morse_code.strip()  # Remove trailing whitespace

def morse_to_text(morse_code):
    morse_code_dict = {".-": 'A', "-...": 'B', "-.-.": 'C', "-..": 'D', ".": 'E', "..-.": 'F',
                       "--.": 'G', "....": 'H', "..": 'I', ".---": 'J', "-.-": 'K', ".-..": 'L',
                       "--": 'M', "-.": 'N', "---": 'O', ".--.": 'P', "--.-": 'Q', ".-.": 'R',
                       "...": 'S', "-": 'T', "..-": 'U', "...-": 'V', ".--": 'W', "-..-": 'X',
                       "-.--": 'Y', "--..": 'Z',
                       "-----": '0', ".----": '1', "..---": '2', "...--": '3', "....-": '4',
                       ".....": '5', "-....": '6', "--...": '7', "---..": '8', "----.": '9',
                       "/": ' '}
 
    words = morse_code.split('   ')  # Words are separated by three spaces
    translated_text = ''
 
    for word in words:
        letters = word.split(' ')
        for letter in letters:
            # Default to empty string if not found
            translated_text += morse_code_dict.get(letter, '')
        translated_text += ' '  # Add space between words
 
    return translated_text.strip()  # Remove trailing space

# Example usage
text_input = input("Enter the text to convert to Morse code: ")
morse_code_output = text_to_morse(text_input)
print("Text:", text_input)
print("Morse Code:", morse_code_output)

text_output = morse_to_text(morse_code_output)
print("morse code to Text:", text_output)
