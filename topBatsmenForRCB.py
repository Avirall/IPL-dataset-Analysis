import csv
# Open the CSV file
import matplotlib.pyplot as plt
# importing matplot to plot charts

with open('archive/deliveries.csv', newline='') as csvfile:
    # Create a DictReader object
    csv_reader = csv.DictReader(csvfile)
   
    #creating an empty dictionary to store values
    teams_total_score={}
    
    # Iterate through the CSV data
    for row in csv_reader:
        if row['batting_team'] == 'Royal Challengers Bangalore' and row['batsman'] not in teams_total_score:
            teams_total_score[row['batsman']]=int(row['batsman_runs'])
        elif row['batting_team'] == 'Royal Challengers Bangalore':
            teams_total_score[row['batsman']]=teams_total_score[row['batsman']]+int(row['batsman_runs'])
sorted_batsmen=sorted(teams_total_score.items(), key= lambda item:item[1],reverse=True)
x=[item[0] for item in sorted_batsmen[0:10]]
y=[item[1] for item in sorted_batsmen[0:10]]
plt.pie(y,labels=x,autopct='%1.1f%%')
plt.show()
