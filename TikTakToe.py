import tkinter as tk
from tkinter import ttk
from functools import partial
from tkinter import PhotoImage, Tk, Label
import os
import sys
from reportlab.graphics import renderPM
from io import BytesIO
import base64
import xml.etree.ElementTree as ET

O_image = "iVBORw0KGgoAAAANSUhEUgAAACMAAAAjCAYAAAAe2bNZAAAACXBIWXMAAAsTAAALEwEAmpwYAAAGsmlUWHRYTUw6Y29tLmFkb2JlLnhtcAAAAAAAPD94cGFja2V0IGJlZ2luPSLvu78iIGlkPSJXNU0wTXBDZWhpSHpyZVN6TlRjemtjOWQiPz4gPHg6eG1wbWV0YSB4bWxuczp4PSJhZG9iZTpuczptZXRhLyIgeDp4bXB0az0iQWRvYmUgWE1QIENvcmUgNy4xLWMwMDAgMTE2LmNjZjg0ZTAsIDIwMjIvMDUvMTktMTA6NTk6NDcgICAgICAgICI+IDxyZGY6UkRGIHhtbG5zOnJkZj0iaHR0cDovL3d3dy53My5vcmcvMTk5OS8wMi8yMi1yZGYtc3ludGF4LW5zIyI+IDxyZGY6RGVzY3JpcHRpb24gcmRmOmFib3V0PSIiIHhtbG5zOnhtcD0iaHR0cDovL25zLmFkb2JlLmNvbS94YXAvMS4wLyIgeG1sbnM6ZGM9Imh0dHA6Ly9wdXJsLm9yZy9kYy9lbGVtZW50cy8xLjEvIiB4bWxuczpwaG90b3Nob3A9Imh0dHA6Ly9ucy5hZG9iZS5jb20vcGhvdG9zaG9wLzEuMC8iIHhtbG5zOnhtcE1NPSJodHRwOi8vbnMuYWRvYmUuY29tL3hhcC8xLjAvbW0vIiB4bWxuczpzdEV2dD0iaHR0cDovL25zLmFkb2JlLmNvbS94YXAvMS4wL3NUeXBlL1Jlc291cmNlRXZlbnQjIiB4bXA6Q3JlYXRvclRvb2w9IkFkb2JlIFBob3Rvc2hvcCAyMi41IChXaW5kb3dzKSIgeG1wOkNyZWF0ZURhdGU9IjIwMjUtMDMtMjlUMTg6MzA6MjcrMDM6MDAiIHhtcDpNb2RpZnlEYXRlPSIyMDI1LTAzLTI5VDIwOjQ2OjAyKzAzOjAwIiB4bXA6TWV0YWRhdGFEYXRlPSIyMDI1LTAzLTI5VDIwOjQ2OjAyKzAzOjAwIiBkYzpmb3JtYXQ9ImltYWdlL3BuZyIgcGhvdG9zaG9wOkNvbG9yTW9kZT0iMyIgcGhvdG9zaG9wOklDQ1Byb2ZpbGU9InNSR0IgSUVDNjE5NjYtMi4xIiB4bXBNTTpJbnN0YW5jZUlEPSJ4bXAuaWlkOmM5NzgzMjY4LTA3NTMtN2Q0NC1iZWI4LTk4MzE5OGMwMzQ4OSIgeG1wTU06RG9jdW1lbnRJRD0ieG1wLmRpZDo3MGY1N2MwZS1lOWUyLWVlNDktYWFhYy0zOWNiOTQ2NzExOWQiIHhtcE1NOk9yaWdpbmFsRG9jdW1lbnRJRD0ieG1wLmRpZDo3MGY1N2MwZS1lOWUyLWVlNDktYWFhYy0zOWNiOTQ2NzExOWQiPiA8eG1wTU06SGlzdG9yeT4gPHJkZjpTZXE+IDxyZGY6bGkgc3RFdnQ6YWN0aW9uPSJjcmVhdGVkIiBzdEV2dDppbnN0YW5jZUlEPSJ4bXAuaWlkOjcwZjU3YzBlLWU5ZTItZWU0OS1hYWFjLTM5Y2I5NDY3MTE5ZCIgc3RFdnQ6d2hlbj0iMjAyNS0wMy0yOVQxODozMDoyNyswMzowMCIgc3RFdnQ6c29mdHdhcmVBZ2VudD0iQWRvYmUgUGhvdG9zaG9wIDIyLjUgKFdpbmRvd3MpIi8+IDxyZGY6bGkgc3RFdnQ6YWN0aW9uPSJzYXZlZCIgc3RFdnQ6aW5zdGFuY2VJRD0ieG1wLmlpZDoyMDQ1YTk2My0xMjFiLTYwNDEtYWZlOS1jYzkzZjUwZjYwMDgiIHN0RXZ0OndoZW49IjIwMjUtMDMtMjlUMTg6NDc6MjcrMDM6MDAiIHN0RXZ0OnNvZnR3YXJlQWdlbnQ9IkFkb2JlIFBob3Rvc2hvcCAyMi41IChXaW5kb3dzKSIgc3RFdnQ6Y2hhbmdlZD0iLyIvPiA8cmRmOmxpIHN0RXZ0OmFjdGlvbj0ic2F2ZWQiIHN0RXZ0Omluc3RhbmNlSUQ9InhtcC5paWQ6Yzk3ODMyNjgtMDc1My03ZDQ0LWJlYjgtOTgzMTk4YzAzNDg5IiBzdEV2dDp3aGVuPSIyMDI1LTAzLTI5VDIwOjQ2OjAyKzAzOjAwIiBzdEV2dDpzb2Z0d2FyZUFnZW50PSJBZG9iZSBQaG90b3Nob3AgMjIuNSAoV2luZG93cykiIHN0RXZ0OmNoYW5nZWQ9Ii8iLz4gPC9yZGY6U2VxPiA8L3htcE1NOkhpc3Rvcnk+IDwvcmRmOkRlc2NyaXB0aW9uPiA8L3JkZjpSREY+IDwveDp4bXBtZXRhPiA8P3hwYWNrZXQgZW5kPSJyIj8+IzrDPQAAAjFJREFUWMPtmDtIHUEUhq+PwsaUNiFBUExAIylzlaBeAtqlENLYBTUKMXbiAwSFKAhBwaiNCtFGEjGKCkoMaUzhCyy0iI0oFlopGozvzT/wXxjHvbM7665Y3OJr7sw5+83s7pyzN2RZVui+EIrLaGWqplSSQRXoBZ8kukAnCNvERCliXA/olhgE75n7eowLmVlggUuJK1KukallnB0iZ6KpjGBGk7RMI/NWEzdpGxNDJgs081Zsa5LOgY+gQoqtBu3glyZuC3xm7FMnmSJNIjuWpNglw9iXsWQegRyu7kQJ2gE/wTK4UMYWwQuyYCDyD3wAEZCpygyDY3BuE9jBFTwEmzbjp8Qy5JLX+6LKfNUEtVLmscNz5JV+VWZImfAXVHIbG8A0WOFq/JbpsrtN8oQD8IQ70hiAgEy3k4zYmULKNN0HmYK4DH74pkw44tkhxuoClulTZcaVCfs8BMVYTcAyI6pMmLdjmKesYAK0eTjm3XAGBkALKI5Vm8IB74J8+mY7Fcoc9hxr4DAACVFy1lnT8tz0M6KxSmNh9FvmB3gAUq41WQ7NVSr4E4DMb5Bk2ukl8NUuZS97W4kx8IY5PbWdbnpat7zTXsNApoQtxoJh1T5hC/odvPJLJkoGT2a3MntsyJxze5DJBBsGMrtSG+K7jHjl00EumNdIiDr3jPLJQcnIjGhkRo3z3VKmGNTzszX6UA/yu+n1XctEeS7tSIHnPD7J5INV1rKIPzLx/2du8h85dEb9iRfOrgAAAABJRU5ErkJggg=="
X_image = "iVBORw0KGgoAAAANSUhEUgAAACIAAAAiCAYAAAA6RwvCAAAACXBIWXMAAAsTAAALEwEAmpwYAAAGsmlUWHRYTUw6Y29tLmFkb2JlLnhtcAAAAAAAPD94cGFja2V0IGJlZ2luPSLvu78iIGlkPSJXNU0wTXBDZWhpSHpyZVN6TlRjemtjOWQiPz4gPHg6eG1wbWV0YSB4bWxuczp4PSJhZG9iZTpuczptZXRhLyIgeDp4bXB0az0iQWRvYmUgWE1QIENvcmUgNy4xLWMwMDAgMTE2LmNjZjg0ZTAsIDIwMjIvMDUvMTktMTA6NTk6NDcgICAgICAgICI+IDxyZGY6UkRGIHhtbG5zOnJkZj0iaHR0cDovL3d3dy53My5vcmcvMTk5OS8wMi8yMi1yZGYtc3ludGF4LW5zIyI+IDxyZGY6RGVzY3JpcHRpb24gcmRmOmFib3V0PSIiIHhtbG5zOnhtcD0iaHR0cDovL25zLmFkb2JlLmNvbS94YXAvMS4wLyIgeG1sbnM6ZGM9Imh0dHA6Ly9wdXJsLm9yZy9kYy9lbGVtZW50cy8xLjEvIiB4bWxuczpwaG90b3Nob3A9Imh0dHA6Ly9ucy5hZG9iZS5jb20vcGhvdG9zaG9wLzEuMC8iIHhtbG5zOnhtcE1NPSJodHRwOi8vbnMuYWRvYmUuY29tL3hhcC8xLjAvbW0vIiB4bWxuczpzdEV2dD0iaHR0cDovL25zLmFkb2JlLmNvbS94YXAvMS4wL3NUeXBlL1Jlc291cmNlRXZlbnQjIiB4bXA6Q3JlYXRvclRvb2w9IkFkb2JlIFBob3Rvc2hvcCAyMi41IChXaW5kb3dzKSIgeG1wOkNyZWF0ZURhdGU9IjIwMjUtMDMtMjlUMTg6NDE6NTIrMDM6MDAiIHhtcDpNb2RpZnlEYXRlPSIyMDI1LTAzLTI5VDIwOjQ2OjI0KzAzOjAwIiB4bXA6TWV0YWRhdGFEYXRlPSIyMDI1LTAzLTI5VDIwOjQ2OjI0KzAzOjAwIiBkYzpmb3JtYXQ9ImltYWdlL3BuZyIgcGhvdG9zaG9wOkNvbG9yTW9kZT0iMyIgcGhvdG9zaG9wOklDQ1Byb2ZpbGU9InNSR0IgSUVDNjE5NjYtMi4xIiB4bXBNTTpJbnN0YW5jZUlEPSJ4bXAuaWlkOjY2NTZmNTY5LWEyNmMtOTA0YS1iZGYwLTdjOTliNTM0YTExZSIgeG1wTU06RG9jdW1lbnRJRD0ieG1wLmRpZDplNjRjNThkYi1hNGQxLTVkNDUtOTE3My1kZjhlODJhYTQwZDIiIHhtcE1NOk9yaWdpbmFsRG9jdW1lbnRJRD0ieG1wLmRpZDplNjRjNThkYi1hNGQxLTVkNDUtOTE3My1kZjhlODJhYTQwZDIiPiA8eG1wTU06SGlzdG9yeT4gPHJkZjpTZXE+IDxyZGY6bGkgc3RFdnQ6YWN0aW9uPSJjcmVhdGVkIiBzdEV2dDppbnN0YW5jZUlEPSJ4bXAuaWlkOmU2NGM1OGRiLWE0ZDEtNWQ0NS05MTczLWRmOGU4MmFhNDBkMiIgc3RFdnQ6d2hlbj0iMjAyNS0wMy0yOVQxODo0MTo1MiswMzowMCIgc3RFdnQ6c29mdHdhcmVBZ2VudD0iQWRvYmUgUGhvdG9zaG9wIDIyLjUgKFdpbmRvd3MpIi8+IDxyZGY6bGkgc3RFdnQ6YWN0aW9uPSJzYXZlZCIgc3RFdnQ6aW5zdGFuY2VJRD0ieG1wLmlpZDo0MDBiMDFhNS04MzUzLTk3NDItOTQyNC03ZGMwZDIyOWEwMjciIHN0RXZ0OndoZW49IjIwMjUtMDMtMjlUMjA6NDI6NDYrMDM6MDAiIHN0RXZ0OnNvZnR3YXJlQWdlbnQ9IkFkb2JlIFBob3Rvc2hvcCAyMi41IChXaW5kb3dzKSIgc3RFdnQ6Y2hhbmdlZD0iLyIvPiA8cmRmOmxpIHN0RXZ0OmFjdGlvbj0ic2F2ZWQiIHN0RXZ0Omluc3RhbmNlSUQ9InhtcC5paWQ6NjY1NmY1NjktYTI2Yy05MDRhLWJkZjAtN2M5OWI1MzRhMTFlIiBzdEV2dDp3aGVuPSIyMDI1LTAzLTI5VDIwOjQ2OjI0KzAzOjAwIiBzdEV2dDpzb2Z0d2FyZUFnZW50PSJBZG9iZSBQaG90b3Nob3AgMjIuNSAoV2luZG93cykiIHN0RXZ0OmNoYW5nZWQ9Ii8iLz4gPC9yZGY6U2VxPiA8L3htcE1NOkhpc3Rvcnk+IDwvcmRmOkRlc2NyaXB0aW9uPiA8L3JkZjpSREY+IDwveDp4bXBtZXRhPiA8P3hwYWNrZXQgZW5kPSJyIj8+a8DnJwAAAStJREFUWMPt18kOgjAQBuA+jh58BbeDGycF9aYe3ZCjj+wDuMatziQ2IaSFoS2Khkn+A4mWL6WUKeOcszyEFZCfgYSqAhkze9WENMQFFVKG7CB3yNQCogrZQ44CQ4EIBH/nYYipQQ6h8RBTp0BG75ngFjAtyCky1hOypj4axNwkA8wtIII0awRrqMAsCIg25Cz57ybtYhXlQa6SAZcxiE4SQgeSFkNC6EKwXAVmFfpNV4HwZQPqQrAcyEX2BqRFmEKw+oqZSZot6xCsnmRmZLPEsobEYUiIv4M4hEfjZw3JxWIdxNzwY6+vS9hdybvqT2/xnsYXWPXlDXQhQ4OepJWEMWmMsEubGTZGmC0VkptWsRRpnk07+apu8xzGIGLyreNEPg5Yxdm3gETyAgi9isTvFn1BAAAAAElFTkSuQmCC"

