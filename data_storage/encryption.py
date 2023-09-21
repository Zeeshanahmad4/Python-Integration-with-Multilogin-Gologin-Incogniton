from base64 import b64encode, b64decode

class EncryptionUtil:
    def encrypt(self, data):
        """Encrypts the given data."""
        return b64encode(data.encode()).decode()
    
    def decrypt(self, encrypted_data):
        """Decrypts the given encrypted data."""
        return b64decode(encrypted_data.encode()).decode()
 
