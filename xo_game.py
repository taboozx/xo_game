import random
from itertools import cycle


class TicTacToe:
    X = ''  # player 1 user/easy/medium
    O = ''  # player 2 user/easy/medium
    dead_loop = 0

    def menu(self) -> list:
        TicTacToe.dead_loop += 1
        if TicTacToe.dead_loop == 3:
            TicTacToe.dead_loop = 0
            return 'Bad parameters!'

        parameters = ['start', 'easy', 'medium', 'user', 'exit']
        command = input('Input command: ').split(' ')
        if command[0] == 'exit':
            exit()
        elif len(command) != 3:
            print('Bad parameters!')
            return self.menu()
        else:
            for c in command:
                if c not in parameters:
                    print('Bad parameters!')
                    command = self.menu()
                    break

            TicTacToe.dead_loop = 0
            return command

    @staticmethod
    def execute_command(command: list) -> tuple:
        if command[0] == 'start':
            print('log: start command')
            if command[1] == 'user':
                print('log: user plays as X')
                X = 'user'
                pass
            elif command[1] == 'easy':
                print('log: computer plays as X')
                X = 'easy'
                pass
            elif command[1] == 'medium':
                print('log: computer plays as X')
                X = 'medium'
            if command[2] == 'user':
                print('log: user plays as O')
                O = 'user'
                pass
            elif command[2] == 'easy':
                print('log: computer plays as O')
                O = 'easy'
                pass
            elif command[2] == 'medium':
                print('log: computer plays as O')
                O = 'medium'
        return X, O

    def create_field(self):
        self.field = [[], [], []]
        in1 = '_________'

        for i, cell in enumerate(list(in1)):
            if i < 3:
                self.field[0].append(cell)
            elif 2 < i < 6:
                self.field[1].append(cell)
            else:
                self.field[2].append(cell)

    def drow_field(self):
        print('---------')
        for i, cell in enumerate(self.field):
            cell = list(map(lambda s: s.replace('_', ' '), cell))
            print('|', ' '.join(cell), '|')
        print('---------')

    def check_input(self, coord, XO):
        X, O = XO
        print(f'log: X is {X} O is {O}')
        if self.field[coord[0] - 1][coord[1] - 1] != '_':
            print('This cell is occupied! Choose another one!')
            self.check_input(self.validator(self.turn_define(), XO), XO)
        else:
            self.field[coord[0] - 1][coord[1] - 1] = self.turn_define()
            return self.field

    def validator(self, turn, XO):
        X, O = XO
        while True:
            if turn == 'X':
                if X == 'user':
                    coord = input('Enter the coordinates:').split(' ')
                elif X == 'easy':
                    coord = self.computer_turn_easy().split(' ')
                elif X == 'medium':
                    coord = self.computer_turn_medium().split(' ')
            else:
                if O == 'user':
                    coord = input('Enter the coordinates:').split(' ')
                elif O == 'easy':
                    coord = self.computer_turn_easy().split(' ')
                elif O == 'medium':
                    coord = self.computer_turn_medium().split(' ')

            if coord[0] not in ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']:
                print('You should enter numbers!')
            elif len(coord) < 2:
                print('Coordinates should be two')
            elif coord[1] not in ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']:
                print('You should enter numbers!')
            else:
                coord = list(map(lambda el: int(el), coord))
                if coord[0] > 3 or coord[0] < 1:
                    print('Coordinates should be from 1 to 3!')
                elif coord[1] > 3 or coord[1] < 1:
                    print('Coordinates should be from 1 to 3!')
                else:
                    return coord

    def check_results(self):
        line1 = self.field[0][0] + self.field[0][1] + self.field[0][2]
        line2 = self.field[1][0] + self.field[1][1] + self.field[1][2]
        line3 = self.field[2][0] + self.field[2][1] + self.field[2][2]

        row1 = self.field[0][0] + self.field[1][0] + self.field[2][0]
        row2 = self.field[0][1] + self.field[1][1] + self.field[2][1]
        row3 = self.field[0][2] + self.field[1][2] + self.field[2][2]

        diagonale1 = self.field[0][0] + self.field[1][1] + self.field[2][2]
        diagonale2 = self.field[0][2] + self.field[1][1] + self.field[2][0]

        winner = ['XXX', 'OOO']

        for win in winner:
            if win == line1 or win == line2 or win == line3 \
                    or win == row1 or win == row2 or win == row3 \
                    or win == diagonale1 or win == diagonale2:
                print(f'{win[0]} wins')
                return False

        value_error_counter = 0
        for cell in self.field:
            try:
                cell.index('_')
            except ValueError:
                value_error_counter += 1

        if value_error_counter == 3:
            print('Draw')
            return False

        return True

    def ai_desigion(self):
        line1 = self.field[0][0] + self.field[0][1] + self.field[0][2]
        line2 = self.field[1][0] + self.field[1][1] + self.field[1][2]
        line3 = self.field[2][0] + self.field[2][1] + self.field[2][2]

        row1 = self.field[0][0] + self.field[1][0] + self.field[2][0]
        row2 = self.field[0][1] + self.field[1][1] + self.field[2][1]
        row3 = self.field[0][2] + self.field[1][2] + self.field[2][2]

        diagonale1 = self.field[0][0] + self.field[1][1] + self.field[2][2]
        diagonale2 = self.field[0][2] + self.field[1][1] + self.field[2][0]

        ai_desigion = ['XX_', 'X_X', '_XX', 'OO_', 'O_O', '_OO']

        field_lines = [line1, line2, line3, row1, row2, row3, diagonale1, diagonale2]

        for i, line in enumerate(field_lines):
            if line in ai_desigion:
                # print('Making move level "medium"')
                cell = line.index("_") + 1
                if i in (0, 1, 2):
                    return f'{i + 1} {cell}'
                elif i in (3, 4, 5):
                    return f'{cell} {i - 2}'
                elif i == 6:
                    if cell == 1:
                        return '1 1'
                    elif cell == 2:
                        return '2 2'
                    elif cell == 3:
                        return '3 3'
                elif i == 7:
                    if cell == 1:
                        return '1 3'
                    elif cell == 2:
                        return '2 2'
                    elif cell == 3:
                        return '3 1'
        else:
            print('ai didnt find descision')
            return self.computer_turn_easy()

    def turn_define(self):
        counter_o = 0
        counter_x = 0
        for line in self.field:
            for char in line:
                if char == 'O':
                    counter_o += 1
                elif char == 'X':
                    counter_x += 1
        if counter_x > counter_o:
            return 'O'
        if counter_x == counter_o:
            return 'X'
        else:
            return 'X'

    def computer_turn_easy(self):
        easy_move = (f'{random.randint(1, 3)} {random.randint(1, 3)}')
        print('Making move level "easy"')
        return easy_move

    def computer_turn_medium(self):
        '''If it already has two in a row and can win with one further move, it does so.'''
        return self.ai_desigion()

    def game(self):
        while True:
            XO = game.execute_command(game.menu())
            self.create_field()
            self.drow_field()

            for turn in cycle('XO'):
                self.ai_desigion()
                coord = self.validator(turn, XO)
                self.check_input(coord, XO)
                self.drow_field()
                if not self.check_results():
                    break


if __name__ == '__main__':
    TicTacToe().menu()
