# coding=utf-8
import pandas as pd

data = pd.read_csv("cat_data.csv", sep=",", engine="python", encoding="utf-8")
print(data)
data.at[1,u"Consumption"] = 50
print(data)
