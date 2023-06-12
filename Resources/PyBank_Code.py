# Allow us to create file paths across operations systems and read CSV files
import os
import csv

#Assign CSV path to CSV file you want it to read
csvpath = "/Users/reneeagnor/Desktop/Homework/python_challenge_old/PyBank/Resources/budget_data.csv"


#Plain Reading of the CSV File and assign variables
with open(csvpath) as PyBank_data:
    reader = csv.reader(PyBank_data, delimiter=",")
    header = next(reader)
    first_row = next(reader)
    first_net = int(first_row[1])
    prev_net= first_net
    total_net =first_net
    count = 1
    list_changes=[]
    greatest_increase = 0
    greatest_increase_month = " "
    greatest_decrease = 0
    greatest_decrease_month = " "

    #Find the difference between rows of profit/Find greatest increase and decrese with corresponding months
    for row in reader:
        total_net+=int(row[1])
        count = count + 1
        net_change = int(row[1])-prev_net
        list_changes+=[net_change]
        prev_net=int(row[1])
        avg= sum(list_changes)/len(list_changes)
        if net_change > greatest_increase:
            greatest_increase = net_change
            greatest_increase_month = str(row[0])
        if net_change < greatest_decrease:
            greatest_decrease = net_change
            greatest_decrease_month = str(row[0])

#Round the average to 2 decimal places
average_change_rounded = round(avg,2)

#Print statements
print ("Financial Analysis")
print ("-----------------------------")
print("Total Months: " + str(count))
print("Total: " + "$" + str(total_net))
print("Average Change: " + "$" + str(average_change_rounded))
print("Greatest Increase in Profits: " + str(greatest_increase_month) + " ($" + str(greatest_increase) + ")")
print("Greatest Decrease in Profits: " + str(greatest_decrease_month) + " ($" + str(greatest_decrease) + ")")
