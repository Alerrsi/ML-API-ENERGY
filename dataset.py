import pandas as pd
from pandas.io.parsers.readers import read_csv

datos = read_csv("Feb_2023.csv")

columnas = [col for col in datos.columns if "Active_Power" in col]

active_power = datos[columnas]

# print(active_power.head())
# print(active_power.columns)


print(active_power.shape)
