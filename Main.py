import pandas as pd
from datetime import datetime
import matplotlib.pyplot as plt


def add_expense(df, csv_path):
    try:
        # Input and validation
        date_str = input("Enter date (YYYY-MM-DD): ").strip()
        date = datetime.strptime(date_str, "%Y-%m-%d")

        amount = float(input("Enter amount: ").strip())
        if amount <= 0:
            raise ValueError("Amount must be positive.")

        # Validate category
        category = input("Enter category (Food, Transport, Entertainment, Utilities, Health, Shopping, Education): ").strip()
        valid_categories = ["Food", "Transport", "Entertainment", "Utilities", "Health", "Shopping", "Education"]
        if category not in valid_categories:
            raise ValueError("Invalid category.")

        # Capture description
        description = input("Enter description: ").strip()

        # Add new record
        new_entry = {"Date": date, "Amount": amount, "Category": category, "Description": description}
        df = pd.concat([df, pd.DataFrame([new_entry])], ignore_index=True)

        # Save updated DataFrame
        df.to_csv(csv_path, index=False)
        print("Expense added successfully!")

    except Exception as e:
        print(f"Error: {e}")

    return df

def view_expenses(df):
    # Display all recorded expenses
    if df.empty:
        print("No expenses recorded yet.")
    else:
        print(df)

def edit_expense(df, csv_path):
    try:
        print(df)  # Display current expenses
        index = int(input("Enter the index of the expense to edit: ").strip())

        # Validate index
        if index < 0 or index >= len(df):
            raise ValueError("Invalid index.")

        print("Leave blank to keep the current value.")

        # Input updated values
        new_date = input(f"Enter new date (YYYY-MM-DD) [{df.at[index, 'Date']}]: ").strip()
        if new_date:
            df.at[index, 'Date'] = datetime.strptime(new_date, "%Y-%m-%d")

        new_amount = input(f"Enter new amount [{df.at[index, 'Amount']}]: ").strip()
        if new_amount:
            df.at[index, 'Amount'] = float(new_amount)

        new_category = input(f"Enter new category [{df.at[index, 'Category']}]: ").strip()
        if new_category:
            df.at[index, 'Category'] = new_category

        new_description = input(f"Enter new description [{df.at[index, 'Description']}]: ").strip()
        if new_description:
            df.at[index, 'Description'] = new_description

        # Save updated DataFrame
        df.to_csv(csv_path, index=False)
        print("Expense updated successfully!")

    except Exception as e:
        print(f"Error: {e}")

    return df

def delete_expense(df, csv_path):
    try:
        print(df)  # Display current expenses
        index = int(input("Enter the index of the expense to delete: ").strip())

        # Validate index
        if index < 0 or index >= len(df):
            raise ValueError("Invalid index.")

        # Confirm deletion
        confirm = input(f"Are you sure you want to delete this expense? (y/n): ").strip().lower()
        if confirm == 'y':
            df.drop(index, inplace=True)
            df.reset_index(drop=True, inplace=True)
            df.to_csv(csv_path, index=False)
            print("Expense deleted successfully!")
        else:
            print("Deletion canceled.")

    except Exception as e:
        print(f"Error: {e}")

    return df

def show_summary(df):
    try:
        if df.empty:
            print("No expenses to summarize.")
            return

        # Display total spending
        print(f"Total Spending: {df['Amount'].sum()}")

        # Group and display spending by month
        df['Month'] = df['Date'].dt.to_period('M')
        monthly_spending = df.groupby('Month')['Amount'].sum()
        print("\nTotal Spending Each Month:")
        print(monthly_spending)

        # Category spending option
        option = input("\nView category spending for (a) All months or (b) Latest month? (a/b): ").strip().lower()

        if option == 'b':
            latest_month = df['Month'].max()
            category_spending = df[df['Month'] == latest_month].groupby('Category')['Amount'].sum()
            print(f"\nCategory Spending for {latest_month}:")
        else:
            category_spending = df.groupby('Category')['Amount'].sum()
            print("\nTotal Spending on Categories:")

        print(category_spending)

        # Visualize expense trend
        visualize = input("\nDo you want a visual representation? (y/n): ").strip().lower()
        if visualize == 'y':
            df = df.sort_values('Date')
            plt.plot(df['Date'], df['Amount'], marker='o')
            plt.xlabel('Date')
            plt.ylabel('Amount')
            plt.title('Expense Trend')
            plt.grid(True)
            plt.show()

    except Exception as e:
        print(f"Error: {e}")

def search_expenses(df):
    try:
        print("Search by: (a) Date (b) Category (c) Keyword")
        option = input("Choose an option (a/b/c): ").strip().lower()

        # Search logic based on user choice
        if option == 'a':
            date_str = input("Enter date (YYYY-MM-DD): ").strip()
            search_result = df[df['Date'] == pd.to_datetime(date_str)]
        elif option == 'b':
            category = input("Enter category: ").strip()
            search_result = df[df['Category'].str.lower() == category.lower()]
        elif option == 'c':
            keyword = input("Enter keyword: ").strip().lower()
            search_result = df[df['Description'].str.lower().str.contains(keyword)]
        else:
            print("Invalid option.")
            return

        # Display search results
        if search_result.empty:
            print("No matching expenses found.")
        else:
            print(search_result)

    except Exception as e:
        print(f"Error: {e}")

def main():
    csv_path = "expense_tracker.csv"

    # Load existing data or create new CSV
    try:
        df = pd.read_csv(csv_path, parse_dates=["Date"])
    except FileNotFoundError:
        df = pd.DataFrame(columns=["Date", "Amount", "Category", "Description"])

    # Main menu loop
    while True:
        print("\nExpense Tracker Menu:")
        print("1. Add Expense")
        print("2. View Expenses")
        print("3. Edit Expense")
        print("4. Delete Expense")
        print("5. Show Summary")
        print("6. Search Expenses")
        print("7. Exit")

        choice = input("Choose an option (1-7): ").strip()

        if choice == '1':
            df = add_expense(df, csv_path)
        elif choice == '2':
            view_expenses(df)
        elif choice == '3':
            df = edit_expense(df, csv_path)
        elif choice == '4':
            df = delete_expense(df, csv_path)
        elif choice == '5':
            show_summary(df)
        elif choice == '6':
            search_expenses(df)
        elif choice == '7':
            print("Exiting program.")
            break
        else:
            print("Invalid option. Please choose again.")

if __name__ == "__main__":
    main()
