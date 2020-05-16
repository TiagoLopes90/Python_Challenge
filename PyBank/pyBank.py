import csv
file_path = 'Resources/budget_data.csv'

data=[]

with open(file_path) as csvfile:
    csvreader = csv.reader(csvfile,delimiter=',')
    csv_header = next(csvreader)
    for row in csvreader:
        data.append(row)

monthIncrease = data[0][0]
monthDecrease = data[0][0]
greatIncrease = 0.0
greatDecrease = 0.0
totalAmount = float(data[0][1])
totalChange = 0.0
monthCount = 1

for i in range(1,len(data)):
    monthCount+=1
    totalAmount+=float(data[i][1])
    change = float(data[i][1])-float(data[i-1][1])
    totalChange+=change
    if change > greatIncrease:
        greatIncrease = change
        monthIncrease = data[i][0]
    if change < greatDecrease:
        greatDecrease = change
        monthDecrease = data[i][0]


averageChange = float(totalChange/(monthCount-1))
#another option for the average :averageChange2 = float((float(data[-1][1])-(float(data[0][1])))/(monthCount-1))


#Writing TXT File
output_file = "Analysis/output.txt"

with open (output_file,'w') as output:

    output.write("Financial Analysis\n")
    output.write("--------------------------------------------\n")
    output.write(f'Total Months: {monthCount}\n')
    output.write(f'Total: {totalAmount}\n')
    output.write(f'Average Change: {round(averageChange,2)}\n')
    output.write(f'Greatest Increase in Profits: {monthIncrease} (${str(greatIncrease)})\n')
    output.write(f'Greatest Decrease in Profits: {monthDecrease} (${str(greatDecrease)})')

#Print at the terminal
print(f'Financial Analysis\n--------------------------------------------\nTotal Months: {monthCount}\nTotal: {totalAmount}\nAverage Change: {round(averageChange,2)}\nGreatest Increase in Profits: {str(monthIncrease)} (${str(greatIncrease)})\nGreatest Decrease in Profits: {monthDecrease} (${str(greatDecrease)})')


