from BankApp import BankAccount, Bank, BankUI

mybank = Bank("WallStreetBank")
myui = BankUI()
print(myui.request_chooser('2'))

while True:
    myui.print_menu(mybank.get_name())
    stay = myui.request_handling(str(input()), mybank)
    if not stay:
        break




