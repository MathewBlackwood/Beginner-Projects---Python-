#Need to create a way to store a holding of 5-9 decks of cards that will:
  # Shuffle completely at the start of a game 
  # Maintain their order as the game goes on 
  # can be randomly re-shuffled 

#Need to create a dealer that takes to random cards from the 6 decks in order 
  #Dealer has the option to reshuffle the deck if he's losing money 
  #Dealer needs to reveal his cards before the player and if it's blackjack all players lose

#Need to Setup the player class with the option of 6 positions
  #Player needs the basic functions Hit, Double, Split 
  #Player needs a "Ask for advice" option 

#Need to setup the "Friend" who's a gambling expert and will you advise on what to do
  #Expert will be based on advise from a popular blackjack website - could potentially use the +1, +0, -1 system, though i think
  #there should be a more mathematically sound option for each response variable based on which card the dealer is showing
  #e.g. if he's showing 16 and you're showing 15, but the count is at a certain point where 6 of each card between 6-9 has already been presented 
  #Statistically you're better off standing because the next card is a guaruanteed to be a 10 meaning a dealer bust - which means you should 
  #bet as much as you possibly can 


import random

friendHand = []
friendBet = 0

playerHand = []
playerBet = 0 
playerBalance = 1000
gameInPlay = False
betMade = False

dealerHand = []


deck = [2,3,4,5,6,7,8,9,10,"J","Q","K","A"]
deckNumber = 0
cardPool = []

#Functions below - Thought: Maybe intergrate them into classes, gives scalability

#Function 1: Shuffle cards - Maybe used by dealer every x hands - or if player wins too much 
def shuffleCards(cardPool): 
    random.shuffle(cardPool)

#Function 2: Used to cleanup cards from all 3 players 
def returnAllCards(cardPool):
    cardPool.extend(friendHand)
    friendHand.clear()

    cardPool.extend(playerHand) #Copies the cards back to the cardpool at the end 
    playerHand.clear()          #Deletes the cards in the players hands 

    cardPool.extend(dealerHand)
    dealerHand.clear()

#Function 3: Setting up drawing a card from the cardpool and then appending it to the respective hand
def dealCard(cardPool, hand): 
    if cardPool:
        card = cardPool.pop(0)  # Draws a card from the card pool
        hand.append(card)       # Appends the drawn card to the player's hand
    else:
        print("No more cards left in the pool!")

#Function 4: Check for blackjack in any hand - Keeping it seperate to value check
def checkForBlackJack(hand): 
    if len(hand) == 2: 
        if ("A" in hand) and any(card in hand for card in [10,"J","Q","K"]): 
            return True
        else: 
            return False

#Function 5: Calculate the total value of the players hand 
def calculateHand(hand):
    value = 0
    aceCounter = 0

    for card in hand: 
        if card in ["J", "Q", "K"]: 
            value += 10 
        elif card == "A":
            aceCounter += 1 
            value += 11
        else: 
            value += card

    while value > 21 and aceCounter:
        value -= 10
        aceCounter -= 1

    return value



#GameLoop/GameStart
while playerBalance > 0: 

# PART1: Deciding the number of decks to play with: 
    #The below will take the input of deckNumber and fill up cardPool and then Shuffle the cards using the shared function
    while not (4 <= deckNumber <= 7):
        deckNumber = int(input("Please advise how many decks you want to play with (between 4 and 7): "))
        if not (4 <= deckNumber <= 7):
            print("We need a number between 4 and 7 Sir!")

    for _ in range(deckNumber):
        cardPool.extend(deck)
        shuffleCards(cardPool)

    print(cardPool)

#GAME - Part 2 - MAIN LOOP
#Create a bet and tie it to the game itself

    while not betMade:
        playerBet = int(input("Please confirm the amount you wish to bet with, Sir: "))
        
        if playerBet > playerBalance:
            print("Apologies sir, but you do not have enough funds to supplement your bet.")
        elif playerBet <= 0:
            print("Please enter a valid bet amount greater than 0.")
        else:
            #If the bet is Valid - The below will: 1. Update and print the balance, then deal the cards. 
            print("Thank you Sir, We will now begin dealing cards.")
            playerBalance = playerBalance - playerBet
            print(f"You have: {playerBet} on the table, and your remaining balance is {playerBalance}")
            gameInPlay = True
            betMade = True

