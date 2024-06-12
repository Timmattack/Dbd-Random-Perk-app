import tkinter as tk
from tkinter import messagebox


def show_checked(checkable_vars: dict):
    checked_items = []
    for k in checkable_vars:
        if checkable_vars[k].get():
            checked_items.append(f"Option {k}")

    if checked_items:
        messagebox.showinfo("Checked Items", "You checked: " + ", ".join(checked_items))
    else:
        messagebox.showinfo("Checked Items", "No options were checked.")


def Launch_app(checkable_vars: dict):
    # Création de la fenêtre, et de sa taille
    root = tk.Tk()
    root.title("Chaos mode, but the mode isn't live")
    root.iconbitmap('../tkinter/icone/skull.ico')
    root.configure(background='#7d8cd2')

    root.geometry("800x600")
    root.resizable(False, False)

    root.update_idletasks()
    width = root.winfo_screenwidth() // 2 + root.winfo_screenwidth() // 4
    height = root.winfo_screenheight() // 2 + root.winfo_screenheight() // 4
    x = (root.winfo_screenwidth() // 2) - (width // 2)
    y = (root.winfo_screenheight() // 2) - (height // 2)
    root.geometry('{}x{}+{}+{}'.format(width, height, x, y))
    
    #Organisation de la taille des grilles
    
    the_len: int = len(checkable_vars)
    for i in range(the_len//4+1):
        root.grid_rowconfigure(i, weight=1)
    for i in range(4):
        root.grid_columnconfigure(i, weight=1)
    
    #Création des variables pour checkbox
    for k in checkable_vars:
        checkable_vars[k]= tk.BooleanVar()
    
    #Création des boutons
    checkboxes = []
    for k in checkable_vars:
        checkboxes.append(tk.Checkbutton(root, text=f"Option {k}", variable = checkable_vars[k], bg="#7d8cd2"))

    btn_show = tk.Button(root, text="Show Checked Options", command=lambda: show_checked(checkable_vars), bg="#955555")
    
    #Placement des boutons
    for i in range(the_len):
        checkboxes[i].grid(row=i//4, column=i%4)
    
    btn_show.grid(row=the_len//4 + 1 )

    # Start the main event loop
    root.mainloop()


def main():
    #Dict qui contiendra le nom des survs ?
    checkable_vars = {"A": 0, "B": 0, "C": 0, "D": 0, "E": 0, "F": 0, "G": 0, "H": 0, "I": 0, "J": 0, "K": 0, "L": 0, "M": 0, "N": 0, "O": 0, "P": 0, "Q": 0, "R": 0, "S": 0, "T": 0}
    Launch_app(checkable_vars)

if __name__ == "__main__":
    main()