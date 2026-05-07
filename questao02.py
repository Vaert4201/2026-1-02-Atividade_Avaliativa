import random

repeticoes = int(input('Digite a quantidade de números aleatórios.'))

contador = 1

while contador <= repeticoes:
    num = random.randint(1, 100)
    print(f'{contador}o número aleatório: {num}')
    contador += 1

