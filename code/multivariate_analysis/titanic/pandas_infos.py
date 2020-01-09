import pandas as pd

# Load the data to a pandas dataframe
df = pd.read_csv("./input/titanic.csv")

# general info on the dataframe
print('---\ngeneral info on the dataframe')
print(df.info())

# print the columns of the dataframe
print('---\ncolumns of the dataset')
print(df.columns)

# print the first 10 lines of the dataframe
print('---\nfirst lines')
print(df.head(10))

# print the correlation matrix of the dataset
print('---\nCorrelation matrix')
print(df.corr())

# print the standard deviation
print('---\nStandard deviation')
print(df.std())

# get specific values in the dataframe
passenger_id = 25
print('---\nall info on passenger ' + str(passenger_id))
print(df.loc[passenger_id])
print('---\nage of passenger ' + str(passenger_id))
print(df.loc[passenger_id]['Age'])
print(df.loc[passenger_id]['Name'])
print(df.loc[passenger_id]['Sex'])
print(df.loc[passenger_id]['Survived'])
print(df.loc[passenger_id]['Embarked'])
print(df.loc[passenger_id]['Cabin'])
print(df.loc[passenger_id]['Pclass'])

__import__('ipdb').set_trace()


# ipdb.set_trace()
