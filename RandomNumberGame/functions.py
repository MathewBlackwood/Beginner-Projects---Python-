import random

#Star vs list Positioning =          [0]

                            #[2]            [3]
                    
  
                            #   [4]      [1]
#half star combinations i.e. (comets) - (To use for calculating point payouts)
    #(0, 1, 4), (3, 4, 2), (1, 2, 0), (4, 3, 0) (2, 1, 3)


#This function will generate a random emoji from a list "smileys" based on it's corresponding probability in the list of "smileysProbability"
def generateEmoji(): 

    smileys = ["😭", "😂", "🥲", "🧐", "🤠", "😍", "🤑"]
    smileysProbability = [4, 6, 10, 11, 10, 6, 3] #Double each valude to get its %chance of appearing - i.e. 11 = 22%

    return random.choices(smileys, smileysProbability, k=5)


#Check for a comet (See description above)
def checkForComets(star): 
    cometPatterns = [
        (0, 1, 4),
        (3, 4, 2),
        (1, 2, 0),
        (4, 3, 0),
        (2, 1, 3)
    ]
    count = 0
    for a, b, c in cometPatterns:
        if star[a] == star[b] == star[c]:
            count += 1
    return count



#Check for a full completed star
def checkForStar(star):
    if all(emoji == star[0] for emoji in star):
        return True
    return False


#Basic point distrubtion (NEEDS TO BE ADJUSTED - based on the emoji probability - maybe us a Match-Case to filter - Personal Reminder: Emoji's are strings)
def pointsDistribute(star, bet):
    if checkForStar(star):
        return bet * 5  
    
    comets = checkForComets(star)
    if comets > 0:
        return bet * 2 * comets
    
    else:
        return 0  # Loss

def main():
    return

if __name__ == '__main__':
    main()

    