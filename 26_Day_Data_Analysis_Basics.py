# Day 26 - Basic data processing with tables

# Representing a tabular dataset using dictionaries
data = [
    {"Name": "Item A", "Price": 10, "Quantity": 5},
    {"Name": "Item B", "Price": 20, "Quantity": 2},
    {"Name": "Item C", "Price": 15, "Quantity": 4}
]

print("Data Table Overview:")
total_revenue = 0

for row in data:
    item_total = row["Price"] * row["Quantity"]
    total_revenue += item_total
    print(row["Name"], "- Revenue:", item_total)

print("Total Revenue across all items:", total_revenue)