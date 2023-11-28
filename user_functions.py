import json
import hashlib
import random
import string


# Function to load user data from a JSON file
def load_users():
    try:
        with open('users.json', 'r') as f:
            return json.load(f)
    except FileNotFoundError:
        return {}


# Function to save user data to a JSON file
def save_users(users):
    with open('users.json', 'w') as f:
        json.dump(users, f, indent=2)


# Function to load artwork data from a JSON file
def load_artworks():
    try:
        with open('artworks.json', 'r') as f:
            return json.load(f)
    except FileNotFoundError:
        return []


# Function to save artwork data to a JSON file
def save_artworks(artworks):
    with open('artworks.json', 'w') as f:
        json.dump(artworks, f, indent=2)


# Function to retrieve all artworks
def retrieve_all_artworks():
    artworks = load_artworks()
    for artwork in artworks:
        print(f"Title: {artwork['title']}")
        print(f"Artist: {artwork['artist']}")
        print(f"Description: {artwork['description']}")
        print(f"Image URL: {artwork['imageUrl']}")
        print(f"Reviews : {artwork['reviews']}")
        print("\n++++++++++ \n")


# Function to add an artwork
def add_artwork():
    artworks = load_artworks()

    title = input("Enter the title of the artwork: ")
    artist = input("Enter the artist of the artwork: ")
    description = input("Enter the description of the artwork: ")
    imageUrl = input("Enter the image URL:")

    new_artwork = {
        "title": title,
        "artist": artist,
        "description": description,
        "reviews": [],
        "Image": imageUrl
    }

    artworks.append(new_artwork)
    save_artworks(artworks)

    print("Artwork added successfully!")


# Function to review an artwork
def review_artwork():
    artworks = load_artworks()

    title = input("Enter the title of the artwork you want to review: ")

    for artwork in artworks:
        if artwork['title'] == title:
            review = input("Enter your review: ")
            artwork['reviews'].append(review)
            save_artworks(artworks)
            print("Review added successfully.")
            break
    else:
        print(f"Artwork with title '{title}' not found.")


# Function to create a new user account
def create_account():
    users = load_users()

    username = input("Enter your username: ")
    password = input("Enter your password: ")

    # Check if the username already exists
    if username in users:
        print("Username already exists. Please choose a different one.")
        return

    # Hash the password before storing
    hashed_password = hashlib.sha256(password.encode()).hexdigest()

    # Store user data
    users[username] = {'password': hashed_password, 'reviews': []}
    save_users(users)

    print("Account created successfully!")


# Function to log in
def login():
    users = load_users()

    username = input("Enter your username: ")
    password = input("Enter your password: ")

    # Check if the username exists
    if username not in users:
        print("Invalid username.")
        return False

    # Hash the provided password for comparison
    hashed_password = hashlib.sha256(password.encode()).hexdigest()

    # Check if the hashed password matches the stored password
    if hashed_password == users[username]['password']:
        print("Login successful!")
        return True
    else:
        print("Invalid password.")
        return False


# Function for password recovery
def recover_password():
    users = load_users()

    username = input("Enter your username: ")

    # Check if the username exists
    if username not in users:
        print("Invalid username.")
        return

    # Simulate a password recovery mechanism by generating a temporary password
    temporary_password = ''.join(random.choices(string.ascii_letters + string.digits, k=8))
    print(f"Temporary password: {temporary_password}")

    # Update the stored password with the temporary password
    users[username]['password'] = hashlib.sha256(temporary_password.encode()).hexdigest()
    save_users(users)


# Function to exit the program
def exit_application():
    print("Exiting Vivid Vision Vault. Goodbye!")
    exit()
