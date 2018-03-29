from copy import deepcopy
import random

class Board:
    def __init__(self, side=3):
        # here we assume square board. using side` to allow easy later expansion
        self.side = side
        # board is represented through list
        self.tiles = [' ' for _ in range(side * side)]
        self.legal_moves = [i for i in range(side * side)]

    def check_move(self, move):
        """
        Check if move is legal.

        :param move: number of cell
        """

        # check boundaries
        if not (0 <= move < self.side * self.side):
            return False

        # check if tile is empty
        if self.tiles[move] == ' ':
            return True
        else:
            return False

    def tiles_as_str(self):
        """Return cells of board, separated by comma."""
        return ','.join(self.tiles)  #short string representation. used for storage

    def __str__(self):
        # Good string representation of board. Show this to player.
        result = ''
        for row in range(self.side):
            line = '|'.join([' ' + self.tiles[row * self.side + col] + ' ' for col in range(self.side)])
            result += line + '\n'

            # don't print at the bottom
            if row != self.side - 1:
                line = '+'.join(['---' for _ in range(self.side)])
                result += line + '\n'

        return result

    def check_winner(self):
        """
        Return 'x' if x won, 'o' if o won, 't' if tie, 'c' if game isn't ended yet.
        :return: string
        """

        side = self.side  # shortcut

        # we check with built-in `set`
        # if there is only one unique element in a row, column or diagonal -- it's a win

        # first check rows
        for i in range(side):
            if len(set(self.tiles[i * side:i * side + side])) == 1:
                if self.tiles[i * side] != ' ':  # it mustn't be just empty line
                    return self.tiles[i * side]  # this will retunr the symbol of winner

        # now check columns
        for i in range(side):
            if len(set(self.tiles[i::side])) == 1:
                if self.tiles[i] != ' ':
                    return self.tiles[i]

        # diagonals
        if len(set([self.tiles[i * side + i] for i in range(side)])) == 1:
            if self.tiles[0] != ' ':
                return self.tiles[0]
        if len(set([self.tiles[i * side + side - i - 1] for i in range(side)])) == 1:
            if self.tiles[side - 1] != ' ':
                return self.tiles[side - 1]

        # if we got here, it means no one scored a win
        # if there is at least one empty space
        if ' ' in self.tiles:
            return 'c'

        # the only possible option now
        return 't'

class Game:
    BAD_MOVES_FILENAME = 'bad_moves.txt'

    def __init__(self):
        self.board = Board()
        self.rollback_board = None
        self.bad_moves = self.read_bad_moves()
        self.current_player = 'x'

    def play(self):
        while self.make_move():
            pass

    def read_bad_moves(self):
        bad_moves = []
        try:
            # read and store bad positions
            with open(self.BAD_MOVES_FILENAME) as f:
                for line in f:
                    # last symbol is `\n`
                    bad_moves.append(line[:-1])
        except FileNotFoundError:
            # if starting game fresh in new directory to not die with exception
            with open(self.BAD_MOVES_FILENAME, 'w+') as _:
                pass

        return bad_moves

    def make_computer_move(self):
        """Make move for computer. Method changes state of object."""

        def loosing_move(move_):
            # make a move and see if it leads to bad position
            # it's not a problem to change board, since here we will revert change if move happen to be bad
            self.board.tiles[move_] = 'x'
            for board in self.bad_moves:
                if board == self.board.tiles_as_str():
                    return True
            # all checks passed, move is good or not yet bad
            return False

        self.rollback_board = deepcopy(self.board)

        # choose random legal non-loosing move
        move = random.choice(self.board.legal_moves)
        # cycle should always end, since game can always be tied
        while loosing_move(move):  # if move is good, it won't be reverted
            # this part is here, if you want to see how effective pseudo-AI is (or for debug)
            # on 50 stored positions it is still pretty weak
            # print('\n--------------------------------\nCaught bad move\n')
            # print(self.board)
            # print('----------------------------------\n')

            move = random.choice(self.board.legal_moves)
            # rollback from a bad move
            self.board = deepcopy(self.rollback_board)

        # not a legal move anymore
        self.board.legal_moves.remove(move)

    def make_player_move(self):
        """Make a move for player. Method changes state of object."""

        # this will be used to improve pseudo-AI
        self.rollback_board = deepcopy(self.board)
        while True:
            # we don't want errors with bad input
            try:
                print(self.board)
                # `-1` to cast from normal human numbering to python 0-base
                move = int(input("Enter a move(1-{}): ".format(self.board.side ** 2))) - 1
                # neither do we want illegal moves
                if not self.board.check_move(move):
                    print("Move is illegal. Try again.\n")
                else:
                    break
            except ValueError:
                print("Unrecognized input. Must be integer.\n")

        self.board.tiles[move] = 'o'
        # don't forget to disallow this move for computer
        self.board.legal_moves.remove(move)
        print(self.board)

    def make_move(self):
        """Make move and change active player."""
        # make move and return True if game is still playable
        # return False if game ended
        if self.current_player == 'x':
            self.make_computer_move()
            self.current_player = 'o'
        elif self.current_player == 'o':
            # technically this check is not needed (`else` is enough), but just for clarity
            self.make_player_move()
            self.current_player = 'x'

        result = self.board.check_winner()
        if result == 'x':
            self.game_end_player_lost()
        elif result == 'o':
            self.game_end_player_won()
        elif result == 't':
            self.game_end_tie()
        elif result == 'c':
            return True

        return False

    def game_end_player_lost(self):
        print(self.board)
        print("You lost, Player.\n")

    def game_end_player_won(self):
        print("You won.\n")
        # have to save position that led to lose
        with open(self.BAD_MOVES_FILENAME, 'a') as f:
            f.write(self.rollback_board.tiles_as_str() + '\n')

    def game_end_tie(self):
        print(self.board)
        print("You got a tie (in a game, not cloth tie to suit).")

def play_game():
    # Reset board and play again
    print("Game started.")
    game = Game()
    game.play()

def main():
    play_game()
    while True:
        choice = input("Wanna play again? y/n: ")
        if choice == 'n':
            print("Good bye, Player.")
            break
        elif choice == 'y':
            play_game()
        else:
            print("Didn't understand. ")


if __name__ == '__main__':
    main()