#Deal cards + Checking for Blackjack: 

    if gameInPlay: 

        dealCard(cardPool, friendHand)
        dealCard(cardPool, playerHand)
        dealCard(cardPool, dealerHand)

        dealCard(cardPool, friendHand)
        dealCard(cardPool, playerHand)
        dealCard(cardPool, dealerHand)

        print(f"Player cards are:{playerHand}, player total:", calculateHand(playerHand))
        print(f"Dealer cards are: *,{dealerHand[0]}",)
        print(f"Friends cards are:{friendHand} friend total: ", calculateHand(playerHand))

    #Checking for blackjack before player is given options 
        if checkForBlackJack(playerHand): 
            playerBalance += playerBet * 2.5
            playerBet = 0
            print("Player has hit BlackJack!")
            gameInPlay = False

        elif checkForBlackJack(playerHand) and checkForBlackJack(dealerHand):
            playerBalance += playerBet
            playerBet = 0
            print("Push!")
            gameInPlay = False

        elif checkForBlackJack(playerHand) and checkForBlackJack(friendHand): 
            playerBalance += playerBet * 2.5
            playerBet = 0
            friendBet = 0       #keep this simple until the actual game loop is setup properly for the player
            print("Player, and friend have hit BlackJack, well done guys!")
            gameInPlay = False

        elif checkForBlackJack(friendHand):
            print("Your friend has hit BlackJack - give them a tap on the back!")

        else: 
            print("No BlackJacks, game moves forward") 
        
        

    #Ask for a choice 

    while gameInPlay: 
        action = input("Please Advise: Hit, Double, Stand? ").lower()

        match action: 
            case "hit": 
                dealCard(cardPool, playerHand)
                print(f"Your cards: {playerHand}")

                if calculateHand(playerHand) > 21: 
                    print("Bust! You exceeded 21.")
                    betMade = 0
                    gameInPlay = False

            case "double": 
                if playerBet <= playerBalance: 
                    playerBalance -= playerBet
                    playerBet *= 2

                    print(f"Your total bet is now {playerBet}, and your remaining balance is {playerBalance}")
                    dealCard(cardPool, playerHand)
                    print(f"Your cards: {playerHand}")
                    
                    if calculateHand(playerHand) > 21: 
                        print("Bust! You exceeded 21.")
                        betMade = 0
                        gameInPlay = False
                    else:
                        # End player's turn after doubling down
                        gameInPlay = False  # Player can't take any more actions after doubling

                else: 
                    print("Sorry Sir, you do not have enough funds. Please make another choice.")

            case "stand":
                print("You chose to stand. Dealer's turn now.")
                gameInPlay = False  # End player's turn

            case _:
                print("Invalid choice. Please choose Hit, Double, or Stand.")

    #Dealers turn after player choices have been made: 
    if calculateHand(playerHand) <= 21 and not gameInPlay: 
        print(f"Dealers cards are: {dealerHand}")

        while calculateHand(dealerHand) < 17: 
            dealCard(cardPool, dealerHand)
            print(f"Dealers cards are now showing: {dealerHand}")


        playerTotal = calculateHand(playerHand)
        dealerTotal = calculateHand(dealerHand)

        if dealerTotal > 21: 
            print(f"Dealer Busts on a {dealerTotal}")
            playerBalance += playerBet * 2
            playerBet = 0
            print(f"your balance is now {playerBalance}")
            

        elif playerTotal > dealerTotal: 
            print(f"Player's {playerTotal} beats Dealer's {dealerTotal}, congratulations")
            playerBalance += playerBet * 2
            playerBet = 0
            print(f"your balance is now {playerBalance}")
            

        elif playerTotal < dealerTotal:
            print(f"Dealer's {dealerTotal} beats Player's {playerTotal}, Sorry!")
            playerBet = 0
            print(f"your balance is now {playerBalance}")
            
        else:
            print(f"It's a push!")
            playerBalance += playerBet
            print(f"your balance is now {playerBalance}")

    print(f"Player balance is now {playerBalance}")
    returnAllCards(cardPool)
    betMade = False


#End game - create a clear playerBet and reroute to player balance based on weather they lost or won 


#Note: Friend is dealt first - then player, then Dealer at the end - Need to build in a hide dealer's first card function - maybe another variable to store is as a *? - Could easily just have it * at the beggining 
#then randomly pick a card - but that doesn't emulate a real world scenarion 
