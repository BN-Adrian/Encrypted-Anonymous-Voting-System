from vote import vote
from encryption import generate_key
import os

def main():
    print("bine ai venit la vote")
    print("1 = vreau sa votez")
    print("0 = nu vreau sa votez")

    optiune=input("alege o optiune : ").strip()
    if optiune == "1":
        print("bravo...ai ales sa faci ceva")
        vote()
    else:
        print("mai bine asa")

if __name__=="__main__":
    main()