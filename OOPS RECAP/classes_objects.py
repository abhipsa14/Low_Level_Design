class Student:

    # attributes
    # we can also define attributes in a method too, with self keyword and initiate it's value in that method.
    # name=""
    # age=0
    # gender=""

    # methods
    # def set_info(self):
    #     self.name=input("Enter name:")
    #     self.age=int(input("Enter age:"))
    #     self.gender=input("Enter gender:")

    # In python, __init__() is a special method which is also called as a constructor. It is automatically called when an object of a class is created.

    def __init__(self,name:str,age:int,gender:str):
        self.name=name
        self.age=age
        self.gender=gender

    # def set_info(self):
    #     self.name="Lakan"
    #     self.age=21
    #     self.gender="Male"
    def display(self) -> None:
        print(f"Name:{self.name}")
        print(f"Age:{self.age}")
        print(f"Gender:{self.gender}")

    def get_age(self)->int:
        return self.age

## First Object
s1=Student("Jinshi",19,"Male")
# s1.set_info()
s1.display()
print(s1.get_age())

# Second object
s2=Student("Lakan",35,"Male")
s2.display()