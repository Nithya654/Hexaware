import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from abc import ABC, abstractmethod
from entity.models import Asset
from util.DBConnUtil import get_connection


class AssetManagementService(ABC):

    @abstractmethod
    def addAsset(self, asset: Asset) -> bool:
        """Adds a new asset to the system."""
        pass

    @abstractmethod
    def updateAsset(self, asset: Asset) -> bool:
        """Updates information about an existing asset."""
        pass

    @abstractmethod
    def deleteAsset(self, asset_id: int) -> bool:
        """Deletes an asset from the system based on its ID."""
        pass

    @abstractmethod
    def allocateAsset(self, asset_id: int, employee_id: int, allocation_date: str) -> bool:
        """
        Allocates an asset to an employee on a specified allocation date.
        """
        pass

    @abstractmethod
    def deallocateAsset(self, asset_id: int, employee_id: int, return_date: str) -> bool:
        """
        Deallocates an asset from an employee on a specified return date.
        """
        pass

    @abstractmethod
    def performMaintenance(self, asset_id: int, maintenance_date: str, description: str, cost: float) -> bool:
        """
        Records maintenance activity for an asset, including the date, description, and cost.
        """
        pass

    @abstractmethod
    def reserveAsset(self, asset_id: int, employee_id: int, reservation_date: str, start_date: str, end_date: str) -> bool:
        """
        Reserves an asset for a specified employee for a specific period,
        starting from the start date to the end date. The reservation is made on the reservation date.
        """
        pass

    @abstractmethod
    def withdrawReservation(self, reservation_id: int) -> bool:
        """
        Withdraws a reservation for an asset identified by the reservation ID.
        The reserved asset becomes available for allocation again.
        """
        pass
