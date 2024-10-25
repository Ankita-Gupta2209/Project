import tkinter as tk
from tkinter import messagebox

def check_winner():
    global winner
    for combo in [[0, 1, 2], [3, 4, 5], [6, 7, 8], [0, 3, 6], [1, 4, 7], [2, 5, 8], [0, 4, 8], [2, 4, 6]]:
        if Buttons[combo[0]]["text"] == Buttons[combo[1]]["text"] == Buttons[combo[2]]["text"] != "":
            Buttons[combo[0]].config(bg="green")
            Buttons[combo[1]].config(bg="green")
            Buttons[combo[2]].config(bg="green")
            messagebox.showinfo("Tic-Tac-Toe", f"Player {Buttons[combo[0]]['text']} wins!")
            winner = True
            return

def button_click(index):
    if Buttons[index]["text"] == "" and not winner:
        Buttons[index]["text"] = current_player
        check_winner()
        toggle_player()

def toggle_player():
    global current_player
    current_player = "X" if current_player == "O" else "O"
    label.config(text=f"Player {current_player}'s turn")

# Initialize the main window
root = tk.Tk()
root.title("Tic-Tac-Toe")

# Create buttons and bind them to the click event
Buttons = []
for i in range(9):
    button = tk.Button(root, text="", font=("normal", 25), width=6, height=2, command=lambda i=i: button_click(i))
    button.grid(row=i // 3, column=i % 3)
    Buttons.append(button)

# Initialize current player and winner status
current_player = "X"
winner = False
label = tk.Label(root, text=f"Player {current_player}'s turn", font=("normal", 16))
label.grid(row=3, column=0, columnspan=3)

# Start the Tkinter event loop
root.mainloop()