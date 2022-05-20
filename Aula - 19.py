pessoas = {'nome': 'Gustavo', 'sexo': 'M', 'idade': 22}
print(f'O {pessoas["nome"]} tem  {pessoas["idada"]} anos')

pessoas = {'nome': 'Gustavo', 'sexo': 'M', 'idade': 22}
print(pessoas.keys())

pessoas = {'nome': 'Gustavo', 'sexo': 'M', 'idade': 22}
for k in pessoas.keys():
    print(k)

pessoas = {'nome': 'Gustavo', 'sexo': 'M', 'idade': 22}
pessoas['nome'] = 'Leandro' #troca
pessoas['peso'] = 98.5 #adicionar
for k, v in pessoas.items():
    print(f'{k} = {v}')

brasil = []
estado1 = {'uf': 'Rio de Janeiro', 'sigla': 'RJ'}
estado2 = {'uf': 'São Paulo', 'sila': 'SP'}
brasil.append(estado1)
brasil.append(estado2)

print(brasil[1]['sigla'])

estado = {}
brasil = []
for c in range(0, 3):
    estado['uf'] = str(input('Unidade Federativa: '))
    estado['sila'] = str(input('Sigla do Estado: '))
    brasil.append(estado.copy())
for e in brasil:
    for v in e.values():
        print(v, end= ' ')
    print()

        