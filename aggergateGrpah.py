import CountrySpecificVariablesUtls
import matplotlib.pyplot as plt
import numpy as np
print("Starting Up")
# Only loads what we need
CountrySpecificVariablesUtls.load()
print("Loading is done")

# HDI Cutoffs - https://hdr.undp.org/en/content/human-development-report-2020-readers-guide#:~:text=Human%20development%20classification&text=The%20cutoff%2Dpoints%20are%20HDI,for%20very%20high%20human%20development.
low = .550          # >.550
medium = .699       # .55 <= x <= .699
high = .7           # .70 <= x <= .799
veryHigh = .8

data = CountrySpecificVariablesUtls.getAllCountrySpecificVariablesRecords()
print("Record collection is done")
x = []
y = []

# Getting aggregate
dic = {}
counts = {}
for record in data:
    if record.new_deaths_smoothed is not None:
        if record.date not in dic.keys():
            dic[record.date] = record.new_deaths_smoothed
            counts[record.date] = 1
        else:
            dic[record.date] += record.new_deaths_smoothed
            counts[record.date] += 1

for key in sorted(dic.keys()):
    x.append(key)
    y.append(dic[key])

# print(x)
print(y)

# Graphing
plt.plot(x, y)
plt.title("Total New Deaths - All Countries")
plt.xlabel("Date")
plt.ylabel("Deaths")

#
# ax2 = plt.twinx()
# ax2.plot(x2, y2, c="blue")

# Color Stuff
left_value = min(y)
right_value = max(y)
span = abs(left_value-right_value)
cmap = plt.get_cmap("hot").reversed()
color_index = np.arange(left_value, right_value, span/100)

i = 0
for index in sorted(color_index):
    index_value = (index-left_value)/span
    color = cmap(index_value)
    # print(index)
    # print(color)
    # print("dis the y value: "+ str(y[i]))
    plt.fill_between(x, left_value, y, where=y>=index, color=color)
    i += 1
    # plt.show()

plt.show()