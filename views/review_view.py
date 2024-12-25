from controllers import review_controller

def review_menu():
    print("\n--- Review Management ---")
    print("1. Create a new review")
    print("2. View all reviews")
    print("3. View reviews by movie ID")
    print("4. View a review by ID")
    print("5. Update a review")
    print("6. Delete a review")
    print("7. Exit")

def create_review_view():
    movie_id = input("Enter the movie ID: ")
    user_id = input("Enter the user ID: ")
    review_rating = input("Enter the review rating: ")
    response = review_controller.create_review(movie_id, user_id, float(review_rating))
    print(response)

def view_all_reviews_view():
    reviews = review_controller.get_reviews()
    if reviews:
        print("\nReviews:")
        for review in reviews:
            print(f"ID: {review['_id']}, Movie ID: {review['movie_id']}, User ID: {review['user_id']}, Rating: {review['review_rating']}")
    else:
        print("No reviews found.")

def view_reviews_by_movie_view():
    movie_id = input("Enter the movie ID: ")
    reviews = review_controller.get_reviews_by_movie(movie_id)
    if reviews:
        print("\nReviews for Movie ID:")
        for review in reviews:
            print(f"ID: {review['_id']}, User ID: {review['user_id']}, Rating: {review['review_rating']}")
    else:
        print("No reviews found for this movie.")

def view_review_by_id_view():
    review_id = input("Enter the review ID: ")
    review = review_controller.get_review(review_id)
    if "error" in review:
        print(review["error"])
    else:
        print(f"\nID: {review['_id']}\nMovie ID: {review['movie_id']}\nUser ID: {review['user_id']}\nRating: {review['review_rating']}")

def update_review_view():
    review_id = input("Enter the review ID to update: ")
    review_rating = input("Enter the new review rating: ")
    response = review_controller.update_review(review_id, float(review_rating))
    print(response)

def delete_review_view():
    review_id = input("Enter the review ID to delete: ")
    response = review_controller.delete_review(review_id)
    print(response)

# Main Menu Loop
def main():
    while True:
        review_menu()
        choice = input("\nEnter your choice: ")

        if choice == "1":
            create_review_view()
        elif choice == "2":
            view_all_reviews_view()
        elif choice == "3":
            view_reviews_by_movie_view()
        elif choice == "4":
            view_review_by_id_view()
        elif choice == "5":
            update_review_view()
        elif choice == "6":
            delete_review_view()
        elif choice == "7":
            print("Exiting Review Management. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
