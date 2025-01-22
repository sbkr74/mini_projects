from cryptography.fernet import Fernet
import os

def write_key(keypath):
    """Generate and write a new Fernet key."""
    key = Fernet.generate_key()
    with open(keypath, "wb") as key_file:
        key_file.write(key)

def load_key(keypath):
    """Load the existing Fernet key."""
    with open(keypath, "rb") as key_file:
        return key_file.read()

def check_key(keypath):
    """Ensure the Fernet key file exists and is not empty."""
    if not os.path.exists(keypath) or os.path.getsize(keypath) == 0:
        write_key(keypath)
    else:
        print("Key has already been generated.")

def get_access(keypath):
    """Authenticate user and initialize Fernet."""
    access = "Denied"
    while True:
        mstr_pwd = input("Enter Master Password [0000] to Access Password Manager: ")
        if mstr_pwd.isdigit() and int(mstr_pwd) == 0:
            print("Access Accepted.")
            key = load_key(keypath)
            fer = Fernet(key)
            return "Accepted", fer
        else:
            print("Access: ",access)
            print("Invalid Master Password. Try again.")

def view(filepath, fer):
    """View stored account credentials."""
    if not os.path.exists(filepath):
        print("No passwords stored yet.")
        return

    with open(filepath, "r") as f:
        for line in f.readlines():
            data = line.strip()
            account, pwd = data.split("|")
            print("Account:", account, "Password:", fer.decrypt(pwd.encode()).decode())

def add(filepath, fer):
    """Add a new account credential."""
    account_name = input("Account Name: ")
    pwd = input("Enter Your Password: ")
    encrypted_pwd = fer.encrypt(pwd.encode()).decode()
    with open(filepath, "a") as f:
        f.write(f"{account_name}|{encrypted_pwd}\n")
    print("Password saved successfully.")

if __name__ == "__main__":
    name = input("Enter your name: ")
    filepath = "password_manager/files/password.txt"
    keypath = "password_manager/files/key.key"
    os.makedirs(os.path.dirname(filepath), exist_ok=True)  # Ensure the directory exists
    check_key(keypath)
    access, fer = get_access(keypath)

    if access == "Accepted":
        print(f"{name.upper()} has been authorized.")
        while True:
            choice = input("\nWould you like to view or add passwords? Type [view/add] or [q/Q] to quit: ").lower()
            if choice == "q":
                break
            elif choice == "view":
                view(filepath, fer)
            elif choice == "add":
                add(filepath, fer)
            else:
                print("Invalid choice. Please select [view/add/q].")
