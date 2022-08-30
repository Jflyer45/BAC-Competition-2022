import GovernmentResponseUtls
import matplotlib.pyplot as plt
import numpy as np

print("Starting Up")
GovernmentResponseUtls.load()
print("Loading is done")
test = GovernmentResponseUtls.getAllGovernmentResponseRecord()
data = GovernmentResponseUtls.getByHDI(0, .55)
data2 = GovernmentResponseUtls.getByHDI(.55, .699)
data3 = GovernmentResponseUtls.getByHDI(.7, .799)
data4 = GovernmentResponseUtls.getByHDI(.8, 1)
print("Record collection is done")
print("Amount of records: " + str(len(data)))

# For Workplace Closing line
x = []
y = []
dic = {}
counts = {}
for record in data:
    if record.H7_VaccinationPolicy is not None:
        if record.Date not in dic.keys():
            dic[record.Date] = record.H7_VaccinationPolicy
            counts[record.Date] = 1
        else:
            dic[record.Date] += record.H7_VaccinationPolicy
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
    if record.H7_VaccinationPolicy is not None:
        if record.Date not in dic.keys():
            dic[record.Date] = record.H7_VaccinationPolicy
            counts[record.Date] = 1
        else:
            dic[record.Date] += record.H7_VaccinationPolicy
            counts[record.Date] += 1

for key in sorted(dic.keys()):
    x2.append(key)
    y2.append(float(dic[key]) / float(counts[key]))

x2 = np.array(x2)
y2 = np.array(y2)
#######################3
# For Workplace Closing line
x3 = []
y3 = []
dic = {}
counts = {}
for record in data3:
    if record.H7_VaccinationPolicy is not None:
        if record.Date not in dic.keys():
            dic[record.Date] = record.H7_VaccinationPolicy
            counts[record.Date] = 1
        else:
            dic[record.Date] += record.H7_VaccinationPolicy
            counts[record.Date] += 1

for key in sorted(dic.keys()):
    x3.append(key)
    y3.append(float(dic[key]) / float(counts[key]))

x3 = np.array(x3)
y3 = np.array(y3)
#########################################################################
# For Workplace Closing line
x4 = []
y4 = []
dic = {}
counts = {}
for record in data4:
    if record.H7_VaccinationPolicy is not None:
        if record.Date not in dic.keys():
            dic[record.Date] = record.H7_VaccinationPolicy
            counts[record.Date] = 1
        else:
            dic[record.Date] += record.H7_VaccinationPolicy
            counts[record.Date] += 1

for key in sorted(dic.keys()):
    x4.append(key)
    y4.append(float(dic[key]) / float(counts[key]))

x4 = np.array(x4)
y4 = np.array(y4)
###########################################################################3

# Graphing
plt.plot(x4,y4, c='green', lw='.5', label="Very High HDI")
plt.plot(x3,y3, c='lime', lw='.5', label="High HDI")
plt.plot(x2,y2, c='orange', lw='.5', label="Medium HDI")
plt.plot(x,y, c='red', lw='.5', label="Low HDI")
plt.ylim(0, 5)
plt.title("Vaccination Availability - By HDI")
plt.xlabel("Date")
plt.ylabel("Flag Level")
plt.legend()

plt.show()
