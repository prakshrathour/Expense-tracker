import json

try:
    with open("expense.json", "r") as file:
        expense = json.load(file)
except FileNotFoundError:
    expense = []

def save_data():
    with open("expense.json", "w") as file:
        json.dump(expense, file, indent=4)

print("Welcome to the Expense Tracker !")

def add_exp():
    while True:
        category = input("Enter the category: ").strip()
        if category == "":
            print("Category cannot be empty.")
        else:
            category = category.title()
            break

    while True:
        try:
            amount = float(input(f"Enter the amount spent on {category}: "))
            if amount <= 0:
                print("Amount must be greater than 0.")
                continue
            break
        except ValueError:
            print("Invalid input! Please enter a numeric value.")

    note = input("Enter the note (optional): ").strip()
    if note == "":
        note = "No note"


    expense.append({
        "category": category,
        "amount": amount,
        "note": note
    })

    print(f"✅ Added: {category} | {amount} | {note}")
    save_data()


def view_exp():
    if not expense:
        print("\n⚠️ No Expenses Available.\n")
        return

    print("\n📊 Your Expenses:")
    print("-" * 50)
    print(f"{'ID':<5}{'Category':<15}{'Amount':<10}{'Note'}")
    print("-" * 50)

    for i, item in enumerate(expense, start=1):
        print(f"{i:<5}{item['category']:<15}{item['amount']:<10}{item['note']}")

    print("-" * 50)

def total():
    total_spend = 0

    for item in expense:
        total_spend += item["amount"]

    print(f"\n💰 Total Spending: ₹{total_spend:.2f}\n")

def category_spend():
    if not expense:
        print("\n⚠️ No Expenses Available.\n")
        return

    category_totals = {}

    for item in expense:
        cat = item["category"]
        category_totals[cat] = category_totals.get(cat, 0) + item["amount"]

    print("\n📊 Category-wise Spending:")
    print("-" * 30)

    for cat, total in category_totals.items():
        print(f"{cat:<15} : ₹{total:.2f}")

    print("-" * 30)
    

def edit_exp():
    if not expense:
        print("No expenses to edit.")
        return

    view_exp()

    while True:
        try:
            edit_id = int(input("Enter the ID to edit ✏️ : "))
            break
        except ValueError:
            print("Invalid input! Please enter a number.")

    index = edit_id - 1

    if not (0 <= index < len(expense)):
        print("ID not found.")
        return

    item = expense[index]
    print(f"\nEditing: {item['category']} | {item['amount']} | {item['note']}")
    print("(Press Enter to keep the current value)\n")

    new_category = input(f"Category [{item['category']}]: ").strip()
    if new_category:
        item['category'] = new_category.title()

    while True:
        new_amount = input(f"Amount [{item['amount']}]: ").strip()
        if new_amount == "":
            break
        try:
            new_amount = float(new_amount)
            if new_amount <= 0:
                print("Amount must be greater than 0.")
                continue
            item['amount'] = new_amount
            break
        except ValueError:
            print("Invalid input! Please enter a numeric value.")

    new_note = input(f"Note [{item['note']}]: ").strip()
    if new_note:
        item['note'] = new_note

    print(f"✅ Updated: {item['category']} | {item['amount']} | {item['note']}")
    save_data()


def del_exp():
    if not expense:
        print("No expenses to delete.")
        return

    view_exp()

    while True:
        try:
            delete = int(input("Enter the ID to delete 🗑️: "))
            break
        except ValueError:
            print("Invalid input! Please enter a number.")

    index = delete - 1

    if 0 <= index < len(expense):
        expense.pop(index)
        print("Deleted successfully.")
    else:
        print("ID not found.")
    save_data()

while True:
    print("\n========= Expense Tracker =========")
    print("1. ➕ Add Expense")
    print("2. 📋 View Expenses")
    print("3. 💰 Total Spending")
    print("4. 📊 Category Spending")
    print("5. ❌ Delete Expense")
    print("6. ✏️ Edit Entry")
    print("7. 🚪 Exit")
    print("===================================")

    while True:
        try:
            choice=int(input("Enter a valid choice from above : "))
            break
        except ValueError:
            print("Invalid input! Please enter a number.")


    if choice==1:
        add_exp()
    elif choice==2:
        view_exp()
    elif choice==3:
        total()
    elif choice==4:
        category_spend()
    elif choice==5:
        del_exp()
    elif choice==6:
        edit_exp()
    elif choice==7:
        print("Exiting...")
        break
    else:
        print("Enter a valid option...")

