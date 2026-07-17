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