def lin():
    print('-' * 30)


lin()
print('     CONTROLE DE TERRENOS     ')
lin()

largura = float(input('Largura (m): '))
comprimento = float(input('Comprimento (m): '))
área = (largura * comprimento)

print(f'A área de um terreno {largura} x {comprimento} é de {área}m2')

#Solução do professor
def área(larg, compr):
    a = larg * compr
    print(f'A área de um terreno {larg} x {compr} é de {a}m2.')


print('-' * 20)
print('   CONTROLE DE TERRENOS   ')
print('-' * 20)

l = float(input('Largura (m): '))
c = float(input('Comprimento (m): '))
área(l, c)