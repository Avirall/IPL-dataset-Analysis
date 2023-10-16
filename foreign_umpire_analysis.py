import csv
# Open the CSV file
import matplotlib.pyplot as plt
# importing matplot to plot charts

with open('archive/matches.csv', newline='') as csvfile:
    # Create a DictReader object
    csv_reader = csv.DictReader(csvfile)
    
    umpire_names=set()
    
    for row in csv_reader:
        umpire_names.add(row['umpire1'])
        umpire_names.add(row['umpire2'])

print(umpire_names)
print(len(umpire_names))

with open('archive/umpires.csv', newline='') as csvfile:
    # Create a DictReader object
    csv_reader = csv.DictReader(csvfile)
    
    umpire_nation={}
    for row in csv_reader:
        if row['umpire'] in umpire_names and row[' country'] !=' India':
            umpire_nation[row['umpire']]=row[' country']
    print(umpire_nation)
    
    plt.bar(umpire_nation.values(),umpire_nation.keys())
    plt.show()