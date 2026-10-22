import csv

with open("data/house/house.csv", "r") as f:
#     with open("data/house/house2.csv", "w") as g:
#         for row in f:
#             g.write(row)

    reader = csv.DictReader(f, delimiter=",")
    for row in reader:
        loyer = int(row["loyer"])
        surface = int(row["surface"])
        print(loyer / surface)

# class HouseRepository
# attributs : surfaces: list[int]=[], loyers: list[int]=[]
# __init__
# load(path: str) : alimente surfaces et loyers
# compute_loyer_m2() -> list[float]
# Bonus : add(loyer: int, surface: int)
# Bonus : save(path: str)
