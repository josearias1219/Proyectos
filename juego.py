"""
Requisitos:
 * - Tablero de 7x6 (7 en el eje "x" y 6 en el "y").
 * - Fichas Rojas y Amarillas. La primera partida la comienza siempre la Roja
 *   (la segunda la Amarilla, la tercera la Roja...).
 * - No hay que implementar una funcionalidad que te permita jugar contra la App.
 *   Se asume que jugarán dos personas reales alternándose.
 * - Al seleccionar la columna se coloca la ficha en la parte inferior.
 * - Guardar el número partidas ganadas de cada equipo mientras la App no se finaliza.
 * - Dos botones para reiniciar la partida en marcha y para resetear el
 *   contador de victorias y derrotas.
 * - Puedes añadirle todas las funcionalidades extra que consideres.

"""

import tkinter as tk
from tkinter import messagebox

class ConectaCuatro:
    def __init__(self, root):
        self.root = root
        self.root.title("Conecta Cuatro")
        
        self.turn = 0  # 0 for Red, 1 for Yellow
        self.wins = {"Rojo": 0, "Amarillo": 0}
        
        self.board = [[None for _ in range(7)] for _ in range(6)]
        
        self.create_widgets()
        self.reset_board()

    def create_widgets(self):
        self.canvas = tk.Canvas(self.root, width=700, height=600, bg='blue')
        self.canvas.grid(row=0, column=0, columnspan=7)
        
        self.columns = [tk.Button(self.root, text=f"{i+1}", command=lambda c=i: self.drop_token(c)) for i in range(7)]
        for i, button in enumerate(self.columns):
            button.grid(row=1, column=i)
        
        self.reset_button = tk.Button(self.root, text="Reiniciar Partida", command=self.reset_board)
        self.reset_button.grid(row=2, column=0, columnspan=3)
        
        self.reset_scores_button = tk.Button(self.root, text="Resetear Contador", command=self.reset_scores)
        self.reset_scores_button.grid(row=2, column=4, columnspan=3)
        
        self.score_label = tk.Label(self.root, text=f"Rojo: {self.wins['Rojo']} | Amarillo: {self.wins['Amarillo']}")
        self.score_label.grid(row=3, column=0, columnspan=7)

    def reset_board(self):
        self.board = [[None for _ in range(7)] for _ in range(6)]
        self.turn = 0 if sum(self.wins.values()) % 2 == 0 else 1
        self.update_canvas()

    def reset_scores(self):
        self.wins = {"Rojo": 0, "Amarillo": 0}
        self.update_score_label()

    def drop_token(self, column):
        for row in range(5, -1, -1):
            if self.board[row][column] is None:
                self.board[row][column] = "Rojo" if self.turn == 0 else "Amarillo"
                if self.check_win(row, column):
                    winner = "Rojo" if self.turn == 0 else "Amarillo"
                    self.wins[winner] += 1
                    messagebox.showinfo("Juego Terminado", f"¡{winner} ha ganado!")
                    self.reset_board()
                elif all(all(cell is not None for cell in row) for row in self.board):
                    messagebox.showinfo("Juego Terminado", "¡Es un empate!")
                    self.reset_board()
                else:
                    self.turn = 1 - self.turn
                self.update_canvas()
                self.update_score_label()
                return
        messagebox.showwarning("Columna Llena", "Esta columna está llena, selecciona otra columna.")

    def update_canvas(self):
        self.canvas.delete("all")
        for row in range(6):
            for col in range(7):
                x0 = col * 100 + 10
                y0 = row * 100 + 10
                x1 = x0 + 80
                y1 = y0 + 80
                color = 'white' if self.board[row][col] is None else 'red' if self.board[row][col] == "Rojo" else 'yellow'
                self.canvas.create_oval(x0, y0, x1, y1, fill=color, outline='black')

    def update_score_label(self):
        self.score_label.config(text=f"Rojo: {self.wins['Rojo']} | Amarillo: {self.wins['Amarillo']}")

    def check_win(self, row, col):
        directions = [(1, 0), (0, 1), (1, 1), (1, -1)]
        color = self.board[row][col]
        for dr, dc in directions:
            count = 1
            for d in (1, -1):
                r, c = row + d*dr, col + d*dc
                while 0 <= r < 6 and 0 <= c < 7 and self.board[r][c] == color:
                    count += 1
                    r += d*dr
                    c += d*dc
                if count >= 4:
                    return True
        return False

if __name__ == "__main__":
    root = tk.Tk()
    game = ConectaCuatro(root)
    root.mainloop()

