import csv

import matplotlib.pyplot as plt


l = []
with open(r"/home/ubuntu/project1/deliveries.csv", "r") as k:
    read = csv.reader(k)
    for i in read:
        l.append(i)


ind_batting = l[0].index(
    "batting_team"
)  #  It gives the index of batting_team in the list
ind_truns = l[0].index("total_runs")  #  It gives the index of total_runs


d = {}
for i in range(1, len(l)):
    if l[i][ind_batting] in d:
        if l[i][ind_truns] is not None:
            d[l[i][ind_batting]] += int(l[i][ind_truns])
    else:
        d[l[i][ind_batting]] = int(l[i][ind_truns])


x = []
y = []
for i, j in d.items():
    x.append(i)
    y.append(j)
plt.figure(figsize=(35, 10))
plt.pie(y, labels=x, autopct="%1.1f%%")
# plt.plot(x, y, "o")
plt.title("Runs scored by Teams")
# plt.xticks(rotation=45, fontsize=8)
# plt.xlabel("Batting_Team")
# plt.ylabel("Total_runs")
plt.show()
