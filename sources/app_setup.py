import tkinter as tk
from tkinter import messagebox, simpledialog

from Datas import Init_Perks, cool_print_dict

from random import randint, seed

from click_in_DBD import do_the_thing

seed()

def make_dict_checkable_vars(Role_Perks: dict):
    checkable_vars = {k:tk.BooleanVar() for k in Role_Perks}
    del checkable_vars["All"]
    
    return checkable_vars


#On va chercher à générer la liste des perks possédées
def get_checked(checkable_vars: dict):
    checked_items = []
    for k in checkable_vars:
        if checkable_vars[k].get():
            checked_items.append(f"{k}")
    
    return checked_items


def build_checked_perks(checked_items, Role_Perks: dict):
    checked_perks = [ perk
        for k in checked_items
        for perk in Role_Perks[k]
    ]
    
    for perk in Role_Perks["All"]:
        checked_perks.append(perk)
    
    return checked_perks


#On choisit 4 compétences
def place_i_end_list(i, L, L_length):
    if(i<L_length):
        p = L[i]
        L[i] = L[L_length-1]
        L[L_length-1] = p


def choose_4_perks(checked_perks: list[str]):
    the_len = len(checked_perks)
    for i in range(4):
        p = randint(0,the_len-1-i)
        place_i_end_list(p, checked_perks, the_len-i)
    
    return checked_perks[-4::]


class CustomDialog(simpledialog.Dialog):
    def __init__(self, parent, the_perks, title=None):
        self.result = None
        self.perks = the_perks
        super().__init__(parent, title)
        """
        self.lift()
        self.attributes("-topmost", True)
        self.after_idle(self.attributes, '-topmost', False)
        """
        
    def body(self, master):
        tk.Label(master, text=f"Vos compétences aléatoires:{", ".join(self.perks)}").grid(row=0, column=0, padx=10, pady=10)
        return None  # Initial focus

    def buttonbox(self):
        box = tk.Frame(self)

        tk.Button(box, text="Annuler", width=10, command=self.cancel).pack(side=tk.LEFT, padx=5, pady=5)
        tk.Button(box, text="Relancer", width=10, command=self.reroll, default=tk.ACTIVE).pack(side=tk.LEFT, padx=5, pady=5)
        tk.Button(box, text="Équiper ces compétences", width=10, command=self.equip_perks).pack(side=tk.LEFT, padx=5, pady=5)

        self.bind("<Escape>", self.cancel)

        box.pack()

    def cancel(self, event=None):
        self.result = "cancel"
        self.destroy()
    
    def reroll(self, event=None):
        self.result = "reroll"
        self.destroy()
    
    def equip_perks(self, event=None):
        self.result = "equip"
        self.destroy()


def save_checked(checkable_vars, filename="../tkinter/Survivor_options.txt"):
        with open(filename, "w") as file:
            for name, var in checkable_vars.items():
                if var.get():
                    file.write(name + "\n")
        messagebox.showinfo("Sauvegarde", "Vos préférences sont sauvegardées")


def load_checked(checkable_vars, filename="../tkinter/Survivor_options.txt"):
        try:
            with open(filename, "r") as file:
                checked_options = file.read().splitlines()
                for name in checkable_vars:
                    if name in checked_options:
                        checkable_vars[name].set(True)
                    else:
                        checkable_vars[name].set(False)
        except FileNotFoundError:
            messagebox.showwarning("Aïe", "Pas de sauvegarde trouvée.")


