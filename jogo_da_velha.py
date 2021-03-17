global coluna1, coluna2, coluna3, coluna4, coluna5, coluna6, coluna7, coluna8, coluna9, coluna10, coluna11

#Função para assimilar as jogadas dos jogadores
def status_jogo(jogada, player):
    
    if player == 1:

        if jogada == '1':
            coluna2[0] = 'X'
        elif jogada == '2':
            coluna6[0] = 'X'
        elif jogada == '3':
            coluna10[0] = 'X'
        elif jogada == '4':
            coluna2[2] = 'X'
        elif jogada == '5':
            coluna6[2] = 'X'
        elif jogada == '6':
            coluna10[2] = 'X'
        elif jogada == '7':
            coluna2[4] = 'X'
        elif jogada == '8':
            coluna6[4] = 'X'
        elif jogada == '9':
            coluna10[4] = 'X'
        else:
            pass
    elif player == 2:
        
        if jogada == '1':
            coluna2[0] = 'O'
        elif jogada == '2':
            coluna6[0] = 'O'
        elif jogada == '3':
            coluna10[0] = 'O'
        elif jogada == '4':
            coluna2[2] = 'O'
        elif jogada == '5':
            coluna6[2] = 'O'
        elif jogada == '6':
            coluna10[2] = 'O'
        elif jogada == '7':
            coluna2[4] = 'O'
        elif jogada == '8':
            coluna6[4] = 'O'
        elif jogada == '9':
            coluna10[4] = 'O'
        else:
            pass

    #Imprime conforme a atualização das jogadas
    for i in range(len(coluna1)):
        print(coluna1[i], coluna2[i], coluna3[i], coluna4[i], coluna5[i], coluna6[i], coluna7[i], coluna8[i], coluna9[i], coluna10[i], coluna11[i])


#Função para computar o jogo
def computa_jogo():

    #Condições de jogadas verticais
    if (coluna2[0] == 'X') and (coluna2[2] == 'X') and (coluna2[4] == 'X'):
        print("\nJogador 1 Ganhou!\n")
        return False
    elif (coluna2[0] == 'O') and (coluna2[2] == 'O') and (coluna2[4] == 'O'):
        print("\nJogador 2 Ganhou!\n")
        return False
    elif (coluna6[0] == 'X') and (coluna6[2] == 'X') and (coluna6[4] == 'X'):
        print("\nJogador 1 Ganhou!\n")
        return False
    elif (coluna6[0] == 'O') and (coluna6[2] == 'O') and (coluna6[4] == 'O'):
        print("\nJogador 2 Ganhou!\n")
        return False
    elif (coluna10[0] == 'X') and (coluna10[2] == 'X') and (coluna10[4] == 'X'):
        print("\nJogador 1 Ganhou!\n")
        return False
    elif (coluna10[0] == 'O') and (coluna10[2] == 'O') and (coluna10[4] == 'O'):
        print("\nJogador 2 Ganhou!\n")
        return False
    
    #Condições de jogadas horizontais
    elif (coluna2[0] == 'X') and (coluna6[0] == 'X') and (coluna10[0] == 'X'):
        print("\nJogador 1 Ganhou!\n")
        return False
    elif (coluna2[0] == 'O') and (coluna6[0] == 'O') and (coluna10[0] == 'O'):
        print("\nJogador 2 Ganhou!\n")
        return False
    elif (coluna2[2] == 'X') and (coluna6[2] == 'X') and (coluna10[2] == 'X'):
        print("\nJogador 1 Ganhou!\n")
        return False
    elif (coluna2[2] == 'O') and (coluna6[2] == 'O') and (coluna10[2] == 'O'):
        print("\nJogador 2 Ganhou!\n")
        return False
    elif (coluna2[4] == 'X') and (coluna6[4] == 'X') and (coluna10[4] == 'X'):
        print("\nJogador 1 Ganhou!\n")
        return False
    elif (coluna2[4] == 'O') and (coluna6[4] == 'O') and (coluna10[4] == 'O'):
        print("\nJogador 2 Ganhou!\n")
        return False
    
    #Condições de jogadas diagonais
    elif (coluna2[0] == 'X') and (coluna6[2] == 'X') and (coluna10[4] == 'X'):
        print("\nJogador 1 Ganhou!\n")
        return False
    elif (coluna2[0] == 'O') and (coluna6[2] == 'O') and (coluna10[4] == 'O'):
        print("\nJogador 2 Ganhou!\n")
        return False
    elif (coluna10[0] == 'X') and (coluna6[2] == 'X') and (coluna2[4] == 'X'):
        print("\nJogador 1 Ganhou!\n")
        return False
    elif (coluna10[0] == 'O') and (coluna6[2] == 'O') and (coluna2[4] == 'O'):
        print("\nJogador 2 Ganhou!\n")
        return False
    else:
        return True


#Jogadores começam com nenhuma jogada
jogada_1 = 0
jogada_2 = 0
jogo_continua = True

#Contador para o número de jogadas
contador = 0


print("\nBem vindo ao Jogo da Velha!\n")
print("Jogador 1 será 'X' e Jogador 2 será 'O'\n")
print("Para escolher sua jogada indique o número (1 a 9)\n")

#Imprimindo o tabuleiro de jogo
coluna1 = [' ', '-', ' ', '-', ' ']
coluna2 = ['1', '-', '4', '-', '7']
coluna3 = [' ', '-', ' ', '-', ' ']
coluna4 = ['|', '|', '|', '|', '|']

coluna5 = [' ', '-', ' ', '-', ' ']
coluna6 = ['2', '-', '5', '-', '8']
coluna7 = [' ', '-', ' ', '-', ' ']
coluna8 = ['|', '|', '|', '|', '|']

coluna9 = [' ', '-', ' ', '-', ' ']
coluna10 = ['3', '-', '6', '-', '9']
coluna11 = [' ', '-', ' ', '-', ' ']


for i in range(len(coluna1)):
    print(coluna1[i], coluna2[i], coluna3[i], coluna4[i], coluna5[i], coluna6[i], coluna7[i], coluna8[i], coluna9[i], coluna10[i], coluna11[i])


while jogo_continua and contador < 9:
    jogada_1 = input("\nJogador 1, sua vez: ")
    status_jogo(jogada_1, 1)
    contador += 1

    if computa_jogo() == True and contador < 9:
        jogada_2 = input("Jogador 2, sua vez: ")
        status_jogo(jogada_2, 2)
        contador += 1

        if computa_jogo() == True:
            pass
        else:
            jogo_continua = False
    elif contador == 9:
        print("\nEmpate!")
    else:
        jogo_continua = False
    

