import csv
import os
from datetime import datetime

# Define the file name for storing data
DATA_FILE = 'expenses.csv'

# Define the categories for expenses
CATEGORIES = ['Food', 'Transportation', 'Entertainment', 'Utilities', 'Others']

# Function to initialize the data file if it doesn't exist
def initialize_data_file():
    if not os.path.exists(DATA_FILE):
        with open(DATA_FILE, mode='w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(['Date', 'Category', 'Amount', 'Description'])

# Function to add a new expense
def add_expense():
    try:
        date = input("Enter the date (YYYY-MM-DD): ")
        datetime.strptime(date, '%Y-%m-%d')  # Validate date format
        print("Select a category: ")
        for idx, category in enumerate(CATEGORIES, start=1):
            print(f"{idx}. {category}")
        category_idx = int(input("Enter the category number: "))
        category = CATEGORIES[category_idx - 1]
        amount = float(input("Enter the amount (in Rupees): "))
        description = input("Enter a brief description: ")

        with open(DATA_FILE, mode='a', newline='') as file:
            writer = csv.writer(file)
            writer.writerow([date, category, amount, description])
        print("Expense added successfully!\n")

    except ValueError:
        print("Invalid input. Please try again.\n")

# Function to read all expenses from the data file
def read_expenses():
    expenses = []
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, mode='r') as file:
            reader = csv.DictReader(file)
            for row in reader:
                expenses.append(row)
    return expenses

# Function to display monthly summary
def display_monthly_summary():
    expenses = read_expenses()
    monthly_summary = {}

    for expense in expenses:
        date = expense['Date']
        amount = float(expense['Amount'])
        month = date[:7]  # Extract YYYY-MM

        if month in monthly_summary:
            monthly_summary[month] += amount
        else:
            monthly_summary[month] = amount

    print("Monthly Summary:")
    for month, total in monthly_summary.items():
        print(f"{month}: ₹{total:.2f}")
    print()

# Function to display category-wise expenditure
def display_category_wise_expenditure():
    expenses = read_expenses()
    category_summary = {category: 0.0 for category in CATEGORIES}

    for expense in expenses:
        category = expense['Category']
        amount = float(expense['Amount'])
        if category in category_summary:
            category_summary[category] += amount

    print("Category-wise Expenditure:")
    for category, total in category_summary.items():
        print(f"{category}: ₹{total:.2f}")
    print()

# Main function to run the expense tracker
def main():
    initialize_data_file()

    while True:
        print("Expense Tracker Menu:")
        print("1. Add Expense")
        print("2. View Monthly Summary")
        print("3. View Category-wise Expenditure")
        print("4. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            add_expense()
        elif choice == '2':
            display_monthly_summary()
        elif choice == '3':
            display_category_wise_expenditure()
        elif choice == '4':
            print("Exiting the Expense Tracker. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.\n")

if __name__ == "__main__":
    main()
