import tkinter as tk
from tkinter import messagebox

from Datas import Init_Perks, cool_print_dict

def show_checked(checkable_vars: dict):
    checked_items = []
    for k in checkable_vars:
        if checkable_vars[k].get():
            checked_items.append(f"{k}")

    if checked_items:
        messagebox.showinfo("Personnages possédés", "Vous avez: " + ", ".join(checked_items))
    else:
        messagebox.showinfo("Aucun personnage ?", "Vous n'avez personnes ?_?.")


def make_dict_checkable_vars(Role_Perks: dict):
    checkable_vars = {k:0 for k in Role_Perks}
    del checkable_vars["All"]
    
    return checkable_vars


class Application(tk.Tk):
    def __init__(self, All_Perks):
        super().__init__()
        
        #Création de la fenêtre et sa taille
        self.title("Chaos mode, but the mode isn't live")
        self.iconbitmap('../tkinter/icone/skull.ico')
        self.configure(background='#7d8cd2')
        
        self.geometry("800x600")
        self.resizable(False, False)
        
        self.update_idletasks()
        width = self.winfo_screenwidth() // 2 + self.winfo_screenwidth() // 4
        height = self.winfo_screenheight() // 2 + self.winfo_screenheight() // 4
        x = (self.winfo_screenwidth() // 2) - (width // 2)
        y = (self.winfo_screenheight() // 2) - (height // 2)
        self.geometry('{}x{}+{}+{}'.format(width, height, x, y))
        
        #Première page de choix du rôle        
        tk.Label(self, text="Choisissez votre rôle", font=("Arial", 24)).pack(pady=20)
        
        self.button1 = tk.Button(self, text="Survivant", command=lambda: self.survivor_window(All_Perks["survivors"]))
        self.button1.pack(pady=10)
        
        self.button2 = tk.Button(self, text="Tueur", command=lambda: self.killer_window(All_Perks["killers"]))
        self.button2.pack(pady=10)
    
    def clear_content(self):
        for widget in self.winfo_children():
            widget.destroy()
    
    def make_checkables_window(self, checkable_vars):
        the_len: int = len(checkable_vars)
        for i in range(the_len//4+1):
            self.grid_rowconfigure(i, weight=1)
        for i in range(4):
            self.grid_columnconfigure(i, weight=1)
    
        #Création des variables pour checkbox
        for k in checkable_vars:
            checkable_vars[k]= tk.BooleanVar()
    
        #Création des boutons
        checkboxes = []
        for k in checkable_vars:
            checkboxes.append(tk.Checkbutton(self, text=f"{k}", variable = checkable_vars[k], bg="#7d8cd2"))

        btn_show = tk.Button(self, text="Show Checked Options", command=lambda: show_checked(checkable_vars), bg="#955555")
    
        #Placement des boutons
        for i in range(the_len):
            checkboxes[i].grid(row=i//4, column=i%4)
    
        btn_show.grid(row=the_len//4 + 1 )
    
    def survivor_window(self, surv_perks):
        self.clear_content()
        
        checkable_vars = make_dict_checkable_vars(surv_perks)
        self.make_checkables_window(checkable_vars)
    
    def killer_window(self, killer_perks):
        self.clear_content()
        
        checkable_vars = make_dict_checkable_vars(killer_perks)
        self.make_checkables_window(checkable_vars)



    
"""
def Launch_app(checkable_vars: dict, All_Perks: dict):
    
    Survs_dict = {k:0 for k in All_Perks["survivors"]}
    del Survs_dict["All"]
    
    Killers_dict = {k:0 for k in All_Perks["killers"]}
    del Killers_dict["All"]
    
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
        checkboxes.append(tk.Checkbutton(root, text=f"{k}", variable = checkable_vars[k], bg="#7d8cd2"))

    btn_show = tk.Button(root, text="Show Checked Options", command=lambda: show_checked(checkable_vars), bg="#955555")
    
    #Placement des boutons
    for i in range(the_len):
        checkboxes[i].grid(row=i//4, column=i%4)
    
    btn_show.grid(row=the_len//4 + 1 )

    # Start the main event loop
    root.mainloop()
"""

#On va chercher à générer la liste des perks possédées
def get_checked(checkable_vars: dict):
    checked_items = []
    for k in checkable_vars:
        if checkable_vars[k].get():
            checked_items.append(f"{k}")
    
    return checked_items

def build_checked_perks(checked_items, Role_Perks):
    checked_perks = [ perk
        for k in checked_items
        for perk in Role_Perks[k]
    ]
    
    return checked_perks
    

def main():
    #Dict qui contiendra le nom des survs
    All_Perks = {
        "survivors": {
            "Dwight Fairfield": ['Bond', 'Leader', 'Prove Thyself'], 
            "Meg Thomas": ['Adrenaline', 'Quick & Quiet', 'Sprint Burst'], 
            "Claudette Morel": ['Botany Knowledge', 'Empathy', 'Self-Care'],
            "All": ['Feur1', 'Feur2', 'Feur3', 'Feur4']
        }, 
        "killers": {
            "The Trapper": ['Agitation', 'Brutal Strength', 'Unnerving Presence'],
            "The Wraith": ['Bloodhound', 'Predator', 'Shadowborn'],
            "The Hillbilly": ['Enduring', 'Lightborn', 'Tinkerer'],
            "All": ['Feur1', 'Feur2', 'Feur3', 'Feur4']
        }
    }
    
    app = Application(All_Perks)
    
    app.mainloop()

if __name__ == "__main__":
    main()
    