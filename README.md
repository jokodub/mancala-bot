# mancalabot
This is a dump for all my mancala bot code

It's meant to look at all possible moves and return the best one. Right now it can only play greedy (depth = 0).

The rules of mancala (at least the version I play):
1. Each player has a pot on one side of the board.
2. Players take turns choosing a pile from one of the holes. Moving counter-clockwise, beans from the selected pile are deposited in each of the following hole until you run out of beans.
3. If you drop your last bean into your pot, you get a free turn.
4. If you drop the last bean into an empty hole on your side of the board, you can capture beans from the hole on the opposite side.
5. The game ends when all six holes on either side of the board are empty. If a player has any beans on their side of the board when the game ends, he will capture all of those beans.
