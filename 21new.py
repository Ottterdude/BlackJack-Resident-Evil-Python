from random import choice
from time import sleep

# listas
mao2 = []
mao1 = []
triunfos1 = ['c1', 'c10', 'a1', 'a2', 'p17', 'p24']
triunfos2 = ['c2', 'c3', 'a1', 'a2', 'p17', 'p24']
baralhotriunfos = []
baralho = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]

# maos dos jogadores
total1 = int(0)
total2 = int(0)
compra = int(0)
inicial1 = int(0)
inicial2 = int(0)

# açoes
acao1 = str()
ultimaacao1 = str()
acao2 = str()
ultimaacao2 = str()
usar1 = str()
usar2 = str()

# valores do jogo
valorpartida = int(21)
vida1 = int(10)
vida2 = int(10)
aposta1 = int(1)
aposta2 = int(1)
cont_aposta = int(1)

# outros
b = '-=' * 25

############


def turnoinicial():
    global inicial1, compra, total1, inicial2, total2
    inicial1 = choice(baralho)
    total1 += inicial1
    baralho.remove(inicial1)

    compra = choice(baralho)
    mao1.append(compra)
    total1 += compra
    baralho.remove(compra)
    ###############################
    inicial2 = choice(baralho)
    total2 += inicial2
    baralho.remove(inicial2)

    compra = choice(baralho)
    mao2.append(compra)
    total2 += compra
    baralho.remove(compra)


def turno1():
    global acao1, total1, valorpartida, compra, ultimaacao1, ultimaacao2, usar1
    print(f'\033[1;91mVida {vida1}/10     Aposta {aposta1}')
    print(f'\033[0:31:40mSuas cartas sao: {inicial1},{mao1} e o total é: {total1}/{valorpartida}')
    print(f'As cartas de seu oponente sao: ?,{mao2} e o total é: ?+{total2 - inicial2}/{valorpartida}')
    sleep(1)
    acao1 = str(input('[1] Comprar\n[2] Passar\n[3] Usar triunfo\n'))
    if acao1 == '1':
        if total1 >= valorpartida:
            print('Voce ja estorou.\nTente outra opcao')
            turno1()
        else:
            compra = choice(baralho)
            total1 += compra
            mao1.append(compra)
            baralho.remove(compra)
        print(f'Voce comprou um: {compra}')
        sleep(1)
        print(f'Suas cartas sao: {inicial1},{mao1} e o total é: {total1}/{valorpartida}')
        print(f'As cartas de seu oponente sao: ?,{mao2} e o total é: ?+{total2 - inicial2}/{valorpartida}')
        print(f'\033[1;91m{vida1}/10')
        print(f'\033[0:31:40m{b}')
        ultimaacao1 = str('1')
        sleep(1)
    elif acao1 == '2':
        print('Fim do turno')
        ultimaacao1 = str('2')
        print(f'Suas cartas sao: {inicial1},{mao1} e o total é: {total1}/{valorpartida}')
        print(f'As cartas de seu oponente sao: ?,{mao2} e o total é: ?+{total2 - inicial2}/{valorpartida}')
        print(f'\033[1;91m{vida1}/10')
        print(f'\033[0:31:40m{b}')
        sleep(1)
    elif acao1 == '3':
        print(f'Voce possui os triunfos: {triunfos1}')
        usar1 = str(input(f'Qual deseja usar?\n'))
        if usar1 in triunfos1:
            if usar1[0] == 'c':
                triunfo_compra(1, usar1[1:3])
            if usar1[0] == 'a':
                triunfo_aposta(1, usar1[1])
                print(f'A aposta do seu inimigo aumento em {usar1[1]}, total: {aposta2}')
            if usar1[0] == 'p':
                triunfo_partida(usar1[1:3])
                print(f'O valor da partida agora é {valorpartida}')
        else:
            print('Voce não possui esse triunfo')
        turno1()
    else:
        print('Opcao invalida tente novamente')
        turno1()


