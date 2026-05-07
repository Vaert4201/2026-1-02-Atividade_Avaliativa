n = int(input('Digite a quantidade de números que você deseja:'))
contador = 0
soma = 0
maior = float('-inf')
menor = float('inf')
valores = []
while contador < n:
    repeticoes = int(input(f'Informe o valor {contador + 1}: '))
    valores.append(repeticoes)
    soma += repeticoes
    contador += 1
    maior = max(maior, repeticoes)
    menor = min(menor, repeticoes)
    media = soma / contador

acima_media = 0
contador = 0

while contador < n:
    if valores[contador] > media:
        acima_media += 1
    contador += 1

print(' RESULTADOS:')
print(f'Soma total: {soma}')
print(f'Média: {media}')
print(f'Maior valor: {maior}')
print(f'Menor valor: {menor}')
print(f'Quantidade de valores acima da média: {acima_media}')