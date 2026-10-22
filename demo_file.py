import csv

# with open("data/house/house.csv", "r") as f:
#     with open("data/house/house2.csv", "w") as g:
#         for row in f:
#             g.write(row)

#     reader = csv.DictReader(f, delimiter=",")
# for row in reader:
#     loyer = int(row["loyer"])
#     surface = int(row["surface"])
#     print(loyer / surface)

# class HouseRepository
# attributs : surfaces: list[int]=[], loyers: list[int]=[]
# __init__
# load(path: str) : alimente surfaces et loyers
# compute_loyer_m2() -> list[float]
# test
# Bonus : add(loyer: int, surface: int)
# Bonus : save(path: str)

class HouseRepository:

    def __init__(self):
        self.loyers: list[int] = []
        self.surfaces: list[int] = []

    def load(self, path: str):
        with open(path, "r") as f:
            reader = csv.DictReader(f)
            for row in reader:
                loyer = int(row["loyer"])
                surface = int(row["surface"])
                self.loyers.append(loyer)
                self.surfaces.append(surface)

    def compute_loyer_m2(self) -> list[float]:
        result = []
        for loyer, surface in zip(self.loyers, self.surfaces):
            result.append(loyer / surface)
        return result
    
    def add(self, loyer: int, surface: int):
        self.loyers.append(loyer)
        self.surfaces.append(surface)

    def save(self, path: str):
        with open(path, "w") as f:
            f.write("loyer,surface\n")
            for loyer, surface in zip(self.loyers, self.surfaces):
                f.write(f"{loyer},{surface}\n")