def turno2():
    global acao2, total2, valorpartida, compra, ultimaacao2, ultimaacao1, usar2
    print(f'\033[1;96mVida {vida2}/10     Aposta {aposta2}')
    print(f'\033[0:36:40mSuas cartas sao: {inicial2},{mao2} e o total é: {total2}/{valorpartida}')
    print(f'As cartas de seu oponente sao: ?,{mao1} e o total é: ?+{total1 - inicial1}/{valorpartida}')
    sleep(1)
    acao2 = str(input('[1] Comprar\n[2] Passar\n[3] Usar triunfo\n'))
    sleep(1)
    if acao2 == '1':
        if total2 >= valorpartida:
            print('Voce ja estorou.\nTente outra opcao')
            turno2()
        else:
            compra = choice(baralho)
            total2 += compra
            mao2.append(compra)
            baralho.remove(compra)
            print(f'Voce comprou um: {compra}')
            sleep(1)
            print(f'Suas cartas sao: {inicial2},{mao2} e o total é: {total2}/{valorpartida}')
            print(f'As cartas de seu oponente sao: ?,{mao1} e o total é: ?+{total1 - inicial1}/{valorpartida}')
            print(f'\033[1;96m{vida2}/10')
            print(f'\033[0:36:40m{b}')
            ultimaacao2 = str('1')
            sleep(1)
    elif acao2 == '2':
        print('Fim do turno')
        ultimaacao2 = str('2')
        print(f'Suas cartas sao: {inicial2},{mao2} e o total é: {total2}/{valorpartida}')
        print(f'As cartas de seu oponente sao: ?,{mao1} e o total é: ?+{total1 - inicial1}/{valorpartida}')
        print(f'\033[1;96m{vida2}/10')
        print(f'\033[0:36:40m{b}')
        sleep(1)
    elif acao2 == '3':
        print(f'Voce possui os triunfos: {triunfos2}')
        usar2 = str(input(f'Qual deseja usar?\n'))
        if usar2 in triunfos2:
            if usar2[0] == 'c':
                triunfo_compra(2, usar2[1:3])
            if usar2[0] == 'a':
                triunfo_aposta(2, usar2[1])
                print(f'A aposta do seu inimigo aumento em {usar2[1]}, total: {aposta1}')
            if usar2[0] == 'p':
                triunfo_partida(usar2[1:3])
                print(f'O valor da partida agora é {valorpartida}')
        else:
            print('Voce não possui esse triunfo')
        turno2()
    else:
        print('Opcao invalida tente novamente')
        turno2()


def resultado():
    global vida1, vida2
    print('\033[1;93mE o vencedor é')
    sleep(1)
    print('.')
    sleep(1)
    print('.')
    sleep(1)
    print('.')
    sleep(1)
    if valorpartida >= total1 > total2 or total2 > valorpartida >= total1:
        print(f'{total1} X {total2}\nJogador 1 Parabens!!!!!')
        vida2 -= aposta2
    elif valorpartida >= total2 > total1 or total1 > valorpartida >= total2:
        print(f'{total1} X {total2}\nJogador 2 Parabens!!!!!')
        vida1 -= aposta1
    else:
        print(f'{total1} X {total2}\nEmpate!!!!!')


def resetar():
    global mao1, mao2, total1, total2, baralho, compra, inicial1, inicial2, acao1, acao2, ultimaacao1, ultimaacao2, \
        valorpartida, aposta1, aposta2
    mao2 = []
    mao1 = []
    total1 = int(0)
    total2 = int(0)
    baralho = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
    compra = int(0)
    inicial1 = int(0)
    inicial2 = int(0)
    acao1 = str()
    ultimaacao1 = str()
    acao2 = str()
    ultimaacao2 = str()
    valorpartida = int(21)
    aposta1 = cont_aposta
    aposta2 = cont_aposta


def triunfo_compra(jog, num):
    global total1, total2
    num = int(num)
    if jog == 1:
        if num in baralho:
            baralho.remove(num)
            mao1.append(num)
            total1 += num
            print(f'Voce comprou um: {num}')
            triunfos1.remove(usar1)
        else:
            print(f'Está carta não esta no baralho')
    else:
        if num in baralho:
            baralho.remove(num)
            mao2.append(num)
            total2 += num
            print(f'Voce comprou um: {num}')
            triunfos1.remove(usar2)
        else:
            print(f'Está carta não esta no baralho')


def triunfo_aposta(jog, apo):
    global aposta1, aposta2
    if jog == 1:
        aposta2 += int(apo)
    else:
        aposta1 += int(apo)


def triunfo_partida(pa):
    global valorpartida
    valorpartida = int(pa)


while True:
    turnoinicial()
    while True:
        if ultimaacao1 == '2' and ultimaacao2 == '2':
            break
        turno1()
        if ultimaacao1 == '2' and ultimaacao2 == '2':
            break
        turno2()
    sleep(1)
    print('\033[1;93mFim da Rodada')
    sleep(3)
    resultado()
    resetar()
    cont_aposta += 1
    aposta1 = cont_aposta
    aposta2 = cont_aposta
    print(b)
    sleep(5)
    if vida1 <= 0:
        print('Não foi dessa vez voce morreu jogador 1')
        break
    elif vida2 <= 0:
        print('Não foi dessa vez voce morreu jogador 2')
        break
