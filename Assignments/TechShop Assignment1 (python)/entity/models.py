class Customers:
    def __init__(self, customer_id, first_name, last_name, email, phone, address):
        self.__customer_id = customer_id
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.phone = phone
        self.address = address

    @property
    def customer_id(self):
        return self.__customer_id

    @property
    def full_name(self):
        return f"{self.first_name} {self.last_name}"

    def calculate_total_orders(self, orders):
        return len([order for order in orders if order.customer.customer_id == self.__customer_id])

    def get_customer_details(self):
        return f"Customer ID: {self.customer_id}, Name: {self.full_name}, Email: {self.email}, Phone: {self.phone}, Address: {self.address}"

    def update_customer_info(self, email=None, phone=None, address=None):
        if email:
            self.email = email
        if phone:
            self.phone = phone
        if address:
            self.address = address


#products
class Products:
    def __init__(self, product_id, product_name, description, price):
        self.__product_id = product_id
        self.product_name = product_name
        self.description = description
        self.price = price

    @property
    def product_id(self):
        return self.__product_id

    def get_product_details(self):
        return f"Product ID: {self.product_id}, Name: {self.product_name}, Price: {self.price}, Description: {self.description}"

    def update_product_info(self, description=None, price=None):
        if description:
            self.description = description
        if price is not None and price >= 0:
            self.price = price

    def is_product_in_stock(self, inventory):
        return inventory.get_quantity_in_stock() > 0

#orders
from datetime import datetime

class Orders:
    def __init__(self, order_id, customer, order_date=None, total_amount=0.0, status='Processing'):
        self.__order_id = order_id
        self.customer = customer  # Composition with Customers
        self.order_date = order_date or datetime.now()
        self.total_amount = total_amount
        self.status = status

    @property
    def order_id(self):
        return self.__order_id

    def calculate_total_amount(self, order_details):
        self.total_amount = sum(od.calculate_subtotal() for od in order_details if od.order.order_id == self.__order_id)
        return self.total_amount

    def get_order_details(self, order_details):
        return [od.get_order_detail_info() for od in order_details if od.order.order_id == self.__order_id]

    def update_order_status(self, new_status):
        self.status = new_status

    def cancel_order(self, inventory, order_details):
        for od in order_details:
            if od.order.order_id == self.__order_id:
                inventory.add_to_inventory(od.product.product_id, od.quantity)
        self.status = 'Cancelled'

#orderdetails
class OrderDetails:
    def __init__(self, order_detail_id, order, product, quantity):
        self.__order_detail_id = order_detail_id
        self.order = order  # Composition with Orders
        self.product = product  # Composition with Products
        self.quantity = quantity
        self.discount = 0

    @property
    def order_detail_id(self):
        return self.__order_detail_id

    def calculate_subtotal(self):
        return self.quantity * self.product.price * (1 - self.discount)

    def get_order_detail_info(self):
        return f"OrderDetailID: {self.order_detail_id}, Product: {self.product.product_name}, Quantity: {self.quantity}, Subtotal: {self.calculate_subtotal()}"

    def update_quantity(self, new_quantity):
        if new_quantity > 0:
            self.quantity = new_quantity

    def add_discount(self, discount):
        if 0 <= discount < 1:
            self.discount = discount

#inventory
from datetime import datetime

class Inventory:
    def __init__(self, inventory_id, product: Products, quantity_in_stock: int, last_stock_update=None):
        self.__inventory_id = inventory_id
        self.product = product  # Composition: Product object
        self.quantity_in_stock = quantity_in_stock
        self.last_stock_update = last_stock_update or datetime.now()

    @property
    def inventory_id(self):
        return self.__inventory_id

    def get_product(self):
        return self.product

    def get_quantity_in_stock(self):
        return self.quantity_in_stock

    def add_to_inventory(self, quantity):
        if quantity > 0:
            self.quantity_in_stock += quantity
            self.last_stock_update = datetime.now()

    def remove_from_inventory(self, quantity):
        if quantity > 0 and quantity <= self.quantity_in_stock:
            self.quantity_in_stock -= quantity
            self.last_stock_update = datetime.now()
        else:
            raise Exception("InsufficientStockException: Not enough stock available.")

    def update_stock_quantity(self, new_quantity):
        if new_quantity >= 0:
            self.quantity_in_stock = new_quantity
            self.last_stock_update = datetime.now()

    def is_product_available(self, quantity_to_check):
        return self.quantity_in_stock >= quantity_to_check

    def get_inventory_value(self):
        return self.product.price * self.quantity_in_stock

    def __str__(self):
        return f"Inventory ID: {self.inventory_id}, Product: {self.product.product_name}, In Stock: {self.quantity_in_stock}, Last Updated: {self.last_stock_update.strftime('%Y-%m-%d %H:%M:%S')}"
