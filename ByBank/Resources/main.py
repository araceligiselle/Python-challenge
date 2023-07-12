import os
import csv
 
budget_csv = os.path.join('..', 'Resources', "budget_data.csv")

row_count = 0
data = []

with open(budget_csv) as budget_file:
    csvbudget = csv.reader(budget_file, delimiter=',')

    csv_header = next(csvbudget)
    print(csv_header)

    data = list(csvbudget)

    for row in csvbudget:
        print(row)

'Calculate Months'
row_count = len(data)

print('Total Months: ', row_count)

'Calculate Total Profit/Loses'
total_profit_losses = 0

for row in data:
    profit_loss = int(row[1])
    total_profit_losses += profit_loss

print('Total Profit/Losses: $',total_profit_losses)

'Calculate the average change'
changes = []
average_change = 0
num_changes = row_count - 1

if num_changes > 0:
    total_change = 0
    for i in range(1, row_count):
        current_loss = int(data[i][1])
        prev_profit_loss = int(data[i-1][1])
        change = current_loss - prev_profit_loss
        total_change += change

    average_change = total_change / num_changes

print('Average Change: $', format(average_change, ',.2f'))

'Calculate the Greatest Increase/Decrease'
current_change = 0
great_increase = 0
increase_changes_date = ""
great_decrease = 0
decrease_changes_date = ""
prev_profit_loss = None

for row in data:
    date = row[0]
    profit_loss = int(row[1])
    
    if prev_profit_loss is not None:
        current_change = profit_loss - prev_profit_loss
        changes.append(current_change)

    if current_change > great_increase:
        great_increase = current_change
        increase_changes_date = date
    
    if current_change < great_decrease:
        great_decrease = current_change
        decrease_changes_date = date

    prev_profit_loss = profit_loss

if great_increase !=0 and great_decrease !=0:
    print('Greatest Increase in Profits: ', increase_changes_date, '$' + format(great_increase))
    print('Greatest Decrease in Profits: ', decrease_changes_date, '$' + format(great_decrease))

'Export to Text file'
print(budget_file)
output_file = 'financial_analysis.txt'
with open(output_file, 'w') as txt_file:
    first_output = (
        f'Total Months: {row_count}\n'
        f'Total Profit/Losses: ${total_profit_losses}\n'
    )
    txt_file.write(first_output)
    total_change = 0
    for i in range(1, row_count):
        current_loss = int(data[i][1])
        prev_profit_loss = int(data[i-1][1])
        change = current_loss - prev_profit_loss
        total_change += change
    average_change = total_change / num_changes
    next_output = (f'Average Change: ${average_change:.2f}\n')
    txt_file.write(next_output)
    final_output = (
        f'Greatest Increase in Profits: {increase_changes_date}, ${great_increase}\n'
        f'Greatest Decrease in Profits: {decrease_changes_date}, ${great_decrease}\n'
    )
    txt_file.write(final_output)
