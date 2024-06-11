import tkinter as tk
from tkinter import messagebox

NUMBER_OF_BUTTON: int = 40

checkable_vars = []

def show_checked():
    global checkable_vars
    checked_items = []
    for i in range(NUMBER_OF_BUTTON):
        if checkable_vars[i].get():
            checked_items.append(f"Option {i}")

    if checked_items:
        messagebox.showinfo("Checked Items", "You checked: " + ", ".join(checked_items))
    else:
        messagebox.showinfo("Checked Items", "No options were checked.")


def main():
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
    for i in range(NUMBER_OF_BUTTON//4+1):
        root.grid_rowconfigure(i, weight=1)
    for i in range(4):
        root.grid_columnconfigure(i, weight=1)
    
    #Création des boutons
    global checkable_vars
    for i in range(NUMBER_OF_BUTTON):
        checkable_vars.append(tk.BooleanVar())

    checkboxes = []
    for i in range(NUMBER_OF_BUTTON):
        checkboxes.append(tk.Checkbutton(root, text=f"Option {i}", variable = checkable_vars[i]))

    btn_show = tk.Button(root, text="Show Checked Options", command=show_checked)
    
    #Placement des boutons
    for i in range(NUMBER_OF_BUTTON):
        checkboxes[i].grid(row=i//4, column=i%4)
    
    btn_show.grid(row=NUMBER_OF_BUTTON//4 + 1 )

    # Start the main event loop
    root.mainloop()

if __name__ == "__main__":
    main()