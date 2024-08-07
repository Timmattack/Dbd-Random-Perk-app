import pyautogui as ag
import pygetwindow as gw
import time

# True si Dbd est "présent" dans la barre de tâche
def is_dbd_on() -> bool:
    All_Titles = gw.getAllTitles()
    if 'DeadByDaylight  ' in All_Titles:
        return True
    else:
        return False

# Met Dbd au premier plan
def open_Dbd() -> int:    
    window = gw.getWindowsWithTitle('DeadByDaylight')[0]

    if window:
        window.activate()
        return 0
    else:
        return -1

#Parce que le jeu pue le zgeg, on va déplacer la souris, puis cliquer
#Sinon, le résultat n'est pas celui qu'on attend
def click_it():
    time.sleep(0.2)
    ag.click()
    time.sleep(0.5)
    
# Clique sur la fenêtre menant aux compétences
def click_perks_window():
    ag.moveTo(141, 230)
    click_it()

# Clique sur le i-ème slot de perk
def click_perk_slot_i(i: int):
    ag.moveTo(394 + 166*i, 410)
    click_it()

# Clique sur la barre de recherche
def click_search_bar():
    ag.moveTo(x=872, y=523)
    click_it()

# écrit le nom de la compétence
def type_perk(perk: str):
    ag.write(perk)
    time.sleep(0.25)
    ag.press('enter')

# Clique sur la première compétence trouvée
def click_first_found_perk():
    ag.moveTo(x=383, y=609)
    click_it()

# équipe la compétence dans le slot i
def equip_perk_i(i: int, perk: str):
    click_perk_slot_i(i)

    click_search_bar()

    type_perk(perk)
    
    click_first_found_perk()

# équipe les 4 compétences dans le jeu
def do_the_thing(perks_array: list):
    
    try:
        open_Dbd()
        time.sleep(1)
        
        click_perks_window()
        time.sleep(1)
        
        
        for i, perk in enumerate(perks_array):
            equip_perk_i(i, perk)
    except KeyboardInterrupt:
        print("arrêt de la procédure")
    except Exception:
        print(f"{Exception = }")


def main():
    
    if not is_dbd_on():
        print("Dbd n'est pas ouvert")
    else:
        print("Ctrl-C pour arrêtter")
        
        do_the_thing(["Balanced landing", "Deja vu", "Botany knowledge", "Bond"])



    
if __name__ == "__main__":
    main()
