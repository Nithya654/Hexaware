import pyodbc

def get_connection():
    try:
        conn_str = (
            "DRIVER={SQL Server};"
            "SERVER=NITHYA;"
            "DATABASE=asserts;"  # Change this if your DB name is different
            "Trusted_Connection=yes;"
        )
        conn = pyodbc.connect(conn_str)
        return conn
    except pyodbc.Error as e:
        print("Database connection error:", e)
        return None
