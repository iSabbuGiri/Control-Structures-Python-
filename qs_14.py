'''Write a function that reads a CSV file. It should return a list of
dictionaries, using the first row as key names, and each subsequent
row as values for those keys.'''

import csv

def reading_csv(filename):
    with open(filename, 'r') as store:
        csv_reader = csv.DictReader(store)


        for line in csv_reader:
            print(line)


filename = 'file.csv'
reading_csv(filename)