# O_svg = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 12.19 11.26"><defs><style>.cls-1{fill:#ff68b4;}</style></defs><g id="Layer_2" data-name="Layer 2"><g id="Layer_1-2" data-name="Layer 1"><path class="cls-1" d="M12.12,1.92c-.14-.16-.44,0-.68-.06h0c-.14,0-.21,0-.2-.18s0-.39,0-.59,0-.17-.17-.16-.41,0-.61,0-.16,0-.15-.15V.17c0-.12,0-.17-.16-.17H7.64c-.14,0-.16.05-.16.18s0,.4,0,.61,0,.16-.16.15S7,1,6.79.93s-.26,0-.25.24,0,.36,0,.54,0,.18-.17.17H5.8c-.14,0-.19,0-.18-.17s0-.39,0-.59,0-.19-.18-.18-.41,0-.61,0S4.67.9,4.67.79s0-.43,0-.64S4.65,0,4.54,0H2c-.12,0-.16,0-.16.15s0,.39,0,.59,0,.21-.19.2-.34,0-.51,0-.25,0-.24.22,0,.34,0,.51,0,.23-.2.22-.34,0-.51,0S0,1.93,0,2.11C0,2.66,0,3.2,0,3.75H0V5.06c0,.56,0,.56.57.56C1,5.62,1,5.62.94,6c0,.56,0,.56.55.56a1.21,1.21,0,0,0,.19,0c.15,0,.19.05.19.2s-.11.58,0,.69.48,0,.74,0,.14,0,.14.12v.49c0,.34,0,.34.33.34.61,0,.61,0,.61.62,0,.33-.06.33.3.33.63,0,.64,0,.63.63,0,.24,0,.33.31.31s.48-.1.61,0,0,.39,0,.58,0,.34.31.31.46.06.58,0,.06-.4,0-.6,0-.32.3-.3.46.07.58,0,.06-.4.05-.6.06-.32.31-.31.46.1.59,0,0-.38,0-.58,0-.32.34-.32a1.38,1.38,0,0,1,.29,0c.24,0,.33,0,.31-.3,0-.64,0-.65.64-.64.24,0,.33,0,.31-.3s-.1-.46,0-.59.38,0,.58,0H11c.21,0,.25-.06.24-.24s-.09-.5,0-.64.43,0,.65,0,.27-.05.26-.25c0-.93,0-1.86,0-2.79C12.16,2.35,12.26,2.06,12.12,1.92Zm-8.39.72c0,.12,0,.17-.17.16s-.36,0-.54,0-.25,0-.24.23,0,.41,0,.61v.58h0c0,.41,0,.81,0,1.22,0,.13,0,.18-.16.17s-.41,0-.61,0-.16-.05-.16-.17V3c0-.14,0-.19.18-.18a3.55,3.55,0,0,1,.46,0c.21,0,.29-.06.29-.24a5.23,5.23,0,0,0,0-.56c0-.12,0-.17.16-.16H3C3.94,1.9,3.7,1.67,3.73,2.64Z"/></g></g></""svg>"""
# x_svg = """<svg xmlns=")http://www.w3.org/2000/svg" viewBox="0 0 13.41 13.41"><defs><style>.cls-1{fill:none;stroke:#000;stroke-miterlimit:10;stroke-width:2px;}</style></defs><g id="Layer_2" data-name="Layer 2"><g id="Layer_1-2" data-name="Layer 1"><line class="cls-1" x1="0.71" y1="0.71" x2="12.71" y2="12.71"/><line class="cls-1" x1="0.71" y1="12.71" x2="12.71" y2="0.71"/></g></g></svg>"""

