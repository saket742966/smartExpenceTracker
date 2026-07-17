from storage import save_expenses
from storage import load_expenses

expenses = load_expenses()

if expenses:
    ids = [expense["id"] for expense in expenses]
    next_id = max(ids) + 1
else:
    next_id = 1

def add_expense():
    global next_id
    
    category = input("Enter Category of Expense: ")
    
    description = input("Enter a description: ")
    
    while True:
        try:
            amount = int(input("Enter Amount: "))
            if amount > 0 :
                break
            
        except ValueError:
            print("Invalid input.")

    payment_method = input("Payment Method used: ")
    
    
    expense_data = {
        "id": next_id,
        "category": category,
        "description": description,
        "amount": amount,
        "payment_method": payment_method
    }
    
    next_id += 1
    print("Expense Added Successfully")
    expenses.append(expense_data)
    save_expenses(expenses)


def view_expenses():
    print("\n" + "=" * 50)
    print(" " * 17 + "ALL EXPENSES")
    print("=" * 50)

    if not expenses:
        print("\nNo expenses found.\n")
        print("=" * 50)
        return

    for index, expense in enumerate(expenses, start=1):
        print(f"\nExpense #{index}")
        print("-" * 40)
        print(f"Expense ID       : {expense['id']}")
        print(f"Category        : {expense['category']}")
        print(f"Description     : {expense['description']}")
        print(f"Amount          : ₹{expense['amount']}")
        print(f"Payment Method  : {expense['payment_method']}")

    print("\n" + "=" * 50)
    print(f"Total Expenses: {len(expenses)}")
    print("=" * 50)
    
    
def delete_expense():
    print("\n" + "=" * 50)
    print(" " * 17 + "DELETE EXPENSE")
    print("=" * 50)

    # Validate Expense ID
    while True:
        try:
            del_id = int(input("Enter Expense ID: "))
            if del_id > 0:
                break
            else:
                print("Expense ID must be greater than 0.")
        except ValueError:
            print("Please enter a valid integer.")

    found = False

    for expense in expenses:
        if expense["id"] == del_id:
            found = True

            print("\nExpense Found:\n")
            print(f"ID              : {expense['id']}")
            print(f"Category        : {expense['category']}")
            print(f"Description     : {expense['description']}")
            print(f"Amount          : ₹{expense['amount']}")
            print(f"Payment Method  : {expense['payment_method']}")

            choice = input("\nDelete this expense? (y/n): ").lower()

            if choice == "y":
                expenses.remove(expense)
                save_expenses(expenses)
                print("\nExpense deleted successfully.")
            else:
                print("\nDeletion cancelled.")

            break

    if not found:
        print("\nExpense ID not found.")
        
        
def edit_expense():
    print("\n" + "=" * 50)
    print(" " * 17 + "EDIT EXPENSE")
    print("=" * 50)

    while True:
        try:
            expense_id = int(input("Enter Expense ID: "))

            if expense_id > 0:
                break
            else:
                print("Expense ID must be greater than 0.")

        except ValueError:
            print("Enter a valid Expense ID!")
     
            
    found = False
    
    for expense in expenses:
        if expense['id'] == expense_id:
            found = True
            
            print("\n" + "-" * 15 + " CURRENT EXPENSE " + "-" * 15)
            
            print(f"ID              : {expense['id']}")
            print(f"Category        : {expense['category']}")
            print(f"Description     : {expense['description']}")
            print(f"Amount          : ₹{expense['amount']}")
            print(f"Payment Method  : {expense['payment_method']}")
            break
    
    if not found :
        print("Expense ID not found.")
        
        return
        
    
    print('\n' + "-" * 50)
    print(" " * 17 + "WHAT DO YOU WANT TO EDIT?")
    print("-" * 50 + "\n")
        
    print("1. Category")
    print("2. Description")
    print("3. Amount")
    print("4. Payment Method")
    print("5. Cancel\n")
    
    choice = input("Enter a Choice: ")
    
    if choice == '1' :
        pass
        
    elif choice == '2':
        pass
    
    elif choice == '3':
        pass
        
    elif choice == '4':
        pass
        
    elif choice == '5':
        pass
        
    else:
        pass
        