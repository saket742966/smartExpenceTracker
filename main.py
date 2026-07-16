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
print(menu)

choice = int(input("Enter your choice: "))
print(choice)

if choice == 1:
    print("Add Expence Selected")

elif choice == 2:
    print("View Expenses Selected")
    
elif choice == 3:
    print("Search Expenses Selected")
    
elif choice == 4:
    print("Edit Expenses Selected")

elif choice == 5:
    print("Delete Expenses Selected")

elif choice == 6:
    print("Reports Selected")
    
elif choice == 7:
    print("Save Data Selected")
    
elif choice == 8:
    print("Exited")
    
else: 
    print("Invalid Input !!")