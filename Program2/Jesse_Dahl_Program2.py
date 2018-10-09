# ---------------------------------------
# CSCI 127, Joy and Beauty of Data
# Program 2: Cribbage
# Jesse Dahl
# Last Modified: October 8, 2018
# ---------------------------------------
"""
This program reads in a list of card values and iterates through them, creating lists that contain sublists
with each "card in hand". The "evaluate_hand" and "print_hand" functions identifies each 'three of a kind',
'pair', 'sequence', and 'fifteen' within each set of cards and prints the total possible points each set earns.
"""
# ---------------------------------------

def evaluate_hand(list):
    numeric=[]
    total = [int(0)]

    #Creates a list containing only the card values of each hand
    for i in list:
        numeric.append(i[0])
    
    #Function that identifies if all the card values are the same within each hand and returns the total points
    def three_of_a_kind():
        if all(i==numeric[0] for i in numeric):
            total[0] += 6
        return(total)

    #Function that identifies if each hand contains two out of three identical card values and returns total
    def pair():
        seen = set() #The set() function creates an unordered collection of unique items with no duplicate items
        duplicated = [t for t in numeric if t in seen or seen.add(t)] #adds duplicated values to a list
        if (len(duplicated) == 1):
            total[0]+=2
        return(total)
    
    #Function that identifies if each hand contains three consecutive values (in any order)
    def sequence():
        seen = set(numeric)
        sortedList = []
        if len(seen)==3: #if the length of "seen" is equal to 3, there are no duplicated values in the hand
            for i in seen:
                sortedList.append(i) #If there are no duplicates in the hand, append the values to list "sortedList"
            sortedList.sort()#sorts the list in numeric order
            for i in range(len(sortedList)-1):
                if (sortedList[i]+1 == sortedList[i+1]): #Basically says to check if the value+1 is equal to the next value in the list
                    total[0]+=(3/2) #If the statement above is correct, add 1.5 points for each consecutive value (making a total of 3 points)
        return(total) 

    #Function that checks if any possible values within each hand adds to 15
    #*Very stupid way to do this. I could definitely figure out a better way but this will work for now
    def fifteen():
        fif = 15
        f = numeric[0]
        s = numeric[1]
        l = numeric[2]
        if(f+s==fif):
            total[0]+=2
        if(f+l==fif):
            total[0]+=2
        if(s+l==fif):
            total[0]+=2
        if(f+s+l==fif):
            total[0]+=2
        return(total)

    #Function calls
    three_of_a_kind()
    pair()
    sequence()
    fifteen()
    
    #Prints the total points for each hand
    print("Points scored: %.0f" %(total[0]))
    print()

#Function that just prints each hand's card value and suit
def print_hand(list):

    print("Cribbage Hand")
    print("-------------")
    print("Card 1: %s of %s" %(list[0][0],list[0][1].capitalize()))
    print("Card 2: %s of %s" %(list[1][0],list[1][1].capitalize()))
    print("Card 3: %s of %s" %(list[2][0],list[2][1].capitalize()))
    #print("Points scored: ")

# --------------------------------------
# Do not change anything below this line
# --------------------------------------

def process_hands(cribbage_input, cards_in_hand):    

    for hand in cribbage_input:
        hand = hand.split()
        hand_as_list = []
        for i in range(cards_in_hand):
            hand_as_list.append([int(hand[0]), hand[1]])
            hand = hand[2:]
        print_hand(hand_as_list)
        evaluate_hand(hand_as_list)
        
# --------------------------------------

def main():
    cribbage_file= open("cribbage.txt", "r")
    process_hands(cribbage_file, 3)
    cribbage_file.close()

# --------------------------------------

main()