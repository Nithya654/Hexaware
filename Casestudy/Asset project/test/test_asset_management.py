import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
import unittest
from dao.AssetManagementServiceImpl import AssetManagementServiceImpl
from entity.models import Asset
from exception.AssetException import AssetNotFoundException

class TestAssetManagement(unittest.TestCase):
    def setUp(self):
        self.service = AssetManagementServiceImpl()

    def test_add_asset(self):
        asset = Asset(None, "Mouse", "Peripheral", "SN1234", "2023-01-01", "Delhi", "in use", 1)
        self.assertTrue(self.service.addAsset(asset))

    def test_update_invalid_asset(self):
        asset = Asset(9999, "Nonexistent", "Type", "SN0000", "2022-01-01", "Nowhere", "lost", 1)
        with self.assertRaises(AssetNotFoundException):
            self.service.updateAsset(asset)

    def test_delete_invalid_asset(self):
        with self.assertRaises(AssetNotFoundException):
            self.service.deleteAsset(9999)

if __name__ == '__main__':
    unittest.main()
