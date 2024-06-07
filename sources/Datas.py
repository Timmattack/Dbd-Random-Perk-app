import json

'''
# un dict pour les perks
Perks = {}

def charge_cle(cle, fichier: str = "cle_dict.json"):
    f = open(fichier, "r")
    tmp_cle: dict[chr, chr] = json.load(f)
    for i in tmp_cle.keys():
        cle[i] = tmp_cle[i]
    
charge_cle(Perks, "perks.json")

attributs = {}

for k in Perks["Ace_In_The_Hole"].keys():
    attributs[k] = 1

Perks_IDs = []
Perks_name = []

for k,v in Perks.items():
    Perks_IDs.append(k)
    Perks_name.append(v['name'])
    for vk in v.keys():
        attributs[vk] += 1

for k in attributs.keys():
    attributs[k] -= 1
'''

#print(attributs)
#print(Perks_IDs)
#print(Perks_name)

'''
IDsXNames = {}

for i in range(len(Perks_IDs)):
    IDsXNames[Perks_IDs[i]] = Perks_name[i]

for k in IDsXNames.keys():
    print("- "+k+": "+IDsXNames[k])
'''