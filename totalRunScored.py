import csv
# Open the CSV file
import matplotlib.pyplot as plt
# importing matplot to plot charts

with open('archive/matches.csv', newline='') as csvfile:
    # Create a DictReader object
    csv_reader = csv.DictReader(csvfile)
   
    #creating an empty dictionary to store values
    teams_total_score={}
    
    # Iterate through the CSV data
    for row in csv_reader:
        if row['team1'] not in teams_total_score:
            teams_total_score[row['batting_team']]=int(row['total_runs'])
        else:
            teams_total_score[row['batting_team']]=teams_total_score[row['batting_team']]+int(row['total_runs'])
print(teams_total_score)
teams_total_score['Rising Pune Supergiant']+=teams_total_score['Rising Pune Supergiants']
del teams_total_score['Rising Pune Supergiants']
print(teams_total_score)
teams=['SRH','RCB','MI','RSP','GL','KKR','KXIP','DD','CSK','RR','DC','Kochi Tuskers','Pune Warriors']
cstyle=['darkorange','darkred','blue','purple','orange','violet','red','cyan','yellow','turquoise','indigo','purple','gold']
plt.bar(teams,teams_total_score.values(),color=cstyle)
fonts={'family':'serif','color':'darkred','size':20}

plt.xlabel('Teams',fontdict=fonts)
plt.ylabel('Total Runs',fontdict=fonts)
plt.title('Total Runs Scored by each Team over the history of IPL',fontdict=fonts)
plt.show()      

