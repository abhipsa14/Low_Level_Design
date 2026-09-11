from abc import ABC, abstractmethod

# Interface (the "contract")
class PaymentMethod(ABC):
    @abstractmethod
    def pay(self, amount: float) -> str:
        pass

    @abstractmethod
    def refund(self, amount: float) -> str:
        pass


# Realizations (concrete classes fulfilling the contract)
class CreditCardPayment(PaymentMethod):
    def pay(self, amount: float) -> str:
        return f"Paid ${amount} using Credit Card"

    def refund(self, amount: float) -> str:
        return f"Refunded ${amount} to Credit Card"


class PayPalPayment(PaymentMethod):
    def pay(self, amount: float) -> str:
        return f"Paid ${amount} using PayPal"

    def refund(self, amount: float) -> str:
        return f"Refunded ${amount} to PayPal balance"


# Usage
methods = [CreditCardPayment(), PayPalPayment()]
for m in methods:
    print(m.pay(100))
    print(m.refund(20))