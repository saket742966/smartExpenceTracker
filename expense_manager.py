expenses = []

def add_expense():
    category = input("Enter Category of Expense: ")
    description = input("Enter a description: ")
    amount = int(input("Enter Amount: "))
    payment_method = input("Payment Method used: ")
    
    
    expense_data = {
        "category": category,
        "description": description,
        "amount": amount,
        "payment_method": payment_method
    }
    
    print("Expense Added Successfully")
    expenses.append(expense_data)


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
        print(f"Category        : {expense['category']}")
        print(f"Description     : {expense['description']}")
        print(f"Amount          : ₹{expense['amount']}")
        print(f"Payment Method  : {expense['payment_method']}")

    print("\n" + "=" * 50)
    print(f"Total Expenses: {len(expenses)}")
    print("=" * 50)