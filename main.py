import csv
import os

DATA_FILE = "transactions.csv"

def initialize_csv():
    if not os.path.exists(DATA_FILE):
        with open(DATA_FILE, 'w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(["date", "type", "category", "amount", "description"])

if __name__ == "__main__":
    initialize_csv()
    print("Personal Finance Tracker initialized.")