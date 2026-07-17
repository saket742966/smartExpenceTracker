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


