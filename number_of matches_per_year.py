import csv
# Open the CSV file
import matplotlib.pyplot as plt
# importing matplot to plot charts

with open('archive/matches.csv', newline='') as csvfile:
    # Create a DictReader object
    csv_reader = csv.DictReader(csvfile)
    
    number_of_matches={}
    for row in csv_reader:
        if row['season'] not in number_of_matches:
            number_of_matches[row['season']]=1
        else:
            number_of_matches[row['season']]+=1

plt.bar(sorted(number_of_matches.keys()),sorted(number_of_matches.values()))
plt.show()