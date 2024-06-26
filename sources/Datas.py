import json

def charge_file(json_dict: dict, fichier: str):
    with open(fichier, "r") as f:
        tmp_dict = json.load(f)
    
    json_dict.update(tmp_dict)
    

def cool_print_dict(dict):
    for k in dict:
        print(f"{k}: {dict[k]}")


'''
Characters
"le num du surv": {"id": "", "name": "", "role": "", "image": ".png", "perks": ["Bond", "Leader", "Prove_Thyself"]}

Perks
"le num de la perk": {"categories": [""], "name": "", "role": "", "character": int/null, "teachable": 40, "image": ".png"}
'''

"""
Pour chaque identifiant de fonction, on retrouve son nom
"""
def cross_id_name(dict1, dict2):
    for k in dict1:
        for i in range(3):
            dict1[k][i] = dict2[dict1[k][i]]["name"]

"""
Créé un dictionnaire contenant les compétences de chaque survivants, et chaque tueurs
    Informations extraites de "Characters.json" et "Perks.json"
"""
def Init_Perks():
    
    Surv_Perks: dict = {}
    Killer_Perks: dict = {}
    
    # un dict pour les Persos: leurs perks
    Characters: dict = {}
    charge_file(Characters, "../data/Characters.json")
    
    
    #On créé le dictionnaire des survivants avec leurs 3 compétences
    #   Puis celui des tueurs
    Surv_Perks = { v["name"]: v["perks"] for k,v in Characters.items() if (v["role"] == "survivor")}
    Killer_Perks = { v["name"]: v["perks"] for k,v in Characters.items() if (v["role"] == "killer")}
    
    Perks = {}
    charge_file(Perks, "../data/Perks.json")
    
    
    #Certaines compétences ne sont pas nomées correctement, On va chercher leurs noms dans 'Perks.json' et les remplacers
    cross_id_name(Surv_Perks, Perks)
    cross_id_name(Killer_Perks, Perks)
    
    #On créé les listes des perks que tt le monde possède
    Surv_null = [ v["name"] for k,v in Perks.items() if ((v["role"] == "survivor") and (v["character"] is None)) ]
    Killer_null = [ v["name"] for k,v in Perks.items() if ((v["role"] == "killer") and (v["character"] is None)) ]
    
    #On ajoute les compétences communes à tout les personnages
    Surv_Perks["All"] = Surv_null
    Killer_Perks["All"] = Killer_null
    
    return {"survivors": Surv_Perks, "killers": Killer_Perks}


def main():
    
    
    print("Initialisation des compétences")
    All_Perks: dict = Init_Perks()
    
    print("\nSurv perks : \n\n")
    cool_print_dict(All_Perks["survivors"])
    print("\nKiller perks : \n\n")
    cool_print_dict(All_Perks["killers"])
    
    
    

if __name__ == "__main__":
    main()