class Account:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Депозит: {amount}. Новый баланс: {self.balance}")
        else:
            print("Сумма депозита должна быть положительной.")

    def withdraw(self, amount):
        if amount > 0:
            if amount <= self.balance:
                self.balance -= amount
                print(f"Снятие: {amount}. Новый баланс: {self.balance}")
            else:
                print("Ошибка: недостаточно средств для снятия.")
        else:
            print("Сумма снятия должна быть положительной.")

account = Account("Alim", 1000)
account.deposit(500)
account.withdraw(200)
account.withdraw(1500)  
account.deposit(-100)  
