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
def save_response(response , fichier: str = "cle_dict.json"):
    f = open(fichier, "w")
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

if __name__ == "__main__":
    menu: int = -1
    
    while(menu<1 or menu>5):
        print("Quelle recherche ?\n\n1-Perks \n2-Maîtrise (Steam ID de TIMMATTACK) \n3-Personnages \n4-Version \n5-Non rien \nChoix : ", end="")
        menu = int(input())
    
    match menu:
        case 1:
            response = requests.get("https://dbd.tricky.lol/api/perks")
            file_name: str = "Perks.json"
        
        case 2:
            response = requests.get("https://dbd.tricky.lol/api/playeradepts?steamid=76561199028517504")
            file_name: str = "User_adepts.json"
        
        case 3:
            response = requests.get("https://dbd.tricky.lol/api/characters")
            file_name: str = "Characters.json"
        
        case 4:
            response = requests.get("https://dbd.tricky.lol/api/versions")
            file_name: str = "Versions.json"
        case _:
            print("\nOk bah rien du coup")
    
    if((menu>=1) and (menu<=4)):
        if(response.status_code == 200):
            respJSON = response.json()
    
            save_response(respJSON, file_name)
            print(f"Résultats sauvegardés dans {file_name}")
            for k in respJSON.keys():
                print(k)
        else:
            print("pas de réponse :(\n code d'erreur :", end=" ")
            print(response.status_code)
    else:
        print("Understandable, Have a nice day")