# Import modules
import csv
import os

# Create variables
date = []
profit_loss = []
profit_loss_change = []

# Create path to csv file
csvpath = os.path.join("Resources", "budget_data.csv")

# Read the csv
with open(csvpath, 'r') as csvfile:
    
    # Create the csvreader object
    csvreader = csv.reader(csvfile)

    # Store the header and iterate past it
    header = next(csvreader)

    # Write csv data to lists
    for row in csvreader:
        date.append(row[0])
        profit_loss.append(int(row[1]))

# Populate the month over month change in profit/loss
for x in range(1, len(profit_loss)):
    last_profit_loss = profit_loss[x - 1]
    current_profit_loss = profit_loss[x]
    profit_loss_change.append(current_profit_loss - last_profit_loss)

# CREATE FUNCTIONS TO CALCULATE FINAL DATA

# Calculate total from a list
def calc_list_sum(list):
    # Initialize counter
    total = 0
    # Iterate through the list and add to counter
    for x in list:
        total += x
    # Return calculated total
    return total

def find_max_change(list):
    max_change = 0
    for x in list:
        # Check if current value is largest in list
        if x > max_change:
            max_change = x
    return max_change

def find_min_change(list):
    min_change = 0
    for x in list:
        # Check if current value is smallest in list
        if x < min_change:
            min_change = x
    return min_change

# Create variables for final outputs
total_months = len(date)
total_profit_loss = calc_list_sum(profit_loss)
total_profit_loss_change = calc_list_sum(profit_loss_change)
average_profit_loss_change = round(total_profit_loss_change / len(profit_loss_change), 2)
greatest_profit_increase = find_max_change(profit_loss_change)
greatest_profit_increase_month = date[profit_loss_change.index(greatest_profit_increase) + 1]
greatest_profit_decrease = find_min_change(profit_loss_change)
greatest_profit_decrease_month = date[profit_loss_change.index(greatest_profit_decrease) + 1]

# Store financial analysis string lines
line_1 = "Financial Analysis"
line_2 = "----------------------------"
line_3 = f"Total Months: {total_months}"
line_4 = f"Total: ${total_profit_loss}"
line_5 = f"Average Change: ${average_profit_loss_change}"
line_6 = f"Greatest Increase in Profits: {greatest_profit_increase_month} (${greatest_profit_increase})"
line_7 = f"Greatest Decrease in Profits: {greatest_profit_decrease_month} (${greatest_profit_decrease})"

# Zip up the report 
report = [line_1, line_2, line_3, line_4, line_5, line_6, line_7]

# Print the report
for line in report:
        print(line)

# Create outfile path
outfile_path = os.path.join("analysis", "analysis.txt")

# Zip up report for export
report_zip = zip(report)

# Print report and export a text file with results
with open(outfile_path, "w") as txtfile:
    # Create writer
    writer = csv.writer(txtfile)

    # Write rows to outfile
    writer.writerows(report_zip)