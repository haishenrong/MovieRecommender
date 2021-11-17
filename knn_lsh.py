from user import User
from methods import read_ratings, read_movies, shuffle_x
from config.mysqlconnection import connectToMySQL
from lsh import min_hash, hash_buckets
import json
import sys

sys.stdout.reconfigure(encoding='utf-8')

TOTAL_USERS = 162541
TOTAL_MOVIES = 62423

# user_ratings = read_ratings(162541)
# for row in user_ratings:
#     print(row.userId)
#     print(row.ratings)

# movies = read_movies()
# for row in movies:
#     print(row)
# Creates hundred_shuffles.csv
# shuffle_x(movies, 100)

# Hash signature
# hash_signature = min_hash(user_ratings, 24)
# for key in hash_signature:
#     print(key, hash_signature[key])

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

for key in hash_buckets:
    print(key, hash_buckets[key])
print(len(hash_buckets))