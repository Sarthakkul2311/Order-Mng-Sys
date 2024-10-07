class DBPropertyUtil:
    @staticmethod
    def getConnectionString(property_file):
        with open(property_file, 'r') as file:
            conn_str = file.readline().strip()
        return conn_str
