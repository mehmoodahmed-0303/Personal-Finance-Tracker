import csv
import os
from datetime import datetime
import matplotlib.pyplot as plt

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
	try:
		t_type = input("Enter type (income/expense): ")
		while t_type not in ['income', 'expense']:
			t_type = input("Invalid type. Enter 'income' or 'expense': ").lower().strip()
		category = input("Enter category (e.g., salary, groceries) :").strip()
		if not category:
			raise ValueError("category can not be empty")

		amount_input = input("Enter amount (positive number): ").strip()
		amount = float(amount_input)
		while amount <= 0:
			amount_input = input("Amount must be positive. Enter amount: ").strip()
			amount = float(amount_input)

		description = input("Enter description: ").strip()
	except ValueError as e:
		if str(e):
			print(f"Error: {e}")
		else:
			print("Error: Invalid amount. Please enter a valid number.")
	except Exception as e:
		print(f"Unexpected error: {e}")
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

def calculate_balance():
	try:
		total_income = 0
		total_expense = 0
		with open(DATA_FILE, 'r') as file:
			reader = csv.reader(file)
			next(reader)
			for row in reader:
				amount = float(row[3])
				if row[1].lower() == 'income':
					total_income += amount
				elif row[1].lower() == 'expense':
					total_expense += amount
		balance = total_income - total_expense
		print(f"\nTotal Income: ${total_income:.2f}")
		print(f"Total Expenses: ${total_expense:.2f}")
		print(f"Current Balance: ${balance:.2f}")
		return balance
	except FileNotFoundError:
		print("No Transactions cound")
		return 0
	except ValueError:
		print("Invalid amount found in transactions")
		return 0

def category_report():
	try:
		categories = {}
		with open(DATA_FILE, 'r') as file:
			reader = csv.reader(file)
			next(reader)
			for row in reader:
				if row[1].lower() == 'expense':
					category = row[2]
					amount = float(row[3])
					categories[category] = categories.get(category, 0) + amount
		if not categories:
			print("No expense found.")
			return
		print("\nExpense report by category: ")
		for category, total in categories.items():
			print(f"{category:<20}: {total:.2f}")
	except FileNotFoundError:
		print("No Transactions found!")
	except ValueError:
		print("Invalid value for transactios found in expense.")


def plot_expense_chart():
	try:
		categories = {}
		with open(DATA_FILE, 'r') as file:
			reader = csv.reader(file)
			next(reader)
			for row in reader:
				if row[1].lower() == 'expense':
					category = row[2]
					amount = float(row[3])
					categories[category] = categories.get(category, 0) + amount
		if not categories:
			print("No expense to plot.")
			return
		plt.bar(categories.keys(), categories.values(), color='skyblue')
		plt.title("Expense by Category")
		plt.xlabel("Category")
		plt.ylabel("Amount ($)")
		plt.xticks(rotation=45)
		plt.tight_layout()
		plt.show()
	except FileNotFoundError:
		print("No transactions found.")
	except ValueError:
		print("Error: Invalid amount found in transactions.")




def show_menu():
	while True:
		print("\nPersonal Finance Tracker Menu: ")
		print("1. Add Transaction")
		print("2. View Transaction History")
		print("3. Check Balance")
		print("4. Category Report")
		print("5. Plot Expense Chart")
		print("6. Exit..")
		choice = input("Enter choice 1-6: ").strip()
		try:
			choice = int(choice)
			if choice== 1:
				get_user_transaction()
			elif choice == 2:
				display_transactions()
			elif choice == 3:
				calculate_balance()
			elif choice == 4:
				category_report()
			elif choice == 5:
				plot_expense_chart()
			elif choice == 6:
				print("Exiting...")
				break
			else:
				print("Invalid choice. Please enter 1-5.")
		except ValueError:
			print("Invalid input. Please enter a number.")


if __name__ == "__main__":
	initialize_csv()
	show_menu()