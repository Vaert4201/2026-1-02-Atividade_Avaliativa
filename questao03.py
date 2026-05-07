numero = int(input('Digite um número inteiro positivo:'))
x = 1
soma = 0
while x < numero:
    if numero % x == 0:
        soma += x
    x += 1

if soma == numero:
    print(f'{numero} é perfeito!')
else:
    print(f'{numero} não é perfeito...')
