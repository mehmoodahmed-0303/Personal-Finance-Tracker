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

if __name__ == "__main__":
    initialize_csv()
    get_user_transaction()
    print("Personal Finance Tracker initialized.")