def load_base64_image(base64_string):
    return tk.PhotoImage(data=base64.b64decode(base64_string))

def resource_path(relative_path):
    """ Get absolute path to resource, works for dev and for PyInstaller """
    try:
        # PyInstaller creates a temp folder and stores path in _MEIPASS
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)

class Board:
    def __init__(self, root):
        self.board = [[" "] * 3 for _ in range(3)]
        self.buttons = [[None for _ in range(3)] for _ in range(3)]
        self.current_player = "O"

        self.x_img = load_base64_image(O_image)
        self.o_img = load_base64_image(X_image)
        # self.x_img = tk.PhotoImage(file="images/X.png")  # Картинка для крестика
        # self.o_img = tk.PhotoImage(file="images/O.png")  # Картинка для нолика


        style = ttk.Style()
        style.theme_use("clam")

        style.configure("Custom.TButton",
                        font=("Courier", 24),
                        width = 2,
                        padding = 5,
                        background="#ffd2ed",
                        foreground="black",
                        bordercolor="#d61483",
                        borderwidth=5,
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
            self.buttons[row][col].config(image=img, text="")

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

    photo = load_base64_image(O_image)
    root.iconphoto(False, photo)
    root.title("Tik Tak Toe")
    game = Board(root)
    root.mainloop()


play()
