from user_functions import retrieve_all_artworks, add_artwork, review_artwork, create_account, login, recover_password, exit_application

# Main program loop
while True:
    print("\n=== Vivid Vision Vault ===", "\n")
    print("1. Retrieve all artworks")
    print("2. Add an artwork")
    print("3. Review an artwork")
    print("4. Create an account")
    print("5. Login")
    print("6. Recover password")
    print("7. Exit")
    print("=========================")

    choice = input("Enter your choice (1-7): ")
    print("\n")

    if choice == '1':
        retrieve_all_artworks()
    elif choice == '2':
        add_artwork()
    elif choice == '3':
        review_artwork()
    elif choice == '4':
        create_account()
    elif choice == '5':
        if login():
            # Implement user-specific functionality after successful login if needed
            pass
    elif choice == '6':
        recover_password()
    elif choice == '7':
        exit_application()
    else:
        print("Invalid choice. Please try again.")
