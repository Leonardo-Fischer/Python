import random #to use randint()
import time #to use sleep()

#---------------Class---------------#

class Player(object):

    #Atributes 
    def __init__(self):
        self.cards = []
        self.score = 0
        self.bet = 0

    #Method that will receive the first two cards
    def get_cards(self, card):
        self.cards.append(card)

#--------------Methods--------------#

#Method that calculates the score
def score_cards(score, value):
    if type(value) == tuple:
        value = 11
        score += value
    else:
        score += value
    return score


def dealer_plays(d_score, d_cards):
    while d_score <= 16:
        d_cards.append((cards_given[random.randint(0,12)]))
        d_score = score_cards(d_score, cards_values[d_cards[-1]])
    return d_score


def calculate_amount(u, bet, d, d_cards, blackjack):

    print("\n*************************")
    print("Dealer's second card: ", d_cards[1])
    print("\nDealer's final score: ", d)
    print("\nYour final score: ", u)
    print("*************************\n")

    if u == d:
        print("It is a Tie!")
        print("Your final amount is %i chips" %(bet))
    elif blackjack:
        print("You've got a Blackjack!!!")
        #The math is 3/2
        bet += (3/2) * bet
        print("Your final amount is %i chips" %(bet))
    elif (u > d and u < 21) or (u < 21 and d > 21):
        print("You won but it's not a Blackjack")
        #The math is 1/1
        bet += bet
        print("Your final amount is %i chips" %(bet))
    else:
        print("You lose!")
        bet = 0
        print("Your final amount is %i chips" %(bet))

    play_again = '0'
    while play_again != 'y' and play_again != 'Y' and play_again != 'n' and play_again!= 'N':
        play_again = input("\nDo you wanna play again? (y/n) ")
    if play_again == 'y' or play_again == 'Y':
        return True
    else:
        return False

#----------------Main---------------#

global cards_values, cards_given
playing = True

#Counter of A's
counter_As = 0
#Sequence os A's that could occur
As_row = ['first', 'second', 'third', 'fourth']


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

    continuing_round = True #Variable to control the flow of one game
    double = False #Variable to check if one Double has happened
    times = 0 #Variable to count how many times the player asked for a card

    user = Player()
    dealer = Player()

    #Asking bet from the user
    user.bet = int(input("\nHow many chips do you wanna bet? ")) #Insert try and execpt here, to accept only integers

    print("\nDealer is giving the cards... ")
    time.sleep(2)

    #Randomizing the cards
    user.get_cards(cards_given[random.randint(0,12)])
    print("\nYour first card: ", user.cards[0])
    user.get_cards(cards_given[random.randint(0,12)])
    print("Your second card: ", user.cards[1])
    
    #Dealer cards
    dealer.get_cards(cards_given[random.randint(0,12)])
    print("\nDealer's first card: ", dealer.cards[0])
    dealer.get_cards(cards_given[random.randint(0,12)])
    print("Dealer's second card: will be revealed by the end of the game ")


    while continuing_round:

        #The scores are reseted every time to avoid repeated sums
        user.score = 0
        dealer.score = 0

        #Adding the player's total score
        for i in range(0, len(user.cards)):
            user.score = score_cards(user.score, cards_values[user.cards[i]])
            if user.cards[i] == 'A':
                counter_As += 1
        #To handle the cases when user.score > 21 and player has one or more A's
        while user.score > 21 and counter_As > 0:
            print("\nYou've scored more than 21, your %s A is now equal to 1 point" %(As_row[counter_As-1]))
            user.score -= 10
            counter_As -= 1
        print("\nYour score: ", user.score)

        #Adding the dealer's total score
        for i in range(0, len(dealer.cards)):
            dealer.score = score_cards(dealer.score, cards_values[dealer.cards[i]])
        

        #In case of a blackjack!
        if user.score == 21 and times == 0:
            playing = calculate_amount(user.score, user.bet, dealer.score, dealer.cards, True)
            continuing_round = False
            break
        #In case the user points exceeds 21 or in case of a Double move
        elif user.score > 21 or double:
            dealer.score = dealer_plays(dealer.score, dealer.cards)
            playing = calculate_amount(user.score, user.bet, dealer.score, dealer.cards, False)
            continuing_round = False
            break
        else:
            pass
        
        #Asking the player what he/she wants to do
        print("\nWhat you are gonna do?")
        move = '0' #Initializing the variable so the while can work
        while move != '1' and move != '2' and move != '3' and move != '4':
            move = input("1)Stand\n2)Hit\n3)Double\n4)Leave\nMove: ")
        move = int(move)
        
        #Stand
        if move == 1:
            dealer.score = dealer_plays(dealer.score, dealer.cards)
            playing = calculate_amount(user.score, user.bet, dealer.score, dealer.cards, False)
            continuing_round = False
        #Hit
        elif move == 2:
            user.get_cards(cards_given[random.randint(0,12)])
            print("\nYour new card is: ", user.cards[-1])
        #Double
        elif move == 3:
            user.bet += user.bet
            user.get_cards(cards_given[random.randint(0,12)])
            print("\nYour new card is: ", user.cards[-1])
            double = True
        #Leave
        elif move == 4:
            continuing_round = False
            playing = False
        else:
            pass
        
        #Increments the times counter
        times += 1