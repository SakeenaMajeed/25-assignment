
import tkinter as tk
from tkinter import messagebox

# Function to handle button click
def button_click(row, col):
    global game_over  # Declare game_over as global
    if board[row][col] == " " and not game_over:
        board[row][col] = current_player
        buttons[row][col].config(text=current_player, state="disabled")
        if check_winner():
            messagebox.showinfo("Game Over", f"Player {current_player} wins!")
            game_over = True  # Set game_over to True when someone wins
        elif is_full():
            messagebox.showinfo("Game Over", "It's a tie!")
            game_over = True  # Set game_over to True when it's a tie
        else:
            switch_player()

# Function to switch players
def switch_player():
    global current_player  # Declare current_player as global
    current_player = "O" if current_player == "X" else "X"

# Function to check for a winner
def check_winner():
    # Check rows, columns, and diagonals
    for i in range(3):
        if board[i][0] == board[i][1] == board[i][2] != " ":
            return True
        if board[0][i] == board[1][i] == board[2][i] != " ":
            return True
    if board[0][0] == board[1][1] == board[2][2] != " ":
        return True
    if board[0][2] == board[1][1] == board[2][0] != " ":
        return True
    return False

# Function to check if the board is full
def is_full():
    return all(cell != " " for row in board for cell in row)

# Initialize the game
root = tk.Tk()
root.title("Tic-Tac-Toe")

# Game variables
board = [[" " for _ in range(3)] for _ in range(3)]
current_player = "X"
game_over = False  # Global variable to track if the game is over

# Create the buttons for the Tic-Tac-Toe grid
buttons = [[None for _ in range(3)] for _ in range(3)]
for i in range(3):
    for j in range(3):
        buttons[i][j] = tk.Button(root, text=" ", width=10, height=3, font=("Arial", 24), command=lambda i=i, j=j: button_click(i, j))
        buttons[i][j].grid(row=i, column=j)

# Run the game
root.mainloop()
