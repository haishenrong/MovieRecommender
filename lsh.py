import io, csv
from datetime import datetime

def min_hash(userList, times=1):
    minHashSignature = {}
    file = io.open('ml-25m/hundred_shuffles.csv', mode="r", encoding="utf-8", errors="ignore")
    csvreader = csv.reader(file)
    movieList = next(csvreader)
    for user in userList:
        minHashSignature[user.userId] = []
    for i in range(0, times):
        for user in userList:
            j = 0
            while j<len(movieList):
                if int(movieList[j]) in user.ratings and user.ratings[int(movieList[j])] >= 4.0:
                    minHashSignature[user.userId].append(movieList[j])
                    break
                j += 1
        movieList = next(csvreader)
    return minHashSignature

def hash_buckets(hash_signature, bandwidth = 3):
    buckets = {}
    for key, value in hash_signature.items():
        for i in range(0, len(value), bandwidth):
            bucketKey = ','.join(value[i:i+bandwidth])
            if bucketKey in buckets and key not in buckets[bucketKey]:
                buckets[bucketKey].append(key)
            else:
                buckets[bucketKey]=[key]
    return buckets
