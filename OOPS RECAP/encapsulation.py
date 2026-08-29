class Bank:
    def __init__(self,name:str,balance:int):
        self.name=name
        ## Private attribute
        self.__balance=balance

    ## Getter(Private attribute access kar skte hain through this method)
    def get_balance(self):
        print(f"Current Balance:{self.__balance}")

    ## Setter(Private attribute access kar skte hain through this method)
    def set_balance(self, new_amount:int):
        self.__balance=new_amount

    ## Private method
    def __isServerLive(self):
        return True

    def deposit(self,amount:int)->None:
        if not self.__isServerLive():
            print("Server is down, try after some time")
        else: 
            self.__balance+=amount
            print(f"Amount deposited, current balance={self.__balance}")

    def withdraw(self,amount:int)->None:
        if not self.__isServerLive():
            print("Server is down, try after some time")
        elif amount>self.__balance:
            print("Not enough money in bank\n")
        else:
            self.__balance-=amount
            print(f"Amount withdrawn, current balance={self.__balance}")

acc=Bank("Abhipsa",1000)
acc.deposit(7000)
acc.withdraw(2000)
