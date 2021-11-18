from user import User
from methods import read_ratings, read_movies, shuffle_x
from config.mysqlconnection import connectToMySQL
from lsh import min_hash, hash_buckets, knn
import json
import sys

sys.stdout.reconfigure(encoding='utf-8')

TOTAL_USERS = 162541
TOTAL_MOVIES = 62423

# user_ratings = read_ratings(50)

# with open('users.json', 'w') as fp:
#     json.dump(user_ratings, fp)

with open('users.json', 'r') as users:
    user_ratings_full = json.load(users)

# for row in user_ratings_full:
#     print(row["userId"])
#     print(row["ratings"])

movies = read_movies()
# for key, val in movies.items():
#    print(key, val)
# Creates hundred_shuffles.csv
# shuffle_x(movies, 100)

# Hash signature
# hash_signature = min_hash(user_ratings_full, 24)
# for key in hash_signature:
#     print(key, hash_signature[key])
# Write signatures
# with open('signatures.json', 'w') as sign:
#     json.dump(hash_signature, sign)

with open('signatures.json', 'r') as sign:
    hash_signature = json.load(sign)

# Bucket making
# hash_buckets = hash_buckets(hash_signature, 2)
# for key in hash_buckets:
#     print(key, hash_buckets[key])
# print(len(hash_buckets))

# Write buckets
# with open('full_result.json', 'w') as fp:
#   json.dump(hash_buckets, fp)


with open('full_result.json', 'r') as res:
    hash_buckets = json.load(res)

# for key in hash_buckets:
#     print(key, hash_buckets[key])
# print(len(hash_buckets))

list_res = knn(hash_buckets, hash_signature, user_ratings_full, movies, 2, 2)

# Write final_dict
with open('final_dict.json', 'w', encoding='utf-8') as fd:
    json.dump(list_res, fd)

# for user in list_res:
#     print(user["userId"])
#     for sim_user in user["similarUsers"]:
#         print(sim_user["userId"], sim_user["minkowski"])
#         print(sim_user["good_unwatched"])
#         print(len(sim_user["similar"]))
# print(len(list_res))

## For Wed
# No fking around
# Implement KNN for one then many
# store many into new dict with similar user info
# small first if there are issues
# push on to db
# start frontend?

## For Thurs