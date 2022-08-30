import GovernmentResponseUtls
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import numpy as np

print("Starting Up")
GovernmentResponseUtls.load()
print("Loading is done")
data = GovernmentResponseUtls.getAllGovernmentResponseRecord()
data2 = GovernmentResponseUtls.getByCountry("United States")
print("Record collection is done")

print(data2[0].Date)
x = []
y = []
shutdownFlags = []

for record in data2:
    x.append(record.Date)
    # x.append(DateFormatter(record.Date))
    shutdownFlags.append(record.C1_SchoolClosing)
    # x.append(record.Date)
    y.append(record.ConfirmedDeaths)

# Graphing
plt.plot(x,y, c='black', lw='.5')

plt.title("USA New Cases & Workplace Shutdown Shading")
plt.xlabel("Date")
plt.ylabel("New Cases Smoothed")
plt.tight_layout()
# plt.fill_between(x, y, where=x2,facecolor='green')
# plt.fill_between(x, y)

# Color Stuff
left_value = 0
right_value = max(shutdownFlags)
span = abs(left_value-right_value)
cmap = plt.get_cmap("hot")
color_index = np.arange(left_value, right_value, span/100)

fig, ax = plt.subplots()
flag0 = mpatches.Patch(color=(0.0416, 0.0, 0.0, 1.0), label="No data or no measurements")
ax.legend(handles=[flag0])


for index in sorted(color_index):
    index_value = (index-left_value)/span
    color = cmap(index_value)
    print(index)
    print(color)
    plt.fill_between(x, left_value, y, where=shutdownFlags>=index, color=color)
    # plt.show()

plt.show()