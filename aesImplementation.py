def SubBytes(state):
  # This function would substitute bytes in the state matrix using an S-box (omitted for brevity)
  # ...
  pass

def ShiftRows(state):
  # This function would perform circular byte shifts in each row of the state matrix (omitted for brevity)
  # ...
  pass

def MixColumns(state):
  # This function would perform mixing operations using a specific matrix (omitted for brevity)
  # ...
  pass

def KeyExpansion(key, Nk, Nr):
  # This function would expand the key schedule from the initial key (omitted for brevity)
  # ...
  pass

def AddRoundKey(state, key):
  for i in range(len(state)):
    state[i] ^= key[i]

def AESEncrypt(plaintext, key, Nr):
  # Padding omitted for brevity. Necessary for AES to work on fixed block sizes
  state = [x for x in plaintext]
  state = [state[i:i+4] for i in range(0, len(state), 4)]  # Convert to state matrix

  # Key expansion
  expandedKey = KeyExpansion(key, Nr)

  # Add initial round key
  AddRoundKey(state, expandedKey[:16])

  # Perform Nr rounds
  for round in range(1, Nr):
    SubBytes(state)
    ShiftRows(state)
    MixColumns(state)
    AddRoundKey(state, expandedKey[round * 16:(round + 1) * 16])

  # Final round (no MixColumns)
  SubBytes(state)
  ShiftRows(state)
  AddRoundKey(state, expandedKey[Nr * 16:])

  # Flatten state matrix
  ciphertext = [val for sublist in state for val in sublist]
  return ciphertext

# Example usage (for educational purposes only)
key = [0x00, 0x01, 0x02, 0x03, 0x04, 0x05, 0x06, 0x07, 0x08, 0x09, 0x0a, 0x0b, 0x0c, 0x0d, 0x0e, 0x0f]
plaintext = [0x00, 0x11, 0x22, 0x33]
Nr = 10  # Number of rounds (10 for AES-128)

ciphertext = AESEncrypt(plaintext, key, Nr)
print(f"Plaintext: {plaintext}")
print(f"Ciphertext: {ciphertext}")