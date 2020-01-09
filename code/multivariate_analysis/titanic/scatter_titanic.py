import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

# Load the data
df = pd.read_csv("./input/titanic.csv")


def assess_correlation(dataframe, column1, column2):
    dataframe.plot(column1, column2, style='o')
    title = column1 + ' vs ' + column2
    filename = column1 + '_vs_' + column2 + '.pdf'
    plt.xlabel(column1)
    plt.ylabel(column2)
    plt.title(title)
    plt.savefig('images/' + filename)


sub_df = df[["Sex", "Survived"]]
sns_plot = sns.catplot(x="Sex", y="Survived", data=sub_df)
sns_plot.savefig("images/Sex_vs_survived.pdf")

sub_df = df[["Pclass", "Survived"]]
sns_plot = sns.catplot(x="Pclass", y="Survived", data=sub_df)
sns_plot.savefig("images/Class_vs_survived.pdf")
