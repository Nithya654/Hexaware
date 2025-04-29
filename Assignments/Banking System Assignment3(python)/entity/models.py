from abc import ABC, abstractmethod
import re


class Customer:
    def __init__(self, customer_id, first_name, last_name, email, phone, address):
        if not re.match(r"[^@]+@[^@]+\.[^@]+", email):
            raise ValueError("Invalid email address.")
        if not re.match(r"^\d{10}$", phone):
            raise ValueError("Phone number must be 10 digits.")
        
        self._customer_id = customer_id
        self._first_name = first_name
        self._last_name = last_name
        self._email = email
        self._phone = phone
        self._address = address

    def __str__(self):
        return f"{self._first_name} {self._last_name} | Email: {self._email} | Phone: {self._phone}"


class BankAccount(ABC):
    _last_acc_no = 1000

    def __init__(self, customer, acc_type, balance):
        BankAccount._last_acc_no += 1
        self._account_number = BankAccount._last_acc_no
        self._customer = customer
        self._account_type = acc_type
        self._balance = balance

    def get_account_number(self):
        return self._account_number

    def get_balance(self):
        return self._balance

    def get_customer(self):
        return self._customer

    def deposit(self, amount):
        if amount <= 0:
            raise ValueError("Deposit amount must be positive.")
        self._balance += amount
        return self._balance

    @abstractmethod
    def withdraw(self, amount):
        pass

    @abstractmethod
    def calculate_interest(self):
        pass

    def __str__(self):
        return f"Account[{self._account_number}] - {self._account_type} - Balance: ${self._balance:.2f}"


class SavingsAccount(BankAccount):
    INTEREST_RATE = 0.045
    MIN_BALANCE = 500

    def __init__(self, customer, balance):
        if balance < SavingsAccount.MIN_BALANCE:
            raise ValueError("Savings Account requires a minimum balance of $500.")
        super().__init__(customer, "Savings", balance)

    def withdraw(self, amount):
        if amount > self._balance - SavingsAccount.MIN_BALANCE:
            raise ValueError("Insufficient funds after maintaining minimum balance.")
        self._balance -= amount
        return self._balance

    def calculate_interest(self):
        interest = self._balance * SavingsAccount.INTEREST_RATE
        self._balance += interest
        return interest


class CurrentAccount(BankAccount):
    OVERDRAFT_LIMIT = 1000

    def __init__(self, customer, balance):
        super().__init__(customer, "Current", balance)

    def withdraw(self, amount):
        if amount > self._balance + CurrentAccount.OVERDRAFT_LIMIT:
            raise ValueError("Withdrawal exceeds overdraft limit.")
        self._balance -= amount
        return self._balance

    def calculate_interest(self):
        return 0  # No interest for current accounts


class ZeroBalanceAccount(BankAccount):
    def __init__(self, customer):
        super().__init__(customer, "ZeroBalance", 0)

    def withdraw(self, amount):
        if amount > self._balance:
            raise ValueError("Insufficient funds in ZeroBalance account.")
        self._balance -= amount
        return self._balance

    def calculate_interest(self):
        return 0  

