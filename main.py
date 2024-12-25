from views import genre_view
from views import user_view
from views import movie_view
from views import review_view

def main_menu():
    print("\n--- Main Application Menu ---")
    print("1. Genre Management")
    print("2. User Management")
    print("3. Movie Management")
    print("4. Review Management")
    print("5. Exit")

def main():
    while True:
        main_menu()
        choice = input("\nEnter your choice: ")

        if choice == "1":
            print("\nEntering Genre Management...")
            genre_view.main()
        elif choice == "2":
            print("\nEntering User Management...")
            user_view.main()
        elif choice == "3":
            print("\nEntering Movie Management...")
            movie_view.main()
        elif choice == "4":
            print("\nEntering Review Management...")
            review_view.main()
        elif choice == "5":
            print("Exiting the application. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()