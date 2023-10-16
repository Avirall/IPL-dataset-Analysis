import csv
# Open the CSV file
import matplotlib.pyplot as plt
# importing matplot to plot charts

with open('archive/deliveries.csv', newline='') as csvfile:
    # Create a DictReader object
    csv_reader = csv.DictReader(csvfile)
    
    extra_runs_per_team={}
    
    for row in csv_reader:
        if int(row['match_id'])>576 and int(row['match_id'])<637:
            if row['bowling_team'] not in extra_runs_per_team:
                extra_runs_per_team[row['bowling_team']]=int(row['extra_runs'])
            else:
                extra_runs_per_team[row['bowling_team']]+=int(row['extra_runs'])

plt.plot(extra_runs_per_team.keys(),extra_runs_per_team.values(),'-or')
plt.show()