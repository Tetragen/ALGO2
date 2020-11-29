"""
Read data from a csv
"""

import csv
import matplotlib.pyplot as plt
from scipy.stats import norm
import numpy as np

# open file
file_name = "mysterious_distro_1.csv"

index = []
data = []

with open("csv_files/" + file_name, "r") as f:
    reader = csv.reader(f)
    row_index = 0
    for row in reader:
        if row_index >= 1:
            index.append(int(row[0]))
            data.append(float(row[1]))
        row_index = row_index + 1

"""
plot the raw data
"""
plt.plot(index, data)
title = "mysterious data 1"
# plt.title(title)
plt.xlabel("index")
plt.ylabel("value")
plt.savefig("distros/distro_1.pdf")
plt.close()

"""
plot a histogram
"""
# use a relevant number of bins !
nbins = 50
plt.hist(data, bins=nbins)
title = f"mysterious distro 1 : histogram, {nbins} bins"
plt.title(title)
plt.xlabel("value")
plt.ylabel("nb of occurrences")
plt.savefig(f"distros/distro_1_hist_{nbins}_bins.pdf")
plt.close()

"""
plot a normalized histogram
"""
plt.hist(data, bins=nbins, density=True)
title = f"mysterious distro 1 : density, {nbins} bins"
plt.title(title)
plt.xlabel("value")
plt.ylabel("density")
plt.savefig(f"distros/distro_1_normed_hist_{nbins}_bins.pdf")

# # Fit a normal distribution to the data:
# mu, std = norm.fit(data)
# print("mean and standard deviation found by fitting a normal distribution")
# print("mean: {}, standard deviation: {}".format(mu, std))
# # Finally
# # Plot the density function
# x = np.linspace(0, 8, 100)
# p = norm.pdf(x, mu, std)
# plt.plot(x, p, "k", linewidth=2)
# title = "mean = %.2f,  std = %.2f" % (mu, std)
# plt.title(title)
# plt.savefig("distros/fitted_distro_1.pdf")
# plt.close()
