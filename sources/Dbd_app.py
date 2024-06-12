import app_setup
from Datas import Init_Perks, cool_print_dict


def main():
    All_Perks = Init_Perks()
    
    Survs_dict = {k:0 for k in All_Perks["survivors"]}
    del Survs_dict["All"]
    
    Killers_dict = {k:0 for k in All_Perks["killers"]}
    del Killers_dict["All"]
    
    app_setup.Launch_app(Survs_dict)
    
    

if __name__ == "__main__":
    main()