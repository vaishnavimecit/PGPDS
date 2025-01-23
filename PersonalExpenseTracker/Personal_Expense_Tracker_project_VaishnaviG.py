import csv

#Function to log expense
# list to hold expense
expenses=[]

def logExp():
    date = input("Enter the date of the expense in YYYY-MM-DD format: ")
    category = input("Enter the category of the expense(Food,Travel,Entertainment,Household): ")
    amount = float(input("Enter the amount spent: "))
    description = input("Enter a brief description of the expense: ")

    #Create a dictionary for the expense
    expense = {
        'date': date,
        'category': category,
        'amount': amount,
        'description': description
    }

    #Variable to store csv header
    global field_names
    field_names = expense.keys()

    #Add the expense to the list
    expenses.append(expense)
    print("Expense logged successfully!")

# Function to view expenses
def viewExp():
    print("\nExpenses Made:")
    for expense in expenses:
        # Validate that all required details are present
        if all(key in expense for key in ('date', 'category', 'amount', 'description')):
            print(f"Date: {expense['date']}, Category: {expense['category']}, Amount: ${expense['amount']:.2f}, Description: {expense['description']}")
        else:
            print("Incomplete entry found, so skipping.")

#Variable to hold the total budget
monthlyBudget = 0

# Function to set and track the budget
def trackBudget():
    global monthlyBudget
    monthlyBudget = float(input("Enter your monthly budget: "))
    totalExpenses = sum(expense['amount'] for expense in expenses)

    if totalExpenses > monthlyBudget:
        print("You have exceeded your budget!")
    else:
        remaining_balance = monthlyBudget - totalExpenses
        print(f"You have ${remaining_balance:.2f} left for the month.")

# Function to save expenses to a file
def saveExp():
    with open("expenses.csv", "w") as file:
        writer = csv.DictWriter(file, fieldnames=field_names)
        if file.tell() == 0:
            writer.writeheader()
        writer.writerows(expenses)
    print("Expenses saved successfully!")

# Function to load expenses from a file
def loadExp():
    global expenses
    try:
        with open("expenses.csv", "r") as file:
            csv_reader  = csv.reader(file)
            for row in csv_reader :
                print(row)
        print("Expenses loaded successfully!")
    except FileNotFoundError:
        print("No previous expenses found. Starting fresh.")

# Function to display the menu
def main():
    loadExp()  # Load expenses when the program starts
    while True:
        print("\nPersonal Expense Tracker")
        print("1. Add Expense")
        print("2. View Expenses")
        print("3. Track Budget")
        print("4. Save Expenses")
        print("5. Show all Expenses")
        print("6. Exit")

        choice = input("Select an option: ")

        if choice == '1':
            logExp()
        elif choice == '2':
            viewExp()
        elif choice == '3':
            trackBudget()
        elif choice == '4':
            saveExp()
        elif choice == '5':
            loadExp()
        elif choice == '6':
            saveExp()  # Save expenses before exiting
            print("Exiting the program.")
            break
        else:
            print("Invalid choice. Please try again.")

# Run the menu function
main()