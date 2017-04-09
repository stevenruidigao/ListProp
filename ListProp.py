import numpy as np
import matplotlib.pyplot as plt; plt.rcdefaults()
import matplotlib.pyplot as plt
from collections import Counter
resp = str(input("Input your data seperated by a comma and a space, like this "+'", "'+": "))
runs = 0
mean = 0
standard_deviation = 0
frequencies = [0]
list2 = list(map(float, resp.split(", ")))
list3 = sorted(list2)
list1 = sorted(set(list3))
a = np.array(list1)
percentup = np.percentile(a, 98.5)
percentdown = np.percentile(a, 1.5)
for x in list1:
    runs += 1
    mean = (mean + float(x)) / runs
    standard_deviation = (standard_deviation + (float(x) - mean) ** 2 / runs) ** (1/2.0)
outlier_definition = 1.25 * standard_deviation + mean
frequencies = list(Counter(list3).values())
print("Response: ", list2)
print("List, ordered: ", list3)
print("Final list:", list1)
print("Mean: ", mean)
print("Standard deviation: ", standard_deviation)
print("Outlier definition: ", outlier_definition)
print("98.5th percentile: ", percentup)
print("1.5th percentile: ", percentdown)
print("Percentiles: ", list(np.percentile(a, [1.5, 98.5])))
print("Frequencies: ", frequencies)
for x in list1:
    if x >= outlier_definition or x <= -1 * (outlier_definition):
        if x >= percentup or x <= percentdown:
            print(x, " is an outlier.")
        else:
            print(x, " isn't an outlier.")
    else:
        print(x, " isn't an outlier.")
print("Creating a graph...")
for x in list1:
    plt.bar(list1, frequencies, width = 0.25, align = 'center', alpha = 1)
    #plt.xticks(np.arange(len(list1))+1, list1)
    plt.ylabel('Frequency')
    plt.title('Data')
plt.show()
