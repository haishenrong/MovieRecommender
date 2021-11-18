import io, csv
from datetime import datetime
import math

def min_hash(userList, times=1):
    minHashSignature = {}
    file = io.open('ml-25m/hundred_shuffles.csv', mode="r", encoding="utf-8", errors="ignore")
    csvreader = csv.reader(file)
    movieList = next(csvreader)
    for user in userList:
        minHashSignature[user["userId"]] = []
    for i in range(0, times):
        for user in userList:
            j = 0
            while j<len(movieList):
                if movieList[j] in user["ratings"] and user["ratings"][movieList[j]] >= 4.0:
                    minHashSignature[user["userId"]].append(movieList[j])
                    break
                j += 1
        movieList = next(csvreader)
    return minHashSignature

def hash_buckets(hash_signature, bandwidth = 2):
    buckets = {}
    for key, value in hash_signature.items():
        for i in range(0, len(value), bandwidth):
            bucketKey = ','.join(value[i:i+bandwidth])
            if bucketKey in buckets and key not in buckets[bucketKey]:
                buckets[bucketKey].append(key)
            else:
                buckets[bucketKey]=[key]
    return buckets

def knn(hash_buckets, hash_signature, users_eval, movies, bandwidth = 2, p=2):
    eval_user_list = []
    # For each user in hash_signature
    for userId, signature in hash_signature.items():
        # New evaluated user
        evaluated_user = {"userId": userId, "similarUsers":[]}
        # Per band of lsh
        #print(len(signature)) 
        for i in range(0, len(signature), bandwidth):
            bucketKey = str(signature[i])+','+str(signature[i+1])
            # Per list of users in bucket of band
            for j in range(0, len(hash_buckets[bucketKey])):
                sim_user = {"userId": hash_buckets[bucketKey][j], "minkowski":0.0, "good_unwatched":[],"similar":[]}
                # if not user_og
                if int(hash_buckets[bucketKey][j]) != int(userId):
                    user_compare = users_eval[int(hash_buckets[bucketKey][j])-1]
                    user_og = users_eval[int(userId)-1]
                    # for each movie ranked
                    for movie, rating in user_compare["ratings"].items():
                        if movie not in user_og["ratings"] and rating>= 4.5:
                            sim_user["good_unwatched"].append({movies[movie]:rating})
                        if movie in user_og["ratings"]:
                            sim_user["minkowski"]+= (abs(rating-user_og["ratings"][movie])**2)
                            sim_user["similar"].append(movies[movie])
                    sim_user["minkowski"] = math.sqrt(sim_user["minkowski"]/2)
                    # 5 nearest neighbors
                    if len(evaluated_user["similarUsers"])< 5:
                        evaluated_user["similarUsers"].append(sim_user)
                    else:
                        furthest_minkow = min(evaluated_user["similarUsers"][0]["minkowski"],evaluated_user["similarUsers"][1]["minkowski"],evaluated_user["similarUsers"][2]["minkowski"],evaluated_user["similarUsers"][3]["minkowski"],evaluated_user["similarUsers"][4]["minkowski"])
                        if furthest_minkow > sim_user["minkowski"] and len(sim_user["similar"])>10:
                            for sim in evaluated_user["similarUsers"]:
                                if sim["minkowski"] == furthest_minkow:
                                    sim = sim_user
                                    break
        eval_user_list.append(evaluated_user)
    return eval_user_list
            
        



