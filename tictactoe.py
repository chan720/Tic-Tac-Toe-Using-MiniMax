#code of tic tac toe using number of winning lines
import tkinter as tk
from tkinter import messagebox
import random
import time

class TicTacToe:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Tic Tac Toe")
        self.current_player = "X"
        self.board = [" " for _ in range(9)]
        self.buttons = []
        self.setup_board()
        self.setup_reset_button()
        self.display_welcome_message()
        self.root.after(3000, self.hide_welcome_message)

    def display_welcome_message(self):
        self.welcome_label = tk.Label(self.root, text="Welcome to Tic Tac Toe!", font=('Helvetica', 18))
        self.welcome_label.grid(row=3, columnspan=3, padx=5, pady=5)

    def hide_welcome_message(self):
        self.welcome_label.grid_forget()

    def setup_board(self):
        for i in range(3):
            for j in range(3):
                button = tk.Button(self.root, text="", font=('Helvetica', 24), width=5, height=2,
                                   command=lambda i=i, j=j: self.on_button_click(i, j))
                button.grid(row=i, column=j, padx=5, pady=5)
                self.buttons.append(button)

    def setup_reset_button(self):
        reset_button = tk.Button(self.root, text="Reset", font=('Helvetica', 14), command=self.reset_game)
        reset_button.grid(row=3, column=1, padx=5, pady=5)

    def on_button_click(self, row, col):
        index = row * 3 + col
        if self.board[index] == " ":
            self.board[index] = self.current_player
            self.buttons[index].config(text=self.current_player, fg='green' if self.current_player == "X" else 'red')
            if self.check_winner():
                messagebox.showinfo("Winner", f"{self.current_player} wins!")
                self.reset_game()
            elif " " not in self.board:
                messagebox.showinfo("Draw", "It's a draw!")
                self.reset_game()
            else:
                self.current_player = "O" if self.current_player == "X" else "X"
                if self.current_player == "O":
                    self.ai_move()

    def ai_move(self):
        best_score = float("-inf")
        best_move = None
        for i in range(9):
            if self.board[i] == " ":
                self.board[i] = "O"
                score = self.minimax(self.board, 0, False)
                self.board[i] = " "
                if score > best_score:
                    best_score = score
                    best_move = i
        self.on_button_click(best_move // 3, best_move % 3)

    def minimax(self, board, depth, is_maximizing):
        if self.check_winner(board) == "X":
            return -10 + depth
        elif self.check_winner(board) == "O":
            return 10 - depth
        elif " " not in board:
            return 0

        if is_maximizing:
            best_score = float("-inf")
            for i in range(9):
                if board[i] == " ":
                    board[i] = "O"
                    score = self.minimax(board, depth + 1, False)
                    board[i] = " "
                    best_score = max(score, best_score)
            return best_score
        else:
            best_score = float("inf")
            for i in range(9):
                if board[i] == " ":
                    board[i] = "X"
                    score = self.minimax(board, depth + 1, True)
                    board[i] = " "
                    best_score = min(score, best_score)
            return best_score

    def check_winner(self, board=None):
        if board is None:
            board = self.board
        lines = [(0, 1, 2), (3, 4, 5), (6, 7, 8),
                 (0, 3, 6), (1, 4, 7), (2, 5, 8),
                 (0, 4, 8), (2, 4, 6)]
        for line in lines:
            if board[line[0]] == board[line[1]] == board[line[2]] != " ":
                return board[line[0]]
        return None

    def reset_game(self):
        for i in range(9):
            self.board[i] = " "
            self.buttons[i].config(text="")
        self.current_player = "X"
    def run(self):
        self.root.mainloop()
        # self.root.mainloop()
if __name__ == "__main__":
    game = TicTacToe()
    
    game.run()