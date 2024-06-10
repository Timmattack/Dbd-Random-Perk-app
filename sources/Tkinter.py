import tkinter as tk
from tkinter import messagebox

def show_checked():
    checked_items = []
    if var1.get():
        checked_items.append("Option 1")
    if var2.get():
        checked_items.append("Option 2")
    if var3.get():
        checked_items.append("Option 3")
    
    if checked_items:
        messagebox.showinfo("Checked Items", "You checked: " + ", ".join(checked_items))
    else:
        messagebox.showinfo("Checked Items", "No options were checked.")

# Create the main window
root = tk.Tk()
root.title("Chaos mode, but the mode isn't live")
root.iconbitmap('../tkinter/icone/skull.ico')


root.geometry("800x600")
root.resizable(False, False)

root.update_idletasks()
width = root.winfo_screenwidth() // 2 + root.winfo_screenwidth() // 4
height = root.winfo_screenheight() // 2 + root.winfo_screenheight() // 4
x = (root.winfo_screenwidth() // 2) - (width // 2)
y = (root.winfo_screenheight() // 2) - (height // 2)
root.geometry('{}x{}+{}+{}'.format(width, height, x, y))

# Variables to hold the state of the checkboxes
var1 = tk.BooleanVar()
var2 = tk.BooleanVar()
var3 = tk.BooleanVar()

# Create checkboxes
checkbox1 = tk.Checkbutton(root, text="Option 1", variable=var1)
checkbox2 = tk.Checkbutton(root, text="Option 2", variable=var2)
checkbox3 = tk.Checkbutton(root, text="Option 3", variable=var3)

# Create a button to show the checked options
btn_show = tk.Button(root, text="Show Checked Options", command=show_checked)

# Layout the widgets
checkbox1.pack()
checkbox2.pack()
checkbox3.pack()
btn_show.pack()

# Start the main event loop
root.mainloop()