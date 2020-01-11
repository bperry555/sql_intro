import os
import csv

csvpath = os.path.join("Resources", "election_data.csv")

canidate = []
vote_count = []
totalvote = 0

with open(csvpath, newline="") as csvfile:
    
    csvreader = csv.reader(csvfile, delimiter=',')
    csvheader = next(csvfile)

    for row in csvreader:
        totalvote += 1
        
        if row[2] not in canidate:
            canidate.append(row[2])
            vote_count.append(1)

        else: vote_count[canidate.index(row[2])] += 1

with open('pypollout.txt', 'w', newline='') as output:
    output.write(f'Election Resultsn\n') 
    output.write('-' * 80 + '\n')
    output.write(f'Total Votes: {totalvote}\n')
    output.write('-' * 80 + '\n')
    for name in range(len(canidate)):
        output.write(f'{canidate[name]}: {format(vote_count[name] / totalvote, ".3%")} ({vote_count[name]})\n')
    output.write('-' * 80 + '\n')
    output.write(f'Winner: {canidate[vote_count.index(max(vote_count))]}\n')
    output.write('-' * 80 + '\n')

print(f'Election Results')
print('-' * 80)
print(f'Total Votes: {totalvote}')
print('-' * 80)

for name in range(len(canidate)):
    print(f'{canidate[name]}: {format(vote_count[name] / totalvote, ".3%")} ({vote_count[name]})')

print('-' * 80)
print(f'Winner: {canidate[vote_count.index(max(vote_count))]}')
print('-' * 80)

