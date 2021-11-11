import csv

import matplotlib.pyplot as plt

u = []
with open(r"/home/ubuntu/project1/umpires.csv", "r") as k:
    read = csv.reader(k)
    for i in read:
        u.append(i)


no_of_umpires_by_country = {}


for i in range(1, len(u)):
    if u[i][1] in no_of_umpires_by_country:
        no_of_umpires_by_country[u[i][1]] += 1  ##  0 -'umpire', 1 - ' country'
    else:
        no_of_umpires_by_country[u[i][1]] = 1

# Removing india
del no_of_umpires_by_country[" India"]


country = []
count = []
for i, j in no_of_umpires_by_country.items():
    country.append(i)
    count.append(j)


plt.figure(figsize=(10, 10))
"""
plt.plot(country, count)
plt.plot(country, count, "o")
"""
plt.bar(country, count)
plt.title("Country vs Number_of_umpires")
plt.xlabel("Country")
plt.ylabel("Count_of_umpires")
plt.show()
