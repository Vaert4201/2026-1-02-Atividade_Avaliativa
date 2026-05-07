import random 

contador = 1

while contador <= 10:
    numero = random.randint(1, 100)
    print(f'{contador}o número aleatório: {numero}')
    contador += 1