import ipdb
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
sns.set(style="ticks")

# load the dataset
titanic_data = pd.read_csv("./titanic.csv")
# ipdb.set_trace()

# select some columns
# selected_titanic_data = titanic_data[[
#     'PassengerId',
#     'Survived',
#     'Pclass',
#     'Age',
#     'Fare']].copy()

# selected_titanic_data = selected_titanic_data.dropna()

# ipdb.set_trace()

# pairplot is the name of the seaborn function
# to plot the scatter matrix
sns.pairplot(titanic_data)
# /, hue="Survived")
# , hue = 'Survived')
# , hue='Survived')


title = 'Scatter matrix of the titanic dataset'
file = 'titanic_scatter_matrix.pdf'
plt.title(title)
plt.savefig(file)
