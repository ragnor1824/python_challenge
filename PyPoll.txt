#Allow us to create file paths across operation systems and read CSV file
import os
import csv

#Assign CSV path to CSV you want it to read
csvpath = "/Users/reneeagnor/Desktop/Homework/python_challenge_old/PyPoll/Resources/election_data.csv"

#Plain reading of the CSV file and assigning variables
with open (csvpath) as PyPoll_data:
    reader = csv.reader(PyPoll_data, delimiter=",") 
    header = next(reader)
    first_row = next(reader)
    canidate_name = []
    votes = {}
    count = 1
    canidate_votes = 0

    #Create a dictionary of unique canidate names and count time's their name is mentioned
    for row in reader:
        name = (row[2])
        if name in votes:
            canidate_votes = votes[name] + 1
            votes.update({name:canidate_votes})
        else:
            votes[name] = 1
       
        list_of_votes = list(dict.values(votes))
       
        count = count + 1

        #If candiate name is not in list, then append(add) to list
        canidate_first = (row[2])
        if canidate_first not in canidate_name:
            canidate_name.append(canidate_first)

#Perform algetbra to get canidates % of vote and convert to percentage
c_votes = (list_of_votes[0]/(count))
c_votes_percent = "{:.3%}".format(c_votes)
d_votes = (list_of_votes[1]/(count))
d_votes_percent = "{:.3%}".format(d_votes)
r_votes = (list_of_votes[2]/(count))
r_votes_percent = "{:.3%}".format(r_votes)

#Find canidate with the popular code
popular_vote = max(votes.values())
canidate_popular_vote = list(votes.keys())[list(votes.values()).index(popular_vote)]

#Print full statemet
print("Election Results")
print("------------------------------------")
print("Total votes: " + str(count))
print("------------------------------------")
print("Charles Casper Stockham: " + str(c_votes_percent) + " (" + str(list_of_votes[0]) + ")")
print("Diana DeGette: " + str(d_votes_percent) + " (" + str(list_of_votes[1]) + ")")
print("Raymon Anthony Doane: " + str(r_votes_percent) + " (" + str(list_of_votes[2]) + ")")
print("------------------------------------")
print("Winner: " + str(canidate_popular_vote))