# File: wk01_prove_tic_tac_toe.py
# Author: Kwazeme Ogubie
# Purpose: Introduction: Ponder and Prove


def main():
  # Initialise the checkerboard positions for input.
  a = ""
  b = ""
  c = ""
  d = ""
  e = ""
  f = ""
  g = ""
  h = ""
  i = ""
  
  # Check for stalemate
  game_counter = 0
  
  # store positions captured by each player in a list.
  positions_x = ["a","b","c","d","e","f","g","h","i"]
  positions_o = ["a","b","c","d","e","f","g","h","i"]

  # New Checkerboard with positions of both players.
  nb = [1,2,3,4,5,6,7,8,9]

  # Print checkerboard on screen.
  print(checkerboard(a=1,b=2,c=3,d=4,e=5,f=6,g=7,h=8,i=9))

  # First Player captures postions
  player_x = int(input("x's turn to choose a square (1-9): "))
  try:
    while player_x < 10 and player_x > 0:
      player_x = int(input("x's turn to choose a square (1-9): "))
      if player_x == 1 and a == "":
        a = "x"
        positions_x[player_x-1] = a
        nb[player_x-1] = a
        print(checkerboard(nb[0],nb[1],nb[2],nb[3],nb[4],nb[5],nb[6],nb[7],nb[8]))
        if check_win(nb) == "x" or check_win(nb) == "o": # Check winning position
          print(f"\nPlayer_{check_win(nb)} has won the game")
          print("Congratulations\n")
          break
        game_counter += 1
        if game_counter == 9:
          print("Wow, So close, It appears there has been a stalemate or draw")
          break
      elif player_x == 2 and b == "":
        b = "x"
        positions_x[player_x-1] = b
        nb[player_x-1] = b
        print(checkerboard(nb[0],nb[1],nb[2],nb[3],nb[4],nb[5],nb[6],nb[7],nb[8]))
        if check_win(nb) == "x" or check_win(nb) == "o": # Check winning position
          print(f"\nPlayer_{check_win(nb)} has won the game")
          print("Congratulations\n")
          break
        game_counter += 1
        if game_counter == 9:
          print("Wow, So close, It appears there has been a stalemate or draw")
          break
      elif player_x == 3 and c == "":
        c = "x"
        positions_x[player_x-1] = c
        nb[player_x-1] = c
        print(checkerboard(nb[0],nb[1],nb[2],nb[3],nb[4],nb[5],nb[6],nb[7],nb[8]))
        if check_win(nb) == "x" or check_win(nb) == "o": # Check winning position
          print(f"\nPlayer_{check_win(nb)} has won the game")
          print("Congratulations\n")
          break
        game_counter += 1
        if game_counter == 9:
          print("Wow, So close, It appears there has been a stalemate or draw")
          break
      elif player_x == 4 and d == "":
        d = "x"
        positions_x[player_x-1] = d
        nb[player_x-1] = d
        print(checkerboard(nb[0],nb[1],nb[2],nb[3],nb[4],nb[5],nb[6],nb[7],nb[8]))
        if check_win(nb) == "x" or check_win(nb) == "o": # Check winning position
          print(f"\nPlayer_{check_win(nb)} has won the game")
          print("Congratulations\n")
          break  
        game_counter += 1
        if game_counter == 9:
          print("Wow, So close, It appears there has been a stalemate or draw")
          break
      elif player_x == 5 and e == "":
        e = "x"
        positions_x[player_x-1] = e
        nb[player_x-1] = e
        print(checkerboard(nb[0],nb[1],nb[2],nb[3],nb[4],nb[5],nb[6],nb[7],nb[8]))
        if check_win(nb) == "x" or check_win(nb) == "o": # Check winning position
          print(f"\nPlayer_{check_win(nb)} has won the game")
          print("Congratulations\n")
          break
        game_counter += 1
        if game_counter == 9:
          print("Wow, So close, It appears there has been a stalemate or draw")
          break
      elif player_x == 6 and f == "":
        f = "x"
        positions_x[player_x-1] = f
        nb[player_x-1] = f
        print(checkerboard(nb[0],nb[1],nb[2],nb[3],nb[4],nb[5],nb[6],nb[7],nb[8]))
        if check_win(nb) == "x" or check_win(nb) == "o": # Check winning position
          print(f"\nPlayer_{check_win(nb)} has won the game")
          print("Congratulations\n")
          break
        game_counter += 1
        if game_counter == 9:
          print("Wow, So close, It appears there has been a stalemate or draw")
          break
      elif player_x == 7 and g == "":
        g = "x"
        positions_x[player_x-1] = g
        nb[player_x-1] = g
        print(checkerboard(nb[0],nb[1],nb[2],nb[3],nb[4],nb[5],nb[6],nb[7],nb[8]))
        if check_win(nb) == "x" or check_win(nb) == "o": # Check winning position
          print(f"\nPlayer_{check_win(nb)} has won the game")
          print("Congratulations\n")
          break
        game_counter += 1
        if game_counter == 9:
          print("Wow, So close, It appears there has been a stalemate or draw")
          break
      elif player_x == 8 and h == "":
        h = "x"
        positions_x[player_x-1] = h
        nb[player_x-1] = h
        print(checkerboard(nb[0],nb[1],nb[2],nb[3],nb[4],nb[5],nb[6],nb[7],nb[8]))
        if check_win(nb) == "x" or check_win(nb) == "o": # Check winning position
          print(f"\nPlayer_{check_win(nb)} has won the game")
          print("Congratulations\n")
          break
        game_counter += 1
        if game_counter == 9:
          print("Wow, So close, It appears there has been a stalemate or draw")
          break
      elif player_x == 9 and i == "":
        i = "x"
        positions_x[player_x-1] = i
        nb[player_x-1] = i
        print(checkerboard(nb[0],nb[1],nb[2],nb[3],nb[4],nb[5],nb[6],nb[7],nb[8]))
        if check_win(nb) == "x" or check_win(nb) == "o": # Check winning position
          print(f"\nPlayer_{check_win(nb)} has won the game")
          print("Congratulations\n")
          break
        game_counter += 1
        if game_counter == 9:
          print("Wow, So close, It appears there has been a stalemate or draw")
          break
      else:
        print("That position has been captured. Try another move.")
        continue 
      # 2nd Player cpatures Position
      player_o = int(input("o's turn to choose a square (1-9): "))
      if player_o == 1 and a == "":
        a = "o"
        positions_x[player_o-1] = a
        nb[player_o-1] = a
        print(checkerboard(nb[0],nb[1],nb[2],nb[3],nb[4],nb[5],nb[6],nb[7],nb[8]))
        if check_win(nb) == "x" or check_win(nb) == "o": # Check winning position
          print(f"\nPlayer_{check_win(nb)} has won the game")
          print("Congratulations\n")
          break
        game_counter += 1
        if game_counter == 9:
          print("Wow, So close, It appears there has been a stalemate or draw")
          break
      elif player_o == 2 and b == "":
        b = "o"
        positions_o[player_o-1] = b
        nb[player_o-1] = b
        print(checkerboard(nb[0],nb[1],nb[2],nb[3],nb[4],nb[5],nb[6],nb[7],nb[8]))
        if check_win(nb) == "x" or check_win(nb) == "o": # Check winning position
          print(f"\nPlayer_{check_win(nb)} has won the game")
          print("Congratulations\n")
          break
        game_counter += 1
        if game_counter == 9:
          print("Wow, So close, It appears there has been a stalemate or draw")
          break
      elif player_o == 3 and c == "":
        c = "o"
        positions_o[player_o-1] = c
        nb[player_o-1] = c
        print(checkerboard(nb[0],nb[1],nb[2],nb[3],nb[4],nb[5],nb[6],nb[7],nb[8]))
        if check_win(nb) == "x" or check_win(nb) == "o": # Check winning position
          print(f"\nPlayer_{check_win(nb)} has won the game")
          print("Congratulations\n")
          break
        game_counter += 1
        if game_counter == 9:
          print("Wow, So close, It appears there has been a stalemate or draw")
          break
      elif player_o == 4 and d == "":
        d = "o"
        positions_o[player_o-1] = d
        nb[player_o-1] = d
        print(checkerboard(nb[0],nb[1],nb[2],nb[3],nb[4],nb[5],nb[6],nb[7],nb[8]))
        if check_win(nb) == "x" or check_win(nb) == "o": # Check winning position
          print(f"\nPlayer_{check_win(nb)} has won the game")
          print("Congratulations\n")
          break
        game_counter += 1
        if game_counter == 9:
          print("Wow, So close, It appears there has been a stalemate or draw")
          break
      elif player_o == 5 and e == "":
        e = "o"
        positions_o[player_o-1] = e
        nb[player_o-1] = e
        print(checkerboard(nb[0],nb[1],nb[2],nb[3],nb[4],nb[5],nb[6],nb[7],nb[8]))
        if check_win(nb) == "x" or check_win(nb) == "o": # Check winning position
          print(f"\nPlayer_{check_win(nb)} has won the game")
          print("Congratulations\n")
          break
        game_counter += 1
        if game_counter == 9:
          print("Wow, So close, It appears there has been a stalemate or draw")
          break
      elif player_o == 6 and f == "":
        f = "o"
        positions_o[player_o-1] = f
        nb[player_o-1] = f
        print(checkerboard(nb[0],nb[1],nb[2],nb[3],nb[4],nb[5],nb[6],nb[7],nb[8]))
        if check_win(nb) == "x" or check_win(nb) == "o": # Check winning position
          print(f"\nPlayer_{check_win(nb)} has won the game")
          print("Congratulations\n")
          break
        game_counter += 1
        if game_counter == 9:
          print("Wow, So close, It appears there has been a stalemate or draw")
          break
      elif player_o == 7 and g == "":
        g = "o"
        positions_o[player_o-1] = g
        nb[player_o-1] = g
        print(checkerboard(nb[0],nb[1],nb[2],nb[3],nb[4],nb[5],nb[6],nb[7],nb[8]))
        if check_win(nb) == "x" or check_win(nb) == "o": # Check winning position
          print(f"\nPlayer_{check_win(nb)} has won the game")
          print("Congratulations\n")
          break
        game_counter += 1
        if game_counter == 9:
          print("Wow, So close, It appears there has been a stalemate or draw")
          break
      elif player_o == 8 and h == "":
        h = "o"
        positions_o[player_o-1] = h
        nb[player_o-1] = h
        print(checkerboard(nb[0],nb[1],nb[2],nb[3],nb[4],nb[5],nb[6],nb[7],nb[8]))
        if check_win(nb) == "x" or check_win(nb) == "o": # Check winning position
          print(f"\nPlayer_{check_win(nb)} has won the game")
          print("Congratulations\n")
          break
        game_counter += 1
        if game_counter == 9:
          print("Wow, So close, It appears there has been a stalemate or draw")
          break
      elif player_o == 9 and i == "":
        i = "o"
        positions_o[player_o-1] = i
        nb[player_o-1] = i
        print(checkerboard(nb[0],nb[1],nb[2],nb[3],nb[4],nb[5],nb[6],nb[7],nb[8]))
        if check_win(nb) == "x" or check_win(nb) == "o": # Check winning position
          print(f"\nPlayer_{check_win(nb)} has won the game")
          print("Congratulations\n")
          break
        game_counter += 1
        if game_counter == 9:
          print("Wow, So close, It appears there has been a stalemate or draw")
          break
      else:
        print("That position has been captured. Try another move.")
        continue  
  except:
      print("You must enter a number between 1 - 9:")
  
