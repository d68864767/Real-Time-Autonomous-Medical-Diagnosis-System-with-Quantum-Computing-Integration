```python
# Import necessary libraries
from cryptography.fernet import Fernet
import os

class Security:
    def __init__(self):
        self.key = None
        self.cipher_suite = None

    def generate_key(self):
        """
        This function generates a key and save it into a file
        """
        self.key = Fernet.generate_key()
        with open("secret.key", "wb") as key_file:
            key_file.write(self.key)

    def load_key(self):
        """
        Load the previously generated key
        """
        return open("secret.key", "rb").read()

    def encrypt_message(self, message):
        """
        Encrypts a message
        """
        self.load_key()
        self.cipher_suite = Fernet(self.key)
        encoded_message = message.encode()
        encrypted_message = self.cipher_suite.encrypt(encoded_message)
        return encrypted_message

    def decrypt_message(self, encrypted_message):
        """
        Decrypts an encrypted message
        """
        self.load_key()
        self.cipher_suite = Fernet(self.key)
        decrypted_message = self.cipher_suite.decrypt(encrypted_message)
        return decrypted_message.decode()

    def secure_patient_data(self, patient_data):
        """
        This function secures patient data by encrypting it
        """
        encrypted_data = {}
        for key, value in patient_data.items():
            encrypted_data[key] = self.encrypt_message(value)
        return encrypted_data

    def retrieve_patient_data(self, encrypted_data):
        """
        This function retrieves patient data by decrypting it
        """
        decrypted_data = {}
        for key, value in encrypted_data.items():
            decrypted_data[key] = self.decrypt_message(value)
        return decrypted_data

if __name__ == "__main__":
    security = Security()
    security.generate_key()
    patient_data = {
        "name": "John Doe",
        "age": "30",
        "diagnosis": "Healthy"
    }
    encrypted_data = security.secure_patient_data(patient_data)
    print(encrypted_data)
    decrypted_data = security.retrieve_patient_data(encrypted_data)
    print(decrypted_data)
```
