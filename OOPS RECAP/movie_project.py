class Movie:
    def __init__(self,movie_name:str,total_seats:int,ticket_price:int,booked_seats:int=0):
        self.movie_name=movie_name
        self.total_seats=total_seats
        self.ticket_price=ticket_price
        self.booked_seats=booked_seats

    def book_tickets(self,num_of_tickets:int)->None:
        if self.booked_seats+num_of_tickets>self.total_seats:
            print("Sorry! Not enough seats available.")
        else:
            self.booked_seats+=num_of_tickets
            print(f"{num_of_tickets} tickets booked successfully for {self.movie_name}.")
    def show_status(self)->None:
        print(f"Movie Name:{self.movie_name}")
        print(f"Total Seats:{self.total_seats}")
        print(f"Booked Seats:{self.booked_seats}")
        print(f"Available Seats:{self.total_seats-self.booked_seats}")

m1= Movie("Inception",100,80,20)
m1.show_status()
m1.book_tickets(10)
m1.show_status()