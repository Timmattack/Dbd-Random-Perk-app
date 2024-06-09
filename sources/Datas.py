import json

def charge_file(cle, fichier: str = "cle_dict.json"):
    f = open(fichier, "r")
    tmp_cle: dict[chr, chr] = json.load(f)
    for i in tmp_cle.keys():
        cle[i] = tmp_cle[i]


#print(attributs)

'''
IDsXNames = {}

for i in range(len(Perks_IDs)):
    IDsXNames[Perks_IDs[i]] = Perks_name[i]

for k in IDsXNames.keys():
    print("- "+k+": "+IDsXNames[k])
'''

def main():
    # un dict pour les perks
    Perks = {}
    charge_file(Perks, "perks.json")
    

if __name__ == "__main__":
    main()