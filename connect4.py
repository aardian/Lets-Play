from rich import print
from rich.prompt import IntPrompt


class ConnectFour:

    def __init__(self, height=6, width=7):
        self.height = height
        self.width = width
        self.board = [[' '] * width for row in range(height)]

    def draw_board(self):
        tokens = {' ': ' ', '0': '[blue]O[/]', '1': '[red]O[/]'}

        print('| ' + ' | '.join([str(i + 1) for i in range(self.width)]) + ' |\n\n')
        for row in self.board:
            row_to_draw = '| ' + ' | '.join([tokens[col] for col in row]) + ' |'
            print(row_to_draw)

    def get_column(self, index):
        return [row[index] for row in self.board]

    def get_row(self, index):
        return self.board[index]

    def get_diagonals(self):
        diagonals = []

        for i in range(self.height + self.width - 1):
            diag1, diag2 = [], []
            for j in range(max(i - self.height + 1, 0), min(i + 1, self.height)):
                diag1.append(self.board[self.height - i + j - 1][j])
                diag2.append(self.board[i - j][j])
            diagonals.append(diag1)
            diagonals.append(diag2)

        return diagonals

    def insert_token(self, team, col):
        if ' ' not in self.get_column(col):
            return False

        row = self.height - 1
        while self.board[row][col] != ' ':
            row -= 1
        self.board[row][col] = team
        return True

    def check_win(self):
        four_in_a_row = (['0', '0', '0', '0'], ['1', '1', '1', '1'])

        # Check rows
        for row in range(self.height):
            for col in range(self.width - 3):
                if self.get_row(row)[col:col + 4] in four_in_a_row:
                    return True

        # Check columns
        for col in range(self.width):
            for row in range(self.height - 3):
                if self.get_column(col)[row:row + 4] in four_in_a_row:
                    return True

        # Check diagonals
        for diag in self.get_diagonals():
            for idx, _ in enumerate(diag):
                if diag[idx:idx + 4] in four_in_a_row:
                    return True

        return False

    def play(self):
        team = '0'
        colors = {'0': '[blue]', '1': '[red]'}
        while True:
            self.draw_board()

            col = IntPrompt.ask(f"Team {colors[team]}{team}[/] choose column") - 1
            ok = self.insert_token(team, col)
            while not ok:
                print('column is full!')
                col = IntPrompt.ask(f"Team {colors[team]}{team}[/] choose column") - 1
                ok = self.insert_token(team, col)

            if self.check_win():
                self.draw_board()
                print(f"Team {colors[team]}{team}[/] wins!\n")
                break

            team = '1' if team == '0' else '0'

game = ConnectFour()
game.play()