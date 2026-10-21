from account import Account

class FixedDeposit(Account):
    def __init__(self,balance):
        super().__init__(balance)
    def deposit(self,amount:int):
        self.balance+=amount
        print(f"Deposited Rs.{amount} to Fixed Deposit Account. Current Balance: Rs.{self.balance}")