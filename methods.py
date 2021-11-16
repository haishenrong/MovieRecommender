from user import User
import csv
import io
import random

def read_ratings(amt=10):

    file = io.open('ml-25m/ratings.csv', mode="r", encoding="utf-8", errors="ignore")
    #print(type(file))
    csvreader = csv.reader(file)
    info = []
    info =  next(csvreader)
    #print(info)
    rows = []
    currUser = User(1)
    for row in csvreader:
        if row[0] != str(currUser.userId):
            #print(row[0])
            rows.append(currUser)
            currUser = User(row[0])
        if int(row[0]) > amt:
            break
        currUser.ratings[int(row[1])] = float(row[2])
    return rows;

def read_movies():
    file = io.open('ml-25m/movies.csv', mode="r", encoding="utf-8", errors="ignore")
    csvreader = csv.reader(file)
    info =  next(csvreader)
    rows = []
    #k = 0
    for row in csvreader:
        rows.append(int(row[0]))
        #k+=1

    return rows;

def shuffle_x(movies, x):
    shuffled_list =  []
    filename = "hundred_shuffles.csv"
    with open(filename, 'w', newline='') as csvfile: 
        csvwriter = csv.writer(csvfile) 
        for i in range(0,x):
            random.shuffle(movies)
            shuffled_list.append(movies[:])
        csvwriter.writerows(shuffled_list)
    return