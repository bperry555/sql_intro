import os
import csv

# create and set variables for profit/loss, total months, greatest increase, greatestest decrease, average change, and previous profit/loss
pltotal = 0
months = 0
gincrease = 0
gdecrease = 0
avechange = 0
prevpl = 0

# set the path of the dataset.
csvpath = os.path.join("Resources", "budget_data.csv")

# open the csvfile
with open(csvpath, newline='') as csvfile:
    # use the reader function to iterate through the file.
    csvreader = csv.reader(csvfile, delimiter=',')
    # store the header into cvsheader and move to the next line.
    csvheader = next(csvreader)
    # iterate through the file
    for row in csvreader:
        # add each line to get the total of months
        months += 1
        # add all the profit/loss totals
        pltotal += int(row[1])
        # find the difference by taking the current profit/loss subracted by the previous profit/loss
        diff = int(row[1]) - prevpl
        # calculate the average change only if the previous profit/loss wasn't zero.
        if prevpl != 0:
            avechange += diff
        # checks to see if the new difference is bigger then any previous difference.  If it is, then it is the new greatest increase.
        if diff > gincrease:
            gincrease = diff
            imonth = row[0]
        # checks to see if the enew difference is less then any previous difference.  If it is, then it is the new lowest decrease.
        if diff < gdecrease:
            gdecrease = diff
            dmonth = row[0]
        # sets the previous profit/loss variable to check against the new profit/loss on the next row.
        prevpl = int(row[1])
# calculates the average change by dividing the average change by how many months there are minus 1 to acount for the first extry with no difference.
avechange = (avechange / (months - 1))
# prints all the output to "bankpyout.txt".
with open('bankpyout.txt', 'w', newline='') as output:
    output.write('Financial Analysis\n')
    output.write(('-' * 80) + '\n')
    output.write(f'Total Months: {months}\n')
    output.write(f'Total: ${pltotal}\n')
    output.write(f"Average Change: $  {format(avechange, '.2%')}\n")
    output.write(f'Greatest Increase in Profits: {imonth} (${gincrease})\n')
    output.write(f'Greatest Decrease in Profits: {dmonth} (${gdecrease})\n')
# prints all the output to the console.
print('Financial Analysis')
print("-" * 80)
print(f'Total Months: {months}')
print(f'Total: ${pltotal}')
print("Average Change: $" + "{0:.2f}".format(avechange,2))
print(f'Greatest Increase in Profits: {imonth} (${gincrease})')
print(f'Greatest Decrease in Profits: {dmonth} (${gdecrease})')