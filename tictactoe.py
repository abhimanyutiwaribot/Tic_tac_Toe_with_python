import itertools
from colorama import Back, Fore, Style, just_fix_windows_console, init
just_fix_windows_console()
init()
def win(current_game):
    def same(l):
        if l.count(l[0])== len(l) and l[0]!=0:
            return True
        else:
            return False
        
    #horizontally
    for row in game:
        if same(row):
            print(f"Player {row[0]} is the winner horizontally")
            return True

    #vertically
    for col in range(len(game)):
        check=[]
        for row in game:
            check.append(row[col])
        if same(check):
            print(f"Player {check[0]} is the winner vertically")
            return True

    #up to down diagonally
    diags=[]
    for ix in range(len(game)):
        diags.append(game[ix][ix])
    if same(diags):
        print(f"Player {diags[0]} is the winner diagonally")
        return True

    #down to up diagonally
    diags=[]
    for col, row in enumerate(reversed(range(len(game)))):
        diags.append(game[row][col])
    if same(diags):
        print(f"Player {diags[0]} is the winner diagonally")
        return True
    
    return False
    

def game_board_change(game_map,row=0, column=0, played=0, just_display=False):
    try:
        if game_map[row][column] != 0:
            print("The Position is occupied! Choose another!")
            return game_map, False
        s = "   "+"  ".join([str(i) for i in range(game_size)])
        print(s)
        if not just_display:
            game[row][column]=played
        for count, row in enumerate(game_map):
            colored_row=""
            for item in row:
                if item == 0:
                    colored_row += "   "
                elif item == 1:
                    colored_row += Back.MAGENTA + ' X ' + Style.RESET_ALL
                elif item == 2:
                    colored_row += Back.CYAN + ' O ' + Style.RESET_ALL
            print(count,colored_row)
        return game_map, True
    
    except IndexError as e:
        print("Error: make sure you input row/column as 0 1 or 2?",e)
        return game_map, False
    except Exception as e:
        print("Something went very wrong!",e)
        return game_map, False

play = True
players = [1,2]

while play:
    game_size= int(input("What size of TIC TAC TOE you want to play? : "))
    if game_size != 1:
        
        game=[[0 for i in range(game_size)]for i in range(game_size)]
        game, _ =game_board_change(game, just_display=True)
        game_won = False
        player_choice = itertools.cycle([1, 2])

        while not game_won:
            current_player = next(player_choice)
            print(f"Current Player:{current_player}")
            player=False

            while not player:
                row_choice=int(input("What row do you want to play? (0, 1, 2): "))
                column_choice=int(input("What column do you want to play? (0, 1, 2): "))
                game, player=game_board_change(game,row_choice,column_choice,current_player)

            if win(game):
                game_won = True
                play_again=input("DO YOU Want to play again? (y/ n): ")
                if play_again.lower() == "y":
                    print("Restarting!")
                elif play_again.lower() == "n":
                    print("THANKYOU FOR PLAYING !")
                    play = False
                else:
                    print("Not a valid answer , so see you later !!")
                    play = False
    else:
        print("I CAN FEEL U BROSKI , I KNOW YOU ARE ALONE  ")
        game_size = False