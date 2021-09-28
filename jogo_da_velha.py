from random import randint
itens = ('Pedra', 'Papel', 'Tesoura')
computador = randint(0,2)
ques = int(input('''Suas Opções:
[1] - Pedra
[2] - Papel
[3] - Tesoura
Escolha sua jogada: '''))
if computador == 0:
    if ques == 1:
        print('COMPUTADOR JOGOU {}'.format(itens[computador]))
        print('EMPATE!!!')
    if ques == 2:
        print('COMPUTADOR JOGOU {}'.format(itens[computador]))
        print('VOCÊ GANHOU!!!')
    if ques == 3:
        print('COMPUTADOR JOGOU {}'.format(itens[computador]))
        print('COMPUTADOR GANHOU!!!')
elif computador == 1:
    if ques == 1:
        print('COMPUTADOR JOGOU {}'.format(itens[computador]))
        print('COMPUTADOR GANHOU!!!')
    if ques == 2:
        print('COMPUTADOR JOGOU {}'.format(itens[computador]))
        print('EMPATE!!!')
    if ques == 3:
        print('COMPUTADOR JOGOU {}'.format(itens[computador]))
        print('VOCÊ GANHOU!!!')
elif computador == 2:
    if ques == 1:
        print('COMPUTADOR JOGOU {}'.format(itens[computador]))
        print('VOCÊ GANHOU!!!')
    if ques == 2:
        print('COMPUTADOR JOGOU {}'.format(itens[computador]))
        print('VOCÊ PERDEU!!!')
    if ques == 3:
        print('COMPUTADOR JOGOU {}'.format(itens[computador]))
        print('EMPATE!!!')
