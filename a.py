import random

elemets = "+-/*!&$#?=@abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"
pass_length = int(input('passwordnya mau berapa digit?'))

password = ''

for i in range(pass_length):
    password += random.choice(elemets)

print(password)