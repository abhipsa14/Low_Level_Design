class Animal:

    def __init__(self,name:str,age:int):
        self.name=name
        self.age=age
    def eat(self):
        print(f"{self.name} is eating.")
    def sleep(self):
        print(f"{self.name} is sleeping.")


class Dog(Animal):
    def __init__(self,name:str,age:int,breed:str):
        super().__init__(name,age)
        self.breed=breed
    def bark(self):
        print(f"{self.name} is barking.")
    def fetch(self):
        print(f"{self.name} is fetching the ball and his age is {self.age} and his breed is {self.breed}.")


d1=Dog("Buddy",3,"Golden Retriever")
d1.fetch()