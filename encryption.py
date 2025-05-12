from cryptography.fernet import Fernet
import os

def generate_key():
    #cheie de 32 bytes
    key=Fernet.generate_key()
    with open("keys/secret.key","wb") as key_file:
        key_file.write(key)

def load_key():
    with open("keys/secret.key","rb")as key_file:
        return key_file.read()

def encrypt_vote(vote:str)->str:
    key=load_key()
    f=Fernet(key)
    token=f.encrypt(vote.encode())
    return token.decode()

def decrypt_vote(token:str)->str:
    key=load_key()
    f=Fernet(key)
    vote=f.decrypt(token.encode())
    return vote.decode()
