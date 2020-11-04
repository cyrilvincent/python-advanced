import csv


# Ouvrir et parser house/house.csv
# Calculer le loyer moyen et max et loyer/m2 moyen et max

with open("data/house/house.csv") as f:
    reader = csv.DictReader(f)
    loyer_sum = 0
    loyer_max = 0
    loyerm2_sum = 0
    loyerm2_max = 0
    nb = 0
    for row in reader:
        nb += 1
        loyer = float(row["loyer"])
        loyer_sum += loyer
        if loyer > loyer_max:
            loyer_max = loyer
        surface = float(row["surface"])
        loyerm2 = loyer / surface
        loyerm2_sum += loyerm2
        if loyerm2 > loyerm2_max:
            loyerm2_max = loyerm2
    print(loyer_max, loyer_sum / nb, loyerm2_max, loyerm2_sum / nb)

