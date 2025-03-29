import tkinter as tk
from tkinter import ttk
from functools import partial


class Board:
    def __init__(self, root):
        self.board = [[" "] * 3 for _ in range(3)]
        self.buttons = [[None for _ in range(3)] for _ in range(3)]
        self.current_player = "O"

        self.x_img = tk.PhotoImage(file="X.png")  # Картинка для крестика
        self.o_img = tk.PhotoImage(file="O.png")  # Картинка для нолика


        style = ttk.Style()
        style.theme_use("clam")  # Используем тему, которая поддерживает кастомизацию

        style.configure("Custom.TButton",
                        font=("Courier", 24),
                        width = 2,
                        padding = 5,
                        background="pink",  # Цвет фона кнопки (не всегда работает)
                        foreground="black",  # Цвет текста
                        bordercolor="#d61483",  # Цвет границы (не всегда применяется)
                        borderwidth=5,  # Толщина границы
                        relief="solid")


        for i in range(3):
            for j in range(3):
                btn = ttk.Button(root, text=" ", style="Custom.TButton",
                                 command=lambda row=i, col=j: self.make_move(row, col))
                btn.grid(row=i, column=j, padx=5, pady=5, ipadx=10, ipady=10)
                # btn = tk.Button(root, text=" ", font=("Courier", 24), width=5, height=2, bg="pink",
                #                 border="1px #d61483", command=lambda row=i, col=j: self.make_move(row, col))
                # btn.grid(row=i, column=j)
                self.buttons[i][j] = btn

        self.win_label = tk.Label(root, text="", font=("Courier", 24), fg="#d61483")
        self.win_label.grid(row=3, column=0, columnspan=3)

        self.new_game_button = tk.Button(root, text="New Game", font=("Courier", 16), width=15, height=1, bg="pink", command=self.reset_board)
        self.new_game_button.grid(row=4, column=0, columnspan=3, pady=10)
        self.new_game_button.grid_remove()


    def make_move(self, row, col):
        if self.board[row][col] == " ":
            self.board[row][col] = self.current_player
            self.buttons[row][col].config(text=self.current_player)
            img = self.o_img if self.current_player == "O" else self.x_img
            self.buttons[row][col].config(image=img, text="")  # Убираем текст, ставим картинку

            if self.check_winner():
                return self.show_winner(self.current_player)
            if self.is_full():
                return self.show_winner("Draw")
            self.current_player = "X"
            self.ai_move()

    def ai_move(self):
        move = self.best_move()
        if move:
            row, col = move
            self.board[row][col] = "X"
            self.buttons[row][col].config(image=self.x_img, text="")
            if self.check_winner():
                return self.show_winner("X")
            if self.is_full():
                return self.show_winner("Draw")
            self.current_player = "O"
    def check_winner(self):
        for i in range(3):
            if self.board[i][0] == self.board[i][1] == self.board[i][2] and self.board[i][0] != " ":
                return self.board[i][0]
            if self.board[0][i] == self.board[1][i] == self.board[2][i] and self.board[0][i] != " ":
                return self.board[0][i]
        if self.board[0][0] == self.board[1][1] == self.board[2][2] and self.board[0][0] != " ":
            return self.board[0][0]
        if self.board[0][2] == self.board[1][1] == self.board[2][0] and self.board[0][2] != " ":
            return self.board[0][2]
        return None;

    def is_full(self):
        for i in range(3):
            for j in range(3):
                if self.board[i][j] == " ":
                    return False
        return True

    def minimax(self, depth, ai_turn):
        winner = self.check_winner()
        if winner == "X":
            return 1;
        if winner == "O":
            return -1;
        if self.is_full():
            return 0;

        if ai_turn:
            best_score = -float("inf")
            for i in range(3):
                for j in range(3):
                    if self.board[i][j] == " ":
                        self.board[i][j] = "X"
                        score = self.minimax(depth + 1, False)
                        self.board[i][j] = " "
                        best_score = max(best_score, score)
            return best_score
        else:
            best_score = float("inf")
            for i in range(3):
                for j in range(3):
                    if self.board[i][j] == " ":
                        self.board[i][j] = "O"
                        score = self.minimax(depth + 1, True)
                        self.board[i][j] = " "
                        best_score = min(best_score, score)
            return best_score
    def best_move(self):
        best_score = -float("inf")
        move = None;
        for i in range(3):
            for j in range(3):
                if self.board[i][j] == " ":
                    self.board[i][j] = "X"
                    score = self.minimax(0, False);
                    self.board[i][j] = " "
                    if score > best_score:
                        best_score = score
                        move = (i, j)
        return move

    def show_winner(self, winner):
        if winner == "Draw":
            self.win_label.config(text="DRAW!")
        else:
            self.win_label = tk.Label(text=f"WINNER: {winner}", font=("Courier", 24), fg="#d61483")
            self.win_label.grid(row=3, column=0, columnspan=3)
        self.new_game_button.grid()
        for i in range(3):
            for j in range(3):
                self.buttons[i][j].config(state=tk.DISABLED)

    def reset_board(self):
        self.board = [[" "] * 3 for _ in range(3)]
        self.current_player = "O"
        self.win_label.config(text="")
        self.new_game_button.grid_remove()
        for i in range(3):
            for j in range(3):
                self.buttons[i][j].config(image="", text=" ", state=tk.NORMAL)
def play():
    root = tk.Tk()
    root.title("Tik Tak Toe")
    game = Board(root)
    root.mainloop()


play()
