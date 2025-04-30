import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from dao.AssetManagementService import AssetManagementService
from util.DBConnUtil import get_connection


from entity.models import Asset
from exception.AssetException import AssetNotFoundException, AssetNotMaintainException
import datetime

class AssetManagementServiceImpl(AssetManagementService):

    def addAsset(self, asset: Asset) -> bool:
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("""
            INSERT INTO assets (name, type, serial_number, purchase_date, location, status, owner_id)
            VALUES (?, ?, ?, ?, ?, ?, ?)
        """, (asset.name, asset.type, asset.serial_number, asset.purchase_date,
              asset.location, asset.status, asset.owner_id))
        conn.commit()
        return True

    def updateAsset(self, asset: Asset) -> bool:
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("""
            UPDATE assets SET name=?, type=?, serial_number=?, purchase_date=?, location=?, status=?, owner_id=?
            WHERE asset_id=?
        """, (asset.name, asset.type, asset.serial_number, asset.purchase_date,
              asset.location, asset.status, asset.owner_id, asset.asset_id))
        if cursor.rowcount == 0:
            raise AssetNotFoundException(f"Asset ID {asset.asset_id} not found.")
        conn.commit()
        return True

    def deleteAsset(self, asset_id: int) -> bool:
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("DELETE FROM assets WHERE asset_id=?", (asset_id,))
        if cursor.rowcount == 0:
            raise AssetNotFoundException(f"Asset ID {asset_id} not found.")
        conn.commit()
        return True

    def allocateAsset(self, asset_id: int, employee_id: int, allocation_date: str) -> bool:
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("""
            INSERT INTO asset_allocations (asset_id, employee_id, allocation_date)
            VALUES (?, ?, ?)
        """, (asset_id, employee_id, allocation_date))
        conn.commit()
        return True

    def deallocateAsset(self, asset_id: int, employee_id: int, return_date: str) -> bool:
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("""
            UPDATE asset_allocations
            SET return_date=?
            WHERE asset_id=? AND employee_id=? AND return_date IS NULL
        """, (return_date, asset_id, employee_id))
        if cursor.rowcount == 0:
            raise AssetNotFoundException(f"No active allocation found for asset ID {asset_id} and employee ID {employee_id}.")
        conn.commit()
        return True

    def performMaintenance(self, asset_id: int, maintenance_date: str, description: str, cost: float) -> bool:
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("""
            INSERT INTO maintenance_records (asset_id, maintenance_date, description, cost)
            VALUES (?, ?, ?, ?)
        """, (asset_id, maintenance_date, description, cost))
        conn.commit()
        return True

    def reserveAsset(self, asset_id: int, employee_id: int, reservation_date: str, start_date: str, end_date: str) -> bool:
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("""
            INSERT INTO reservations (asset_id, employee_id, reservation_date, start_date, end_date, status)
            VALUES (?, ?, ?, ?, ?, 'pending')
        """, (asset_id, employee_id, reservation_date, start_date, end_date))
        conn.commit()
        return True

    def withdrawReservation(self, reservation_id: int) -> bool:
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("""
            UPDATE reservations SET status='withdrawn'
            WHERE reservation_id=?
        """, (reservation_id,))
        if cursor.rowcount == 0:
            raise AssetNotFoundException(f"Reservation ID {reservation_id} not found.")
        conn.commit()
        return True

    # Optional: Helper method to check last maintenance date
    def check_maintenance_due(self, asset_id: int) -> bool:
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("""
            SELECT MAX(maintenance_date)
            FROM maintenance_records
            WHERE asset_id=?
        """, (asset_id,))
        result = cursor.fetchone()
        if result[0] is None:
            raise AssetNotMaintainException("Asset has no maintenance history.")
        last_maint_date = result[0]
        if (datetime.datetime.now().date() - last_maint_date).days > 730:
            raise AssetNotMaintainException("Asset not maintained in the last 2 years.")
        return True
