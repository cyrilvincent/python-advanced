import csv

with open("data/house/house.csv") as f:
    reader = csv.DictReader(f)
    # for row in reader:
    #     print(row["loyer"])
    res = (float(row["loyer"]) / float(row["surface"]) for row in reader)
    res_filter = (row for row in res if row > 50)
    for row in res_filter:
        print(row)
