from user import User
from methods import read_ratings, read_movies, shuffle_x
from lsh import min_hash, hash_buckets
import sys

sys.stdout.reconfigure(encoding='utf-8')

TOTAL_USERS = 162541
TOTAL_MOVIES = 62423

user_ratings = read_ratings(75000)
movies = read_movies()
# for row in user_ratings:
#     print(row.userId)
#     print(row.ratings)

# for row in movies:
#     print(row)
# Creates hundred_shuffles.csv
# shuffle_x(movies, 100)
hash_signature = min_hash(user_ratings, 10)
# for key in hash_signature:
#     print(key, hash_signature[key])
hash_buckets = convert_bucket(hash_signature, 3)

