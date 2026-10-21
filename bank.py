class Account:
    """
    Docstring for Account
    """

    def __init__(self, id: str, owner: str, bank: str):
        self.balance = 0.
        self.id = id
        self.owner = owner
        self.bank = bank

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
    
