from abc import ABC, abstractmethod


class ICustomerServiceProvider(ABC):

    @abstractmethod
    def get_account_balance(self, acc_no: int) -> float:
        pass

    @abstractmethod
    def deposit(self, acc_no: int, amount: float) -> float:
        pass

    @abstractmethod
    def withdraw(self, acc_no: int, amount: float) -> float:
        pass

    @abstractmethod
    def transfer(self, from_acc_no: int, to_acc_no: int, amount: float):
        pass

    @abstractmethod
    def get_account_details(self, acc_no: int):
        pass


class IBankServiceProvider(ICustomerServiceProvider):

    @abstractmethod
    def create_account(self, customer, acc_type: str, balance: float = 0):
        pass

    @abstractmethod
    def list_accounts(self) -> list:
        pass

    @abstractmethod
    def calculate_interest(self):
        pass

