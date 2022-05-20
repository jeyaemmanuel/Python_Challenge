from operator import countOf
import os
import csv

#Path to collect data from the resources folder
pybank_csv = os.path.join('Resources','budget_data.csv')
total_months = 0
total_profit_losses = 0
greatest_increase_profits = 0
greatest_decrease_losses = 0
average_profit_losses = 0

def budget_analysis(budget_data):
    global total_months
    global total_profit_losses
    global greatest_increase_profits
    global greatest_decrease_losses
    global average_profit_losses

    budget_date = budget_data[0]
    profit_losses = int(budget_data[1])
        
    total_months = total_months + 1
    total_profit_losses = total_profit_losses + profit_losses
    
    # greatest_increase_profits = profit_losses.max()
    # greatest_decrease_losses = profit_losses.min()

    if greatest_increase_profits < profit_losses:
        greatest_increase_profits = profit_losses
    else:
        greatest_decrease_losses = profit_losses
    

    # print(total_months)
    # print(total_profit_losses)
    # print(average_profit_losses)

with open(pybank_csv, 'r') as csvfile:

    csvreader = csv.reader(csvfile,delimiter =',')
    header = next(csvreader)
    for row in csvreader:
        budget_analysis(row)
    # average_profit_losses = total_profit_losses / total_months
    print(total_months)
    print(total_profit_losses)
    print(average_profit_losses)   
    print(greatest_increase_profits)
    print(greatest_decrease_losses)

   


# Your task is to create a Python script that analyses the records to calculate each of the following:


# The total number of months included in the dataset


# The net total amount of "Profit/Losses" over the entire period


# The average of the changes in "Profit/Losses" over the entire period


# The greatest increase in profits (date and amount) over the entire period


# The greatest decrease in losses (date and amount) over the entire period




# As an example, your analysis should look similar to the one below:

# Financial Analysis
# ----------------------------
# Total Months: 86
# Total: $38382578
# Average  Change: $-2315.12
# Greatest Increase in Profits: Feb-2012 ($1926159)
# Greatest Decrease in Profits: Sep-2013 ($-2196167)




# In addition, your final script should both print the analysis to the terminal and export a text file with the results.