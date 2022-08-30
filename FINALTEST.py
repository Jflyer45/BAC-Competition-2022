import GovernmentResponseUtls, CountrySpecificVariablesUtls
import matplotlib.pyplot as plt
import numpy as np

print("Starting Up")
GovernmentResponseUtls.load()
CountrySpecificVariablesUtls.load()
print("Loading is done")
data = GovernmentResponseUtls.getAllGovernmentResponseRecord()
data3 = CountrySpecificVariablesUtls.getAllCountrySpecificVariablesRecords()
print("Record collection is done")

x = []
y = []
dic1 = {}
for record in data3:
    if record.date not in dic1.keys() and record.new_deaths_smoothed is not None:
        dic1[record.date] = record.new_deaths_smoothed
    else:
        dic1[record.date] += record.new_deaths_smoothed

for key in sorted(dic1.keys()):
    x.append(key)
    y.append(dic1[key])

x2 = []
y2 = []
dic2 = {}
for record in data3:
    if record.date not in dic2.keys() and record.new_cases_smoothed is not None:
        dic2[record.date] = record.new_cases_smoothed
    else:
        dic2[record.date] += record.new_cases_smoothed

for key in sorted(dic2.keys()):
    x2.append(key)
    y2.append(dic2[key])


print("Subplotting")
fig, ax1 = plt.subplots()

ax1.set_xlabel("Time")
ax1.set_ylabel("New Cases")
ax1.plot(x2,y2, c='black', lw=.5, label= "New Cases")
ax1.set_title("Total New Cases and Deaths - All Countries")


ax2 = ax1.twinx()
ax2.plot(x, y, c="black", label="New Cases")
ax2.set_ylabel("Deaths", color="red")
ax2.tick_params(axis="y", labelcolor="red")

# # Graphing
# plt.plot(x,y, c='black', lw='.5', label="E1_IncomeSupport")
# # plt.plot(x2,y2, c='red', lw='.5', label="School Shutdown")
#
# plt.ylim(0, 3)
# plt.title("Income Support Very High HDI")
# plt.xlabel("Date")
# plt.ylabel("Flag Level")
# plt.legend()
#
plt.legend()
plt.show()
