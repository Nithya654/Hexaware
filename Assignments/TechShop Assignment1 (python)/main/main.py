import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from dao.implementation import CustomerServiceImpl, ProductServiceImpl, OrderServiceImpl, InventoryServiceImpl
from entity.models import Customers, Products, Orders
from datetime import datetime
from util.db_conn_util import DBConnection

def main():
    customer_service = CustomerServiceImpl()
    product_service = ProductServiceImpl()
    order_service = OrderServiceImpl()
    inventory_service = InventoryServiceImpl()

    while True:
        print("\n===   TechShop Main Menu ===")
        print("1. Add Customer")
        print("2. Add Product")
        print("3. Place Order")
        print("4. Update Inventory")
        print("5. View All Customers")
        print("6. View All Products")
        print("7. View Order Details")
        print("8. View Inventory")
        print("9. Exit")

        choice = input("Enter your choice: ")

        try:
            if choice == "1":
                customer = Customers(
                    int(input("Customer ID: ")),
                    input("First Name: "),
                    input("Last Name: "),
                    input("Email: "),
                    input("Phone: "),
                    input("Address: ")
                )
                customer_service.add_customer(customer)
                print("✅ Customer added successfully.")

            elif choice == "2":
                product = Products(
                    int(input("Product ID: ")),
                    input("Product Name: "),
                    input("Description: "),
                    float(input("Price: "))
                )
                product_service.add_product(product)
                print("✅ Product added successfully.")

            elif choice == "3":
                order = Orders(
                    int(input("Order ID: ")),
                    Customers(int(input("Customer ID: ")), "", "", "", "", ""),
                    datetime.now(),
                    float(input("Total Amount: ")),
                    "Processing"
                )
                order_service.place_order(order)
                print("✅ Order placed.")

            elif choice == "4":
                pid = int(input("Product ID: "))
                qty = int(input("Quantity to update: "))
                inventory_service.update_inventory(pid, qty)
                print("✅ Inventory updated.")

            elif choice == "5":
                customers = customer_service.get_all_customers()
                for c in customers:
                    print(c)

            elif choice == "6":
                products = product_service.get_all_products()
                for p in products:
                    print(p)

            elif choice == "7":
                order_id = int(input("Enter Order ID: "))
                result = order_service.get_order_details(order_id)
                if result:
                    print("\nOrder ID:", result[0])
                    print("Order Date:", result[1])
                    print("Total Amount:", result[2])
                    print("Customer Name:", result[3], result[4])
                else:
                    print("❌ Order not found.")

            elif choice == "8":
                inventory = inventory_service.get_inventory_status()
                for i in inventory:
                    print(i)

            elif choice == "9":
                print(" Thank you for using TechShop!")
                break

            else:
                print(" ❌Invalid choice. Please try again.")

        except Exception as e:
            print("❌ Error:", e)

if __name__ == "__main__":
    main()

