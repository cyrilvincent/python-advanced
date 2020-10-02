import matplotlib.pyplot as plt
import pandas

x = range(10)
y = range(10)

#plt.plot(x, y)
#plt.scatter(x, y)
# plt.bar(x, y)
# plt.show()

dataframe = pandas.read_csv("data/covid-france.txt")
plt.title("COVID 19")
plt.yscale('log')
plt.scatter(dataframe["ix"], dataframe.NbCas)
plt.bar(dataframe["ix"], dataframe.DC)
plt.show()
