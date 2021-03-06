import csv

import matplotlib.pyplot as plt


l = []
with open(r"/home/ubuntu/project1/deliveries.csv", "r") as k:
    read = csv.reader(k)
    for i in read:
        l.append(i)


ind_batsman = l[0].index("batsman")  # Get the index of the bats_man
ind_batting = l[0].index("batting_team")
ind_truns = l[0].index("total_runs")

b = {}
for i in range(1, len(l)):
    if l[i][ind_batting] == "Royal Challengers Bangalore":
        if l[i][ind_batsman] in b:
            if l[i][ind_truns] is not None:
                b[l[i][ind_batsman]] += int(l[i][ind_truns])
        else:
            b[l[i][ind_batsman]] = int(l[i][ind_truns])
batsman = []
score = []
for i, j in b.items():
    batsman.append(i)
    score.append(j)

"""
plt.figure(figsize=(50, 20))
plt.plot(batsman, score)
plt.plot(batsman, score, "o", ms=2)
plt.xticks(rotation=90, fontsize=8)
plt.title("Bats_Man vs Total_runs")
plt.xlabel("Bats_Man")
plt.ylabel("Total_runs")
plt.show()
"""
plt.figure(figsize=(50, 20))
plt.bar(batsman, score)
plt.xticks(rotation=90, fontsize=8)
plt.title("Bats_Man vs Total_runs")
plt.xlabel("Bats_Man")
plt.ylabel("Total_runs")
plt.show()
