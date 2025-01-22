from cryptography.fernet import Fernet
import os

def check_key():
    filepath = "password_manager/files/key.key"

    if os.path.exists(filepath):
        if os.path.getsize(filepath) == 0:
            write_key()
        else:
            print("Key has been already generated.")
    else:
        write_key()

def get_access():
    access = "Denied"
    while True:
        mstr_pwd = input("Enter Master Password [0000] to Access Password Manager: ")
        key = load_key() + mstr_pwd.encode()
        fer = Fernet(key)

        if mstr_pwd.isdigit():
            if int(mstr_pwd) == 0000:
                access = "Accepted"
                break
            else:
                print("Access: ",access)
                break
        else:
            try:
                mstr_pwd=int(mstr_pwd)
                continue
            except ValueError as e:
                print("ERROR: ",e)
                print("Accept only digits!!!\n")        
    return access

def write_key():
    key = Fernet.generate_key()
    with open("password_manager/files/key.key","wb") as key_file:
        key_file.write(key)

def load_key():
    file = open("password_manager/files/key.key","wb")
    key = file.read()
    file.close()
    return key

def view():
    with open(filepath,"r") as f:
        for line in f.readlines():
            data = line.rstrip()
            account,pwd = data.split("|")
            print("Account:",account," Password:",pwd)


def add():
    account_name = input("Account Name: ")
    pwd = input("Enter Your password: ")
    with open (filepath,"a") as f:
        f.write(account_name + "|" + pwd + "\n")

if __name__=="__main__":
    name = input("Enter your name: ")
    filepath = "password_manager/files/password.txt"
    access = get_access()
    if access == "Accepted":
        print(f"{name.upper()} has been autorized.")
        while True:
            choice = input("\nWould you want to view or add password. Type [view/add] or Press q or Q to Quit: ").lower()
            check_key()
            if choice == 'q':
                break
            elif choice == "view":
                view()
            elif choice == "add":
                add()
            else:
                print("Try again from given option [view/add/q/Q].")
                
            