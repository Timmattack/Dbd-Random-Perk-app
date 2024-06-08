#pip install requests
import requests
import json
import string

'''
https://dbd.tricky.lol/apidocs

response = requests.get("https://dbd.tricky.lol/api/perks")
print(response.status_code)
if(response.status_code == 200):
    print(response.json())
'''
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

#Vérifie le statut de la requête, et sauvegarde si les statut le permet
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

def get_version(save_json: str = "../data/Version.json") -> bool:
    response = requests.get("https://dbd.tricky.lol/api/versions")
    return check_and_save(response, save_json)



def main():
    menu: int = -1
    
    while(menu<1 or menu>5):
        print("Quelle recherche ?\n\n1-Perks \n2-Maîtrise (Steam ID de TIMMATTACK) \n3-Personnages \n4-Version \n5-Non rien \nChoix : ", end="")
        menu = int(input())
    
    match menu:
        case 1:
            b = get_perks()
            
        case 2:
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