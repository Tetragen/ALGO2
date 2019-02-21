import numpy as np
import matplotlib.pyplot as plt
import math

# x, y = np.random.random(size=(2, 10))

# print(x, y)

# for i in range(0, len(x), 2):
#     plt.plot(x[i:i + 2], y[i:i + 2], '-')


# x = [-1, 0.5, 1, -0.5]
# y = [0.5,  1, -0.5, -1]

n_data = 20

data_1 = np.random.normal(loc=(2, 0.5), scale=0.1, size=(n_data, 2))
# print('----')
# print(data_1)
# x_1 = data_1[0]
# y_1 = data_1[1]

data_2 = np.random.normal(loc=(0, 0), scale=0.5, size=(n_data, 2))
# print('----')
# print(data_2)
# x_2 = data_2[0]
# y_2 = data_2[1]

data = np.concatenate((data_1, data_2))
# print('----')
# print(data)


x = data[:, 0]
y = data[:, 1]
plt.plot(x, y, 'bo')


def connectpoints(x, y, p1, p2):
    x1, x2 = x[p1], x[p2]
    y1, y2 = y[p1], y[p2]
    plt.plot([x1, x2], [y1, y2], 'k-')

threshold = 3

for (i, j) in [(i, j) for i in range(1, x.shape[0]) for j in range(1, x.shape[0])]:
        # we look points a and b
    x_a = x[i]
    y_a = y[i]
    x_b = x[j]
    y_b = y[j]
    euclidian_distance = math.sqrt((x_a - x_b)**2 + (y_a - y_b)**2)
    if euclidian_distance <= threshold:
        connectpoints(x, y, i, j)

# plt.axis('equal')
plt.savefig('clustering_threshold/thres_' + str(threshold) + '.pdf')
plt.close()
