import pyodbc

class DBUtil:
    @staticmethod
    def getDBConn():
        try:
            conn = pyodbc.connect('Driver={SQL Server};'
                                  'Server=SARTHAKKULKARNI;'
                                  'Database=OrderManagement;'
                                  'Trusted_Connection=yes;')
            return conn
        except Exception as e:
            print(f"Connection failed: {e}")
