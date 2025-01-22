from cryptography.fernet import Fernet
import os
import hashlib

# Paths for storing data
USER_FILE = "password_manager/files/users.txt"
KEY_DIR = "password_manager/files/keys/"
PASSWORD_DIR = "password_manager/files/passwords/"

# Ensure necessary directories exist
os.makedirs(KEY_DIR, exist_ok=True)
os.makedirs(PASSWORD_DIR, exist_ok=True)

def hash_password(password):
    """Hash a password using SHA256."""
    return hashlib.sha256(password.encode()).hexdigest()

def write_key(username):
    """Generate and save a unique Fernet key for the user."""
    key = Fernet.generate_key()
    with open(f"{KEY_DIR}{username}.key", "wb") as key_file:
        key_file.write(key)

def load_key(username):
    """Load the Fernet key for the user."""
    with open(f"{KEY_DIR}{username}.key", "rb") as key_file:
        return key_file.read()

def check_user(username, password):
    """Check if a user exists and validate the master password."""
    if not os.path.exists(USER_FILE):
        return False
    
    hashed_pwd = hash_password(password)
    with open(USER_FILE, "r") as file:
        for line in file:
            user, stored_hash = line.strip().split("|")
            if user == username and stored_hash == hashed_pwd:
                return True
    return False

def register_user(username, password):
    """Register a new user and create their key."""
    hashed_pwd = hash_password(password)
    
    # Check if user already exists
    if os.path.exists(USER_FILE):
        with open(USER_FILE, "r") as file:
            for line in file:
                user, _ = line.strip().split("|")
                if user == username:
                    print("User already exists.")
                    return False

    # Save user credentials
    with open(USER_FILE, "a") as file:
        file.write(f"{username}|{hashed_pwd}\n")
    
    # Generate and save the user's key
    write_key(username)
    print(f"User {username} registered successfully!")
    return True

def view_passwords(username, fer):
    """View passwords for the logged-in user."""
    user_password_file = f"{PASSWORD_DIR}{username}.txt"
    if not os.path.exists(user_password_file):
        print("No passwords stored yet.")
        return

    with open(user_password_file, "r") as file:
        for line in file.readlines():
            account, pwd = line.strip().split("|")
            print(f"Account: {account}, Password: {fer.decrypt(pwd.encode()).decode()}")

def add_password(username, fer):
    """Add a new password for the logged-in user."""
    user_password_file = f"{PASSWORD_DIR}{username}.txt"
    account_name = input("Account Name: ")
    password = input("Enter Your Password: ")
    encrypted_pwd = fer.encrypt(password.encode()).decode()
    
    with open(user_password_file, "a") as file:
        file.write(f"{account_name}|{encrypted_pwd}\n")
    print("Password saved successfully.")
def main():
    print("Welcome to the Password Manager!")
    while True:
        action = get_user_action()
        if action == "quit":
            break
        elif action in ["login", "register"]:
            handle_user_action(action)
        else:
            print("Invalid action. Please choose [login/register/quit].")

def get_user_action():
    """Prompt the user to choose an action."""
    return input("Do you want to [login/register/quit]? ").lower()

def handle_user_action(action):
    """Handle the login or registration action."""
    username = input("Enter your username: ")
    password = input("Enter your master password: ")

    if action == "register":
        if register_user(username, password):
            return

    if action == "login":
        if check_user(username, password):
            handle_logged_in_user(username)
        else:
            print("Invalid username or password.")

def handle_logged_in_user(username):
    """Handle actions for a logged-in user."""
    print(f"Welcome back, {username}!")
    key = load_key(username)
    fer = Fernet(key)

    while True:
        choice = get_logged_in_user_action()
        if choice == "logout":
            break
        elif choice == "view":
            view_passwords(username, fer)
        elif choice == "add":
            add_password(username, fer)
        else:
            print("Invalid choice.")

def get_logged_in_user_action():
    """Prompt the logged-in user to choose an action."""
    return input("\nWould you like to [view/add] passwords or [logout]? ").lower()

if __name__ == "__main__":
    main()
