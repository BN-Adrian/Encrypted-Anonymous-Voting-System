# Encrypted-Anonymous-Voting-System

    encryption.py

generate_key():
  generam o cheie unica de criptare de 256 biti
  Criptarea Fernet este simetrica si folosim cheie pentru criptare si decriptare

load_key():
  deschide fisierul "secret.key" si returneaza cheia sub forma de bytes

encrypt_vote():
  transforma un vot (ex:"A") in text criptat (ex:"AAAA") pentru a-l salva in fisier
  ciptarea face votul anonim si inaccesibil oricui il vede in fisierul de voturi
