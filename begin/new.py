

"""Roll a pair of dice.
Add the values of the roll.
Ask the user to guess a number.
Compare the user's guess to the total value.
Determine the winner (user or computer)."""

from random import randint
from time import sleep

def get_user_guess():
  guess = int(raw_input("Guess a number: "))
  return guess
def roll_dice(number_of_sides):
  first_roll = randint(1, number_of_sides)
  second_roll = randint(1, number_of_sides)
  max_val = number_of_sides * 2 
  print "The maximum possible value is: %d" % max_val
  guess = get_user_guess()
  if (guess > max_val):
    print "No guessing higher than the maximum possible value!"
    return
  else:
    print "Rolling..."
    sleep(2)
    print "The 1st roll is: %d" % first_roll
    sleep(1)
    print "The 2nd roll is: %d" % second_roll
    sleep(1)
    total_roll = first_roll + second_roll
    print "The total value is: %d" % total_roll
    print "Result..."
    sleep(1)
    if guess == total_roll:
      print "You won!"
    else:
      print "You lost, try again."

roll_dice(6)




## Guess a ship


from random import randint

board = []

for x in range(5):
  board.append(["O"] * 5)

def print_board(board):
  for row in board:
    print " ".join(row)

print_board(board)

def random_row(board):
  return randint(0, len(board) - 1)

def random_col(board):
  return randint(0, len(board[0]) - 1)

ship_row = random_row(board)
ship_col = random_col(board)
print ship_row
print ship_col

# Everything from here on should go in your for loop!
# Be sure to indent four spaces!
for turn in range(4):
  print "Turn", turn + 1
  guess_row = int(raw_input("Guess Row: "))
  guess_col = int(raw_input("Guess Col: "))

  if guess_row == ship_row and guess_col == ship_col:
    print "Congratulations! You sunk my battleship!"
    break
  else:
    if (guess_row < 0 or guess_row > 4) or (guess_col < 0 or guess_col > 4):
      print "Oops, that's not even in the ocean."
    elif(board[guess_row][guess_col] == "X"):
      print "You guessed that one already."
    else:
      print "You missed my battleship!"
      board[guess_row][guess_col] = "X"
      if turn == 3:
        print "Game Over"
    # Print (turn + 1) here!
    print_board(board)