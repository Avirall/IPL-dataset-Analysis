import csv
import matplotlib.pyplot as plt
# Create an empty dictionary to store the number of matches played by each team
teams_matches = {}

# Open the CSV file
with open('archive/matches.csv', newline='') as csvfile:  # Replace 'your_file.csv' with the actual file path
    csv_reader = csv.DictReader(csvfile)
    
    for row in csv_reader:
        season = row['season']
        team1 = row['team1']
        team2 = row['team2']
        
        # Update the number of matches played for team1
        if team1 not in teams_matches:
            teams_matches[team1] = {season: 1}
        else:
            if season in teams_matches[team1]:
                teams_matches[team1][season] += 1
            else:
                teams_matches[team1][season] = 1
        
        # Update the number of matches played for team2
        if team2 not in teams_matches:
            teams_matches[team2] = {season: 1}
        else:
            if season in teams_matches[team2]:
                teams_matches[team2][season] += 1
            else:
                teams_matches[team2][season] = 1
teams_matches['Rising Pune Supergiant'].update(teams_matches['Rising Pune Supergiants'])
del teams_matches['Rising Pune Supergiants']

print(teams_matches)