from controllers import user_controller,movie_controller

def user_menu():
    print("\n--- User Management ---")
    print("1. Create a new user")
    print("2. View all users")
    print("3. View a user by ID")
    print("4. Update a user")
    print("5. Delete a user")
    print("6. Exit")

def create_user_view():
    name = input("Enter the user's name: ")
    gmail = input("Enter the user's Gmail: ")
    watched_movies = input("Enter watched movies (comma-separated IDs, optional): ").split(",")
    watched_movies = [movie.strip() for movie in watched_movies if movie.strip()]
    favourite_genres = input("Enter favourite genres (comma-separated, optional): ").split(",")
    favourite_genres = [genre.strip() for genre in favourite_genres if genre.strip()]
    response = user_controller.create_user(name, gmail, watched_movies, favourite_genres)
    print(response)

def view_all_users_view():
    users = user_controller.get_users()
    if users:
        print("\nUsers:")
        for user in users:
            print(f"ID: {user['_id']}, Name: {user['name']}, Gmail: {user['gmail']}")
    else:
        print("No users found.")

def view_user_by_id_view():
    user_id = input("Enter the user ID: ")
    user = user_controller.get_user(user_id)
    if "error" in user:
        print(user["error"])
    else:
        print(f"\nID: {user['_id']}\nName: {user['name']}\nGmail: {user['gmail']}\nWatched Movies: {user['watched_movies']}\nFavourite Genres: {user['favourite_genres']}")

def update_user_view():
    user_id = input("Enter the user ID to update: ")
    name = input("Enter the new name (leave blank to skip): ")
    gmail = input("Enter the new Gmail (leave blank to skip): ")
    watched_movies = input("Enter new watched movies (comma-separated IDs, optional, leave blank to skip): ").split(",")
    watched_movies = [movie.strip() for movie in watched_movies if movie.strip()]
    favourite_genres = input("Enter new favourite genres (comma-separated, optional, leave blank to skip): ").split(",")
    favourite_genres = [genre.strip() for genre in favourite_genres if genre.strip()]
    response = user_controller.update_user(
        user_id, 
        name=name if name.strip() else None, 
        gmail=gmail if gmail.strip() else None, 
        watched_movies=watched_movies if watched_movies else None, 
        favourite_genres=favourite_genres if favourite_genres else None
    )
    print(response)

def delete_user_view():
    user_id = input("Enter the user ID to delete: ")
    response = user_controller.delete_user(user_id)
    print(response)

# Main Menu Loop
def main():
    while True:
        user_menu()
        choice = input("\nEnter your choice: ")

        if choice == "1":
            create_user_view()
        elif choice == "2":
            view_all_users_view()
        elif choice == "3":
            view_user_by_id_view()
        elif choice == "4":
            update_user_view()
        elif choice == "5":
            delete_user_view()
        elif choice == "6":
            print("Exiting User Management. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
