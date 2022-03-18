import sys
from tasks.encriptFile import password_encrypt
from tasks.const import SECRET

password = sys.argv[1]

encrypted_secret = password_encrypt(SECRET.encode(), password)

with open("secret.txt", "wb") as file:
    file.write(encrypted_secret)
