import csv

with open("data/covid-france.txt","r") as f:
    content = f.read()
    reader = csv.DictReader(f)
    # for row in reader:
    #     if float(row["NbCas"]) > 10:
    #         print(float(row["DC"]) / float(row["NbCas"]))
    res = [float(row["DC"]) / float(row["NbCas"]) for row in reader if float(row["NbCas"]) > 10]
    for letality in res:
        print(letality)
    print(sum(res) / len(res), min(res), max(res))

    # Filtrer les données NbCas > 10
    # Afficher en stream le taux de létalité chaque jour : Map
    # Calculer la létalité moyenne, min ,max : Reduce