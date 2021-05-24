import numpy as np
import os, random
def limpaTela():
    os.system('cls')

def titulo():
    print('='*50)
    print('\t\t\t\t\033[7;30;42mJogo dos Dados\033[m')
    print('='*50)

class InputError:
    pass

class cores:
    ciano = '\033[1;36m'
    branco = '\033[1;97m'
    amarelo = '\033[1;33m'
    verde = '\033[92m'
    vermelho = '\033[91m'


continuar = 'S'
def simulacao(num):
      try:
            ganha = perde = 0
            prejuizo = -5
            lucro = 20
            lucroLiquido  = []
            lucroMedio = []
            for i in range(num):
                dado1 = random.randint(1, 6)
                dado2 = random.randint(1, 6)
                print(dado1, dado2, end='\n')
                if dado1 == dado2:
                        lucroLiquido.append(lucro)
                        ganha += 1
                else:
                    lucroLiquido.append(prejuizo)
                    perde += 1
            resultado = ganha * 20 + perde * -5
            lucroMedio.append(lucroLiquido)
            #print(lucroMedio)
            print('Você ganhou {} vez(es) e perdeu {} vez(es)'.format(ganha, perde))
            print('Seu lucro líquido foi de {}'.format(resultado))
            #print(lucroLiquido)
            print(f'Lucro médio {np.array(lucroMedio).mean()}')#lucro medio de 'num' rodadas
      except ValueError:
        print('Valor inválido. Deve-se digitar apenas inteiros positivos')


while True:
    titulo()
    num = int(input(cores.amarelo + 'Digite quantas vezes deseja realizar o jogo: \033[m'))
    simulacao(num)
    continuar = str(input('Deseja jogar novamente? [S/N]')).upper().strip()[0]
    if continuar in 'Nn':
        break
    if continuar not in 'SsNn':
        raise InputError
    limpaTela()

print(cores.verde + 'Obrigada, volte sempre!')