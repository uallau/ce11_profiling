# everything stored here is in dist list
# keys are: username, password, email
user_database = []

# User Management Functions
# Register a new user
def register_user():
    print("Registering a new user...")
    print("Type 'exit' to cancel registration.\n")
    
    # get username then check for uniqueness, else asked again
    while True:
        # take input for username
        username = input("Enter a username: ") 
        if username.lower() == 'exit':
            print("Registration cancelled.")
            return
        
        # if empty, ask again
        while not username:
            print("Username cannot be empty. Please try again.")
            username = input("Enter a username: ")
            if username.lower() == 'exit':
                print("Registration cancelled.")
                return
        
        # check username input by finding any match in user_database
        # since user_database is a list of dicts then check each by key
        # with variable user representing each dict, check if username key matches input
        # use any() instead of for, faster and cleaner
        # checks only any match not iterates all and does not return list
        if any(user['username'] == username for user in user_database):
            print("Username already exists. Please choose a different username.")
        else:
            break
    
    # get email then check for uniqueness, else asked again
    while True:
        # take input for email
        email = input("Enter your email: ")
        if email.lower() == 'exit':
            print("Registration cancelled.")
            return
        
        # if empty
        while not email:
            print("Email cannot be empty. Please try again.")
            email = input("Enter your email: ")
            if email.lower() == 'exit':
                print("Registration cancelled.")
                return
        
        # same logic with username check
        if any(user['email'] == email for user in user_database):
            print("Email already registered. Please use a different email.")
        else:
            break
        
    # take input for password
    password = input("Enter a password: ")
    if password.lower() == 'exit':
        print("Registration cancelled.")
        return
    
    #if empty
    while not password:
        print("Password cannot be empty. Please try again.")
        password = input("Enter a password: ")
        if password.lower() == 'exit':
            print("Registration cancelled.")
            return
    
    # store new user in user_database
    user_database.append({'username': username, 'email': email, 'password': password})
    print(f"User {username} registered successfully!")

# Login an existing user
def login_user():
    print("Logging in...")
    print("Type 'exit' to cancel login.\n")
    username = input("Enter your username: ")
    if username.lower() == 'exit':
        print("Login cancelled.")
        return
    
    # if empty
    while not username:
        print("Username cannot be empty. Please try again.")
        username = input("Enter your username: ")
        if username.lower() == 'exit':
            print("Login cancelled.")
            return
        
    password = input("Enter your password: ")
    if password.lower() == 'exit':
        print("Login cancelled.")
        return
    
    # if empty
    while not password:
        print("Password cannot be empty. Please try again.")
        password = input("Enter your password: ")
        if password.lower() == 'exit':
            print("Login cancelled.")
            return

    # Check if user exists and password matches
    # iterate through user_database to find matching username
    for user in user_database:
        # if username matches, check password
        if user['username'] == username:
            # check password if matches/correct
            if user['password'] == password:
                print("Login successful!")
                # can call other functions here after login
                return
            else:
                # do not reveal if username exists or not for security
                # incorrect password
                # ask password again until correct or exit
                # two print enter password or exit
                while True:
                    print("Incorrect password. Please try again.")
                    password = input("Enter your password: ")
                    if password.lower() == 'exit':
                        print("Login cancelled.")
                        return
                    if user['password'] == password:
                        print("Login successful!")
                        return
    # if no matching username found after checking all users
    print("Username not found.")
    return

# View user profile
def view_user_profile():
    print("Viewing user profile...")
    print("Type 'exit' to cancel.\n")
    
    username = input("Enter the username of the profile to view: ")
    if username.lower() == 'exit':
        print("Profile viewing cancelled.")
        return

    # Check if username exists in user_database
    # iterate through user_database to find matching username
    for user in user_database:
        if user['username'] == username:
            print(f"Profile of {username}:")
            print(f"Email: {user['email']}")
            return
        else:
            while True:
                # if no matching username found, ask again or exit
                print("Username not found. Please try again.")
                username = input("\nEnter the username of the profile to view: ")
                if username.lower() == 'exit':
                    print("Profile viewing cancelled.")
                    return
                            
                for user in user_database:
                    if user['username'] == username:
                        print(f"Profile of {username}:")
                        print(f"Email: {user['email']}")
                        return
    print("Username not found.")
    
# List all registered users
def list_all_users():
    # check if user_database is empty
    if not user_database:
        print("No users registered.")
        return
    
    # other option
    # if len(user_database) == 0:
    #     print("No users registered.")
    #     return
    
    # iterate through user_database and print username and email
    print("Listing all registered users:\n")
    for user in user_database:
        print(f"Username: {user['username']}")

def main():
    while True:
        print("\nWelcome! What would you like to do?")
        print("1. Register User")
        print("2. Login User")
        print("3. View User Profile")
        print("4. List All Users")
        print("5. Exit")
        choice = input("Enter your choice (1/2/3/4/5): ")
        
        if choice == '1':
            register_user()
        elif choice == '2':
            login_user()
        elif choice == '3':
            view_user_profile()
        elif choice == '4':
            list_all_users()
        elif choice == '5':
            print("Exiting the program. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 5.")

main()