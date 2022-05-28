"""
Objects:

Board: knows where every X and O are
Player: Knows how to tick X or O (based on empty cells which he reads from the board)
WinStrategy: Knows when a player wins based on a single strategy (for example: row sequence, col sequence, diagonal...)
Game: implements the game loop: player turns, looks for winner and tie and terminates game accordingly.

"""