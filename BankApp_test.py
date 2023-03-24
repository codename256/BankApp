from BankApp import BankAccount, Bank, BankUI
import os

mybank = Bank("WallStreetBank")
myui = BankUI()
# print(mybank.acc_db[0].get_owner())
print(myui.request_chooser('2'))

while True:
    myui.print_menu(mybank.get_name())
    request = myui.request_chooser(str(input()))

    if request == 'create' or request == '1':
        os.system('cls')
        mybank.add_new_acc()
        print("Account successfully created")
        print(mybank.get_last_acc())

    elif request == 'withdraw' or request == '2':
        print("Log in to you account by 1. <accnum> 2. <name>")
        searchby = str(input()).lower().lstrip().rstrip()
        print("Write the account number: ")
        accnum = str(input()).lower().lstrip().rstrip()
        if searchby == '1' or searchby == 'accnum':
            print(mybank.search_by_num(accnum))

    elif request == 'exit' or request == '5':
        break

    elif request == 'showdb' or request == '6':
        print("Password: ")
        if input() == '123123':
            print('\n'+"-"*20)
            mybank.print_the_database()
            print("-"*20, end='\n\n')
        else:
            print("Access denied")
    else:
        os.system('cls')
        print("<<< Sorry there's no such request. Try again >>>")



