import sqlite3

class DatabaseConnector:
    def __init__(self, db_config):
        self.db_config = db_config
        self.connection = None
    
    def connect(self):
        """Connect to the database."""
        self.connection = sqlite3.connect(self.db_config['db_name'])
    
    def close(self):
        """Close the database connection."""
        if self.connection:
            self.connection.close()

    # Other database related methods can be added as required 
