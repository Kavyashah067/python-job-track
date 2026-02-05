import csv
from tracker import load_jobs

def show_menu():
    print("\nJob Application Tracker")
    print("1. Add job application")
    print("2. View all applications")
    print("3. Filter applications by status")
    print("4. Exit")
    
def load_jobs():
    with open("data/jobs.csv", mode="r", newline="") as file:
        reader = csv.reader(file)
        return list(reader)

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
    all_jobs = load_jobs()
    if len(all_jobs) <= 1:
        print("No job applications found.")
        return
        
    print ("\nYour Job Applications:\n")
    for i, row in enumerate(all_jobs[1:], start=1):
        company, role, location, status = row
        print(f"{i}. {company} | {role} | {location} | {status}")

def filter_jobs_by_status():
    status_filter = input("Enter status to filter by (applied/interview/rejected): ").lower()
    all_jobs = load_jobs()

    if len(all_jobs) <= 1:
        print("No job applications found.")
        return
        
    filtered_jobs = []
    for row in all_jobs[1:]:
        if row[3].lower() == status_filter:
            filtered_jobs.append(row)

    if not filtered_jobs:
        print(f"No applications found with status '{status_filter}'.")
        return
        
    print(f"\n Applications with status '{status_filter}':\n")
    for i, row in enumerate(filtered_jobs, start=1):
        company, role, location, status = row
        print(f"{i}. {company} | {role} | {location} | {status}")

def main():
    applications = load_jobs()

    while True:
        show_menu()
        choice = input("Enter your choice (1-4): ")

        if choice == "1":
            add_job()
        elif choice == "2":
            view_jobs()
        elif choice == "3":
            filter_jobs_by_status()
        elif choice == "4":
            print("Exiting application. Goodbye!")
            break
        else:
            print("Invalid choice. Try again.")
    
if __name__ == "__main__":
    main()