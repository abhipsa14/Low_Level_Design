class PaymentProcessor:
    def pay(self, payment_method:str, amount:int):
        if payment_method=="UPI":
            print(f"Starting UPI Transaction of Rs.{amount}")
            print("UPI Transaction finished.")
        elif payment_method=="credit_card":
            print(f"Starting Credit Card Transaction of Rs.{amount}")
            print("Credit Card Transaction finished.")
        elif payment_method=="debit_card":
            print(f"Starting Debit Card Transaction of Rs.{amount}")
            print("Debit Card Transaction finished.")

        elif payment_method=="net_banking":
            print(f"Starting Net Banking Transaction of Rs.{amount}")
            print("Net Banking Transaction finished.")