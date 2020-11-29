"""
Read data from a csv
"""

import csv
import matplotlib.pyplot as plt
from scipy.stats import norm
import numpy as np

# open file
file_name = 'mysterious_distro_2.csv'

index = []
data = []

with open('csv_files/' + file_name, 'r') as f:
    reader = csv.reader(f)
    row_index = 0
    for row in reader:
        if row_index >= 1:
            index.append(int(row[0]))
            data.append(float(row[1]))
        row_index = row_index + 1

"""
plot the data
"""
plt.plot(index, data)
title = 'mysterious data 2'
plt.title(title)
plt.xlabel('index')
plt.ylabel('value')
plt.savefig('distros/distro_2.pdf')
plt.close()

"""
plot a histogram
"""
# CHANGE THE NUMBER OF BINS
nbins = 5
plt.hist(data, bins=nbins)
title = f"mysterious distro 2 : histogram, {nbins} bins"
plt.title(title)
plt.xlabel('value')
plt.ylabel('nb of occurrences')
plt.savefig(f"distros/distro_2_hist_{nbins}_bins.pdf")
plt.close()

"""
plot a normalized histogram
"""
plt.hist(data, bins=nbins, density=True)
title = f"mysterious distro 2 : density, {nbins} bins"
plt.title(title)
plt.xlabel('value')
plt.ylabel('density')
plt.savefig(f"distros/distro_2_normed_hist_{nbins}_bins.pdf")
plt.close()
