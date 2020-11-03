import csv

with open("data/covid-france.txt") as f:
    reader = csv.DictReader(f)
    letalities = (float(row["DC"]) / float(row["NbCas"]) for row in reader if float(row["NbCas"]) != 0)
    print(list(letalities))
    # for row in reader:
    #     letality = float(row["DC"]) / float(row["NbCas"])
    #     print(letality)

# Ouvrir et parser house/house.csv
# Calculer le loyer moyen et max et loyer/m2 moyen et max