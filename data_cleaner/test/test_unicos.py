import pandas as pd

prueba = pd.read_csv("prueba.csv")
un_values = prueba['MOTIVO'].unique()

list = pd.Series(un_values)
list.to_csv('test_uniques.csv')