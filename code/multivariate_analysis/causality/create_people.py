"""
Exercise 4
"""

import csv

file_name = 'grades.csv'

with open('csv_files/' + file_name, 'w') as csvfile:
    filewriter = csv.writer(csvfile, delimiter=',')
    filewriter.writerow(['Student', 'Math grade', 'Age', 'Height', 'Month of birth'])
    filewriter.writerow(['Toni', '19', 16, 180, 2])
    filewriter.writerow(['David', '10', 12, 130, 4])
    filewriter.writerow(['Laure', '15', 15, 155, 1])
    filewriter.writerow(['Sergio', '5', 9, 120, 10])
    filewriter.writerow(['Mohammed', '16', 15, 165, 12])
    filewriter.writerow(['Ada', '18', 16, 160, 4])
    filewriter.writerow(['Kylian', '14', 14, 140, 11])
    filewriter.writerow(['Mats', '8', 9, 120, 3])
    filewriter.writerow(['Sabrina', '9', 10, 130, 9])
    filewriter.writerow(['Paul', '12', 13, 145, 8])
