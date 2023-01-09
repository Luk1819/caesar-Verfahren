def caesar_encrypt(plaintext, shift):
  ciphertext = ""
  for ch in plaintext:
    if ch.isalpha():
      shift_ch = chr((ord(ch) - ord('a') + shift) % 26 + ord('a'))
      ciphertext += shift_ch
    else:
      ciphertext += ch
  return ciphertext

plaintext = "hello"
shift = 3
ciphertext = caesar_encrypt(plaintext, shift)
print("Plaintext:", plaintext)
print("Ciphertext:", ciphertext)
