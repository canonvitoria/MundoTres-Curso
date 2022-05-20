teste = list()
teste.append('Gustavo')
teste.append(40)
print(teste)

#Adicionando mais pessoas
galera = list()
galera.append(teste[:])
teste[0] = 'Maria'
teste[1] = 22
galera.append(teste[:])
print(galera)

#Fatiamento
galera = [['João', 19], ['Ana', 33], ['Joaquim', 13], ['Maria', 45]]
print(galera[0])  # Somente dados do João
print(galera[0][0]) #Somente 'João'

#Criando uma lista
galera = [['João', 19], ['Ana', 33], ['Joaquim', 13], ['Maria', 45]]
for p in galera:
    print(p[0])

#Ou

galera = [['João', 19], ['Ana', 33], ['Joaquim', 13], ['Maria', 45]]
for p in galera:
    print(f'{p[0]} tem {p[1]} anos de idade')

#Pedindo nome e idade
galera = list()
dado = list()
for c in range(0, 3):
    dado.append(str(input("Nome: ")))
    dado.append(int(input('Idade: ')))
    galera.append(dado[:])
    dado.clear()
print(galera)

#Mostrar dados especificos
totmai = 0
totmen = 0
for p in galera:
    if p[1] >= 21:
        print(f'{p[0]} é maior de idade')
        totmai += 1
    else:
        print(f'p{[0]} é menor de idade')
      #  totmen += teste = list()
teste.append('Gustavo')
teste.append(40)
print(teste)

#Adicionando mais pessoas
galera = list()
galera.append(teste[:])
teste[0] = 'Maria'
teste[1] = 22
galera.append(teste[:])
print(galera)

#Fatiamento
galera = [['João', 19], ['Ana', 33], ['Joaquim', 13], ['Maria', 45]]
print(galera[0])  # Somente dados do João
print(galera[0][0]) #Somente 'João'

#Criando uma lista
galera = [['João', 19], ['Ana', 33], ['Joaquim', 13], ['Maria', 45]]
for p in galera:
    print(p[0])

#Ou

galera = [['João', 19], ['Ana', 33], ['Joaquim', 13], ['Maria', 45]]
for p in galera:
    print(f'{p[0]} tem {p[1]} anos de idade')

#Pedindo nome e idade
galera = list()
dado = list()
for c in range(0, 3):
    dado.append(str(input("Nome: ")))
    dado.append(int(input('Idade: ')))
    galera.append(dado[:])
    dado.clear()
print(galera)

#Mostrar dados especificos
totmai = 0
totmen = 0
for p in galera:
    if p[1] >= 21:
        print(f'{p[0]} é maior de idade')
        totmai += 1
    else:
        print(f'p{[0]} é menor de idade')
        totmen += 1