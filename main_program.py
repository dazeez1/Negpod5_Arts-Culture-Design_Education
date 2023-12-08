import psycopg2

from user_functions import retrieve_all_artworks, add_artwork, review_artwork, create_account, login, recover_password, \
    exit_application

# Establishing connection to  a database


conn = psycopg2.connect(
    database="Vivid",
    user="postgres",
    password="120903",
    host="localhost",
    port="5433"
)
cursor = conn.cursor()
cursor.execute("select version()")
data = cursor.fetchone()
print("🚀🚀connection established to: ", data)


def run_app():
    print("\n=== Vivid Vision Vault ===", "\n")
    print("1. Retrieve all artworks")
    print("2. Add an artwork")
    print("3. Review an artwork")
    print("4. Exit")
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
        exit_application()
    else:
        print("Invalid choice. Please try again.")

# Main program loop
while True:
    print("\n=== Vivid Vision Vault ===", "\n")
    print("1. Login")
    print("2. Don't have an account yet? Create Account")
    print("3. Forgot password")
    print("4. Exit")

    choice = input("Enter your choice (1-4): ")
    print("\n")
    if choice == '1':
        if login():
            run_app()

    elif choice == '2':
        if create_account():
            run_app()

    elif choice == '3':
        recover_password()
    elif choice == '4':
        exit_application()

    else:
        print("Invalid choice. Please try again.")

