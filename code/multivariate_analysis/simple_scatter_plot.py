import numpy as np
import matplotlib.pyplot as plt

nb_points = 200
x_data = np.random.uniform(-10, 10, (nb_points, 1))
noise_std = 4
# y_data = 3*x_data+np.random.normal(0, noise_std, (nb_points, 1))
pure_y_data = 3*x_data
noise = np.random.normal(0, noise_std, (nb_points, 1))
noisy_y_data = noise+pure_y_data
# __import__('ipdb').set_trace()
plt.plot(x_data, noisy_y_data, 'o')
plt.xlabel("x coordinate")
plt.ylabel("y coordinate")
plt.title("scatter plot")
plt.savefig("simple_scatter_plot.pdf")
