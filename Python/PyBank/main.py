import os
import csv

pltotal = 0
months = 0
gincrease = 0
gdecrease = 0
avechange = 0
prevpl = 0

csvpath = os.path.join("Resources", "budget_data.csv")

with open(csvpath, newline='') as csvfile:

    csvreader = csv.reader(csvfile, delimiter=',')

    csvheader = next(csvreader)

    for row in csvreader:
        months += 1
        
        pltotal += int(row[1])
        
        diff = int(row[1]) - prevpl
        
        if prevpl != 0:
            avechange += diff

        if diff > gincrease:
            gincrease = diff
            imonth = row[0]
        
        if diff < gdecrease:
            gdecrease = diff
            dmonth = row[0]
        
        prevpl = int(row[1])

avechange = (avechange / (months - 1))

with open('bankpyout.txt', 'w', newline='') as output:
    output.write('Financial Analysis\n')
    output.write(('-' * 80) + '\n')
    output.write(f'Total Months: {months}\n')
    output.write(f'Total: ${pltotal}\n')
    output.write("Average Change: $" + "{0:.2f}\n".format(avechange,  2))
    output.write(f'Greatest Increase in Profits: {imonth} (${gincrease})\n')
    output.write(f'Greatest Decrease in Profits: {dmonth} (${gdecrease})\n')

print('Financial Analysis')
print("-" * 80)
print(f'Total Months: {months}')
print(f'Total: ${pltotal}')
print("Average Change: $" + "{0:.2f}".format(avechange,2))
print(f'Greatest Increase in Profits: {imonth} (${gincrease})')
print(f'Greatest Decrease in Profits: {dmonth} (${gdecrease})')