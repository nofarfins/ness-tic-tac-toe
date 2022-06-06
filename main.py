import sys
from abc import ABCMeta, abstractmethod
import random
import time


class Board:
    """
    Holds players' picks in cells. Board size is NxN.
    """
    EMPTY_CELL = '_'

    def __init__(self, size=3):
        self.size = size
        self.board = [[self.EMPTY_CELL] * size for i in range(size)]

    def __str__(self):
        return "\n".join(' '.join(row) for row in self.board)

    def mark(self, row, col, mark):
        if row >= self.size:
            raise ValueError('Row out of bounds!')

        if col >= self.size:
            raise ValueError('Col out of bounds!')

        if self.board[row][col] == self.EMPTY_CELL:
            self.board[row][col] = mark
        else:
            raise ValueError("Cell not empty")
        if mark == self.board[0][0] and mark == self.board[0][1] and mark == self.board[0][2] \
                or mark == self.board[1][0] and mark == self.board[1][1] and mark == self.board[1][2] \
                or mark == self.board[2][0] and mark == self.board[2][1] and mark == self.board[2][2] \
                or mark == self.board[0][0] and mark == self.board[1][0] and mark == self.board[2][0] \
                or mark == self.board[0][1] and mark == self.board[1][1] and mark == self.board[2][1] \
                or mark == self.board[0][2] and mark == self.board[1][2] and mark == self.board[2][2] \
                or mark == self.board[0][2] and mark == self.board[1][1] and mark == self.board[2][0] \
                or mark == self.board[0][0] and mark == self.board[1][1] and mark == self.board[2][2]:
            sys.exit(f"{mark} win the game!")

    def check_drow(self):
        sys.exit("its drow")


class Player(metaclass=ABCMeta):
    def __init__(self, name, marker):
        self.name = name
        self.marker = marker

    @abstractmethod
    def play(self, board: Board):
        """
        Get desired location for next tick.
        """
        pass


class HumanPlayer(Player):
    def play(self, board: Board):
        while True:
            try:
                row = int(input('Please choose row between 0-2: '))
                col = int(input('Please choose col between 0-2:'))
            except ValueError:
                print("please choose number not sring")
            else:
                break

        return row, col


#Option 1 - You can't beat the computer!

class ComputerPlayer(Player):
    def play(self, board: Board):
        while True:
            if board.board[0][0] == board.EMPTY_CELL:
                row = 0
                col = 0
            else:
                if board.board[0][0] != board.EMPTY_CELL:
                    row = 0
                    col = 2
                    if board.board[1][0] == board.EMPTY_CELL:
                        row = 1
                        col = 0
                    if board.board[2][0] == board.EMPTY_CELL:
                        row = 2
                        col = 0
                    if board.board[0][0] != board.EMPTY_CELL and board.board[0][1] != board.EMPTY_CELL:
                        row = 0
                        col = 2
                    if board.board[1][2] != board.EMPTY_CELL and board.board[2][2] != board.EMPTY_CELL:
                        row = 0
                        col = 2
                    if board.board[0][1] != board.EMPTY_CELL and board.board[0][2] != board.EMPTY_CELL:
                        row = 0
                        col = 0
                    if board.board[0][0] != board.EMPTY_CELL and board.board[0][2] != board.EMPTY_CELL:
                        row = 0
                        col = 1
                    if board.board[1][0] != board.EMPTY_CELL and board.board[1][2] != board.EMPTY_CELL:
                        row = 1
                        col = 1
                    if board.board[1][0] != board.EMPTY_CELL and board.board[1][1] != board.EMPTY_CELL:
                        row = 1
                        col = 2
                    if board.board[1][1] != board.EMPTY_CELL and board.board[1][2] != board.EMPTY_CELL:
                        row = 1
                        col = 0
                    if board.board[2][0] != board.EMPTY_CELL and board.board[2][1] != board.EMPTY_CELL:
                        row = 2
                        col = 2
                    if board.board[2][0] != board.EMPTY_CELL and board.board[2][2] != board.EMPTY_CELL:
                        row = 2
                        col = 1
                    if board.board[2][1] != board.EMPTY_CELL and board.board[2][2] != board.EMPTY_CELL:
                        row = 2
                        col = 0
                    if board.board[0][0] != board.EMPTY_CELL and board.board[0][1] != board.EMPTY_CELL:
                        row = 0
                        col = 2

            if board.board[0][0] != board.EMPTY_CELL and board.board[0][1] != board.EMPTY_CELL and board.board[0][
                2] != board.EMPTY_CELL \
                    and board.board[1][0] != board.EMPTY_CELL and board.board[1][1] != board.EMPTY_CELL and \
                    board.board[1][2] != board.EMPTY_CELL \
                    and board.board[2][0] != board.EMPTY_CELL and board.board[2][1] != board.EMPTY_CELL and \
                    board.board[2][2] != board.EMPTY_CELL:
                Board.check_drow(board)

            return row, col


# Option 2 - Computer selects randomly

# class ComputerPlayer(Player):
#     def play(self, board: Board):
#         while True:
#             row = random.randint(0, 2)
#             col = random.randint(0, 2)
#
#             if board.board[row][col] == Board.EMPTY_CELL:
#                 return row, col

class Game:
    """
    Game loop.
    """

    @staticmethod
    def play_turn(board: Board, player: Player):
        row, col = player.play(board)
        try:
            board.mark(row, col, player.marker)
        except ValueError as e:
            print(str(e))


def main():
    board = Board(3)
    player1 = HumanPlayer('Nofar', 'X')
    player2 = ComputerPlayer('Computer', 'O')

    while True:
        # if player1 start the game we should print the board firstly
        # print(board)
        Game.play_turn(board, player2)
        print(board)
        Game.play_turn(board, player1)
        print(board)
        time.sleep(1)


if __name__ == '__main__':
    main()
