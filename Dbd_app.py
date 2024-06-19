from app_setup import Application
from Datas import Init_Perks, cool_print_dict


def main():
    All_Perks = Init_Perks()
    
    app = Application(All_Perks)
    
    app.mainloop()
    
    

if __name__ == "__main__":
    main()