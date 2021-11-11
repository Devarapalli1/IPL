import csv

import matplotlib.pyplot as plt

m = []
with open(r"/home/ubuntu/project1/matches.csv", "r") as k:
    read = csv.reader(k)
    for i in read:
        m.append(i)


no_of_matches = len(m) - 1
print("Total Number of Matches: ", no_of_matches)
ind_season = m[0].index("season")


no_of_games_by_season = {}
for i in range(1, len(m)):
    if m[i][1] in no_of_games_by_season:
        no_of_games_by_season[m[i][ind_season]] += 1
    else:
        no_of_games_by_season[m[i][ind_season]] = 1


ind_team1 = m[0].index("team1")
ind_team2 = m[0].index("team2")


w = {}
for i in range(1, len(m)):
    if m[i][ind_season] in w:
        if m[i][ind_team1] in w[m[i][ind_season]]:
            w[m[i][ind_season]][m[i][ind_team1]] += 1
        else:
            w[m[i][ind_season]][m[i][ind_team1]] = 1
        if m[i][ind_team2] in w[m[i][ind_season]]:
            w[m[i][ind_season]][m[i][ind_team2]] += 1
        else:
            w[m[i][ind_season]][m[i][ind_team2]] = 1
    else:
        w[m[i][ind_season]] = {}
        w[m[i][ind_season]][m[i][ind_team1]] = 1
        w[m[i][ind_season]][m[i][ind_team2]] = 1


teams = []
##  To get unique teams from the csv file
for i in range(1, len(m)):
    if m[i][ind_team1] not in teams:
        teams.append(m[i][ind_team1])
    if m[i][ind_team2] not in teams:
        teams.append(m[i][ind_team2])

team_list = [[] for i in range(len(teams))]
for i in w:
    for j in range(0, len(teams)):
        if teams[j] in w[i]:
            team_list[j].append(w[i][teams[j]])
        else:
            team_list[j].append(0)


def addl(l1, l2):
    l = []
    for i in range(0, len(l1)):
        l.append(l1[i] + l2[i])
    return l


season = []
count_per_season = []
for i, j in no_of_games_by_season.items():
    season.append(i)
    count_per_season.append(j)


l = []
l.append(team_list[0])
for i in range(1, len(team_list) - 1):
    l.append(addl(l[i - 1], team_list[i]))


plt.figure(figsize=(20, 20))
plt.bar(season, team_list[0])
for i in range(1, len(team_list)):
    plt.bar(season, team_list[i], bottom=l[i - 1])
plt.legend(teams, bbox_to_anchor=(1, 1))
plt.show()
