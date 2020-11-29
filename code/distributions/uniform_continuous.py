import numpy as np
import matplotlib.pyplot as plt

nb_data = 5000
x_min = 41
x_max = 42

style = {'facecolor': 'blue', 'alpha': 0.2, 'pad': 10}
x = np.random.uniform(x_min, x_max, nb_data)
plt.plot(range(nb_data), x, 'o')
title = f"Uniform distribution : [{x_min}, {x_max}]"
plt.xlabel('datapoint index')
plt.ylabel('datapoint value')
plt.title(title, bbox=style)
plt.ylim([34, 55])
plt.savefig(f"classic_distributions/unif_continuous_{x_min}_{x_max}.pdf")
plt.close()

nbins = 50
plt.hist(x, bins=nbins)
title_hist = 'Histogram ' + title
plt.xlabel('datapoint value')
plt.ylabel('number of occurrences')
plt.title(title, bbox=style)
plt.savefig(f"classic_distributions/hist_unif_continuous_{x_min}_{x_max}.pdf")
plt.close()
