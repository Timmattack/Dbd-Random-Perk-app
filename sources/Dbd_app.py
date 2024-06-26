
from APIs import update_all_data
from app_setup import Application
from Datas import Init_Perks, cool_print_dict


def main():
    
    err: int = update_all_data()
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
        
        
    All_Perks = Init_Perks()
    
    app = Application(All_Perks)
    
    app.mainloop()
    

if __name__ == "__main__":
    main()