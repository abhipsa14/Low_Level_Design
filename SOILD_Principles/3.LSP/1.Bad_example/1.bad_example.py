from abc import ABC, abstractmethod

class BankAccount(ABC):
    def __init__(self,balance:int):
        self.balance:int =balance

    @abstractmethod
    def withdraw(self):
        pass
    @abstractmethod
    def deposit(self):
        pass

class SavingsAccount(BankAccount):
    def __init__(self, balance):
        super().__init__(balance)

    def withdraw(self,amount:int):
        if self.balance<amount:
            print("Insufficient Balance")
        else:
            self.balance-=amount
            print(f"Withdrawn Rs.{amount} from Savings Account. Current Balance: Rs.{self.balance}")
    def deposit(self,amount:int):
        self.balance+=amount
        print(f"Deposited Rs.{amount} to Savings Account. Current Balance: Rs.{self.balance}")



class FixedDepositAccount(BankAccount):
    def __init__(self, balance):
        super().__init__(balance)

    def withdraw(self,amount:int):
       raise Exception("Withdrawals are not allowed from Fixed Deposit Account before maturity.")
    
    def deposit(self,amount:int):
        self.balance+=amount
        print(f"Deposited Rs.{amount} to Fixed Deposit Account. Current Balance: Rs.{self.balance}")


s=SavingsAccount(1000)
s.withdraw(500)
s.deposit(2000)

fd=FixedDepositAccount(5000)
fd.deposit(2000)
fd.withdraw(1000)  # This will raise an exception since withdrawals are not allowed from Fixed Deposit Account before maturity.