from random import randint
from time import sleep
numeros = []
def mega_sena(lista):
    print('_-_'*30)
    print('    Seja Bem vindo ao Programa que gera 6 números para o jogo da megasena    ')
    print('_-_' * 30)
    sleep(1)
    print('Sorteando os 6 números a serem jogados..........')
    for n in range(0,6):
        n=randint(1,61)
        lista.append(n)
        print({n}, end=' ', flush=True)
        sleep(0.5)

mega_sena(numeros)