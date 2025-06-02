import csv
import os
from datetime import datetime
import matplotlib.pyplot as plt
import json

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


def delete_Transactions():
	try:
		transactions = []
		with open(DATA_FILE, 'r') as file:
			reader = csv.reader(file)
			headers = next(reader)
			transactions = list(reader)
		if not transactions:
			print("No transactions to delete!")
			return

		print("\nSelect Transactions to delete: ")
		print(f"\n{'Index':<6} {headers[0]:<20} {headers[1]:<10} {headers[2]:15} {headers[3]:<10} {headers[4]}")
		for i, row in enumerate(transactions, 1):
			print(f"{i:<6} {row[0]:<20} {row[1]:<10} {row[2]:<15} {row[3]:<10} {row[4]}")
		index = input("Enter transaction index to delete or 'cancel' to exit")
		if index.lower() == 'cancel':
			print("Deletion Canceled!")
			return
		try:
			index = int(index) - 1
			if 0 <= index <= len(transactions):
				deleted = transactions.pop(index)
				with open(DATA_FILE, 'w', newline='') as file:
					writer = csv.writer(file)
					writer.writerow(headers)
					writer.writerows(transactions)
					print(f"Deleted: {deleted[0]} | {deleted[1]} | {deleted[2]} | {deleted[3]} | {deleted[4]}")
			else:
				print("Invalid Index")
		except ValueError:
			print("Error: Please enter a valid number or 'cancel'")
	except FileNotFoundError:
		print("No transactions found.")
	except Exception as e:
		print(f"Unexpected error: {e}")


def edit_transaction():
	try:
		transactions = []
		with open(DATA_FILE, 'r') as file:
			reader = csv.reader(file)
			headers = next(reader)
			transactions = list(reader)

		if not transactions:
			print("No transactions to edit")
			return

		print("\nSelect Transactions to edit:")
		print(f"{'Index':<6} {headers[0]:<20} {headers[1]:<10} {headers[2]:<15} {headers[3]:<10} {headers[4]}")
		for i, row in enumerate(transactions, 1):
			print(f"{i:<6} {row[0]:<20} {row[1]:<10} {row[2]:<15} {row[3]:<10} {row[4]}")
		while True:
			index_input = input("Enter transaction index to edit or 'cancel' to exit: ").strip()
			if index_input.lower() == 'cancel':
				print("edit Canceled..")
				break
			try:
				index = int(index_input) - 1
				if 0 <= index <= len(transactions):
					print(f"editing: {transactions[index][0]} | {transactions[index][1]} | {transactions[index][2]} | {transactions[index][3]} | {transactions[index][4]}")
					t_type = input("Enter new transaction type (income/expense, or press enter to keep origional): ").lower().strip()
					t_type = t_type if t_type in ['income','expense'] else transactions[index][1]
					category = input("Enter new category (or press enter to keep origional)").strip()
					category = category if category else transactions[index][2]
					input_amount = input("Enter new amount (or press enter to keep origional)").strip()
					amount = float(input_amount) if input_amount else float(transactions[index][3])
					if amount <= 0:
						print("new amount must be positive. keeping origional amount")
						amount = float(transactions[index][3])
					description = input("Enter new description (or press enter to keep origional)")
					description = description if description else transactions[index][4]

					transactions[index] = [datetime.now().strftime('%Y-%m-%d %H:%M:%S'), t_type, category, str(amount), description]
					with open(DATA_FILE, 'w', newline='') as file:
						writer = csv.writer(file)
						writer.writerow(headers)
						writer.writerows(transactions)
					print("transaction Updated.")
				else:
					print("Invalid Index.")
			except ValueError:
				print("Error: Invalid input for amount or index")
	except FileNotFoundError:
		print("No transactions found for editing")
	except Exception as e:
		print(f"Unexpected error: {e}")



def export_to_json():
	try:
		transactions = []
		with open(DATA_FILE, 'r') as file:
			reader = csv.reader(file)
			headers = next(reader)
			for row in reader:
				transactions.append({'date':row[0],'type':row[1],'category':row[2],'amount':float(row[3]),'description':[4]})
		if  not transactions:
			print("No transactions to export.")
			return
		with open('transactions.json','w') as file:
			json.dump(transactions, file, indent=4)
		print("transactions exported to transactions.json")
	except ValueError:
		print("Error: Invalid data in transactions.")
	except FileNotFoundError:
		print("No transactions found.")
	except Exception as e:
		print(f"Unexpected Error: {e}")







def show_menu():
	while True:
		print("\nPersonal Finance Tracker Menu: ")
		print("1. Add Transaction")
		print("2. View Transaction History")
		print("3. Check Balance")
		print("4. Category Report")
		print("5. Plot Expense Chart")
		print("6. Delete Transaction")
		print("7. Edit Transaction")
		print("8. Export to json")
		print("9. Exit..")
		choice = input("Enter choice 1-9: ").strip()
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
				delete_Transactions()
			elif choice == 7:
				edit_transaction()
			elif choice == 8:
				export_to_json()
			elif choice == 9:
				print("Exiting...")
				break
			else:
				print("Invalid choice. Please enter 1-9.")
		except ValueError:
			print("Invalid input. Please enter a number.")


if __name__ == "__main__":
	initialize_csv()
	show_menu()