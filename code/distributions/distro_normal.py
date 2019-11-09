import numpy as np
import matplotlib.pyplot as plt

nb_data = 1000
mean = 1
# standard deviation
std = 0.1

style = {'facecolor': 'blue', 'alpha': 0.2, 'pad': 10}
x = np.random.normal(loc=mean, scale=std, size=nb_data)
plt.plot(range(nb_data), x, 'o')
title = 'Normal distribution, mean=' + \
    str(mean) + ', standard deviation=' + str(std)
plt.xlabel('datapoint index')
plt.ylabel('datapoint value')
plt.title(title, bbox=style)
plt.savefig('classic_distros/normal_m_' +
            str(mean) + '_std_' + str(std) + '.pdf')
plt.close()

nbins = 50
plt.hist(x, bins=nbins)
title_hist = 'Histogram ' + title
plt.xlabel('datapoint value')
plt.ylabel('number of occurrences')
plt.title(title, bbox=style)
plt.savefig('classic_distros/hist_normal_m_' +
            str(mean) + '_std_' + str(std) + '.pdf')
plt.close()
