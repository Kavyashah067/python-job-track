import csv
from tracker import load_jobs

def show_menu():
    print("\nJob Application Tracker")
    print("1. Add job application")
    print("2. View all applications")
    print("3. Exit")
    
def add_job():
    company = input("Company name: ")
    role = input("Role: ")
    location = input("Location: ")
    status = input("Status (applied/interview/rejected): ")

    with open("data/jobs.csv", mode="a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow([company, role, location, status])

    print("Job saved successfully")

def view_jobs():
    with open("data/jobs.csv", mode="r", newline="") as file:
        reader = csv.reader(file)
        rows = list(reader)

        if len(rows) <= 1:
            print("No job applications found.")
            return
        
        print ("\nYour Job Applications:\n")
        for i, row in enumerate(rows[1:], start=1):
            company, role, location, status = row
            print(f"{i}. {company} | {role} | {location} | {status}")

def main():
    applications = load_jobs()

    while True:
        show_menu()
        choice = input("Enter your choice (1-3): ")

        if choice == "1":
            add_job()
        elif choice == "2":
            view_jobs()
        elif choice == "3":
            print("Exiting application. Goodbye!")
            break
        else:
            print("Invalid choice. Try again.")
    
if __name__ == "__main__":
    main()