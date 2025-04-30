import pyodbc
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))



from util.db_properties import DB_CONFIG

class DBConnection:
    @staticmethod
    def get_connection():
        try:
            conn_str = (
                f"DRIVER={DB_CONFIG['DRIVER']};"
                f"SERVER={DB_CONFIG['SERVER']};"
                f"DATABASE={DB_CONFIG['DATABASE']};"
                f"Trusted_Connection={DB_CONFIG['TRUSTED_CONNECTION']};"
            )
            return pyodbc.connect(conn_str)
        except pyodbc.Error as e:
            print("❌ Database connection error:", e)
            return None
