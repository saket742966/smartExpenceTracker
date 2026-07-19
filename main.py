from expense_manager import *


menu = '''
==================================================
              SMART EXPENSE TRACKER
==================================================

Welcome! Manage your daily expenses with ease.

-------------------- MENU --------------------

  1. Add Expense
  2. View Expenses
  3. Search Expenses
  4. Edit Expense
  5. Delete Expense
  6. Reports
  7. Save Data
  8. Exit

------------------------------------------------

'''

while True: 
    
    print(menu)

    choice = int(input("Enter your choice: "))
    print(choice)

    if choice == 1:
        add_expense()

    elif choice == 2:
        view_expenses()
        
    elif choice == 3:
        search_expense()
                
    elif choice == 4:
        edit_expense()

    elif choice == 5:
        delete_expense()

    elif choice == 6:
        print("Reports Selected")
        
    elif choice == 7:
        print("Save Data Selected")
        
    elif choice == 8:
        break
        
    else: 
        print("Invalid Input !!")