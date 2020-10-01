import csv

with open("data/covid-france.txt") as f:
    reader = csv.DictReader(f)
    for row in reader:
        if float(row["NbCas"]) > 10:
            print(float(row["DC"]) / float(row["NbCas"]))