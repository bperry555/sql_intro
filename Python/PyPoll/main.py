import os
import csv

#set path of data set
csvpath = os.path.join("Resources", "election_data.csv")

#create an empty list to store canidate names into.
canidate = []
#create an empty list to store how many votes each canidate recieves.
vote_count = []
#create and set our total vote count vairable to zero.
totalvote = 0

# Open the csv as the object csvfile.
with open(csvpath, newline="") as csvfile:
    #use the reader fuction to itirate through the csv file with csvreader.
    csvreader = csv.reader(csvfile, delimiter=',')
    # Store the header into cvsheader and move to the next line in csvreader.
    csvheader = next(csvfile)
    #itorate through the whole csv file, count total votes.
    for row in csvreader:
        totalvote += 1
        
        # check if canidate name isn't in the list of canidates, add their name to it and add 1 vote in the vote count list.
        if row[2] not in canidate:
            canidate.append(row[2])
            vote_count.append(1)
        #if their name is in the list, find where in the index their name is and add a vote to the corresponding index.
        else: vote_count[canidate.index(row[2])] += 1

#Write output to pypollout.txt with proper formatting.
with open('pypollout.txt', 'w', newline='') as output:
    output.write(f'Election Resultsn\n') 
    output.write('-' * 80 + '\n')
    output.write(f'Total Votes: {totalvote}\n')
    output.write('-' * 80 + '\n')
    #find how many canidates were found in the file and print them all out with proper stats and formatting.
    for name in range(len(canidate)):
        output.write(f'{canidate[name]}: {format(vote_count[name] / totalvote, ".3%")} ({vote_count[name]})\n')
    output.write('-' * 80 + '\n')
    output.write(f'Winner: {canidate[vote_count.index(max(vote_count))]}\n')
    output.write('-' * 80 + '\n')

#prints same results to the console instead of the pypollout.txt file.
print(f'Election Results')
print('-' * 80)
print(f'Total Votes: {totalvote}')
print('-' * 80)

for name in range(len(canidate)):
    print(f'{canidate[name]}: {format(vote_count[name] / totalvote, ".3%")} ({vote_count[name]})')

print('-' * 80)
print(f'Winner: {canidate[vote_count.index(max(vote_count))]}')
print('-' * 80)

