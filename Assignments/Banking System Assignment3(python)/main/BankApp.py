import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from entity.models import Customer
from dao.implementation import BankServiceProviderImpl
from exceptions.custom_exceptions import *

def main():
    bank = BankServiceProviderImpl()

    while True:
        print("\n--- Welcome to HM Bank ---")
        print("1. Create Account")
        print("2. Deposit")
        print("3. Withdraw")
        print("4. Transfer")
        print("5. Get Account Balance")
        print("6. Get Account Details")
        print("7. List All Accounts")
        print("8. Calculate Interest")
        print("9. Exit")

        choice = input("Enter your choice: ")

        try:
            if choice == '1':
                # ✅ Create Account
                customer_id = input("Enter Customer ID: ")
                fname = input("Enter First Name: ")
                lname = input("Enter Last Name: ")
                email = input("Enter Email: ")
                phone = input("Enter Phone Number: ")
                address = input("Enter Address: ")
                customer = Customer(customer_id, fname, lname, email, phone, address)

                print("Account Types: savings / current / zerobalance")
                acc_type = input("Choose Account Type: ")
                if acc_type.lower() != "zerobalance":
                    balance = float(input("Enter Initial Balance: "))
                    account = bank.create_account(customer, acc_type, balance)
                else:
                    account = bank.create_account(customer, acc_type)

                print("✅ Account created successfully.")
                print(account)

            elif choice == '2':
                # ✅ Deposit
                acc_no = int(input("Enter Account Number: "))
                amount = float(input("Enter Deposit Amount: "))
                new_balance = bank.deposit(acc_no, amount)
                print(f"✅ Deposit successful. New Balance: ${new_balance:.2f}")

            elif choice == '3':
                # ✅ Withdraw
                acc_no = int(input("Enter Account Number: "))
                amount = float(input("Enter Withdrawal Amount: "))
                new_balance = bank.withdraw(acc_no, amount)
                print(f"✅ Withdrawal successful. New Balance: ${new_balance:.2f}")

            elif choice == '4':
                # ✅ Transfer
                from_acc = int(input("Enter From Account Number: "))
                to_acc = int(input("Enter To Account Number: "))
                amount = float(input("Enter Transfer Amount: "))
                bank.transfer(from_acc, to_acc, amount)
                print("✅ Transfer successful.")

            elif choice == '5':
                # ✅ Get Account Balance
                acc_no = int(input("Enter Account Number: "))
                balance = bank.get_account_balance(acc_no)
                print(f"✅ Current Balance: ${balance:.2f}")

            elif choice == '6':
                # ✅ Get Account Details
                acc_no = int(input("Enter Account Number: "))
                acc = bank.get_account_details(acc_no)
                print("✅ Account Info:")
                print(acc)
                print(acc.get_customer())

            elif choice == '7':
                # ✅ List All Accounts
                accounts = bank.list_accounts()
                if not accounts:
                    print("No accounts found.")
                else:
                    print("✅ List of Accounts:")
                    for acc in accounts:
                        print(acc)

            elif choice == '8':
                # ✅ Calculate Interest
                bank.calculate_interest()
                print("✅ Interest calculation applied to applicable accounts.")

            elif choice == '9':
                print("✅ Thank you for banking with us!")
                break

            else:
                print("Invalid choice. Please try again.")

        except (InvalidAccountException, InsufficientFundException, OverDraftLimitExceededException, ValueError) as e:
            print("Error:", e)
        except Exception as e:
            print("Unexpected error occurred:", e)


if __name__ == "__main__":
    main()
