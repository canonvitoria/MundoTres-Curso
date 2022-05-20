'''valores = []

valores1 = int(input("Digite um valor para a posição 0: "))
valores2 = int(input("Digite um valor para a posição 1: "))
valores3 = int(input("Digite um valor para a posição 2: "))
valores4 = int(input("Digite um valor para a posição 4: "))

valores.append(valores1)
valores.append(valores2)
valores.append(valores3)
valores.append(valores4)

print('-' * 50)
print(f'Você digitou os valores {valores}')
print('-' * 50)

maior = 0
menor = 0
c = 0
if c == 0:
    maior = menor = valores[c]
else:
    if valores[c] > maior:
        maior = valores
    if valores[c] < menor:
        menor = valores[c]
for c, v in enumerate(valores):

print(f'O maior valor digitado foi {maior} e está na posição {c}')'''

listanum = []
mai = 0
men = 0
for c in range(0, 5):
    listanum.append(int(input(f'Digite um valor para a posição {c}: ')))
    if c == 0:
        mai = men = listanum[c]
    else:
        if listanum[c] > mai:
            mai = listanum[c]
        if listanum[c] < men:
            men = listanum[c]

print('-' * 50)
print(f'Você digitou os valores {listanum}')
print('-' * 50)
print(f'O maior valor digitado foi {mai} nas posições ', end='')

for i, v in enumerate(listanum):
    if v == mai:
        print(f'{i}...')

print(f'O menor valor digitado foi {men} nas posições ', end='')
for i, v in enumerate(listanum):
    if v == men:
        print(f'{i}... ', end='')
print()
