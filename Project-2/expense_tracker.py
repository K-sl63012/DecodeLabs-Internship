total = 0

print("===== EXPENSE TRACKER =====")

while True:
    expense = float(input("Enter expense: "))
    total = total + expense

    choice = input("Add another expense? (yes/no): ")

    if choice.lower() == "no":
        break
    elif choice.lower() != "yes":
        print("Invalid choice. Please enter yes or no.")

print("\nTotal Spent: ₹", total)
print("Thank you for using the Expense Tracker!")