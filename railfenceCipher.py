def rail_fence_encrypt(plaintext, rails):
    fence = [[] for _ in range(rails)]
    rail = 0
    direction = 1

    for char in plaintext:
        fence[rail].append(char)
        rail += direction
        if rail == rails - 1 or rail == 0:
            direction *= -1

    cipher_text = ''.join(''.join(rail) for rail in fence)
    return cipher_text

# Example usage
plaintext = input("Enter the plaintext: ")
rails = int(input("Enter the number of rails: "))

encrypted_text = rail_fence_encrypt(plaintext, rails)
print("Plaintext:", plaintext)
print("Number of rails:", rails)
print("Encrypted text:", encrypted_text)
