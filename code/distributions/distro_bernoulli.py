import numpy as np
import matplotlib.pyplot as plt

nb_data = 100
p = 0.3

style = {'facecolor': 'blue', 'alpha': 0.2, 'pad': 10}
x = np.random.binomial(1, p, nb_data)
plt.plot(range(nb_data), x, 'o')
title = 'Bernoulli distribution : p=' + str(p)
plt.xlabel('datapoint index')
plt.ylabel('datapoint value')
plt.title(title, bbox=style)
plt.savefig('classic_distros/bernoulli_' + str(p) + '.pdf')
plt.close()

nbins = 50
plt.hist(x, bins=nbins)
title_hist = 'Histogram ' + title
plt.xlabel('datapoint value')
plt.ylabel('number of occurrences')
plt.title(title, bbox=style)
plt.savefig('classic_distros/hist_bernoulli_' + str(p) + '.pdf')
plt.close()
