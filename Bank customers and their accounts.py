class Account:
    def __init__(self, account_number, balance):
        self.account_number = account_number
        self.balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f'Deposit successful. New balance: {self.balance}')
        else:
            print(f'Negative number not allowed')

    def withdraw(self, amount):
        if amount <= 0:
            print('Enter a positive number')
        elif amount <= self.balance:
            self.balance -= amount
            print(f'Withdrawal successful. New balance: {self.balance}')
        else:
            print('Withdrawal not allowed: insufficient balance')

    def info(self):
        print(f'''Name: {self.account_number}
Balance: {self.balance}
''')


class SavingAccount(Account):
    def __init__(self, account_number, balance, interest_rate, min_balance=1000):
        super().__init__(account_number, balance)
        self.interest_rate = interest_rate
        self.min_balance = min_balance

    def withdraw(self, amount):
        if amount <= 0:
            print(f'Please enter a positive number')
        elif self.balance - amount >= self.min_balance:
            self.balance -= amount
            print(f'Withdrawal successful. New balance: {self.balance}')
        else:
            print(
                f'Withdrawal not allowed: must maintain minimum balance of {self.min_balance}')


class CurrentAccount(Account):
    def __init__(self, account_number, balance, overdraft_limit):
        super().__init__(account_number, balance)
        self.overdraft_limit = overdraft_limit

    def withdraw(self, amount):
        if amount <= 0:
            print('Enter a positive number')
        elif amount <= self.balance + self.overdraft_limit:
            self.balance -= amount
            print(f'Withdrawal successful. New balance: {self.balance}')
        else:
            print(f'Withdrawal not allowed: exceeds overdraft limit')


class Customer(Account):
    def __init__(self, account_number, balance, name, customer_id):
        super().__init__(account_number, balance)
        self.name = name
        self.customer_id = customer_id
        self.accounts = []

    def add_account(self, account):
        if account not in self.accounts:
            self.accounts.append(account)
        else:
            print(f'Account already exits')

    def show_accounts(self):
        for account in self.accounts:
            account.info()


account_types: list[Account] = [SavingAccount(123, 5000, 10),
                                CurrentAccount(123, 1000, 500),
                                Account(125, 5000)
                                ]

for bank in account_types:
    bank.withdraw(2000)
    print('*'.center(20, '-'))
    bank.info()
