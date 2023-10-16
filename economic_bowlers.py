import csv
import matplotlib.pyplot as plt

with open('archive/deliveries.csv', newline='') as csvfile:
    dataset = csv.DictReader(csvfile)

    bowlers = {}
    bowlers_overs = {}
    for row in dataset:
        if 1 <= int(row['match_id']) <= 59:
            if row['bowler'] not in bowlers and row['is_super_over']!=1:
                bowlers[row['bowler']] = int(row['total_runs']) - int(row['legbye_runs']) - int(row['bye_runs'])
                bowlers_overs[row['bowler']]=1
            else:
                bowlers[row['bowler']] += int(row['total_runs']) - int(row['legbye_runs']) - int(row['bye_runs'])
                bowlers_overs[row['bowler']]+=1
for i in bowlers_overs:
    bowlers_overs[i]=bowlers_overs[i]/6
    bowlers[i]=bowlers[i]/bowlers_overs[i]

bowlers=dict(sorted(bowlers.items(),key=lambda items: items[1]))

plt.plot(list(bowlers.values())[:10],list(bowlers.keys())[:10],'-o')
plt.show()
