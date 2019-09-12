class BankAccount:

    def __init__(self, id, owner):
        self.id = id
        self.owner = owner
        self._balance = 0

    def deposit(self, amount):
        if amount > 1000:
            raise ValueError("Montant non possible > 1000")
        else:
            self._balance += amount

    def withdraw(self, amount):
        if not amount > self._balance:
            self._balance -= amount
        else:
            raise ValueError("Solde dépassé")


if __name__ == '__main__':
    b1 = BankAccount(0,"Cyril")
    b1.deposit(1000)
    b1.withdraw(600)
    b1._balance += 10000000
    print(b1)


