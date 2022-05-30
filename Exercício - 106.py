from time import sleep
c = ('\033[m', #SEM COR
     '\033[0;32m',
     '\033[0;33m',
     '\033[0;31m',
     '\033[0;30;44m',
     '\033[0;30;45m',
     '\033[7;30m'
     );


def ajuda(com):
    título(f'Acessando o manual do comando \'{com}\'', 2)
    print(c[0], end='')
    help(com)
    print(c[0], end='')
    sleep(2)


def título(msg, cor = 0):
    tam = len(msg) + 4
    print(c[cor], end='')
    print('~' * tam)
    print(f'  {msg}')
    print('~' * tam)
    print(c[0], end='')
    sleep(1)


comando = ''
while True:
    título('SISTEMA DE AJUDA PyHelp', 1)
    comando = str(input("Função ou Biblioteca > "))
    if comando.upper() == 'FIM':
        break
    else:
        ajuda(comando)
título('Até logo!!', 3)