import GovernmentResponseUtls
import matplotlib.pyplot as plt
import numpy as np

print("Starting Up")
GovernmentResponseUtls.load()
print("Loading is done")
data = GovernmentResponseUtls.getAllGovernmentResponseRecord()
data2 = GovernmentResponseUtls.getByHDI(.8, 1)
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

x = np.array(x)
y = np.array(y)

# For Workplace Closing line
x2 = []
y2 = []
dic = {}
counts = {}
for record in data2:
    if record.E1_IncomeSupport is not None and record.E3_FiscalMeasures is not None:
        if record.Date not in dic.keys():
            dic[record.Date] = record.E3_FiscalMeasures
            counts[record.Date] = 1
        else:
            dic[record.Date] += record.E3_FiscalMeasures
            counts[record.Date] += 1

for key in sorted(dic.keys()):
    x2.append(key)
    y2.append(float(dic[key]) / float(counts[key]))

x2 = np.array(x2)
y2 = np.array(y2)

# Graphing
plt.plot(x,y, c='black', lw='.5', label="E1_IncomeSupport")
# plt.plot(x2,y2, c='red', lw='.5', label="School Shutdown")

plt.ylim(0, 3)
plt.title("Income Support Very High HDI")
plt.xlabel("Date")
plt.ylabel("Flag Level")
plt.legend()

plt.show()
