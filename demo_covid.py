import csv
import matplotlib.pyplot as plt

with open("data/covid-france.txt") as f:
    reader = csv.DictReader(f)
    letalities = (float(row["DC"]) / float(row["NbCas"]) for row in reader if float(row["NbCas"]) != 0)
    print(list(letalities))
    for row in reader:
        letality = float(row["DC"]) / float(row["NbCas"])
        print(letality)

with open("data/covid-france.txt") as f:
    reader = list(csv.DictReader(f))
    nbcas = [float(row["NbCas"]) for row in reader]
    dc = [float(row["DC"]) for row in reader]
plt.subplot(2,1,1)
plt.plot(range(len(nbcas)), nbcas)
plt.subplot(2,1,2)
plt.plot(range(len(dc)), dc)
#plt.yscale("log")
plt.show()
