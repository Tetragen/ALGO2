import matplotlib.pyplot as plt
# import ipdb
import pandas as pd

# Load the data to a pandas dataframe
df = pd.read_csv("./csv_files/grades.csv")

print(df.info())
print(df.head())
print(df.corr())

var1 = "Height"
var2 = "Age"
df.plot(var1, var2, style='o')
title = f"{var1} vs {var2}"
filename = f"{var1}_vs_{var2}.pdf"
plt.title(title)
plt.savefig('images/' + filename)
