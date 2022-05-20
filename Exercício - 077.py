palavras = ('PROGRAMACAO', 'DESENHO', 'SONHO', 'VIAGEM',
            'CURSO', 'ESTUDAR', 'AMOR', 'CASA', 'TRABALHAR',
            'LIVROS', 'FELICIDADE', 'REALIZACAO')

for p in palavras:
    print(f'\nNa palavra {p} temos', end=' ')
    for letras in p:
        if letras.lower() in 'aeiou':
            print(letras, end = ' ')








