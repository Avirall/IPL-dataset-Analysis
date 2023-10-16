import csv
import matplotlib.pyplot as plt

with open('archive/matches.csv', newline='') as csvfile:
    dataset = csv.DictReader(csvfile)
    
    Seasons={}
    for row in dataset:
        if row['season'] not in Seasons:
            Seasons[row['season']]={}
        if row['winner'] not in Seasons[row['season']]:
            Seasons[row['season']][row['winner']]=1
        else:
            Seasons[row['season']][row['winner']]+=1
            
sorted_matches_played = dict(sorted(Seasons.items(),key=lambda x : x[0]))

list_teams = []
for season_data in sorted_matches_played.values():
    for team in season_data.keys():
        if team not in list_teams:
            list_teams.append(team)

team_wins = {team: [year_data.get(team, 0) for year_data in sorted_matches_played.values()] for team in list_teams}
values = list(team_wins.values())
positions = [season for season in range(2008,2018)]
color_codes = [
    "#3366FF",  # Blue
    "#FFFF33",  # Yellow
    "#FF5733",  # Red 
    "#33FF57",  # Green
    "#FF33FF",  # Pink
    "#33FFFF",  # Cyan
    "#FF9933",  # Orange
    "#9933FF",  # Purple
    "#33FF99",  # Teal
    "#FF33CC",  # Magenta
    "#33CCFF",  # Sky Blue
    "#FFCC33",  # Gold
    "#33FFCC",  # Sea Green
    "#CC33FF",  # Lavender
    "#33CC99",  # Forest Green
]
plt.figure(figsize=(10, 5))
bottom = [0]*len(positions)
for i in range(len(list_teams)):
    plt.bar(positions,values[i],color = color_codes[i],label=list_teams[i],bottom=bottom)
    bottom = [bottom[j] + values[i][j] for j in range(len(positions))]


plt.legend()
plt.show()