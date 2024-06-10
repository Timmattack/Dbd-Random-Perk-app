import json

def charge_file(dict, fichier: str):
    with open(fichier, "r") as f:
        tmp_dict = json.load(f)
    for k,v in tmp_dict.items():
        dict[k] = v
    

def cool_print(dict):
    for k in dict:
        print(f"{k}: {dict[k]}")


'''
Characters
"le num du surv": {"id": "", "name": "", "role": "", "image": ".png", "perks": ["Bond", "Leader", "Prove_Thyself"]}

Perks
"le num de la perk": {"categories": [""], "name": "", "role": "", "character": int/null, "teachable": 40, "image": ".png"}
'''

def cross_Pid_Pname(dict1, dict2):
    for k in dict1:
        for i in range(3):
            dict1[k]["perks"][i] = dict2[dict1[k]["perks"][i]]["name"]


def main():
    # un dict pour les Persos X leurs perks
    Characters = {}
    charge_file(Characters, "../data/Characters.json")
    
    """
    On créé le dictionnaire des survivants avec leurs 3 compétences
        Puis celui des tueurs
    """
    Survs_X_3Perks = { k:{"name": v["name"], "perks": v["perks"]} for k,v in Characters.items() if (v["role"] == "survivor")}
    Killer_X_3Perks = { k:{"name": v["name"], "perks": v["perks"]} for k,v in Characters.items() if (v["role"] == "killer")}
    
    #cool_print(Survs_X_3Perks)
    #cool_print(Killer_X_3Perks)
    
    
    Perks = {}
    charge_file(Perks, "../data/Perks.json")
    
    Surv_null = { k:{"name": v["name"] } for k,v in Perks.items() if ((v["role"] == "survivor") and (v["character"] is None)) }
    Killer_null = { k:{"name": v["name"] } for k,v in Perks.items() if ((v["role"] == "killer") and (v["character"] is None)) }
    
    
    
    cross_Pid_Pname(Survs_X_3Perks, Perks)
    cross_Pid_Pname(Killer_X_3Perks, Perks)
    
    cool_print(Survs_X_3Perks)
    cool_print(Killer_X_3Perks)
    #cool_print(Surv_null)
    #cool_print(Killer_null)
    

if __name__ == "__main__":
    main()