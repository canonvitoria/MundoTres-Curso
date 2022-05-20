dados = {}
gols = list()
time = list()

while True:
    dados.clear()
    gols.clear()
    dados['Nome'] = str(input("Nome do jogador: "))
    partidas = int(input(f'Quantas partidas {dados["Nome"]} jogou? '))
    for p in range(0, partidas):
        gols.append(int(input(f"Quantos gols no {p + 1}? ")))
    dados['Gols'] = gols[:]
    dados['Total'] = sum(gols)
    time.append(dados.copy())
    while True:
        p = str(input("Deseja continuar? [S/N] ")).upper()
        if p in 'SsNn':
            break
        print('ERRO! Digite apenas S ou N.')
    if p == 'N':
        break

print('-' * 30)
print('cod ', end='')

for i in dados.keys():
    print(f'{i:<15}', end='')
print()

print('=' * 40)

for k, v in enumerate(time):
    print(f'{k:>2} ', end='')
    for d in v.values():
        print(f'{str(d):<16}', end='')
    print()
print('=' * 40)

while True:
    busca = int(input("Mostrar dados e qual jogador? (999 para INTERROMPER) " ))
    if busca == 999:
        break
    if busca >= len(time):
        print(f'ERRO! Não existe jogador com o código {busca}! ')
    else:
        print(f' -- LEVANTAMENTO DO JOGADOR {time[busca]["Nome"]}: ')
        for i, g in enumerate(time[busca]['Gols']):
            print(f' >> No jogo {i + 1} fez {g} gols.')

    print('-' * 40)

print('VOLTE SEMPRE!!')