dados = {}
gols = list()

dados['Nome'] = str(input("Nome do Jogador: "))
totpartidas = int(input(f'Quantas partidas {dados["Nome"]} jogou? '))

print('-' * 30)
for p in range(0, totpartidas):
    gols.append(int(input(f"Quantos gols na partida {p + 1}?  ")))

dados['Gols'] = gols[:]
dados['Total'] = sum(gols)

print('-' * 30)

print(dados)

print('-' * 30)

print(f'No campo Nome: {dados["Nome"]}')
print(f'No campo Gols: {gols}')
print(f'No campo Total de Gols: {dados["Total"]}')

print('-' * 30)

print(f'O jogador {dados["Nome"]} jogou {totpartidas}')

for i, v in enumerate(dados['Gols']):
    print(f' >>Na partida {i + 1}, fez {v} gols.')