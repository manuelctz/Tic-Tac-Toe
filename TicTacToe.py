###TIC TAC TOE ###
#Import numpy library
import numpy as np

class TicTacToe_Game():
  def __init__(self):
    self.size = 3
    self.playerX = "X"
    self.playerO = "O"
    self.player = self.playerX
    self.winner = ""
    self.board = []
    self.numbers = []
  
  def greeting3x3(self):
    #Displays a greeting message and board structure for 3x3#
    print("WELCOME TO TIC TAC TOE! \n")
    print("The board follows the next pattern: \n")
    print("        1 | 2 | 3 ")
    print("        4 | 5 | 6 ")
    print("        7 | 8 | 9 \n")

  def init_board(self,size):
    #Creates a list with a length to fill all the board#
    for i in range(self.size**2):
      self.board.append("-")
    #Creates a list with all possible board options in strings 
    for i in range(1,(self.size**2+1)):
      self.numbers.append(i)  
    self.numbers = [str(i) for i in self.numbers]
    
  def display_board(self):
    #Displays the board on the terminal#
    count = 1
    print('\n')
    #Print each board element until size of board is reached
    for i in range(len(self.board)):
      print("  %s  |" % (self.board[i]), end="")
      #Print a new line to start next row if board size is reached
      if count == self.size: 
        print("\n")
        count = 0 #Reset the count for next row
      count += 1
    print("\n")

  def take_turn(self,current_player):
    #Takes player's input and updates the board for a valid entry#
    print("It is " + current_player + "'s turn: ")
    
    while True:
      #Take input
      position = input("Please choose a number within board range: ")
      #Check if input is within board range
      if position in self.numbers:
        #Make input an integer and update it to board list's elements
        position = int(position)-1
        #Check if the position is an available spot
        if self.board[position] == '-':
          #Update board list with current player
          self.board[position] = current_player
          #Update board on screen
          self.display_board()
          break #Break out of the loop
        #Display on screen that spot is taken
        print("That spot is taken. Choose another spot!") 
      
  def num_of_players(self):
    #Determines number of players for the game#
    while True:
      num_players = input("Choose number of players (1 or 2): ")
      if num_players in ["1","2"]: #Only 1 or 2 players allowed
        break
      print("Only 1 or 2 players allowed! ")
    return num_players

  def computer_move(self):
    #Makes a random board choice of the available spots#
    #global board, player
    print("Computer's move is: ")
    #Loop until a random choice is made in an available board spot
    while True:
      random = np.random.randint(self.size**2)
      if self.board[random] == "-":
        #Assign the current player to the random spot selected
        self.board[random] = self.player
        #Update the board
        self.display_board()
        break #Break out of the loop
 
  def next_player(self):
    #Flips current player from X to O and vice versa#
    if self.player == self.playerX:
      self.player = self.playerO
    elif self.player == self.playerO:
      self.player = self.playerX

  def check_for_winner(self):
    #Checks for a winner in the game (works for any board size)#
    #Boolean variable to decide if game is over
    decision = True
    #Use numpy to create a numpy array for better access to elements
    np_board = np.array(self.board).reshape(self.size,self.size)     
    # Check all rows and columns for matching X or O
    for i in range(self.size):
      row_i =  np_board[i] #Loop through all the rows
      if len(set(row_i)) == 1 and row_i[0] != "-": #Check rows 
        decision = False 
        self.winner = row_i[0] #Select winner
        break
      col_i =  np_board[:,i] #Loop through all the columns
      if len(set(col_i)) == 1 and col_i[0] != "-": #Check columns
        decision = False
        self.winner = col_i[0] #Select winner
        break
    #Initialize empty lists for diagonals    
    diag_1 = []
    diag_2 = []  
    #Fill out diagonals with current board values
    for j in range(self.size):  
      diag_1.append(np_board[j][j]) #Fill out forward diagonal
      diag_2.append(np_board[j][self.size-j-1]) #Fill out backward diagonal
    #Check if forward diagonal elements are the same player
    if len(set(diag_1)) == 1 and diag_1[0] != "-":
        decision = False
        self.winner = diag_1[0] #Select winner
    #Check if backward diagonal elements are the same player    
    if len(set(diag_2)) == 1 and diag_2[0] != "-":
        decision = False 
        self.winner = diag_2[0] #Select winner    
    #Check if board is full
    if "-" not in self.board:
      decision = False
    return decision 

  def play_TicTacToe(self):
    #Plays the game#
    #Show greeting message
    self.greeting3x3()
    #Create the board list
    self.init_board(self.size)
    #Select number of players
    num_players = self.num_of_players() 
    #Show initial board
    self.display_board()
    #boolean variable to end game loop
    game_ongoing = True
    #While loop for playing the game
    while game_ongoing:
      #Take player's turn
      self.take_turn(self.player)
      #Check for winner in the game and end loop
      game_ongoing= self.check_for_winner()
      #For 1 player mode
      if num_players == "1" and game_ongoing == True:
        #Change player
        self.next_player()
        #Make computer's move
        self.computer_move()
        #Change player
        self.next_player()
        #Check for winner in the game and end loop
        game_ongoing = self.check_for_winner()
      #For 2 player mode  
      else:
        #Change player
        self.next_player()
    #Game over, print winner or tie in screen
    if self.winner == '':
      print("It is a tie!")
    else:
      print("The winner is ", self.winner,"!")

if __name__ == "__main__":
  game = TicTacToe_Game()
  game.play_TicTacToe()