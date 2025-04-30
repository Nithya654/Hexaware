import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
class Asset:
    def __init__(self, asset_id=None, name=None, type=None, serial_number=None, purchase_date=None, location=None, status=None, owner_id=None):
        self.asset_id = asset_id
        self.name = name
        self.type = type
        self.serial_number = serial_number
        self.purchase_date = purchase_date
        self.location = location
        self.status = status
        self.owner_id = owner_id

class Employee:
    def __init__(self, employee_id=None, name=None, department=None, email=None, password=None):
        self.employee_id = employee_id
        self.name = name
        self.department = department
        self.email = email
        self.password = password

class AssetAllocation:
    def __init__(self, allocation_id=None, asset_id=None, employee_id=None, allocation_date=None, return_date=None):
        self.allocation_id = allocation_id
        self.asset_id = asset_id
        self.employee_id = employee_id
        self.allocation_date = allocation_date
        self.return_date = return_date

class MaintenanceRecord:
    def __init__(self, maintenance_id=None, asset_id=None, maintenance_date=None, description=None, cost=None):
        self.maintenance_id = maintenance_id
        self.asset_id = asset_id
        self.maintenance_date = maintenance_date
        self.description = description
        self.cost = cost

class Reservation:
    def __init__(self, reservation_id=None, asset_id=None, employee_id=None, reservation_date=None, start_date=None, end_date=None, status=None):
        self.reservation_id = reservation_id
        self.asset_id = asset_id
        self.employee_id = employee_id
        self.reservation_date = reservation_date
        self.start_date = start_date
        self.end_date = end_date
        self.status = status
