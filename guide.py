# initialized variable to store user profiles
# this is a global variable so all functions can access it.
user_database = []

def register_user():
    """ (Member 2) Registers a new user. """
    print("\n--- Register New User ---")
    
    # TODO: (Member 2: The Registrar)
    # 1. Ask for 'username', 'password', and 'email' using input().
    # 2. Check for duplicates:
    #    - Use a 'for' loop to iterate through 'user_database'.
    #    - For each 'user' (which is a dictionary) in the list,
    #      check if user['username'] is the same as the new username.
    # 3. If a duplicate is found:
    #    - Print "Username already taken. Please try again."
    #    - 'return' to stop the function early.
    # 4. If no duplicate is found:
    #    - Create a new dictionary: new_user = {"username": ..., "password": ..., "email": ...}
    #    - 'append()' this new_user dictionary to the 'user_database' list.
    #    - Print "Registration successful!"
    
    print("This feature is not built yet.") # Placeholder


def login_user():
    """ (Member 3) Logs in an existing user. """
    print("\n--- User Login ---")
    
    # TODO: (Member 3: The Authenticator)
    # 1. Ask for 'username' and 'password' using input().
    # 2. Use a 'for' loop to iterate through 'user_database'.
    # 3. Inside the loop, check if user['username'] matches the input_username
    #    AND user['password'] matches the input_password.
    # 4. If a match is found:
    #    - Print "Login successful! Welcome, [username]."
    #    - 'return' to stop the function.
    # 5. If the loop finishes with no match (meaning the loop ended):
    #    - Print "Invalid username or password."
    
    print("This feature is not built yet.") # Placeholder


def view_profile():
    """ (Member 4) Views a user's profile (email only). """
    print("\n--- View User Profile ---")
    
    # TODO: (Member 4: The Searcher)
    # 1. Ask for the 'username' of the profile they want to view.
    # 2. Use a 'for' loop to iterate through 'user_database'.
    # 3. Inside the loop, check if user['username'] matches the username_to_view.
    # 4. If a match is found:
    #    - Print the profile details (e.g., f"Username: {user['username']}", f"Email: {user['email']}")
    #    - DO NOT print the password.
    #    - 'return' to stop the function.
    # 5. If the loop finishes with no match:
    #    - Print "User not found."
        
    print("This feature is not built yet.") # Placeholder


def list_all_users():
    """ (Member 5) Lists all registered usernames. """
    print("\n--- All Registered Users ---")
    
    # TODO: (Member 5: The Admin)
    # 1. Check if 'user_database' is empty (e.g., if len(user_database) == 0).
    # 2. If it's empty:
    #    - Print "No users registered yet."
    # 3. If it's not empty:
    #    - Print a header (like the one above).
    #    - Use a 'for' loop to iterate through 'user_database'.
    #    - For each 'user' in the list, print only their user['username'].
            
    print("This feature is not built yet.") # Placeholder


def main():
    """ (Member 1) Runs the main program loop. """
    
    # (Member 1: The Architect)
    # This is the main program loop.
    while True:
        # displays a menu of options to the user
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
            break # stops the 'while True' loop
        else:
            # handles invalid input
            print("Invalid choice. Please enter a number between 1 and 5.")


# runs the main program/function
main()