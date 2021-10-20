'''
    dictionaries.py
    Jeff Ondich, 20 October 2021

    Quick illustration, in the context of our Olympics data,
    of how much faster lookup is with a dictionary than
    with a list.
'''

import csv

def dictionary_of_athletes(olympics_file_name):
    athletes = {}
    with open(olympics_file_name) as f:
        reader = csv.reader(f)
        for row in reader:
            name = row[1]
            if name not in athletes:
                athletes[name] = 0
    return athletes

def list_of_athletes(olympics_file_name):
    athletes = []
    with open(olympics_file_name) as f:
        reader = csv.reader(f)
        for row in reader:
            name = row[1]
            if name not in athletes:
                athletes.append(name)
    return athletes

#athletes = list_of_athletes('athlete_events.csv') # slow
athletes = dictionary_of_athletes('athlete_events.csv') # fast
print('# of athletes:', len(athletes))

