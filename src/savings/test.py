import pandas as pd

data = pd.read_csv("cat_data.csv", sep=",",engine="python")

print(data["Is_alive"][2],data["Name"][2])
print(data.shape[0])

