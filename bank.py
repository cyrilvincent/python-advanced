class BankAccount:

    def __init__(self, id, owner):
        self.id = id
        self.owner = owner
        self._balance = 0

    @property
    def balance(self):
        return self._balance

    def deposit(self, amount):
        self._balance += amount

    def withdraw(self, amount):
        if amount <= self._balance:
            self._balance -= amount
            return amount
        else:
            raise ValueError("Amount > Balance")

import unittest

class BankTest(unittest.TestCase):

    def testAccount(self):
        a = BankAccount(0,None)
        self.assertEqual(0, a.balance)
        a.deposit(100)
        self.assertEqual(100, a.balance)
        a.withdraw(60)
        self.assertEqual(40, a.balance)


