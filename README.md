# Personal Finance Tracker

A Python-based command-line application to manage personal finances, track transactions, set budgets, and generate reports. Built as a portfolio project to demonstrate Python programming, file handling, data visualization, and user interaction skills.

## Features
- **Transaction Management**: Add, edit, delete, and search transactions by category.
- **Data Storage**: Store transactions in `transactions.csv` and budgets in `budgets.json`.
- **Reports**: View category-wise expenses, monthly summaries, and sorted transaction history.
- **Budgeting**: Set category budgets with alerts for overspending.
- **Visualization**: Generate bar charts of expenses using `matplotlib`.
- **Import/Export**: Export transactions to `transactions.json` and import back to CSV.
- **Data Validation**: Ensure valid dates, amounts, and predefined categories.

## Tech Stack
- Python 3.x
- Libraries: `csv`, `json`, `datetime`, `matplotlib`
- File Formats: CSV, JSON

## Setup Instructions
1. Clone the repository:
   ```bash
   git clone https://github.com/mehmoodahmed-0303/Personal-Finance-Tracker.git
   cd Personal-Finance-Tracker
```
2. Create and activate a virtual environment (optional but recommended):
```bash
	python -m venv venv
	source venv/bin/activate  # On Windows: venv\Scripts\activate
```
3. Install dependencies:
```bash
	pip install matplotlib
```
4. Run the application:
 ```bash
	python main.py
```

**Usage**
	Launch the app with python main.py to access a menu-driven interface.
	Choose options (1-13) to:
	Add/edit/delete transactions with validated inputs.
	View sorted transaction history or search by category.
	Check balance, category reports, or monthly summaries.
	Set budgets and receive alerts for overspending.
	Plot expense charts or import/export data in JSON format.
	Example: Add a transaction with category groceries, set a budget, and view reports.



**Project Structure**
	main.py: Core application with all functionality.
	transactions.csv: Stores transaction data.
	budgets.json: Stores category budgets.
	data_handler.py, finance_manager.py: Placeholder files for future modularization.
	README.md: Project documentation.


**Future Improvements**
	Modularize code into data_handler.py (file operations) and finance_manager.py (business logic).
	Add a GUI using tkinter or PyQt.
	Implement user authentication for multi-user support.


**Author**
	Mehmood Ahmed
	GitHub: mehmoodahmed-0303
	Built to showcase Python skills for remote programming roles.