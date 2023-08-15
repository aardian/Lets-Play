import random
from rich import print

def play_again():
    play_again = input("Do you want to play again? (Y/N): ")
    if play_again.lower() == "y":
        rock_papper_scissors()
    else:
        print("[bold red]== BYE BYE !! Don't get mad :) ==[/bold red]")

def rock_papper_scissors():
    print("Let's play Rock Paper Scissors\n")

    r = "rock"
    p = "paper"
    s = "scissor"
    all_choices = [r, p, s]

    user = input(f"Enter a choice ({r}, {p}, {s}): ").lower()

    if user not in all_choices:
        print("[bold red]You enetered wrong choice\n")
        return rock_papper_scissors()

    computer = random.choice(all_choices)


    print(f"User chosed {user} and computer chosed {computer}")

    if user == computer:
        print(f"[bold white]== Both players selected {user}. It's a tie! ==[/bold white]\n")
        play_again()
    elif user == r:
        if computer == s:
            print("== Rock smashes scissors! [bold green]You won![/bold green] ==\n")
        else:
            print("== Paper covers rock! [bold red]You lose[/bold red]. ==\n")
            play_again()
    elif user == p:
        if computer == r:
            print("== Paper covers rock! [bold green]You won![/bold green] ==\n")
        else:
            print("== Scissors cuts paper! [bold red]You lose[/bold red]. ==\n")
            play_again()
    elif user == s:
        if computer == p:
            print("== Scissors cuts paper! [bold green]You won![/bold green] ==\n")
        else:
            print("== Rock smashes scissors! [bold red]You lose[/bold red]. ==\n")
            play_again()
    else:
        play_again()

