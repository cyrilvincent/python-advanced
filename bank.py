import unittest
import datetime

class Customer:

    def __init__(self, fname, lname):
        self.lname = lname
        self.fname = fname

class Transaction:

    def __init__(self, amount, date = datetime.datetime.now()):
        self.amount = amount
        self.date = date

class BankAccount:

    count = 0

    def __init__(self, customer:Customer, balance = 0):
        self.id = BankAccount.count
        BankAccount.count += 1
        self._balance = balance
        self.customer = customer
        self.transactions = []

    def deposit(self, amount):
        self._balance += amount
        transac = Transaction(amount)
        self.transactions.append(transac)

    def withdraw(self, amount):
        if amount < self._balance:
            self._balance -= amount
            self.transactions.append(Transaction(-amount))
        else:
            raise ValueError("amount > balance")

    def __repr__(self):
        return f"BankAccount {self.balance} {self.customer.lname}"

    @property
    def balance(self):
        return self._balance

    # def getBalance(self):
    #     return self._balance

class BankAccountTest(unittest.TestCase):

    def testAccount(self):
        customer = Customer("Cyril", "Vincent")
        account = BankAccount(customer)
        self.assertEqual(0, account.balance)
        account.deposit(100)
        self.assertEqual(100, account.balance)
        account.withdraw(50)
        self.assertEqual(50, account.balance)
        account2 = BankAccount(Customer("Cyril", "Vincent"), 50)
        self.assertNotEqual(account, account2)
        print(account, account2)
        account.deposit(100)
        #<=>
        BankAccount.deposit(account, 100)

    def testId(self):
        a1 = BankAccount(Customer("Cyril", "Vincent"))
        self.assertEqual(2,a1.id)
        a2 = BankAccount(Customer("Cyril", "Vincent"))
        self.assertEqual(3, a2.id)
        print(a1)
