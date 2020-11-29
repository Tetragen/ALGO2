"""
Read data from a csv
"""

import csv
import matplotlib.pyplot as plt
from scipy.stats import norm
import numpy as np
from scipy.stats.stats import pearsonr

# open file
file_name = 'mysterious_distro_3.csv'

index = []
data_1 = []
data_2 = []
data_3 = []
data_4 = []
data_5 = []

with open(file_name, 'r') as f:
    reader = csv.reader(f)
    row_index = 0
    for row in reader:
        if row_index >= 1:
            index.append(int(row[0]))
            data_1.append(float(row[1]))
            data_2.append(float(row[2]))
            data_3.append(float(row[3]))
            data_4.append(float(row[4]))
            data_5.append(float(row[5]))
        row_index = row_index + 1

data = [data_1,
        data_2,
        data_3,
        data_4,
        data_5]

cov = np.cov(data)

plt.imshow(cov)
plt.title('covariance matrix')
plt.savefig('covariance.pdf')
plt.close()

l = [(i, j) for i in range(0, 5) for j in range(0, 5)]

correlation_matrix = np.zeros((5, 5))

# Edit here
for (i, j) in l:
    correlation_matrix[i][j] = 3

im = plt.imshow(correlation_matrix, vmin=-1, vmax=1)
plt.colorbar(im)
plt.title('correlation matrix')
plt.savefig('correlation_matrix.pdf')
plt.close()
