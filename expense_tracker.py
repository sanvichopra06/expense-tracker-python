def add_expense(expenses):
        print("Adding an expense")
        #dictionary stores data as key-value pairs.
        amount = int(input("Enter amount to add: "))
        category = input("Enter category of expense: ")
        desc = input("Add a description of the expense: ")
        expense = {
            "amount" : amount,
            "category" : category,
            "description" : desc
        }
        expenses.append(expense) 

def view_expenses(expenses):
    print("View all expenses")
    if not expenses: 
        print("No Expenses to display")
    else:
        print(f"{'Amount':<12}{'Category':<15}{'Description':<25}") 
        #using f-strings for tabular formatting
        for i in expenses: 
            print(f"{i['amount']:<12}{i['category']:<15}{i['description']:<25}")
     
def total_expenses(expenses):
    total = 0
    if not expenses:
        print("No Expenses to display")
    else:
        for i in expenses:
            total += i['amount']
    return total

def spending_by_category(expenses):
    cat_expenses = {}
    if not expenses:
            print("No Expenses to display")
    else:
        for i in expenses:
            cat_expenses[i['category']]= cat_expenses.get(i['category'],0) + i['amount']
            #.get() gives the value for a key pair
        for key, value in cat_expenses.items(): 
            print(f"{key:<12}{value:<15}")
           
            
print("Expense Tracker: Track your money, one expense at a time")
expenses = [] #list stores multiple items in a single variable.
while (True): 
    choice= int(input("Choose a Task to manage your expenses: \n" 
    "1. Add a new expense\n" 
    "2. View all expenses\n"
    "3. View total spending\n"
    "4. View spending by category\n"
    "5. Exit\n"))

    if choice == 1:
        add_expense(expenses)
    elif choice == 2:
        view_expenses(expenses)
    elif choice == 3:
        print("Total spending", total_expenses(expenses))
    elif choice == 4: 
        print("Spending by Category")
        spending_by_category(expenses)
    elif choice == 5:
        break
    else:
        print("Error- Enter a number between 1 & 5")