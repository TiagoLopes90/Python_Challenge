import csv

def elections(data, output_file):
    #initiate variables
    candidate_list = []
    candidate_count= []
    totalvotes = 0
    #iterate over the list
    for x in data:
        totalvotes+=1
        #verify if it exist in the list
        if x not in candidate_list:
            #append new candidate
            candidate_list.append(x)
            candidate_count.append(int(0))
        #count based on candidate list
        for i in range(len(candidate_list)):
            if x == candidate_list[i]:
                candidate_count[i] = candidate_count[i]+1
    #defining %
    percentages = [round((number/totalvotes)*100,3) for number in candidate_count]
    
    #Defining Winner
    winner_percentage = 0.0

    for i in range(len(percentages)):
        if percentages[i] > winner_percentage:
            winner_percentage= percentages[i]
            winner = candidate_list[i]
    

    #Print Results
    print("Elections Results")
    print("--------------------------------------------")
    print(f'Total Votes: {totalvotes}')
    print("--------------------------------------------")
    for i in range(len(candidate_list)):
        print(f'{candidate_list[i]}: {percentages[i]}% ({candidate_count[i]})')
    print("--------------------------------------------")
    print(f'Winner: {winner}')
    print("--------------------------------------------")

    #Create output file
    with open(output_file,'w') as output:
        output.write("Elections Results\n")
        output.write("--------------------------------------------\n")
        output.write(f'Total Votes: {totalvotes}\n')
        output.write("--------------------------------------------\n")
        for i in range(len(candidate_list)):
            output.write(f'{candidate_list[i]}: {percentages[i]}% ({candidate_count[i]})\n')
        output.write("--------------------------------------------\n")
        output.write(f'Winner: {winner}\n')
        output.write("--------------------------------------------")


    
    

file_path = "Resources/election_data.csv"

output_path = "Analysis/election_results.txt"

candidate = []

with open(file_path) as csvfile:
    csvreader = csv.reader(csvfile, delimiter = ',')

    csv_header = next(csvreader)

    #iterate over the file
    for row in csvreader:
        candidate.append(row[2])


elections(candidate,output_path)