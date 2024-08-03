from library_item import LibraryItem
import csv

library = []

with open('info.csv',mode='r') as csv_file:
    csv_reader = csv.reader(csv_file)
    for line in csv_reader:
        # print(line)
        # print(type(line))
        item = LibraryItem(key=line[0],name=line[1], director= line[2], rating =line[3], play_count =line[4])
        library.append(item)
        print (line)
    
    



def list_all():
    output = ""
    for key in library:
        item = key
        output += f"{key} {item.info()}\n"
    return output


def get_name(key):
    try:
        item = key
        return item.name
    except KeyError:
        return None


def get_director(key):
    try:
        item = key
        return item.director
    except KeyError:
        return None


def get_rating(key):
    try:
        item = key
        return item.rating
    except KeyError:
        return -1


def set_rating(key, rating):
    try:
        item = key
        item.rating = rating
    except KeyError:
        return


def get_play_count(key):
    try:
        item = key
        return item.play_count
    except KeyError:
        return -1


def increment_play_count(key):
    try:
        item = key
        item.play_count += 1
    except KeyError:
        return
