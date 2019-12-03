class BankAccount:

    def __init__(self, id, owner):
        self.id = id
        self.owner = owner
        self.balance = 0

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
        else:
            raise ValueError("Bad amount")

    def withdraw(self, amount):
        if amount < self.balance:
            self.balance -= amount
            return amount
        else:
            return 0

    # def __del__(self):
    #     if self.balance != 0:
    #         raise ValueError("Bad balance")

import unittest
class BankAccountTest(unittest.TestCase):

    def testCreate(self):
        account = BankAccount(1,"Cyril")
        self.assertEqual(0, account.balance)

    def testDeposit(self):
        account = BankAccount(1, "Cyril")
        account.deposit(100)
        self.assertEqual(100, account.balance)
        with self.assertRaises(ValueError):
            account.deposit(-50)

    def testWithdraw(self):
        account = BankAccount(1, "Cyril")
        account.deposit(100)
        amount = account.withdraw(70)
        self.assertEqual(30, account.balance)
        self.assertEqual(70, amount)
        amount = account.withdraw(40)
        self.assertEqual(30, account.balance)
        self.assertEqual(0, amount)