# check for a winner
def check_win(nb):
  # Check for x winner
  if nb[0] == "x" and nb[3] == "x" and nb[6] == "x":
    winner = "x"
  elif nb[1] == "x" and nb[4] == "x" and nb[7] == "x":
    winner = "x"
  elif nb[2] == "x" and nb[5] == "x" and nb[8] == "x":
    winner = "x"
  elif nb[2] == "x" and nb[4] == "x" and nb[6] == "x":
    winner = "x"
  elif nb[0] == "x" and nb[4] == "x" and nb[8] == "x":
    winner = "x"  
  elif nb[0] == "x" and nb[1] == "x" and nb[2] == "x":
    winner = "x"
  elif nb[3] == "x" and nb[4] == "x" and nb[5] == "x":
    winner = "x"
  elif nb[6] == "x" and nb[7] == "x" and nb[8] == "x":
    winner = "x" 

    # Check o winner
  elif nb[0] == "o" and nb[3] == "o" and nb[6] == "o":
    winner = "o"
  elif nb[1] == "o" and nb[4] == "o" and nb[7] == "o":
    winner = "o"
  elif nb[2] == "o" and nb[5] == "o" and nb[8] == "o":
    winner = "x"
  elif nb[2] == "o" and nb[4] == "o" and nb[6] == "o":
    winner = "o"
  elif nb[0] == "o" and nb[4] == "o" and nb[8] == "o":
    winner = "o"
  elif nb[0] == "o" and nb[1] == "o" and nb[2] == "o":
    winner = "x"
  elif nb[3] == "o" and nb[4] == "o" and nb[5] == "o":
    winner = "o"
  elif nb[6] == "o" and nb[7] == "o" and nb[8] == "o":
    winner = "o"
  else:
    winner = None
  return winner

# Create the checkerboard
def checkerboard(a,b,c,d,e,f,g,h,i):
    board = (f"{a} | {b} | {c} \n -+- -+- \n{d} | {e} | {f} \n -+- -+- \n{g} | {h} | {i} \n")
    return board



if __name__ == "__main__":
    main()
   