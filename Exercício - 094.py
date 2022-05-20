dados = dict()
galera = list()
soma = 0
média = 0

while True:
    dados.clear()
    dados['Nome'] = str(input('Nome: '))
    while True:
        dados['Sexo'] = str(input('Sexo [M/F]: ')).upper()[0]
        if dados['Sexo'] in 'MF':
            break
        else: print(f'ERRO! Por favor, digite apenas M ou F.')
    dados['idade'] = int(input('Idade: '))
    soma += dados['idade']
    galera.append(dados.copy())
    while True:
        resp = str(input('Quer continuar? [S/N] ')).upper()[0]
        if resp in 'SN':
            break
        else: print('Erro! Responda apenas S ou N.')
    if resp == 'N':
        break
print('-' * 30)

print(f'>> Foram cadastradas {len(galera)} pessoas')

média = soma / len(galera)
print(f'>> A média de idade é de {média:5.2f} anos.')

print('>> Todas as mulheres cadastradas foram ', end='')
for p in galera:
    if p['Sexo'] in 'Ff':
        print(f'{p["Nome"]} ', end='')
print()

print('>> Lista de pessoas que estão acima da média de idade: ')
for p in galera:
    if p['idade'] >= média:
        for k, v in p.items():
            print(f'{k} = {v}; ', end='')
        print()
print('<< ENCERRADO >>')