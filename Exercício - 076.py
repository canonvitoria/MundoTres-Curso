preços = ('Lápis', '1.50', 'Borracha', '0.50', 'Caderno', '14.90',
          'Estojo', '15.00', 'Transferidor', '4.20', 'Compasso',
          '9.99', 'Mochila', '100.00', 'Caneta', '2.50', 'Livros',
          '120.00')
print('=' * 50)

print(f'{"LISTAGEM DE PREÇOS":^50}')

print('=' * 50)

print(f"{preços[0]}.....................................R$    {preços[1]}")
print(f"{preços[2]}..................................R$    {preços[3]}")
print(f"{preços[4]}...................................R$   {preços[5]}")
print(f"{preços[6]}....................................R$   {preços[7]}")
print(f"{preços[8]}..............................R$    {preços[9]}")
print(f"{preços[10]}..................................R$    {preços[11]}")
print(f"{preços[12]}...................................R$  {preços[13]}")
print(f"{preços[14]}....................................R$    {preços[15]}")
print(f"{preços[16]}....................................R$  {preços[17]}")

#Maneira feita pelo professor

listagem = ('Lápis', 1.75,
            'Borracha', 2,
            'Caderno', 15.90,
            'Estojo', 25,
            'Transferidor', 4.20,
            'Comopasso', 9.99,
            'Mochila', 120.32,
            'Canetas', 22.30,
            'Livro', 34.90)

print('-' * 40)
print(f'{"LISTAGEM DE PREÇOS":^40}')
print('-' * 40)
for pos in range(0, len(listagem)):
    if pos % 2 == 0:
        print(f'{listagem[pos]:.<30}',end='')
    else:
        print(f'R${listagem[pos]:>7.2f}')
print('-' * 40)