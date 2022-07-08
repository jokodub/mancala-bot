print("Mancala Bot \n")

# Player 2 (Opp)    \/  12 11 10 9  8  7
#                   13                    6
# Player 1 (You)        0  1  2  3  4  5  /\

Lane1 = input("Input your lane, top to bottom or left to right (eg. 4 4 1 2 3 0)\n >").split()
Pot1 = input("How many in your pot?\n >")
Lane2 = input("Input opponent's lane, top to bottom or left to right\n >").split()
Pot2 = input("How many in opponent's pot?\n >")

board = [Lane1[0], Lane1[1], Lane1[2], Lane1[3], Lane1[4], Lane1[5], Pot1, Lane2[5], Lane2[4], Lane2[3], Lane2[2], Lane2[1], Lane2[0], Pot2]  # 14 spaces on board, [6] and [13] are Player 1 and 2's pots respectively
board = [int(x) for x in board] # Make everything integers so its easier to deal with

#Print board to console
print("\n  ", board[12], board[11], board[10], board[9], board[8], board[7],"\n", board[13], "           ", board[6], "\n  ", board[0], board[1], board[2], board[3], board[4], board[5])