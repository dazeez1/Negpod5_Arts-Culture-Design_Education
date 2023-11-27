import json

# Function to load artworks from a JSON file
def load_artworks():
    try:
        with open('artworks.json', 'r') as f:
            return json.load(f)
    except FileNotFoundError:
        return []

# Function to save artworks to a JSON file
def save_artworks(artworks):
    with open('artworks.json', 'w') as f:
        json.dump(artworks, f, indent=2)

# Function to display the main menu
def display_menu():
    print("\n=== Vivid Vision Vault ===")
    print("1. Retrieve all artworks")
    print("2. Add an artwork")
    print("3. Review an artwork")
    print("4. Create an account")
    print("5. Login")
    print("6. Recover password")
    print("7. Exit")
    print("=========================")

# Function to handle user input and execute corresponding functionality
def handle_user_input():
    choice = input("Enter your choice (1-7): ")

    if choice == '1':
        retrieve_all_artworks()
    elif choice == '2':
        add_artwork()
    elif choice == '3':
        review_artwork()
    elif choice == '4':
        create_account()
    elif choice == '5':
        login()
    elif choice == '6':
        recover_password()
    elif choice == '7':
        exit_program()
    else:
        print("Invalid choice. Please try again.")

# Main program loop
while True:
    display_menu()
    handle_user_input()

    # Save artworks to the file after each user interaction
    save_artworks(artworks)

