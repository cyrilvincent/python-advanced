import pandas as pd
import numpy as np
import config.config as config

print(config.version)

# Charger par pandas un house.csv avec le path
# service.load("data/house/house.csv") déduit qu'il faut utiliser read_csv par l'extension
path = "data/house/house.csv"
index = path.rindex(".")
extension = path[index + 1:]
print(extension)
# service.mean("surface") => 65.1
# service.str("surface")
# Tester unittest

