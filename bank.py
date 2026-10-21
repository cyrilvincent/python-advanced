from dataclasses import dataclass


@dataclass
class Bank:

    swift: str
    name: str
    phone: str


class Account:
    """
    Docstring for Account
    """

    nb = 0

    def __init__(self, id: str, owner: str, bank: str):
        self.balance = 0.
        self.id = id
        self.owner = owner
        self.bank = bank
        Account.nb += 1

    def credit(self, amount: float):
        """
        Docstring for credit
        
        :param self: Description
        :param amount: Description
        :type amount: float
        """
        self.balance += amount

    def debit(self, amount: float):
        """
        Docstring for debit
        
        :param self: Description
        :param amount: Description
        :type amount: float
        """
        if amount <= self.balance:
            self.balance -= amount
        else:
            raise ValueError("Amount must be <= balance")

    def __del__(self):
        Account.nb -= 1

# Compter automatiquement le nombre de Account créé
# __del__(self) = destructeur
# a = Account(...)
# a = toto
# a = None
# Sortir du bloc
# del(a)

# Faire le lien Account possède 1 Bank + test
# Faire la classe Transaction : datetime, amount:float (debit < 0)
#   import datetime
#   datetime.datetime.now()
# Account possède * transactions par defaut = []
# Modifier credit et debit pour ajouter automatiquement une trasaction
# 
