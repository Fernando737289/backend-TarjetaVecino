import os 

from cryptography.fernet import Fernet
from dotenv import load_dotenv

load_dotenv()

FERNET_KEY = os.getenv("FERNET_KEY")

cipher = Fernet(
    FERNET_KEY.encode()
)

def encrypt_data(data: str):
    
    return cipher.encrypt(
        data.encode()
    ).decode()
    
def decrypt_data(data: str):
    
    return cipher.decrypt(
        data.encode()
    ).decode()