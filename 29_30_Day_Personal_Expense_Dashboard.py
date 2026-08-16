# Days 29-30 - Personal Expense Dashboard

class ExpenseTracker:
    def __init__(self):
        self.expenses = []

    def add_expense(self, item, category, amount):
        record = {"item": item, "category": category, "amount": amount}
        self.expenses.append(record)
        print("Recorded expense for:", item)

    def total_spending(self):
        return sum(e["amount"] for e in self.expenses)

    def summary_by_category(self):
        categories = {}
        for e in self.expenses:
            cat = e["category"]
            categories[cat] = categories.get(cat, 0) + e["amount"]
        return categories

    def show_dashboard(self):
        print("\n==================================")
        print("    PERSONAL EXPENSE DASHBOARD    ")
        print("==================================")
        for e in self.expenses:
            print(f"- {e['item']:15} [{e['category']:10}] : ${e['amount']:.2f}")
        
        print("----------------------------------")
        print("Total Spending:", f"${self.total_spending():.2f}")
        print("\nCategory Breakdown:")
        for cat, amt in self.summary_by_category().items():
            print(f" * {cat:10} : ${amt:.2f}")
        print("==================================")

# Testing the Capstone Project
tracker = ExpenseTracker()
tracker.add_expense("Groceries", "Food", 45.50)
tracker.add_expense("Bus Fare", "Transport", 12.00)
tracker.add_expense("Dinner Out", "Food", 28.00)
tracker.add_expense("Book", "Education", 15.00)

tracker.show_dashboard()