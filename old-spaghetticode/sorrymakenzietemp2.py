print("Mancala AI (sorry makenzie)")

    # THEM (Blane)  13  12  11  10  9   8
    #             0                        7
    # YOU  (Alane)  1   2   3   4   5   6
board = [0,0,0,0,0,0,0,0,0,0,0,0,0,0] # 14 items, 7 and 0 are pots A and B respectively

movelist = []
results = []
extramoves = []

strategy = int(input("\nWhich strategy?\n1 for Greedy\n2 for Smart\n >"))

if strategy == 2:
    depth = int(input("\nDepth (How many opponent moves)\n >"))

# Alane is YOUR lane
# Blane is THEIR lane
Alane = str.split(input("\nYour lane (top to bottom)\n >"))
Blane = str.split(input("\nOpponent's lane (top to bottom)\n >"))

# Sets board[7] and board[0] to each player's pots, Apot and Bpot respectively
Apot = input("\nYour pot\n >")
Bpot = input("\nOpponent's pot\n >")
board[7] = Apot
board[0] = Bpot


# Print boardstate to console
print("\nCurrent board: \n    ", end='')
i = 13
for x in Blane:
    board[i] += int(x)
    print(board[i], end=' ')
    i -= 1
print("\n", Bpot, "           ", Apot,"\n    ", end='')
i = 1
for x in Alane:
    board[i] += int(x)
    print(board[i], end=' ')
    i += 1



def Testmove(move, tempboard, tempmovelist, mylane):
    ## variable list
    # Anything with "temp" is a copy made of a variable to test with
    # tempboard - copy of the input board, reset every time Testmove is called
    # tempmovelist - list that contains every move taken in one loop, keeps track of extra moves
    # beansleft - how many beans left in your hand, set from amount in the space chosen at start of loop
    # move - the space being tested
    # currentspace - the cursor that goes around the board to drop beans
    # result - output of Testmove, gives the resulting score of any tested space and the moves that led to it
    # extramoves - a list made by Testmoves to tell Testextramoves what needs to be put through the loop again for bonus moves

    tempmovelist.append(move)

    # Set beansleft, takes beans out of the space
    beansleft = int(tempboard[move])
    tempboard[move] = 0

    # Checks for illegal move (trying to play an empty space)
    if beansleft == 0:
        result = "Invalid", tempmovelist, mylane
        return(result)

    # Sets currentspace to the space that comes after the one being tested (first one to have a bean added)
    currentspace = int(move) + 1
    if currentspace == 14:
        currentspace = 0

    # Places a bean in each space until there are none left
    # Uses currentspace to keep track of where it is
    while beansleft != 0:

        if mylane == True:
            # Capture rules: If you land in an empty space in your lane (Alane), then take all beans in the other lane's space
            # Checks if currentspace is in your lane
            if beansleft == 1 and tempboard[currentspace] == 0 and currentspace not in [0,7,8,9,10,11,12,13]:
                tempboard[7] = int(tempboard[7]) + int(tempboard[14 - currentspace])
                tempboard[14 - currentspace] = 0

        if mylane == False:
            # Capture rules: If they land in an empty space in their lane (Blane), then take all beans in the your lane's space
            # Checks if currentspace is in their lane
            if beansleft == 1 and tempboard[currentspace] == 0 and currentspace not in [0,1,2,3,4,5,6,7]:
                tempboard[0] = int(tempboard[0]) + int(tempboard[14 - currentspace])
                tempboard[14 - currentspace] = 0


        # Put a bean in the next space
        tempboard[currentspace] = int(tempboard[currentspace]) + 1

        # Extra move rules: Your final bean lands in your pot (Apot), you may go again
        if beansleft == 1 and currentspace in [0,7]:
            extramoves.append([tempmovelist, tempboard, mylane])

            result = "See extra moves", tempmovelist, mylane
            return(result)


        beansleft -= 1

        # Move to the next space, loops around if hits other pot or end
        currentspace += 1

        if mylane == False and currentspace == 7:
            currentspace = 8

        if mylane == False and currentspace == 14:
            currentspace = 0

        if mylane == True and currentspace == 14:
            currentspace = 1

    # Calculate new pot scores after move
    tempBpot = tempboard[0]
    tempApot = tempboard[7]

    # Returns test results (format: new score, move)
    result = str((int(tempApot)-int(tempBpot))), tempmovelist, mylane
    return(result)




# Check each item in list extramoves (format: move list, boardstate)
def Testextramoves():

    # For every note made in list extramoves by Testmove(), run 6 tests for each space
    for note in extramoves:

        for move in range(1, 7):
            if note[2] == False:
                move += 7
            #Tests spaces 1-6 on a copy of the board any extra move makes (also sends a list of all previous moves to keep track of what exactly is being tested)
            results.append(Testmove(move, note[1].copy(), note[0].copy(), note[2]))

##HEY FUTURE JOHN
#ok so heres what you need to do
#add the boardstate to each result so that smartmove can make the next move
#find a way to not break everything in the process :)
#test (0 2 0 2 0 0) (0 1 0 0 3 0)


# Greedy takes the option with the highest score increase, doesn't care about future moves
def PlayGreedy():
    print("\nTesting with Greedy...")

    index = 1
    for each in Alane:
        results.append(Testmove(index, board.copy(), movelist.copy(), True))
        index += 1

    Testextramoves()

    # Removes all the invalid and extra move messages
    # Ripped this off of stackexchange not totally sure how it works (look up list comprehensions)
    inval = ['Invalid', 'See extra moves']
    finalresults = [k for k in results if k[0] not in inval]

    # Sorts numerically, no idea what lambda does
    finalresults.sort(key=lambda x: float(x[0]))

    # Prints the list to console
    for res in finalresults:
        print(res)

    # Print stats
    print("\n",len(finalresults), "possible moves")
                        #Finds difference between the new score and old score
    print("Best move gives +", int(finalresults[-1][0])-int(Apot)+int(Bpot), " score.",sep='')

    # Prints all moves that result in the same best score
    print("Best moves: ")
    p = 1
    while int(finalresults[-p][0]) == int(finalresults[-1][0]):
        print(finalresults[-p][1])
        p += 1

# Smart looks 1 move into the future (your move then opponent's move) for the most beneficial
# assume opponent will take the move that gives them the most points, take the move that will give you the most overall
def PlaySmart():
    print("\nTesting with Smart...")




# Only Greedy works right now, Smart wont test anything
if strategy == 1:
    PlayGreedy()
else:
    PlaySmart()
