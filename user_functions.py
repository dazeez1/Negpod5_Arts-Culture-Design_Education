import json
import hashlib
import random
import string
import psycopg2
import uuid

# Establishing connection to  a database

conn = psycopg2.connect(
    database="Vivid",
    user="postgres",
    password="120903",
    host="localhost",
    port="5433"
)
cursor = conn.cursor()


# Function to retrieve all artworks
def retrieve_all_artworks():
    # artworks = load_artworks()
    get_artworks_query = """SELECT * FROM artworks"""
    cursor.execute(get_artworks_query)
    artworks = cursor.fetchall()
    for artwork in artworks:
        print(f"Title: {artwork[1]}")
        print(f"Artist: {artwork[2]}")
        print(f"Description: {artwork[3]}")
        print(f"Image URL: {artwork[4]}")
        print(f"Reviews : {artwork[5]}")
        print("\n++++++++++ \n")


# Function to add an artwork
def add_artwork():
    title = input("Enter the title of the artwork: ")
    artist = input("Enter the artist of the artwork: ")
    description = input("Enter the description of the artwork: ")
    imageUrl = input("Enter the image URL:")
    reviews = []

    artwork_insert_query = """INSERT INTO artworks (title, artist, description, reviews, imageurl) VALUES (%s, %s, 
    %s, %s, %s)"""
    try:
        record_to_insert = (title, artist, description, reviews, imageUrl)
        cursor.execute(artwork_insert_query, record_to_insert)
        conn.commit()
    except (Exception, psycopg2.Error) as error:
        print("Failed to insert record into artworks table", error)


# Function to review an artwork
def review_artwork():
    # artworks = load_artworks()
    artwork = ()
    title = input("Enter the title of the artwork you want to review: ")
    get_artwork_by_name_query = """ SELECT * FROM artworks WHERE title = %s """
    try:
        cursor.execute(get_artwork_by_name_query, (title, ))
        artwork = cursor.fetchone()

    except (Exception, psycopg2.Error) as error:
        print("Artwork with the given title doesn't exist", error)
    print(artwork)
    name = input("Enter your name:")
    reviewBody = input("Enter your review: ")
    review = (name, reviewBody)
    artwork[5].append(review)
    new_review = artwork[5]
    print(new_review)
    update_artwork_query = """ UPDATE artworks SET reviews = %s WHERE title = %s """
    try:
        cursor.execute(update_artwork_query, (new_review, title))
        print("Artwork reviewed successfully")
        conn.commit()
    except (Exception, psycopg2.Error) as error:
        print("Artwork not reviewed", error)

    # for artwork in artworks:
    #     if artwork['title'] == title:
    #         name = input("Enter your name: ")
    #         reviewBody = input("Enter your review: ")
    #         artwork['reviews'].append(review)
    #         save_artworks(artworks)
    #         print("Review added successfully.")
    #         break
    # else:
    #     print(f"Artwork with title '{title}' not found.")


# Function to create a new user account
def create_account():
    user_insert_query = """INSERT INTO users (username, password) VALUES (%s, %s)"""
    username = input("Enter your username: ")
    password = input("Enter your password: ")
    hashed_password = hashlib.sha256(password.encode()).hexdigest()
    try:
        cursor.execute(user_insert_query, (username, hashed_password))
        conn.commit()
        print("User created successfully ")
        return True
    except (Exception, psycopg2.Error) as error:
        print("User not created ", error)
        return False


# Function to log in
def login():
    username = input("Enter your username: ")
    password = input("Enter your password: ")
    try:
        get_all_users_query = """ SELECT * FROM users WHERE username = %s AND password = %s"""
        cursor.execute(get_all_users_query, (username, hashlib.sha256(password.encode()).hexdigest()))
    except (Exception, psycopg2.Error) as error:
        print("User Not Logged In", error)
    user = cursor.fetchone()
    if user is None:
        print("Wrong Credentials")
        return False
    else:
        print("User successfully logged in")
        return True


# Function for password recovery
def recover_password():
    try:
        username = input("Enter your username: ")
        get_all_users_query = """ SELECT * FROM users WHERE username = %s """
        cursor.execute(get_all_users_query, (username, ))
    except (Exception, psycopg2.Error) as error:
        print("User Not Found", error)
    user = cursor.fetchone()

    temporary_password = ''.join(random.choices(string.ascii_letters + string.digits, k=8))
    print(f"Temporary password: {temporary_password}")
    try:
        update_user_password_query = """UPDATE users SET password = %s WHERE username = %s"""
        cursor.execute(update_user_password_query, (hashlib.sha256(temporary_password.encode()).hexdigest(), username))
    except (Exception, psycopg2.Error) as error:
        print("Password not recovered,", error)


# Function to exit the program
def exit_application():
    print("Exiting Vivid Vision Vault. Goodbye!")
    exit()
