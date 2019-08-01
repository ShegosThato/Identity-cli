import os
import sys
from accounts import Account

acc = Account()

#displayed on initialization
def initial_start():
    clear_screen()
    print("Welcome to IDENTITY\n1.Add new data\n2.List all data\n3.Search for data\n4.Delete data\n5.Exit")

def clear_screen():
    os.system('cls')

#get the user option of operation
def get_user_option():
    user_opt = int(input("Select your option:\t"))
    if(user_opt ==1):
        add_new_data()
    elif (user_opt == 2):
        list_data()
    elif (user_opt ==3):
        search_data()
    elif (user_opt == 4):
        delete_data()
    else:
        print("Thank you for using system")
        input()
        sys.exit(0)
                    
#adds new data to the database
def add_new_data():
    clear_screen()
    fn = input("What's your first name?\t")
    ln = input("What's your surname?\t")
    id_num = input("Enter your ID number:\t")
    acc.set_first_name(fn)
    acc.set_last_name(ln)
    acc.set_id_number(id_num)
    acc.save_data()

def list_data():
    clear_screen()
    data = acc.list_all()
    for d in data:
        print(d)
    input()

def search_data():
    clear_screen()
    print("****** SEARCH *****\n")
    first_n = input("Enter the first name:\t")
    search_data = acc.search_firstname(first_n)
    print("\n******** Your results *******\n{}".format(str(search_data)))
    input()

def delete_data():
    clear_screen()
    print("****** DELETE ****\n")
    idnum = input('Enter the ID number:\t')    
    acc.delete_account(idnum)
    print("Account deleted")
    input()
    

#---MAIN METHOD--
def main():
    while True:
        initial_start()
        get_user_option()
    
        
if __name__ == '__main__':
    main()