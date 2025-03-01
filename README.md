# Expense Tracker

This Expense Tracker is a Python-based application that allows users to record, manage, and analyze their expenses. The program supports adding, viewing, editing, deleting, summarizing, and searching for expenses, along with visualizing expense trends through graphs.

## Features

1. **Add Expense**: Input expense details including date, amount, category, and description.
2. **View Expenses**: Display all recorded expenses.
3. **Edit Expense**: Modify details of an existing expense by selecting its index.
4. **Delete Expense**: Remove a specific expense entry after confirmation.
5. **Show Summary**: Provide insights into total spending, monthly spending, and category-based expenditure with optional visual representation.
6. **Search Expenses**: Search expenses by date, category, or keyword.
7. **Exit**: Safely terminate the program.

## Technologies Used

- Python 3
- Pandas (for data handling and CSV management)
- Matplotlib (for visualization)

## Prerequisites

Ensure Python and the required libraries are installed.

```bash
pip install pandas matplotlib
```

## How to Run the Application

1. Ensure `expense_tracker.csv` exists, or the program will create it.

2. Run the script:

```bash
python expense_tracker.py
```

## CSV File Structure

The program reads and writes to `expense_tracker.csv` with the following columns:

- Date: Date of the expense (YYYY-MM-DD format)
- Amount: Expense amount (positive float)
- Category: Category of the expense (predefined options)
- Description: A short description of the expense

## User Guide

### Menu Options

1. **Add Expense**:
   - Input the date (YYYY-MM-DD).
   - Enter a positive amount.
   - Choose from valid categories: Food, Transport, Entertainment, Utilities, Health, Shopping, Education.
   - Provide a description.

2. **View Expenses**:
   - Displays all expense records.

3. **Edit Expense**:
   - Select an expense by its index.
   - Modify any field or leave it blank to retain the current value.

4. **Delete Expense**:
   - Select an expense by its index.
   - Confirm deletion to remove it permanently.

5. **Show Summary**:
   - View total spending.
   - Display monthly and category-wise spending.
   - Optionally view a graphical representation of expense trends.

6. **Search Expenses**:
   - Search by date, category, or keyword within descriptions.

7. **Exit**:
   - Ends the session and saves all changes.

## Error Handling

- Validates user input (date format, positive amount, category).
- Handles invalid indices and missing files.
- Displays clear error messages.

## Example Output

```
Expense Tracker Menu:
1. Add Expense
2. View Expenses
3. Edit Expense
4. Delete Expense
5. Show Summary
6. Search Expenses
7. Exit
Choose an option (1-7):
```

## Future Enhancements

- Implement multi-currency support.
- Add user authentication for multiple profiles.
- Export and import expense data in different formats.

## License

This project is licensed under the MIT License.

