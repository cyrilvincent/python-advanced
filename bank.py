import datetime
from typing import *

class Transaction:

    def __init__(self, amount):
        self.amount = amount
        self.date = datetime.datetime.now()

class BankAccount:

    def __init__(self, id, owner):
        self.id = id
        self.owner = owner
        self._balance = 0
        self._transactions:List[Transaction] = []

    @property
    def balance(self):
        return self._balance

    def deposit(self, amount):
        self._balance += amount
        self._transactions.append(Transaction(amount))

    def withdraw(self, amount):
        if amount <= self._balance:
            self._balance -= amount
            self._transactions.append(Transaction(-amount))
            return amount
        else:
            raise ValueError("Amount > Balance")

    @property
    def transactions(self):
        return self._transactions

import unittest

class BankTest(unittest.TestCase):

    def testAccount(self):
        a = BankAccount(0,None)
        self.assertEqual(0, a.balance)
        a.deposit(100)
        self.assertEqual(100, a.balance)
        a.withdraw(60)
        self.assertEqual(40, a.balance)


