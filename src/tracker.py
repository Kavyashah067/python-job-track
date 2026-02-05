import csv
import os

FILE_PATH = "data/jobs.csv"

def load_jobs():
    jobs = []

    if not os.path.exists(FILE_PATH):
        return jobs
    
    with open(FILE_PATH, mode="r", newline="", encoding="utf-8") as file:
        reader = csv.DictReader(file)
        for row in reader:
            jobs.append(row)

    return jobs