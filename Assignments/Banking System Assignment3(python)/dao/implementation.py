from dao.interfaces import IBankServiceProvider
from entity.models import SavingsAccount, CurrentAccount, ZeroBalanceAccount
from exceptions.custom_exceptions import *
from typing import List


class BankServiceProviderImpl(IBankServiceProvider):
    def __init__(self):
        self.accounts = []

    def create_account(self, customer, acc_type: str, balance: float = 0):
        acc_type = acc_type.lower()
        if acc_type == "savings":
            account = SavingsAccount(customer, balance)
        elif acc_type == "current":
            account = CurrentAccount(customer, balance)
        elif acc_type == "zerobalance":
            account = ZeroBalanceAccount(customer)
        else:
            raise ValueError("Invalid account type.")
        self.accounts.append(account)
        return account

    def get_account_by_no(self, acc_no: int):
        for acc in self.accounts:
            if acc.get_account_number() == acc_no:
                return acc
        raise InvalidAccountException("Account not found.")

    def get_account_balance(self, acc_no: int) -> float:
        acc = self.get_account_by_no(acc_no)
        return acc.get_balance()

    def deposit(self, acc_no: int, amount: float) -> float:
        acc = self.get_account_by_no(acc_no)
        return acc.deposit(amount)

    def withdraw(self, acc_no: int, amount: float) -> float:
        acc = self.get_account_by_no(acc_no)
        try:
            return acc.withdraw(amount)
        except ValueError as ve:
            raise InsufficientFundException(str(ve))

    def transfer(self, from_acc_no: int, to_acc_no: int, amount: float):
        from_acc = self.get_account_by_no(from_acc_no)
        to_acc = self.get_account_by_no(to_acc_no)
        self.withdraw(from_acc_no, amount)
        self.deposit(to_acc_no, amount)

    def get_account_details(self, acc_no: int):
        acc = self.get_account_by_no(acc_no)
        return acc

    def list_accounts(self) -> List:
        return self.accounts

    def calculate_interest(self):
        for acc in self.accounts:
            acc.calculate_interest()
