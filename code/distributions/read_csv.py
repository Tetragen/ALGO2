"""
Read data from a csv
"""

import csv

# open file
file_name = 'foot.csv'

players = []
notes = []

with open('csv_files/' + file_name, 'r') as f:
    reader = csv.reader(f)
    # read file row by row
    # convert to lists
    row_index = 0
    for row in reader:
        print(row)
        if row_index >= 1:
            players.append(row[0])
            notes.append(row[1])
        row_index = row_index + 1

print(players)
print(notes)
