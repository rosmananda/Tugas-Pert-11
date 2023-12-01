def otp_encrypt(plaintext, key):
    ciphertext = ""
    for char, key_char in zip(plaintext, key):
        result = ord(char) ^ ord(key_char)
        ciphertext += chr(result)
    return ciphertext

def otp_decrypt(ciphertext, key):
    decrypted_text = ""
    for char, key_char in zip(ciphertext, key):
        result = ord(char) ^ ord(key_char)
        decrypted_text += chr(result)
    return decrypted_text

# Contoh penggunaan
plaintext = "RUSDI"
key = "CRUSH"

# Enkripsi
hasil_enkripsi = otp_encrypt(plaintext, key)
print("Plainteks:", plaintext)
print("Kunci:", key)
print("Hasil Enkripsi:", hasil_enkripsi)

# Dekripsi
hasil_dekripsi = otp_decrypt(hasil_enkripsi, key)
print("Hasil Dekripsi:", hasil_dekripsi)
