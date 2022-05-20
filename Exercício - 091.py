from random import randint
from time import sleep
from operator import itemgetter

jogadores = { 'Jogador-1': randint(1, 6),
              'Jogador-2': randint(1, 6),
              'Jogador-3': randint(1, 6),
              'Jogador-4': randint(1, 6)}

ranking = ()

print(f'Valores sorteados: ')
for k, v in jogadores.items():
    print(f'{k} tirou {v} no dado')
    sleep(1)

ranking= sorted(jogadores.items(), key=itemgetter(1), reverse=True)

print('-' * 35)
print('    == RANKING DOS JOGADORES ==')

for i, v in enumerate(ranking):
    print(f'    {i+1} lugar: {v[0]} com {v[1]} pontos')