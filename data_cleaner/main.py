import pandas as pd
from cleaner import *

df = pd.read_csv("data_cleaner/data_master/detenciones-csv.txt", index_col="UNIDAD")

df = cleaner(df)

df.to_csv('detenciones_data.csv')