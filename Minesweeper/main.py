

import random
import tkinter as tk
from tkinter import messagebox
import time

class Minesweeper:
    def __init__(self, size=5, bombs=3):
        self.size = size
        self.bombs = bombs
        self.board = [[' ' for _ in range(size)] for _ in range(size)]
        self.bomb_positions = set()
        self.revealed = set()
        self.flagged = set()
        self.start_time = None
        
        # Initializing Tkinter window
        self.root = tk.Tk()
        self.root.title("Minesweeper Game")
        
        self.buttons = {}
        self.timer_label = tk.Label(self.root, text="Time: 0", font=('Arial', 14))
        self.timer_label.grid(row=self.size, columnspan=self.size, pady=10)
        
        # Difficulty Selection Dropdown
        self.difficulty_var = tk.StringVar(self.root)
        self.difficulty_var.set("Easy")
        difficulty_menu = tk.OptionMenu(self.root, self.difficulty_var, "Easy", "Medium", "Hard", command=self.change_difficulty)
        difficulty_menu.grid(row=self.size + 1, columnspan=self.size, pady=5)
        
        # Creating game grid with buttons
        for row in range(self.size):
            for col in range(self.size):
                button = tk.Button(self.root, text=" ", width=4, height=2, command=lambda r=row, c=col: self.reveal(r, c))
                button.grid(row=row, column=col)
                self.buttons[(row, col)] = button
        
        # Reset button
        self.reset_button = tk.Button(self.root, text="Reset Game", command=self.reset_game)
        self.reset_button.grid(row=self.size + 2, columnspan=self.size, pady=10)
        
        self.play_sound('start')

    def play_sound(self, action):
        sounds = {
            'start': 'start_sound.mp3',
            'click': 'click_sound.mp3',
            'bomb': 'bomb_sound.mp3',
            'win': 'win_sound.mp3',
            'lose': 'lose_sound.mp3',
        }
        if action in sounds:
            # Replace this with an actual sound playing function
            print(f"Playing sound: {sounds[action]}")

    def _place_bombs(self):
        while len(self.bomb_positions) < self.bombs:
            r, c = random.randint(0, self.size - 1), random.randint(0, self.size - 1)
            self.bomb_positions.add((r, c))

    def _count_adjacent_bombs(self, r, c):
        directions = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]
        count = sum((r+dr, c+dc) in self.bomb_positions for dr, dc in directions)
        return count

    def reveal(self, r, c):
        if not self.start_time:
            self.start_time = time.time()

        if (r, c) in self.flagged:
            return

        if (r, c) in self.bomb_positions:
            self.play_sound('bomb')
            self.end_game("Game Over", "💣 You hit a bomb!")
            return

        if (r, c) in self.revealed:
            return

        self.revealed.add((r, c))
        bomb_count = self._count_adjacent_bombs(r, c)
        self.board[r][c] = str(bomb_count) if bomb_count > 0 else '0'

        button = self.buttons[(r, c)]
        button.config(text=self.board[r][c], state="disabled", relief="sunken", bg="lightblue")

        if bomb_count == 0:
            for dr, dc in [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]:
                nr, nc = r + dr, c + dc
                if 0 <= nr < self.size and 0 <= nc < self.size:
                    self.reveal(nr, nc)

        if len(self.revealed) == (self.size ** 2 - self.bombs):
            self.play_sound('win')
            elapsed_time = int(time.time() - self.start_time)
            self.end_game("Congratulations!", f"🎉 You cleared the board in {elapsed_time} seconds!")

        self.update_timer()

    def update_timer(self):
        if self.start_time:
            elapsed_time = int(time.time() - self.start_time)
            self.timer_label.config(text=f"Time: {elapsed_time}")
        self.root.after(1000, self.update_timer)

    def end_game(self, title, message):
        messagebox.showinfo(title, message)
        self.root.quit()

    def reset_game(self):
        self.size, self.bombs = self._get_difficulty_params()
        self.board = [[' ' for _ in range(self.size)] for _ in range(self.size)]
        self.bomb_positions = set()
        self.revealed = set()
        self.flagged = set()
        self._place_bombs()
        self.start_time = None
        self.timer_label.config(text="Time: 0")

        for button in self.buttons.values():
            button.config(text=" ", state="normal", relief="raised", bg="lightgrey")
        self.play_sound('start')

    def change_difficulty(self, difficulty):
        if difficulty == "Easy":
            self.size = 5
            self.bombs = 5
        elif difficulty == "Medium":
            self.size = 8
            self.bombs = 12
        else:
            self.size = 10
            self.bombs = 20
        self.reset_game()

    def _get_difficulty_params(self):
        if self.difficulty_var.get() == "Easy":
            return 5, 5
        elif self.difficulty_var.get() == "Medium":
            return 8, 12
        else:
            return 10, 20

    def play(self):
        self.root.mainloop()

# Start the game
game = Minesweeper(size=5, bombs=3)
game.play()
