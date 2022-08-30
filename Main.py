import CountrySpecificVariablesUtls
import matplotlib.pyplot as plt

import numpy as np
print("Starting Up")
# Only loads what we need
CountrySpecificVariablesUtls.load()
# GovernmentResponseUtls.load()
print("Loading is done")
data = CountrySpecificVariablesUtls.getAllCountrySpecificVariablesRecords()
data2 = CountrySpecificVariablesUtls.getByHumanDevelopmentIndex(.33, 1)
# data = GovernmentResponseUtls.getAllGovernmentResponseRecord()
# data2 = GovernmentResponseUtls.getByCountry("United States")
print("Record collection is done")
# print(data2[0].Date)
x = []
y = []

for record in data2:
    x.append(record.date)
    y.append(record.new_cases_smoothed)


# Graphing
plt.plot(x,y, c='black', lw='.5')
plt.title("USA New Cases")
plt.xlabel("Date")
plt.ylabel("New Cases Smoothed")
plt.tight_layout()
# plt.fill_between(x, y, where=x2,facecolor='green')
# plt.fill_between(x, y)

plt.show()

# Color Stuff
left_value = 0
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