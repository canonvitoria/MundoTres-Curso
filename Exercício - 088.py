from random import randint
from time import sleep
lista = []
sorteios = []

print('-' * 50)

print(f'               JOGO NA MEGA SENA')

print('-' * 50)

p = int(input('Quantos jogos você quer que eu sorteie?'))
tot = 1
while tot <= p:
    cont = 0
    while True:
        num = randint(1, 60)
        if num not in lista:
            lista.append(num)
            cont += 1
        if cont >= 6:
            break
    lista.sort()
    sorteios.append(lista[:])
    lista.clear()
    tot += 1
print('-' * 15, f' SORTEANDO {p} JOGOS ', '-' * 15)
for i, l in enumerate(sorteios):
    print(f'Jogo {i + 1}: {l}')
    sleep(1)
print(f'-' * 15, '< BOA SORTE! >', '-' * 15)