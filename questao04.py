numero = int(input('Digite o seu número:'))

if numero < 0:
    raise ValueError ('Número deve ser positivo.')

contador = 0

while numero > 0:
    numero //= 10
    contador += 1
print(f'Quantidade de digitos: {contador}')
