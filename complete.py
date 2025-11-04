# initialized variable to store user profiles
# this is a global variable so all functions can access it.
user_database = []

def register_user():
    """ (Member 2) Registers a new user. """
    print("\n--- Register New User ---")
    username = input("Enter a new username: ")
    
    # check existing usernames
    for user in user_database:
        if user['username'] == username:
            print("Username already taken. Please try again.")
            return  # stops/exits the function
    
    # if not existing, proceed to get password and email
    password = input("Enter a new password: ")
    email = input("Enter your email: ")
    
    # assigns the values to a new dictionary and appends to the database
    new_user = {
        "username": username,
        "password": password,  # In a real app, you would hash this!
        "email": email
    }
    user_database.append(new_user)
    
    # confirmation message
    print(f"Registration successful for {username}!")


def login_user():
    """ (Member 3) Logs in an existing user. """
    print("\n--- User Login ---")
    username = input("Enter your username: ")
    password = input("Enter your password: ")
    
    # checks for matching username and password
    for user in user_database:
        # 2. checks if both username and password match
        if user['username'] == username and user['password'] == password:
            print(f"\nLogin successful! Welcome, {username}.")
            return  # stops/exits the function
    
    # display if no match found
    print("\nInvalid username or password.")


def view_profile():
    """ (Member 4) Views a user's profile (email only). """
    print("\n--- View User Profile ---")
    username_to_view = input("Enter the username of the profile to view: ")
    
    # checks for the username in the database if exists
    for user in user_database:
        if user['username'] == username_to_view:
            # if match found, display profile info except password
            print(f"\n--- Profile for {user['username']} ---")
            print(f"Email: {user['email']}")
            return  # stops/exits the function

    # if no match found, display user not found
    print("\nUser not found.")


def list_all_users():
    """ (Member 5) Lists all registered usernames. """
    print("\n--- All Registered Users ---")
    
    # check if user_database is empty
    if len(user_database) == 0:
        print("No users registered yet.")
        return  # stops/exits the function

    # If not empty, print all usernames
    for user in user_database:
        print(user['username'])


def main():
    """ (Member 1) Runs the main program loop. """
    
    # displays a menu of options to the user
    while True:
        print("\nWelcome! What would you like to do?")
        print("1. Register a new user")
        print("2. Log in")
        print("3. View a user's profile")
        print("4. List all registered users")
        print("5. Exit")

        # takes user choice as input
        choice = input("Enter your choice (1-5): ")

        # calls the appropriate function based on user choice
        if choice == '1':
            register_user()
        elif choice == '2':
            login_user()
        elif choice == '3':
            view_profile()
        elif choice == '4':
            list_all_users()
        elif choice == '5':
            # exit the program
            print("Exiting program. Goodbye!")
            break  # stops the 'while True' loop
        else:
            # handles invalid input
            print("Invalid choice. Please enter a number between 1 and 5.")


# runs the main program/function
main()