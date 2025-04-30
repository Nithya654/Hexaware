import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from dao.AssetManagementServiceImpl import AssetManagementServiceImpl
from entity.models import Asset
from exception.AssetException import AssetNotFoundException, AssetNotMaintainException

service = AssetManagementServiceImpl()

def show_menu():
    print("\n====== Digital Asset Management System ======")
    print("1. Add Asset")
    print("2. Update Asset")
    print("3. Delete Asset")
    print("4. Allocate Asset")
    print("5. Deallocate Asset")
    print("6. Perform Maintenance")
    print("7. Reserve Asset")
    print("8. Withdraw Reservation")
    print("9. Exit")

def add_asset():
    name = input("Enter asset name: ")
    type = input("Enter asset type: ")
    serial_number = input("Enter serial number: ")
    purchase_date = input("Enter purchase date (YYYY-MM-DD): ")
    location = input("Enter location: ")
    status = input("Enter status: ")
    owner_id = int(input("Enter owner (employee) ID: "))
    asset = Asset(None, name, type, serial_number, purchase_date, location, status, owner_id)
    if service.addAsset(asset):
        print("✅ Asset added successfully!")

def update_asset():
    try:
        asset_id = int(input("Enter asset ID to update: "))
        name = input("Enter new name: ")
        type = input("Enter new type: ")
        serial_number = input("Enter new serial number: ")
        purchase_date = input("Enter new purchase date (YYYY-MM-DD): ")
        location = input("Enter new location: ")
        status = input("Enter new status: ")
        owner_id = int(input("Enter new owner (employee) ID: "))
        asset = Asset(asset_id, name, type, serial_number, purchase_date, location, status, owner_id)
        if service.updateAsset(asset):
            print("✅ Asset updated successfully!")
    except AssetNotFoundException as e:
        print("❌", e)

def delete_asset():
    try:
        asset_id = int(input("Enter asset ID to delete: "))
        if service.deleteAsset(asset_id):
            print("✅ Asset deleted successfully!")
    except AssetNotFoundException as e:
        print("❌", e)

def allocate_asset():
    try:
        asset_id = int(input("Enter asset ID to allocate: "))
        employee_id = int(input("Enter employee ID: "))
        allocation_date = input("Enter allocation date (YYYY-MM-DD): ")
        if service.allocateAsset(asset_id, employee_id, allocation_date):
            print("✅ Asset allocated successfully!")
    except Exception as e:
        print("❌", e)

def deallocate_asset():
    try:
        asset_id = int(input("Enter asset ID to deallocate: "))
        employee_id = int(input("Enter employee ID: "))
        return_date = input("Enter return date (YYYY-MM-DD): ")
        if service.deallocateAsset(asset_id, employee_id, return_date):
            print("✅ Asset deallocated successfully!")
    except AssetNotFoundException as e:
        print("❌", e)

def perform_maintenance():
    try:
        asset_id = int(input("Enter asset ID for maintenance: "))
        maintenance_date = input("Enter maintenance date (YYYY-MM-DD): ")
        description = input("Enter maintenance description: ")
        cost = float(input("Enter maintenance cost: "))
        if service.performMaintenance(asset_id, maintenance_date, description, cost):
            print("✅ Maintenance recorded successfully!")
    except Exception as e:
        print("❌", e)

def reserve_asset():
    try:
        asset_id = int(input("Enter asset ID to reserve: "))
        employee_id = int(input("Enter employee ID: "))
        reservation_date = input("Enter reservation date (YYYY-MM-DD): ")
        start_date = input("Enter start date (YYYY-MM-DD): ")
        end_date = input("Enter end date (YYYY-MM-DD): ")
        service.check_maintenance_due(asset_id)  # optional check
        if service.reserveAsset(asset_id, employee_id, reservation_date, start_date, end_date):
            print("✅ Asset reserved successfully!")
    except AssetNotMaintainException as e:
        print("❌", e)
    except Exception as e:
        print("❌", e)

def withdraw_reservation():
    try:
        reservation_id = int(input("Enter reservation ID to withdraw: "))
        if service.withdrawReservation(reservation_id):
            print("✅ Reservation withdrawn successfully!")
    except AssetNotFoundException as e:
        print("❌", e)

def main():
    while True:
        show_menu()
        choice = input("Select an option: ")
        if choice == '1':
            add_asset()
        elif choice == '2':
            update_asset()
        elif choice == '3':
            delete_asset()
        elif choice == '4':
            allocate_asset()
        elif choice == '5':
            deallocate_asset()
        elif choice == '6':
            perform_maintenance()
        elif choice == '7':
            reserve_asset()
        elif choice == '8':
            withdraw_reservation()
        elif choice == '9':
            print("👋 Exiting. Goodbye!")
            break
        else:
            print("❗ Invalid option. Try again.")

if __name__ == "__main__":
    main()
