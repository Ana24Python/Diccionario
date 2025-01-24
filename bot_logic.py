import random

def gen_pass(pass_length):
    elements = "+-/*!&$#?=@<>0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
    password = ""

    for i in range(pass_length):
        password += random.choice(elements)

    return password

