import csv
file_path = 'Resources/budget_data.csv'

greatestIncrease = [str(0),0.0]
greatestDecrease = [str(0),0.0]
totalAmount = 0.0
numberMonths = 0
print(type(totalAmount))

with open(file_path) as csvfile:
    csvreader = csv.reader(csvfile,delimiter=',')

    #look for header
    csv_header = next(csvreader)

    #Iterate over the file 
    for row in csvreader:
        numberMonths += 1
        totalAmount += float(row[1])
        #Calculate Greatest Increase and Decrease
        if float(greatestIncrease[1]) < float(row[1]):
            greatestIncrease = row
        if float(greatestDecrease[1]) > float(row[1]):
            greatestDecrease = row

averageChange = totalAmount/numberMonths

#Writing TXT File
output_file = "Analysis/output.txt"

with open (output_file,'w') as output:

    output.write("Financial Analysis\n")
    output.write("--------------------------------------------\n")
    output.write(f'Total Months: {numberMonths}\n')
    output.write(f'Total: {totalAmount}\n')
    output.write(f'Average Change: {round(averageChange,2)}\n')
    output.write(f'Greatest Increase in Profits: {str(greatestIncrease[0])} (${str(greatestIncrease[1])})\n')
    output.write(f'Greatest Decrease in Profits: {str(greatestDecrease[0])} (${str(greatestDecrease[1])})')

#Print at the terminal
print(f'Financial Analysis\n--------------------------------------------\nTotal Months: {numberMonths}\nTotal: {totalAmount}\nAverage Change: {round(averageChange,2)}\nGreatest Increase in Profits: {str(greatestIncrease[0])} (${str(greatestIncrease[1])})\nGreatest Decrease in Profits: {str(greatestDecrease[0])} (${str(greatestDecrease[1])})')


