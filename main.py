import csv
import os
from datetime import datetime

DATA_FILE = "transactions.csv"

def initialize_csv():
    if not os.path.exists(DATA_FILE):
        with open(DATA_FILE, 'w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(["date", "type", "category", "amount", "description"])

def add_transaction(t_type, category, amount, description):
	date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
	with open(DATA_FILE, 'a', newline='') as file:
		writer = csv.writer(file)
		writer.writerow([date, t_type, category, amount, description])
def get_user_transaction():
	t_type = input("Enter transaction type (income/expense) :").lower()
	if t_type not in ['income', 'expense']:
		t_type = input("Invalid type. Enter 'income' or 'expense': ").lower()
	category = input("Enter category (e.g., salary, groceries) :")
	amount = float(input("Enter amount :"))
	while amount <= 0:
		amount = float(input("Amount must be positive. Enter amount: "))
	description = input("Enter description: ")
	add_transaction(t_type, category, amount, description)
	print("transaction recorded!")

def display_transactions():
	try:
		with open(DATA_FILE, 'r') as file:
			reader = csv.reader(file)
			headers = next(reader) # Skip Header row
			print("\nTransaction History: ")
			print(f"{headers[0]:<20} {headers[1]:<10} {headers[2]:<15} {headers[3]:<10} {headers[4]}")
			for row in reader:
				print(f"{row[0]:<20} {row[1]:<10} {row[2]:<15} {row[3]:<10} {row[4]}")
	except FileNotFoundError:
		print("No Transactions found.")


if __name__ == "__main__":
    initialize_csv()
    get_user_transaction()
    display_transactions()
    print("Personal Finance Tracker initialized.")