import numpy as np
import matplotlib.pyplot as plt

nb_points = 200
x_data_1 = np.random.uniform(-10, 10, (int(nb_points/2), 1))
x_data_2 = np.random.uniform(15, 20, (int(nb_points/2), 1))

noise_std = 4
pure_y_data = 3*x_data_1
noise = np.random.normal(0, noise_std, (100, 1))
noisy_y_data_1 = noise+pure_y_data
noisy_y_data_2 = np.random.uniform(-3, 3, (100, 1))

x_data = np.concatenate((x_data_1, x_data_2))
noisy_y_data = np.concatenate((noisy_y_data_1, noisy_y_data_2))

plt.plot(x_data, noisy_y_data, 'o')
plt.xlabel("x coordinate")
plt.ylabel("y coordinate")
plt.title("scatter plot")
plt.savefig("different_scatter_plot.pdf")
