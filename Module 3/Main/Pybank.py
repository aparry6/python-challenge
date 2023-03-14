import csv
from datetime import datetime

# Set file name
file_name = "budget_data.csv"

# Set initial values
total_months = 0
total_profit_loss = 0
previous_profit_loss = None
profit_loss_changes = []
greatest_increase = {"date": None, "amount": 0}
greatest_decrease = {"date": None, "amount": 0}

# Open CSV file and read it
with open(file_name, "r") as file:
    csv_reader = csv.reader(file, delimiter=",")

    # Skip header row
    next(csv_reader)

    # Loop through each row in CSV file
    for row in csv_reader:
        # Count the total number of months
        total_months += 1

        # Get profit/loss for current month
        profit_loss = int(row[1])

        # Add profit/loss to total
        total_profit_loss += profit_loss

        # Calculate change in profit/loss since previous month
        if previous_profit_loss is not None:
            change = profit_loss - previous_profit_loss
            profit_loss_changes.append(change)

            # Check if greatest increase or decrease in profits
            if change > greatest_increase["amount"]:
                greatest_increase["date"] = row[0]
                greatest_increase["amount"] = change

            if change < greatest_decrease["amount"]:
                greatest_decrease["date"] = row[0]
                greatest_decrease["amount"] = change

        # Set previous profit/loss for next iteration
        previous_profit_loss = profit_loss

# Calculate average change in profit/loss
average_change = sum(profit_loss_changes) / len(profit_loss_changes)

# Print results to console
print("Financial Analysis")
print("------------------")
print(f"Total Months: {total_months}")
print(f"Total: ${total_profit_loss}")
print(f"Average Change: ${average_change:.2f}")
print(f"Greatest Increase in Profits: {greatest_increase['date']} (${greatest_increase['amount']})")
print(f"Greatest Decrease in Profits: {greatest_decrease['date']} (${greatest_decrease['amount']})")

