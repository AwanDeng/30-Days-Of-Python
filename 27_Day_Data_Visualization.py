# Day 27 - Text-based data visualization

# Representing data as a chart in text format
sales_data = {
    "Monday": 5,
    "Tuesday": 8,
    "Wednesday": 3,
    "Thursday": 10,
    "Friday": 7
}

print("--- Weekly Sales Chart (Text Bar Graph) ---")
for day, value in sales_data.items():
    bar = "*" * value
    print(f"{day:10} | {bar} ({value})")