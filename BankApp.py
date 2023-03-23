class BankAccount:
    def __init__(self, acc_num, balance, owner, pswd):
        self._acc_num = acc_num
        self._balance = balance
        self._owner = owner
        self.__pass = pswd

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

    def add_new_acc(self):
        # create some user interface and input() to create some simple UI
        print("Enter the new account number: ", end='')
        num = int(input())
        print("Set the balance to: ", end='')
        bal = int(input())
        print("Enter the holder name: ", end='')
        nam = str(input())
        print("Enter the password: ", end='')
        __pswd = str(input()).lower().lstrip().rstrip()
        temp_obj = BankAccount(num, bal, nam, __pswd)
        self.acc_db.append(temp_obj)

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
    pass
