import numpy as np
import matplotlib.pyplot as plt
# import ipdb
import pandas as pd

# Load the data
df = pd.read_csv("./input/titanic.csv")


def make_scatter_plot(dataframe, column1, column2, column3):
    dataframe.plot.scatter(column1, column2, c=column3, cmap='Wistia')
    title = column1 + " vs " + column2 + " vs " + column3
    filename = f"Scatter_{column1}_vs_{column2}_vs_{column3}.pdf"
    plt.title(title)
    plt.savefig('images/' + filename)

make_scatter_plot(df, "PassengerId", "Fare", "Survived")
