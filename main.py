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

        if mark == self.board[0][0] and mark == self.board[0][1] and mark== self.board[0][2]\
                or mark == self.board[1][0] and mark == self.board[0][2] and mark == self.board[1][2]\
                or mark== self.board[2][0] and mark == self.board[2][1] and mark== self.board[2][2]\
                or mark == self.board[0][0] and mark == self.board[1][0] and mark == self.board[2][0] \
                or mark == self.board[0][1] and mark == self.board[1][1] and mark == self.board[2][1] \
                or mark == self.board[0][2] and mark == self.board[1][2] and mark == self.board[2][2] \
                or mark == self.board[0][2] and mark == self.board[1][1] and mark == self.board[2][0] \
                or mark == self.board[0][0] and mark == self.board[1][1] and mark == self.board[2][2] :

                sys.exit(f"{mark} win the game!")

        if self.EMPTY_CELL  not in self.board:
            pass


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
            except ValueError :
                print("please choose number not sring")
            else:
                break

        return row, col


class ComputerPlayer(Player):
    def play(self, board: Board):
        while True:
            row = random.randint(0, 1)
            col = random.randint(0, 1)

            if board.board[row][col] == Board.EMPTY_CELL:
                return row, col


class Game:
    """
    Game loop.
    """
    @staticmethod
    def play_turn(board: Board, player: Player):
        while True:
            row, col = player.play(board)

            try:
                board.mark(row, col, player.marker)
            except ValueError as e:
                print(str(e))
            else:
                break


def main():
    board = Board(3)
    player1 = HumanPlayer('Nofar', 'X')
    player2 = ComputerPlayer('Computer', 'O')

    while True:

        print(board)
        Game.play_turn(board, player1)
        print(board)
        Game.play_turn(board, player2)
        time.sleep(1)


if __name__ == '__main__':
    main()
