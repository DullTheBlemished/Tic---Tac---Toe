import time
import os
import random

# just a LOT of list and variables
board = {"a1": " ", "a2":" ", "a3":" ",
         "b1":" ", "b2":" ", "b3":" ",
         "c1":" ", "c2":" ", "c3":" "}

empty_squares = []

winning_pos = [
    ["a1", "a2", "a3"], ["b1", "b2", "b3"], ["c1", "c2", "c3"], 
    ["a1", "b1", "c1"], ["a2", "b2", "c2"], ["a3", "b3", "c3"], 
    ["a1", "b2", "c3"], ["a3", "b2", "c1"]]                     

scores = {"player": 0, "bot":0}

player_input = 0
bot_input = 0

# I decided to use def because it was better for the portfolio or smth
def check_win():
    for w in winning_pos:
        if board[w[0]] == board[w[1]] and board[w[1]] == board[w[2]] and board[w[0]] != " ":
            if board[w[0]] == "X":
                os.system("cls")
                print_score()
                print_board()
                time.sleep(1)
                os.system("cls")
                scores["player"] += 1
                print("Player wins")
                time.sleep(1)
                os.system("cls")
                reset_board()
                input("'Enter' to play again")
            else: 
                os.system("cls")
                print_score()
                print_board()
                time.sleep(1)
                os.system("cls")
                scores["bot"] += 1
                print("Bot wins (loosing to pure odds btw)")
                time.sleep(1)
                os.system("cls")
                reset_board()
                input("'Enter' to play again")

def reset_board():
    global empty_squares
    for square in board:
        board[square] = " "
    empty_squares = empty_squares2()

# oh btw i never claimed to be an artist so the ai actually had to draw the board for me   
def print_board():
    print(f"""{board["a1"]} | {board["a2"]} | {board["a3"]}
--+---+--
{board["b1"]} | {board["b2"]} | {board["b3"]}
--+---+--
{board["c1"]} | {board["c2"]} | {board["c3"]}""")
    
def empty_squares2():
    empty_squares3 = []
    for s in board:
        if board[s] == " " and s not in empty_squares3:
            empty_squares3.append(s)
    return(empty_squares3)

def print_score():
    print(f"Bot: {scores['bot']}  You: {scores['player']}")

def animation():
    animation = ["bot choosing.", "bot choosing..", "bot choosing..."]
    for a in animation:
        print(a)
        time.sleep(0.3)
        os.system("cls")

def check_draw():
    if len(empty_squares) == 0:
        os.system("cls")
        print_score()
        print_board()
        time.sleep(1)
        os.system("cls")
        print("Tie")
        time.sleep(1)
        os.system("cls")
        reset_board()
        input("'Enter' to play again")
        
def player_turn():
    global empty_squares
    while True:
        player_input = input("collums go a - c and rows goes 1 - 3, input you moves in an alpha-numerical graph format. e.g. top left corner is a1:").replace(" ", "").lower()
        if board[player_input] == " ":
            board[player_input] = "X"
            empty_squares = empty_squares2()
            break
        else:
            print("Invalid input you bum")
            time.sleep(0.5)
            continue
def bot_turn():
    global empty_squares
    if len(empty_squares) > 0:
        os.system("cls")
        animation()
        bot_input = random.choice(empty_squares)
        board[bot_input] = "O"
        empty_squares = empty_squares2()
    else:
        return
    
while True:
    # woah my code is definately so shorttttt
    print_score()
    print_board()
    
    player_turn()
    check_win()
    check_draw()

    bot_turn()
    check_win()
    check_draw()