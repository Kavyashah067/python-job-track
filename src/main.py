import csv
from tracker import load_jobs

DATA_FILE = "data/jobs.csv"
VALID_STATUSES = {"applied", "interview", "rejected"}

def show_menu():
    print("\nJob Application Tracker")
    print("1. Add job application")
    print("2. View all applications")
    print("3. Filter applications by status")
    print("4. Update a job status")
    print("5. Delete a job")
    print("6. Exit")
    
def load_jobs():
    with open(DATA_FILE, mode="r", newline="") as file:
        reader = csv.reader(file)
        return list(reader)
    
def save_jobs(all_jobs):
    with open(DATA_FILE, mode="w", newline="") as file:
        writer = csv.writer(file)

        # write header
        writer.writerow(all_jobs[0])

        # write job rows
        for job in all_jobs[1:]:
            writer.writerow(job)

def add_job():
    company = input("Company name: ")
    role = input("Role: ")
    location = input("Location: ")
    status = input("Status (applied/interview/rejected): ")

    all_jobs = load_jobs()
    all_jobs.append([company, role, location, status])
    save_jobs(all_jobs)

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

def update_job_status():
    all_jobs = load_jobs()

    if len(all_jobs) <= 1:
       print("No job applications to update.")
       return
    
    print("Job Applications:\n")
    for i, job in enumerate(all_jobs[1:], start=1):
        print(f"{i}. {job[0]} | {job[1]} | {job[2]} | {job[3]}")

    try:
        choice = int(input("\nEnter job number to update: "))
        if choice < 1 or choice > len(all_jobs) -1:
            print("Invalid job number.")
            return
        
    except ValueError:
        print("Please enter a valid number.")
        return
    
    new_status = input("Enter new status (applied/interview/rejected): ").lower()
    all_jobs[choice][3] = new_status

    save_jobs(all_jobs)

    print("Job status updated successfully.")

def delete_job():
    all_jobs = load_jobs()

    if len(all_jobs) <= 1:
        print("No job applications to delete.")
        return
    
    print("\nJob Applications:\n")
    for i, job in enumerate(all_jobs[1:], start=1):
        print(f"{i}. {job[0]} | {job[1]} | {job[2]} | {job[3]}")

    try:
        choice = int(input("\nEnter job number to delete: "))
        if choice < 1 or choice > len(all_jobs) -1:
            print("Invalid job number.")
            return
        
    except ValueError:
        print("Please enter a valid number.")
        return
    
    deleted_job = all_jobs.pop(choice)

    save_jobs(all_jobs)

    print(f"🗑️ Deleted job: {deleted_job[0]} | {deleted_job[1]}")

def main():
    applications = load_jobs()

    while True:
        show_menu()
        choice = input("Enter your choice (1-6): ")

        if choice == "1":
            add_job()
        elif choice == "2":
            view_jobs()
        elif choice == "3":
            filter_jobs_by_status()
        elif choice == "4":
            update_job_status()
        elif choice == "5":
            delete_job()
        elif choice == "6":
            print("Exiting application. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")
    
if __name__ == "__main__":
    main()