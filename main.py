from guess_the_number import guess_the_number
from rock_paper_scissors import rock_papper_scissors
from wordle import Wordle
from connect4 import ConnectFour

# while True:
txt = """MINI GAMES!!!
    - Guess The Number (1)
    - Rocker, Paper Scissors (2)
    - Wordle (3)
    - ConnectFour (4)
    - Tic Tac Toe (5)
Select a game (pres a number or "q" to quit): """

while True:
    value = input(txt).lower()
    if value == ("1"):
        guess_the_number()
    elif value == ("2"):
        rock_papper_scissors()
    elif value == ("3"):
        game = Wordle()
        game.play()
    elif value == "q":
            print("Hope to play next time!")
            break
