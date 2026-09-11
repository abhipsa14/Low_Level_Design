from typing import Optional

class Engine:
    def __init__(self, engine_type, horsepower) -> None:
        self.__engine_type=engine_type
        self.__horsepwer=horsepower

    def get_details(self)->str:
        return f"{self.__engine_type} Engine ({self.__horsepwer} HP)"
    def start(self)->None:
        print(f"{self.__engine_type} engine started.")

# Car class (owns Engine - Composition)
class Car:
    def __init__(self, brand, model, engine_type, horsepower)->None:
        self.__brand:str=brand
        self.__model:str=model

        # COMPOSITION Engine is created inside car constructor
        self.__engine = Engine(engine_type,horsepower)
    def get_car_details(self)-> None:
        print(f"\n Car:{self.__brand} {self.__model}")
        print(f"Engine:{self.__engine.get_details()}")

    def start_car(self)->None:
        print(f"Starting {self.__brand}{self.__model}...")
        self.__engine.start()
        print("Car is ready to drive!")


## Creating Car objects
my_car:Car=Car("Toyota","Fortuner","Diesel",204)

## Display car details
my_car.get_car_details()

# Start the car
my_car.start_car()

# IMPORTANT: When we delete the car object is also destroyed
print("\nDeleting the car object...")
del my_car
# Car deleted, Engine also deleted automatically!

# We cannot access engine separately - it was part of the car
# Engine has no independent existence outside the Car

print("Car and its Engine are both destroyed!")