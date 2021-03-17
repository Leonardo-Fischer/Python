import random #to use randint()
import time #to use sleep()

class Player(object):

    #Atributes 
    def __init__(self, cards=[], score=0, bet=0):
        self.cards = cards
        self.score = score
        self.bet = bet

    #Method that will receive the first two cards
    def get_cards(self, card):
        self.cards.append(card)

    #Method that will count the score
    def score_cards(self, value):
        if type(value) == tuple:
            value = 11
            self.score += value
        else:
            self.score += value
    

def stand():
    pass

def hit():
    pass

def double():
    pass

def leave():
    pass

global cards_values, cards_given
playing = True


cards_values = {'A': (1, 11), '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, '10': 10, 'J': 10, 'Q': 10, 'K':10}
cards_given = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']

#Presenting the game
print("\nThis is Blackjack.\n")
print("*********************************************************************")
print("If you win with a Blackjack you'll receive 3/2 of your bet")
print("\nIf you win without a Blackjack you'll receive 1/1 of your bet ")
print("\nIf you get a draw you won't get money but you won't lose your bet")
print("*********************************************************************")

while playing:

    player = Player()
    dealer = Player()

    #Asking bet from the user
    player.bet = int(input("\nHow many chips do you wanna bet? ")) #Insert try and execpt here, to accept only integers

    print("\nDealer is giving the cards... ")
    time.sleep(2)

    #Randomizing the cards
    player.get_cards(cards_given[random.randint(0,12)])
    print("\nPlayer first card: ", player.cards[0])
    player.get_cards(cards_given[random.randint(0,12)])
    print("Player second card: ", player.cards[1])
    
    #Dealer cards
    dealer.get_cards(cards_given[random.randint(0,12)])
    print("\nDealer first card: ", dealer.cards[0])
    dealer.get_cards(cards_given[random.randint(0,12)])
    print("Dealer second card: will be revealed by the end of the game ")

    #---------------------------#

    #Adding the player's total score
    for i in range(0, len(player.cards)):
        player.score_cards(cards_values[player.cards[i]])
    print("\nPlayer's score: ", player.score)


    #if player.score > 21 and player has an 'A':
        # consider A  as 1

    if player.score == 21:
        stand()
    else:
        continue
    
    
    

    #Asking the player what he/she wants to do
    print("\nWhat will you do? ")
    move = input("1)Stand\n2)Hit\n3)Double\n4)Leave\nMove: ") #COLOCAR TRAVA PARA NÃO ACEITAR OUTROS NUMEROS/CARACTERES 
    move = int(move)
    
    if move == 1:
        stand()

    print("Passou")
    """
    double = input("\nDo you wanna double the bet? (y/n) ")

    
    if (double == 'y') or (double =='Y'):
        bet = bet * 2
    else:
    #Asking the player it he/she wants to quit
        leave = input("\nDo you wanna quit this round? (y/n) " )
        if (leave == 'y') or (leave == 'Y'):
            print("\nYou got back %1.0f chips" %(bet/2))
            #print total score
            break
        else:
            continue
    
    """
#Stand -> não pedir mais cartas
#Hit -> pedir mais cartas
#Split -> dividir
#Double -> dobra a aposta mas só ganha mais uma carta


#print(cards_values['A'][0]) Catch 1

