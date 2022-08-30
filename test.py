import GovernmentResponseUtls, CountrySpecificVariablesUtls
import matplotlib.pyplot as plt
import numpy as np

print("Starting Up")
GovernmentResponseUtls.load()
CountrySpecificVariablesUtls.load()
print("Loading is done")
data = GovernmentResponseUtls.getAllGovernmentResponseRecord()
data2 = GovernmentResponseUtls.getByHDI(.8, 1)
data3 = CountrySpecificVariablesUtls.getByHumanDevelopmentIndex(.8, 1)
print("Record collection is done")
print("Amount of records: " + str(len(data2)))

# For Workplace Closing line
x = []
y = []
dic = {}
counts = {}
for record in data2:
    if record.E1_IncomeSupport is not None:
        if record.Date not in dic.keys():
            dic[record.Date] = record.E1_IncomeSupport
            counts[record.Date] = 1
        else:
            dic[record.Date] += record.E1_IncomeSupport
            counts[record.Date] += 1

for key in sorted(dic.keys()):
    x.append(key)
    y.append(float(dic[key]) / float(counts[key]))

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
ax1.set_ylim(0, 3)
ax1.set_xlabel("Time")
ax1.set_ylabel("Index Level")
ax1.plot(x,y, c='black', lw=.5, label= "line 1")
ax1.set_title("Average Income Support Flag VS New Cases - Very High HDI")


ax2 = ax1.twinx()
ax2.plot(x2, y2, c="red")
ax2.set_ylabel("Cases", color="red")
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
plt.show()
