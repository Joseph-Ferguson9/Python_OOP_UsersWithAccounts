class BANKACCOUNT:
    def __init__(self, int_rate=0, balance=0):
        self.interest = int_rate
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        return self

    def withdraw(self, amount):
        if self.balance > amount:
            self.balance -= amount
        else:
            print("ERROR: Insufficent funds!")
        return self

    def display_account_info(self):
        return self.balance

    def yield_interest(self):
        if self.balance > 0:
            self.balance += round(self.balance*self.interest)
        else:
            print("No positive balance to calculate intrest toward.")
        return self


class USER:
    def __init__(self, username, email_address, rate, amount):
        self.name = username
        self.email = email_address
        self.account = BANKACCOUNT(rate, amount)

    def make_deposit(self, amount):
        self.account.deposit(amount)
        return self

    def make_withdrawal(self, amount):
        self.account.withdraw(amount)
        return self

    def display_user_balance(self):
        print(f"{self.name}'s current account balance is ${self.account.display_account_info()}.")

    def transfer_money(self, other_user, amount):
        other_user.account.deposit(amount)
        self.account.withdraw(amount)
        return self
    
    def monthly_interest(self):
        self.account.yield_interest()
        return self

joseph = USER("joebro", "joegferugson@gmail.com", 0.005, 1400)
joseph.display_user_balance()
joseph.make_deposit(300).display_user_balance()
joseph.make_withdrawal(500).display_user_balance()

asa = USER("cookie612", "asadog23@gmail.com", .01, 1000)
asa.display_user_balance()
asa.transfer_money(joseph, 600).display_user_balance()
joseph.display_user_balance()
asa.monthly_interest().display_user_balance()
joseph.monthly_interest().display_user_balance()