class Application(tk.Tk):
    def __init__(self, All_Perks, icon_path = "../tkinter/icone/skull.ico", saves_path = {"survivor": "../tkinter/Survivor_options.txt", "killer": "../tkinter/Killer_options.txt"}):
        super().__init__()
        
        #stock All_perks
        self.surv_perks = All_Perks["survivors"]
        self.killer_perks = All_Perks["killers"]
        
        self.survivor_save_path = saves_path["survivor"]
        self.killer_save_path = saves_path["killer"]
        
        #Création de la fenêtre et sa taille
        self.title("Chaos mode, but the mode isn't live")
        self.iconbitmap(icon_path)
        self.configure(background='#7d8cd2')
        
        self.geometry("800x600")
        self.resizable(False, False)
        
        self.update_idletasks()
        width = self.winfo_screenwidth() // 2 + self.winfo_screenwidth() // 4
        height = self.winfo_screenheight() // 2 + self.winfo_screenheight() // 4
        x = (self.winfo_screenwidth() // 2) - (width // 2)
        y = (self.winfo_screenheight() // 2) - (height // 2)
        self.geometry('{}x{}+{}+{}'.format(width, height, x, y))
        
        
        self.show_main_page()


    def show_main_page(self):
        self.clear_content()
        self.reset_grid_config()
        
        self.grid_rowconfigure(0, weight=1)
        self.grid_rowconfigure(1, weight=2)
        self.grid_rowconfigure(2, weight=1)
        
        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=2)
        self.grid_columnconfigure(2, weight=2)
        self.grid_columnconfigure(3, weight=1)
        
        #Première page de choix du rôle        
        tk.Label(self, text="Choisissez votre rôle", font=("Arial", 24), bg="#7d8cd2").grid(row=0, column=1, columnspan=2)
        
        self.button1 = tk.Button(self, text="Survivant", font=("Arial", 24), command=lambda: self.role_window(self.surv_perks, self.survivor_save_path))
        self.button1.grid(row=1, column=1, sticky='nsew', padx=5)
        
        self.button2 = tk.Button(self, text="Tueur", font=("Arial", 24), command=lambda: self.role_window(self.killer_perks, self.killer_save_path))
        self.button2.grid(row=1, column=2, sticky='nsew', padx=5)


    def role_window(self, role_perks, save_path):
        self.clear_content()
        self.reset_grid_config()
        
        checkable_vars = make_dict_checkable_vars(role_perks)
        self.make_checkables_window(checkable_vars, role_perks, save_path)
    
    
    def open_dialog(self, checkable_vars, Role_perks, the_perks):
        dialog = CustomDialog(self, the_perks, "Vos compétences ce match")
        
        match dialog.result:
            case "reroll":
                self.show_random_perks(checkable_vars, Role_perks)
                
            case "equip":
                do_the_thing(the_perks)
    
    def show_random_perks(self, checkable_vars: dict, Role_perks):
        checked_items = get_checked(checkable_vars)
    
        checked_perks = build_checked_perks(checked_items, Role_perks)
    
        the_perks = choose_4_perks(checked_perks)
        
        self.open_dialog(checkable_vars, Role_perks, the_perks)
        


    def make_checkables_window(self, checkable_vars, role_perks, save_path):
        the_len: int = len(checkable_vars)
        
        #Configuration de la grille
        for i in range(the_len//4+1):
            self.grid_rowconfigure(i, weight=1)
        
        self.grid_columnconfigure(0, weight=1)
        for i in range(1,5):
            self.grid_columnconfigure(i, weight=2)
        
        
        
        #Création des checkbox, et chargement de la sauvegarde
        load_checked(checkable_vars, save_path)
        checkboxes = []
        for k in checkable_vars:
            checkboxes.append(tk.Checkbutton(self, text=f"{k}", variable = checkable_vars[k], bg="#7d8cd2"))
        
        #Placement des checkbox
        for i in range(the_len):
            checkboxes[i].grid(row=i//4, column=i%4+1)
    
        btn_show = tk.Button(self, text="Alors, quelles compétences ?", command=lambda: self.show_random_perks(checkable_vars, role_perks), bg="#955555")
        btn_save = tk.Button(self, text="Sauvegardez vos cases cochées", command=lambda: save_checked(checkable_vars, save_path) ,bg="#008000")
        btn_back = tk.Button(self, text="Retour", command=self.show_main_page)
        
        btn_show.grid(row=the_len//4 + 1, column=0)
        btn_save.grid(row=the_len//4 + 1, column=1)
        btn_back.grid(row=0, column=0)


    def clear_content(self):
        for widget in self.winfo_children():
            widget.destroy()


    def reset_grid_config(self):
        # Réinitialiser les configurations de grid
        for i in range(self.grid_size()[1]):  # Réinitialiser les lignes
            self.grid_rowconfigure(i, weight=0)
        for j in range(self.grid_size()[0]):  # Réinitialiser les colonnes
            self.grid_columnconfigure(j, weight=0)


def main():
    #Dict qui contiendra le nom des survs
    All_Perks = {
        "survivors": {
            "Dwight Fairfield": ['Bond', 'Leader', 'Prove Thyself'], 
            "Meg Thomas": ['Adrenaline', 'Quick & Quiet', 'Sprint Burst'], 
            "Claudette Morel": ['Botany Knowledge', 'Empathy', 'Self-Care'],
            "All": ['sAll1', 'sAll2', 'sAll3', 'sAll4']
        }, 
        "killers": {
            "The Trapper": ['Agitation', 'Brutal Strength', 'Unnerving Presence'],
            "The Wraith": ['Bloodhound', 'Predator', 'Shadowborn'],
            "The Hillbilly": ['Enduring', 'Lightborn', 'Tinkerer'],
            "All": ['kAll1', 'kAll2', 'kAll3', 'kAll4']
        }
    }
    
    app = Application(All_Perks)
    
    app.mainloop()

if __name__ == "__main__":
    main()
    