#pip install requests
import requests
import json
import string
import os

'''
https://dbd.tricky.lol/apidocs

response = requests.get("https://dbd.tricky.lol/api/perks")
print(response.status_code)
if(response.status_code == 200):
    print(response.json())
'''

def charge_file(json_dict: dict, fichier: str):
    with open(fichier, "r") as f:
        tmp_dict = json.load(f)
    
    json_dict.update(tmp_dict)


def save_response(response , fichier: str = "file.json"):
    with open(fichier, "w") as f:
        json.dump(response, f)


# Recherches guez
#Random Perks : https://dbd.tricky.lol/api/randomperks
#player stats (stats bizarre): /api/playerstats?steamid=76561199028517504
#Leaderboard pos : /api/leaderboardposition?steamid=76561199028517504

#Recherches intéressantes
#Perks : https://dbd.tricky.lol/api/perks
#player adepts (succès steam) : https://dbd.tricky.lol/api/playeradepts?steamid=76561199028517504
#characters : /api/characters
#Version : /api/versions

#Vérifie le statut de la requête, et sauvegarde si le statut le permet
def check_and_save(response, save_json: str) -> bool:
    if(response.status_code != 200):
        return False
    else:
        respJSON = response.json()
        save_response(respJSON, save_json)
        return True
    

# Sauvegarde dans un json le résultat de la requête
# Renvoie Faux si il n'y a pas de réponse
def get_perks(save_json: str = "../data/Perks.json") -> bool:
    response = requests.get("https://dbd.tricky.lol/api/perks")
    return check_and_save(response, save_json)

def get_user_adepts(save_json: str = "../data/User_adepts.json", id: str = "76561199028517504") -> bool:
    response = requests.get(f"https://dbd.tricky.lol/api/playeradepts?steamid={id}")
    return check_and_save(response, save_json)

def get_characters(save_json: str = "../data/Characters.json") -> bool:
    response = requests.get("https://dbd.tricky.lol/api/characters")
    return check_and_save(response, save_json)

def get_version(save_json: str = "../data/live_Version.json") -> bool:
    response = requests.get("https://dbd.tricky.lol/api/versions")
    return check_and_save(response, save_json)



def is_different_live_version(local_version_path: str = "../data/local_Version.json", live_version_path: str = "../data/live_Version.json") -> bool:
    local_version: dict = {}
    live_version: dict = {}
    
    charge_file(local_version, local_version_path)
    charge_file(live_version, live_version_path)
    
    return (local_version["perks"]["version"] != live_version["perks"]["version"])

def update_all_data(live_version_path: str = "../data/live_Version.json", 
                    local_version_path: str = "../data/local_Version.json", 
                    perks_path: str = "../data/Perks.json", 
                    characters_path: str = "../data/Characters.json") -> int:
    
    get_version(live_version_path)
    
    if(is_different_live_version(local_version_path, live_version_path)):
        try:
            os.remove(local_version_path)
        except PermissionError:
            return 1
        except Exception as e:
            return 2
        
        os.rename(live_version_path, local_version_path)
        
        if(not get_perks(perks_path)):
            return 3
        if(not get_characters(characters_path)):
            return 4
    
    return 0










def main():
    #print(update_all_data())

    menu: int = -1
    
    while(menu<1 or menu>5):
        print("Quelle recherche ?\n\n1-Perks \n2-Maîtrise (Steam ID de TIMMATTACK) \n3-Personnages \n4-Version \n5-Non rien \nChoix : ", end="")
        menu = int(input())
    
    match menu:
        case 1:
            b = get_perks()
            
        case 2:
    #Bjoureeeee: "76561199024311024"
    #Turtle: "76561198872214345"
    #Miel: "76561198365338996"
    #Niglomancien: "76561199008900338"
            b = get_user_adepts()
            
        case 3:
            b = get_characters()
        
        case 4:
            b = get_version()
            
        case _:
            print("Understandable, Have a nice day")
            b = True

    if(b):
        print("Ok")
    else:
        print("Nok")


if __name__ == "__main__":
    main()