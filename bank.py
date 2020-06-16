import unittest

class BankAccount:

    count = 0

    def __init__(self, customer, balance = 0):
        self.id = BankAccount.count
        BankAccount.count += 1
        self._balance = balance

    def deposit(self, amount):
        self._balance += amount

    def withdraw(self, amount):
        if amount < self._balance:
            self._balance -= amount
        else:
            pass

    @property
    def balance(self):
        return self._balance

    # def getBalance(self):
    #     return self._balance

class BankAccountTest(unittest.TestCase):

    def testAccount(self):
        account = BankAccount("Cyril")
        self.assertEqual(0, account.balance)
        account.deposit(100)
        self.assertEqual(100, account.balance)
        account.withdraw(50)
        self.assertEqual(50, account.balance)
        account2 = BankAccount("Cyril", 50)
        self.assertNotEqual(account, account2)
        print(account, account2)
        account.deposit(100)
        #<=>
        BankAccount.deposit(account, 100)

    def testId(self):
        a1 = BankAccount("")
        self.assertEqual(2,a1.id)
        a2 = BankAccount("")
        self.assertEqual(3, a2.id)
