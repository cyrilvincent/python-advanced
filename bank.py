import unittest

class BankAccount:

    def __init__(self, id, customer, balance = 0):
        self.id = id
        self.balance = balance
        self.customer = customer

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        if amount < self.balance:
            self.balance -= amount
        else:
            pass

class BankAccountTest(unittest.TestCase):

    def testAccount(self):
        account = BankAccount(0,"Cyril")
        self.assertEqual(0, account.balance)
        account.deposit(100)
        self.assertEqual(100, account.balance)
        account.withdraw(50)
        self.assertEqual(50, account.balance)
        account2 = BankAccount(0,"Cyril", 50)
        self.assertNotEqual(account, account2)
        print(account, account2)
        account.deposit(100)
        #<=>
        BankAccount.deposit(account, 100)