from abc import ABC, abstractmethod
from entity.models import Customers, Products, Orders, Inventory


class ICustomerService(ABC):
    @abstractmethod
    def add_customer(self, customer: Customers): pass

    @abstractmethod
    def update_customer_info(self, customer_id, email, phone, address): pass

    @abstractmethod
    def get_all_customers(self): pass


class IProductService(ABC):
    @abstractmethod
    def add_product(self, product: Products): pass

    @abstractmethod
    def update_product(self, product_id, price, description): pass

    @abstractmethod
    def get_all_products(self): pass


class IOrderService(ABC):
    @abstractmethod
    def place_order(self, order: Orders): pass

    @abstractmethod
    def get_order_details(self, order_id): pass

    @abstractmethod
    def update_order_status(self, order_id, status): pass


class IInventoryService(ABC):
    @abstractmethod
    def update_inventory(self, product_id, quantity): pass

    @abstractmethod
    def get_inventory_status(self): pass
