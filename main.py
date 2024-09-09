import random

caracteres = "+-/*!&$#?=@abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"

while True:
    longitud = int(input("Introduce la longitud de la contraseña: "))
    if longitud < 8:
        print("La contraseña debe ser mayor a 8 caracteres")
    else:
        break

contraseña = ""

for x in range(longitud):
    contraseña += random.choice(caracteres)

print("La contraseña generada es:", contraseña)











