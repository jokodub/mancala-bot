print("Mancala Bot \n")

# Player 2 (Opp)    \/  13 12 11 10 9  8
#                    0                    7
# Player 1 (You)        1  2  3  4  5  6  /\

while True:  # Loops if input is wrong
    Lane1 = input("Input your lane, top to bottom or left to right (eg. 4 4 1 2 3 0)\n >").split()
    Pot1 = input("How many in your pot?\n >")
    Lane2 = input("Input opponent's lane, top to bottom or left to right\n >").split()
    Pot2 = input("How many in opponent's pot?\n >")

    if len(Lane1) != 6 or len(Lane2) != 6 or not Pot1.isdigit() or not Pot2.isdigit():  # Check 1
        print("Oops, that isn't a valid board!")
        continue

    board = [Pot2, Lane1[0], Lane1[1], Lane1[2], Lane1[3], Lane1[4], Lane1[5], Pot1, Lane2[5], Lane2[4], Lane2[3], Lane2[2], Lane2[1], Lane2[0]]  # 14 spaces on board, [7] and [0] are Player 1 and 2's pots respectively
    board = [int(x) for x in board] # Make everything integers so its easier to deal with

    if sum(board) != 48 or not all(x >= 0 for x in board):  # Check 2
        print("Oops, that isn't a valid board!")
        continue
    else:
        # Passed all checks, exit loop
        break

#Print board to console
print("\n  ", board[13], board[12], board[11], board[10], board[9], board[8],"\n", board[0], "           ", board[7], "\n  ", board[1], board[2], board[3], board[4], board[5], board[6])

bonusmoves = []
results = []


def Test(inputmove, board, movelist, player):

    # inputmove         > The move we are testing
    # board             > A copy of the board to simulate
    # movelist          > A list of all previous moves, used to keep track of bonus moves
    # player            > Which player's turn it is

    # beans             > How many beans the player has in their hand as they move around the board
    # cursor            > Keeps track of where we are on the board

    if player == 2:
        inputmove += 7

    movelist.append(inputmove)

    # Puts all beans on the space into hand, removes from board
    beans = board[inputmove]
    board[inputmove] = 0
    if beans == 0:
        return(["Invalid move", movelist, player]) # Can't play an empty space

    cursor = inputmove + 1

    while beans > 0:
        # Skip over opponent's pot, checks if cursor has reached the end of the board and loops around
        if cursor == 14 and player == 1:
            cursor = 1
        if cursor == 14 and player == 2:
            cursor = 0
        if cursor == 7 and player == 2:
            cursor = 8

        board[cursor] += 1
        beans -= 1

        if beans == 0 and player == 1 and cursor in [1, 2, 3, 4, 5, 6] and board[cursor] == 1:   # If your turn ends in an empty space on your side, take all beans from opponent's space
            board[7] += board[14 - cursor] + 1
            board[14 - cursor] = 0
            board[cursor] = 0

        if beans == 0 and player == 2 and cursor in [8, 9, 10, 11, 12, 13] and board[cursor] == 1:
            board[0] += board[14 - cursor] + 1
            board[14 - cursor] = 0
            board[cursor] = 0

        if beans == 0 and cursor in [0, 7]:   # Landing in your pot gives you a bonus move
            bonusmoves.append([board, movelist, player])
            return(["Bonus time baby", movelist, player])

        cursor += 1


    if player == 1:
        return([board[7], movelist, player])
    else:
        return([board[0], movelist, player])



def TestBonusMoves():
    for bonusmove in bonusmoves:        # Runs through bonus moves and tests them, yes I know iterating over itself can be bad but it works
        for i in range(1, 7):
            results.append(Test(i, bonusmove[0].copy(), bonusmove[1].copy(), bonusmove[2]))


def Main():
    # Begins the testing
    for i in range(1, 7):
        results.append(Test(i, board.copy(), [], 1))
    TestBonusMoves()

    # Just so it prints nicely
    for result in results:
        print(result)
    sortedresults = [k for k in results if k[0] not in ["Invalid move", "Bonus time baby"]]
    sortedresults.sort(reverse=True)
    print(sortedresults)

Main()
