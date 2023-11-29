import pandas as pd
import matplotlib.pyplot as plt
import config

print(f"Version {config.version}")
dataframe = pd.read_csv(config.path, index_col="t")
print(dataframe.describe())

plt.plot(dataframe.index, dataframe["at"])
plt.plot(dataframe.index, dataframe.vm, "red")
diffs = dataframe.vt - dataframe.vm
plt.plot(dataframe.index, diffs, "green")
plt.show()
