import random

elements = "+-/*!&$#?=@<>abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"
password = ""
pass_length = int(input("Introduce la longitud de la contraseña: "))

for i in range(pass_length):
    password += random.choice(elements)

print(password)