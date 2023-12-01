import hashlib

# Fungsi untuk mengenkripsi teks dengan Vigenere Cipher
def vigenere_encrypt(plain_text, key):
    encrypted_text = ""
    key_length = len(key)
    for i in range(len(plain_text)):
        char = plain_text[i]
        key_char = key[i % key_length]
        encrypted_char = chr(((ord(char) + ord(key_char)) % 26) + ord('A'))
        encrypted_text += encrypted_char
    return encrypted_text

# Fungsi untuk membuat hash dari password dengan SHA-256
def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()

# Data pengguna yang disimpan dalam database
user_database = {
    'username1': {
        'password': hash_password('password1'),
        'key': 'KEY'
    },
    'username2': {
        'password': hash_password('password2'),
        'key': 'SECRET'
    }
}

# Fungsi untuk melakukan login
def login(username, password):
    if username in user_database:
        user_data = user_database[username]
        encrypted_password = vigenere_encrypt(password, user_data['key'])
        if encrypted_password == user_data['password']:
            print("Login berhasil")
        else:
            print("Password salah")
    else:
        print("Username tidak ditemukan")

# Contoh penggunaan
username = input("Masukkan username:")
password = input("Masukkan password:")
login(username, password)