import sys
import os

script_path = os.path.join(os.path.dirname(__file__), 'sources')
sys.path.append(script_path)

from APIs import update_all_data
from app_setup import Application
from Datas import Init_Perks, cool_print_dict


def main():
    
    err: int = update_all_data("data/live_version.json", "data/local_version.json", "data/Perks.json", "data/Characters.json")
    match err:
        case 1:
            print("Permission refusée: Le fichier \"local_Version.json\" ne peut être supprimé")
        case 2:
            print("Une erreur est survenue lors du remplacement de \"local_Version.json\"")
        case 3:
            print("Les compétences n'ont pas pu être récupérées")
        case 4:
            print("Les personnages n'ont pas pu être récupérés")
        case _:
            print("All Ok")


    All_Perks = Init_Perks("data/Characters.json", "data/Perks.json")
    
    app = Application(All_Perks, "tkinter/icone/skull.ico", {"survivor": "tkinter/Survivor_options.txt", "killer": "tkinter/Killer_options.txt"})
    
    app.mainloop()
    

if __name__ == "__main__":
    main()