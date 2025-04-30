import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
class AssetNotFoundException(Exception):
    def __init__(self, message="Asset not found"):
        super().__init__(message)

class AssetNotMaintainException(Exception):
    def __init__(self, message="Asset not maintained in last 2 years"):
        super().__init__(message)
