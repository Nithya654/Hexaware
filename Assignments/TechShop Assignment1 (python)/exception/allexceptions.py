from exception.allexceptions import InvalidDataException, InsufficientStockException


# 1. InvalidDataException – for input validation (e.g. invalid email)
class InvalidDataException(Exception):
    def __init__(self, message="Invalid input data"):
        super().__init__(message)

# Email validation
def register_customer(email):
    if '@' not in email:
        raise InvalidDataException("Please enter a valid email address.")

# Inventory check
def sell_product(inventory, qty):
    if inventory.quantity_in_stock < qty:
        raise InsufficientStockException("Stock too low to fulfill order.")


# 2. InsufficientStockException – when quantity requested > stock
class InsufficientStockException(Exception):
    def __init__(self, message="Not enough stock available"):
        super().__init__(message)

# Email validation
def register_customer(email):
    if '@' not in email:
        raise InvalidDataException("Please enter a valid email address.")

# Inventory check
def sell_product(inventory, qty):
    if inventory.quantity_in_stock < qty:
        raise InsufficientStockException("Stock too low to fulfill order.")


# 3. IncompleteOrderException – when product/order details are missing
class IncompleteOrderException(Exception):
    def __init__(self, message="Order detail is incomplete or missing"):
        super().__init__(message)

# 4. PaymentFailedException – for failed or declined payments
class PaymentFailedException(Exception):
    def __init__(self, message="Payment failed or declined"):
        super().__init__(message)

# 5. DBException – for database errors 
class DBException(Exception):
    def __init__(self, message="Database error occurred"):
        super().__init__(message)

# 6. ConcurrencyException – for conflicting updates
class ConcurrencyException(Exception):
    def __init__(self, message="Concurrent update conflict occurred"):
        super().__init__(message)

# 7. AuthenticationException – for invalid login
class AuthenticationException(Exception):
    def __init__(self, message="Authentication failed"):
        super().__init__(message)

# 8. AuthorizationException – for forbidden access
class AuthorizationException(Exception):
    def __init__(self, message="Unauthorized access"):
        super().__init__(message)
