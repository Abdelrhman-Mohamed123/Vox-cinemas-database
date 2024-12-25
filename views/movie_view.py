from controllers import movie_controller

def movie_menu():
    print("\n--- Movie Management ---")
    print("1. Create a new movie")
    print("2. View all movies")
    print("3. View a movie by ID")
    print("4. Update a movie")
    print("5. Delete a movie")
    print("6. Exit")

def create_movie_view():
    title = input("Enter the movie title: ")
    genre = input("Enter the movie genre: ")
    release_year = input("Enter the release year: ")
    ratings = input("Enter initial ratings (optional, leave blank if none): ")
    ratings = float(ratings) if ratings.strip() else None
    response = movie_controller.create_movie(title, genre, int(release_year), ratings)
    print(response)

def view_all_movies_view():
    movies = movie_controller.get_movies()
    if movies:
        print("\nMovies:")
        for movie in movies:
            print(f"ID: {movie['_id']}, Title: {movie['title']}, Genre: {movie['genre']}, Release Year: {movie['release_year']}, Ratings: {movie['ratings']}")
    else:
        print("No movies found.")

def view_movie_by_id_view():
    movie_id = input("Enter the movie ID: ")
    movie = movie_controller.get_movie(movie_id)
    if "error" in movie:
        print(movie["error"])
    else:
        print(f"\nID: {movie['_id']}\nTitle: {movie['title']}\nGenre: {movie['genre']}\nRelease Year: {movie['release_year']}\nRatings: {movie['ratings']}")

def update_movie_view():
    movie_id = input("Enter the movie ID to update: ")
    title = input("Enter the new title (leave blank to skip): ")
    genre = input("Enter the new genre (leave blank to skip): ")
    release_year = input("Enter the new release year (leave blank to skip): ")
    ratings = input("Enter the new ratings (optional, leave blank to skip): ")
    ratings = float(ratings) if ratings.strip() else None
    response = movie_controller.update_movie(
        movie_id,
        title=title if title.strip() else None,
        genre=genre if genre.strip() else None,
        release_year=int(release_year) if release_year.strip() else None,
        ratings=ratings
    )
    print(response)

def delete_movie_view():
    movie_id = input("Enter the movie ID to delete: ")
    response = movie_controller.delete_movie(movie_id)
    print(response)

# Main Menu Loop
def main():
    while True:
        movie_menu()
        choice = input("\nEnter your choice: ")

        if choice == "1":
            create_movie_view()
        elif choice == "2":
            view_all_movies_view()
        elif choice == "3":
            view_movie_by_id_view()
        elif choice == "4":
            update_movie_view()
        elif choice == "5":
            delete_movie_view()
        elif choice == "6":
            print("Exiting Movie Management. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
