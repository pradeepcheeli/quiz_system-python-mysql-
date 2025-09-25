from admin import add_question, modify_question, delete_question, view_all_questions, view_all_users
from user import take_quiz, highest_scores

# ---------------- Admin Menu ----------------
def admin_menu():
    while True:
        print("\n--- Admin Menu ---")
        print("1. Add Question")
        print("2. Modify Question")
        print("3. Delete Question")
        print("4. View All Questions")
        print("5. View All Users")
        print("6. Logout")

        choice = input("Enter choice: ")

        if choice == "1":
            add_question()
        elif choice == "2":
            modify_question()
        elif choice == "3":
            delete_question()
        elif choice == "4":
            view_all_questions()
        elif choice == "5":
            view_all_users()
        elif choice == "6":
            print("👋 Logging out from Admin...")
            break
        else:
            print("❌ Invalid choice. Please try again.")

# ---------------- User Menu ----------------
def user_menu():
    username = input("Enter your name: ")
    mobile = input("Enter your mobile number: ")

    while True:
        print("\n--- User Menu ---")
        print("1. Take Quiz")
        print("2. View Highest Scores")
        print("3. Logout")

        choice = input("Enter choice: ")

        if choice == "1":
            take_quiz(username, mobile)
        elif choice == "2":
            highest_scores()
        elif choice == "3":
            print(f"👋 Goodbye {username}! Logged out successfully.")
            break
        else:
            print("❌ Invalid choice. Please try again.")

# ---------------- Main Menu ----------------
def main():
    while True:
        print("\n=== Quiz System ===")
        print("1. Admin Login")
        print("2. User Login")
        print("3. Exit")

        choice = input("Enter choice: ")

        if choice == "1":
            admin_id = input("Enter Admin ID: ")
            admin_pass = input("Enter Password: ")
            if admin_id == "admin" and admin_pass == "admin123":
                print("✅ Admin login successful!")
                admin_menu()
            else:
                print("❌ Invalid Admin credentials.")
        elif choice == "2":
            print("\n--- Welcome to the Quiz System ---")
            user_menu()
        elif choice == "3":
            print("👋 Exiting Quiz System... Goodbye!")
            break
        else:
            print("❌ Invalid choice. Please try again.")

# ---------------- Run Program ----------------
if __name__ == "__main__":
    main()
