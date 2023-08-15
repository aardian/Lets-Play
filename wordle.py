import random
from rich import print


class Wordle:

    def __init__(self):
        with open('words.txt', 'r') as f:
            word_list = f.readlines()

        self.word = random.choice(word_list).strip()
        #self.word = "messi"
        self.num_guesses = 0
        self.guess_dict = {
            0: [" "] * 5,
            1: [" "] * 5,
            2: [" "] * 5,
            3: [" "] * 5,
            4: [" "] * 5,
            5: [" "] * 5
        }

    def draw_board(self):
        for guess in self.guess_dict.values():
            print(' | '.join(guess))
            print('==================')

    def get_user_guess(self):
        user_guess = input("Enter 5 letter word: ")
        while len(user_guess) != 5:
            user_guess = input("Not valid, enter 5 letter word: ")

        user_guess = user_guess.lower()

        for idx, char in enumerate(user_guess):
            if char in self.word:
                if char == self.word[idx]:
                    char = f"[green]{char}[/]"
                else:
                    char = f"[yellow]{char}[/]"
            self.guess_dict[self.num_guesses][idx] = char

        self.num_guesses += 1
        return user_guess

    def play(self):
        while True:
            self.draw_board()
            user_guess = self.get_user_guess()

            if user_guess == self.word:
                self.draw_board()
                print(f"[bold green]You won, the word was '{self.word}'\n[/bold green]")
                break

            if self.num_guesses > 5:
                self.draw_board()
                print(f"[bold red]You lost, the word was '{self.word}'\n[/bold red]")
                break