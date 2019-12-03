import csv

with open("mesures/mesures.csv") as f:
    reader = csv.DictReader(f)
    res1 = [float(row["AM"]) * float(row["VM"]) for row in reader]
    res2 = [row for row in reader if abs(float(row["VT"]) - float(row["VM"])) > 1 ]


# Créer la liste des puissances instantanées P = AM * VM
# Trouver les défauts abs(VT - VM) > 1