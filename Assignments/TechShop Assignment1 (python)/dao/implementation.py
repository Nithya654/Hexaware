from util.db_conn_util import DBConnection

from dao.service import ICustomerService, IProductService, IOrderService, IInventoryService

class CustomerServiceImpl(ICustomerService):
    def __init__(self):
        self.conn = DBConnection.get_connection()

    def add_customer(self, customer):
        cursor = self.conn.cursor()
        query = "INSERT INTO Customers (CustomerID, FirstName, LastName, Email, Phone, Address) VALUES (?, ?, ?, ?, ?, ?)"
        cursor.execute(query, customer.customer_id, customer.first_name, customer.last_name, customer.email, customer.phone, customer.address)
        self.conn.commit()

    def update_customer_info(self, customer_id, email, phone, address):
        cursor = self.conn.cursor()
        query = "UPDATE Customers SET Email=?, Phone=?, Address=? WHERE CustomerID=?"
        cursor.execute(query, email, phone, address, customer_id)
        self.conn.commit()

    def get_all_customers(self):
        cursor = self.conn.cursor()
        cursor.execute("SELECT * FROM Customers")
        return cursor.fetchall()


class ProductServiceImpl(IProductService):
    def __init__(self):
        self.conn = DBConnection.get_connection()

    def add_product(self, product):
        cursor = self.conn.cursor()
        query = "INSERT INTO Products (ProductID, ProductName, Description, Price) VALUES (?, ?, ?, ?)"
        cursor.execute(query, product.product_id, product.product_name, product.description, product.price)
        self.conn.commit()

    def update_product(self, product_id, price, description):
        cursor = self.conn.cursor()
        query = "UPDATE Products SET Price=?, Description=? WHERE ProductID=?"
        cursor.execute(query, price, description, product_id)
        self.conn.commit()

    def get_all_products(self):
        cursor = self.conn.cursor()
        cursor.execute("SELECT * FROM Products")
        return cursor.fetchall()


class OrderServiceImpl(IOrderService):
    def __init__(self):
        self.conn = DBConnection.get_connection()

    def place_order(self, order):
        cursor = self.conn.cursor()
        query = "INSERT INTO Orders (OrderID, CustomerID, OrderDate, TotalAmount) VALUES (?, ?, ?, ?)"
        cursor.execute(query, order.order_id, order.customer.customer_id, order.order_date, order.total_amount)
        self.conn.commit()

    def get_order_details(self, order_id):
        cursor = self.conn.cursor()
        query = """
        SELECT o.OrderID, o.OrderDate, o.TotalAmount, c.FirstName, c.LastName
        FROM Orders o
        JOIN Customers c ON o.CustomerID = c.CustomerID
        WHERE o.OrderID = ?
        """
        cursor.execute(query, order_id)
        return cursor.fetchone()

    def update_order_status(self, order_id, status):
        cursor = self.conn.cursor()
        query = "UPDATE Orders SET Status = ? WHERE OrderID = ?"
        cursor.execute(query, status, order_id)
        self.conn.commit()


class InventoryServiceImpl(IInventoryService):
    def __init__(self):
        self.conn = DBConnection.get_connection()

    def update_inventory(self, product_id, quantity):
        cursor = self.conn.cursor()
        query = "UPDATE Inventory SET QuantityInStock = ?, LastStockUpdate = GETDATE() WHERE ProductID = ?"
        cursor.execute(query, quantity, product_id)
        self.conn.commit()

    def get_inventory_status(self):
        cursor = self.conn.cursor()
        cursor.execute("SELECT * FROM Inventory")
        return cursor.fetchall()
