import re
class BankAccount:
    def __init__(self, acc_num, balance, owner, pswd):
        self._acc_num = acc_num
        self._balance = balance
        self._owner = owner
        self._pswd = pswd

    def __repr__(self):
        return f'Account number: {self._acc_num}, Balance: {self._balance}, Owner: {self._owner}'

    def __str__(self):
        return f'Account number: {self._acc_num}, Balance: {self._balance}, Owner: {self._owner}'

    def get_num(self):
        return self._acc_num

    def get_balance(self):
        return self._balance

    def get_owner(self):
        return self._owner

    def deposit(self, value):
        self._balance += value

    def withdraw(self, value):
        self._balance -= value


class Bank:
    def __init__(self, name):
        self.bank_name = name
        self.acc_db = []

    @staticmethod
    def _input_w_regex(self, regex, message):
        while True:
            val = input()
            if re.match(regex, val):
                return val
            else:
                print(message)

    def add_new_acc(self):
        reg_numbers = r'^\d+$'
        reg_names = r'^[a-zA-Z]+[ ]?[a-zA-Z]*$'

        print("Enter the new account number: ", end='')
        num = self._input_w_regex(self, reg_numbers, "Only digits in the account number! Try again.")

        print("Set the balance to: ", end='')
        bal = self._input_w_regex(self, reg_numbers, "Only digits in the balance value! Try again.")

        print("Enter the holder name (first name, last name): ", end='')
        nam = self._input_w_regex(self, reg_names, "First name, last name, only letters! Try again.")

        print("Enter the password: ", end='')
        _pswd = str(input())

        temp_obj = BankAccount(num, bal, nam, _pswd)
        self.acc_db.append(temp_obj)
        del temp_obj

    def take_acc_from_db(self):
        pass

    def file_to_db(self):
        pass

    def remove_acc(self):
        pass

    def search_by_num(self, num):
        for acc in self.acc_db:
            if num == acc.get_num():
                return acc

    def search_by_name(self):
        pass

    def get_last_acc(self):
        return self.acc_db[-1]

    def print_the_database(self):
        for acc in self.acc_db:
            print(acc)

    def get_name(self):
        return self.bank_name


class BankUI:
    all_requests = (
        (1, 'create', '1'),
        (2, 'withdraw', '2'),
        (3, 'deposit', '3'),
        (4, 'delete', '4'),
        (5, 'exit', '5'),
        (6, 'showdb', '6')
    )

    def __init__(self):
        pass

    def print_menu(self, bank):
        print("Hello, welcome in our Bank {bank_name}".format(bank_name=bank))
        print("What would you like to do?: \n"
              "1. <create> an account \n"
              "2. <withdraw> \n"
              "3. <deposit> \n"
              "4. <delete> \n"
              "5. <exit> \n"
              "6. <showdb>", end='\n')

    def request_chooser(self, request):
        switch_case = str(request).lower().lstrip().rstrip()
        for req in self.all_requests:
            if switch_case == req[2]:
                return switch_case
        else:
            print("No such request.")

    def req_create(self):
        pass

    def req_withdraw(self):
        pass





