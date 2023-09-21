from DatabaseConnector import DatabaseConnector
from EncryptionUtil import EncryptionUtil
from MultiLoginAPI import MultiLoginAPI
from GoLoginAPI import GoLoginAPI
from IncognitonAPI import IncognitonAPI

DB_CONFIG = {"db_name": "profile_manager.db"}

def main():
    # Set up the database
    db_connector = DatabaseConnector(DB_CONFIG)
    db_connector.connect()

    # Set up the encryption utility
    encryption_util = EncryptionUtil()

    # Demonstration: Encrypt a password and then decrypt it
    encrypted_password = encryption_util.encrypt("my_password")
    decrypted_password = encryption_util.decrypt(encrypted_password)

    # Set up API integrations
    multilogin = MultiLoginAPI(MULTILOGIN_API_ENDPOINT)
    gologin = GoLoginAPI(GOLOGIN_API_ENDPOINT)
    incogniton = IncognitonAPI(INCOGNITON_API_ENDPOINT)

    # Here, you'd typically call various methods from these classes to perform desired operations
    # For now, it's just a placeholder to show the setup.

    # Close the database connection
    db_connector.close()

if __name__ == "__main__":
    main()
 
