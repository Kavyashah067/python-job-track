def show_menu():
    print("\nJob Application Tracker")
    print("1. Add job application")
    print("2. View all applications")
    print("3. Exit")

def main():
    applications = []

    while True:
        show_menu()
        choice = input("Enter your choice (1-3): ")

        if choice == "1":
            pass
        elif choice == "2":
            pass
        elif choice == "3":
            print("Exiting application. Goodbye!")
            break
        else:
            print("Invalid choice. Try again.")

if __name__ == "__main__":
    main()