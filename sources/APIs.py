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
def sauve_response(response , fichier: str = "cle_dict.json"):
    f = open(fichier, "w")
    json.dump(response, f)

#Perks : https://dbd.tricky.lol/api/perks
#Random Perks : https://dbd.tricky.lol/api/randomperks
#player adepts (succès steam) : https://dbd.tricky.lol/api/playeradepts?steamid=76561199028517504
#player stats (stats bizarre): /api/playerstats?steamid=76561199028517504
#characters : /api/characters
#Leaderboard pos : /api/leaderboardposition?steamid=76561199028517504
#Version : /api/versions

response = requests.get("https://dbd.tricky.lol/api/versions")
print(response.status_code)
if(response.status_code == 200):
    print("Un résultat :D")
    respJSON = response.json()
    
    sauve_response(respJSON, "version.json")
    for k in respJSON.keys():
        print(k)
