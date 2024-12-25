from controllers import genre_controller

def genre_menu():
    print("\n--- Genre Management ---")
    print("1. Create a new genre")
    print("2. View all genres")
    print("3. View a genre by ID")
    print("4. Update a genre")
    print("5. Delete a genre")
    print("6. Exit")

def create_genre_view():
    name = input("Enter the genre name: ")
    description = input("Enter the genre description (optional): ")
    response = genre_controller.create_genre(name, description)
    print(response)

def view_all_genres_view():
    genres = genre_controller.get_genres()
    if genres:
        print("\nGenres:")
        for genre in genres:
            print(f"ID: {genre['_id']}, Name: {genre['name']}, Description: {genre['description']}")
    else:
        print("No genres found.")

def view_genre_by_id_view():
    genre_id = input("Enter the genre ID: ")
    genre = genre_controller.get_genre(genre_id)
    if "error" in genre:
        print(genre["error"])
    else:
        print(f"\nID: {genre['_id']}\nName: {genre['name']}\nDescription: {genre['description']}")

def update_genre_view():
    genre_id = input("Enter the genre ID to update: ")
    name = input("Enter the new genre name (leave blank to skip): ")
    description = input("Enter the new genre description (leave blank to skip): ")
    response = genre_controller.update_genre(
        genre_id, name=name if name.strip() else None, description=description if description.strip() else None
    )
    print(response)

def delete_genre_view():
    genre_id = input("Enter the genre ID to delete: ")
    response = genre_controller.delete_genre(genre_id)
    print(response)

# Main Menu Loop
def main():
    while True:
        genre_menu()
        choice = input("\nEnter your choice: ")

        if choice == "1":
            create_genre_view()
        elif choice == "2":
            view_all_genres_view()
        elif choice == "3":
            view_genre_by_id_view()
        elif choice == "4":
            update_genre_view()
        elif choice == "5":
            delete_genre_view()
        elif choice == "6":
            print("Exiting Genre Management. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
