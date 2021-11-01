import pandas as pd

prueba = pd.read_csv("data_cleaner/prueba_new.csv")
un_values = prueba['MOTIVO'].value_counts()

list = pd.Series(un_values)
list.to_csv('data_cleaner/test/test_uniques.csv')