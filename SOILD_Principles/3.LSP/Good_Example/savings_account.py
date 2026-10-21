from withdrawable_account import withdrawableAccount

class SavingsAccount(withdrawableAccount):
    def __init__(self,balance):
        super().__init__(balance)
    def deposit(self,amount:int):
        self.balance+=amount
        print(f"Deposited Rs.{amount} to Savings Account. Current Balance: Rs.{self.balance}")
    def withdraw(self,amount:int):
        if(self.balance<amount):
            print("Insufficient Balance")
        else:
            self.balance-=amount
            print(f"Withdrawn Rs.{amount} from Savings Account. Current Balance: Rs.{self.balance}")
