import math
"""
Read data from a csv
and build a dissimilarity matrix
"""

import csv

# open file
file_name = "complex_data.csv"

players = []
notes = []
speeds = []
meals = []

with open('csv_files/' + file_name, 'r') as f:
    reader = csv.reader(f)
    # read file row by row
    # convert to lists
    row_index = 0
    for row in reader:
        print(row)
        if row_index >= 1:
            players.append(row[0])
            notes.append(int(row[1]))
            speeds.append(int(row[2]))
            meals.append(row[3])
        row_index = row_index + 1

print(players)
print(notes)
print(speeds)
print(meals)
