import random

chars = "ABCDEFGHIJKLMNOPQRSTUVWXYZ\
    abcdefghijklmnopqrstuvwxyz\
    01234567890\
        !#$%&/()=?\¿¡'*¨´[{^}]`-_.:,;"

n = int(input("Number of characters for your password: "))

password = ""

for i in range(n):
    password += random.choice(chars)

print(password)
