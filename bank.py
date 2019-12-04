class BankAccount:

    _counter = 0

    def __init__(self, owner):
        self.id = BankAccount._counter
        BankAccount._counter += 1
        self.owner = owner
        self._balance = 0

    @property
    def balance(self):
        return self._balance

    def deposit(self, amount):
        if amount > 0:
            self._balance += amount
        else:
            raise ValueError("Bad amount")

    def withdraw(self, amount):
        if amount < self._balance:
            self._balance -= amount
            return amount
        else:
            return 0

    def __repr__(self):
        return f"Account owner: {self.owner} balance: {self.balance}"

    # def __del__(self):
    #     if self.balance != 0:
    #         raise ValueError("Bad balance")

class BankAccountWithInterest(BankAccount):

    def __init__(self, owner, interestRate):
        super().__init__(owner)
        self.interestRate = interestRate

    def computeInterest(self):
        return self.balance * self.interestRate

    def creditInterest(self):
        self.balance += self.computeInterest()

import unittest
class BankAccountTest(unittest.TestCase):

    def testCreate(self):
        account = BankAccount("Cyril")
        self.assertEqual(0, account._balance)
        print(account)

    def testDeposit(self):
        account = BankAccount("Cyril")
        account.deposit(100)
        self.assertEqual(100, account._balance)
        with self.assertRaises(ValueError):
            account.deposit(-50)
        print(account.__dict__)

    def testWithdraw(self):
        account = BankAccount("Cyril")
        account.deposit(100)
        amount = account.withdraw(70)
        self.assertEqual(30, account.balance)
        self.assertEqual(70, amount)
        amount = account.withdraw(40)
        self.assertEqual(30, account.balance)
        self.assertEqual(0, amount)
        account._balance += 100000000

    def testInterest(self):
        account = BankAccountWithInterest("Cyril", 0.05)
        account.deposit(100)
        self.assertEqual(5, account.computeInterest())

    def testSale(self):
        account = BankAccount(None)
        account.__dict__ = {'id': 1, 'owner': 'Cyril', '_balance': 100}
        self.assertEqual("Cyril", account.owner)


