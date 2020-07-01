import csv
import pickle
#
# with open("data/media/books.csv") as f:
#     reader = csv.DictReader(f)
#     #print(sum((float(row["price"]) for row in reader)))
#     # for row in reader:
#     #     print(row["price"])
#     inmemory = list(reader)
#     with open("data/media/books.pickle", "wb") as f2:
#         pickle.dump(inmemory, f2)

# with open("data/media/books.pickle", "rb") as f:
#     values = pickle.load(f)
#     for row in values:
#         print(row["title"])
#
# print(values)
import json
# with open("data/media/books.json","w") as f:
#     json.dump(values, f)

with open("data/media/books.json") as f:
    values = json.load(f)
    print(values)


