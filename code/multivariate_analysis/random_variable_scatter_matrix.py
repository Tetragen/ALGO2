import numpy as np
import pandas as pd
from matplotlib import pyplot as plt
from pandas.plotting import scatter_matrix


df = pd.DataFrame(np.random.randn(1000, 4),
                  columns=['A', 'B', 'C', 'D'])
scatter_matrix(df, alpha=0.2)
plt.savefig('random_scatter_matrix.pdf')
plt.close()
