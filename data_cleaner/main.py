import numpy as np
import pandas as pd
from cleaner import *

df = pd.read_csv("data_master/detenciones-csv.txt", index_col="UNIDAD")

#reemplaza valores NaN
df["MOTIVO"] = df["MOTIVO"].fillna('NO INFORMADO')

#lee csv con lista de keys para reemplazar
keys_orden = pd.read_csv("replace_data/orden_detencion.csv")
keys_sanitaria = pd.read_csv("replace_data/infraccion_sanitaria.csv")
keys_nullvalues = pd.read_csv("replace_data/null_values.csv")
keys_contra_autoridad = pd.read_csv("replace_data/contra_autoridad.csv")
keys_desordenes_publ = pd.read_csv("replace_data/desordenes_publicos.csv")
keys_hurto_simple = pd.read_csv("replace_data/hurto_simple.csv")
keys_manejo_armas = pd.read_csv("replace_data/manejo_armas.csv")
keys_receptacion = pd.read_csv("replace_data/receptacion.csv")
keys_robo_intimidacion = pd.read_csv("replace_data/robo_intimidacion.csv")
keys_robo_lugar_no_habit = pd.read_csv("replace_data/robo_lugar_no_habit.csv")
keys_robo_violencia = pd.read_csv("replace_data/robo_violencia.csv")
keys_contra_propiedad = pd.read_csv("replace_data/contra_propiedad.csv")
keys_danos_propiedad = pd.read_csv("replace_data/danos_propiedad.csv")

#envia csv para ser convertido en lista
keys_orden = list_generator(keys_orden)
keys_sanitaria = list_generator(keys_sanitaria)
keys_nullvalues = list_generator(keys_nullvalues)
keys_contra_autoridad = list_generator(keys_contra_autoridad)
keys_desordenes_publ = list_generator(keys_desordenes_publ)
keys_hurto_simple = list_generator(keys_hurto_simple)
keys_manejo_armas = list_generator(keys_manejo_armas)
keys_receptacion = list_generator(keys_receptacion)
keys_robo_intimidacion = list_generator(keys_robo_intimidacion)
keys_robo_lugar_no_habit = list_generator(keys_robo_lugar_no_habit)
keys_robo_violencia = list_generator(keys_robo_violencia)
keys_contra_propiedad = list_generator(keys_contra_propiedad)
keys_danos_propiedad = list_generator(keys_danos_propiedad)

#metodo que devuelve dictionary con keys de lista para reemplazar valores en columna MOTIVO del DF
replace_orden = orden_aprehension(keys_orden)
replace_sanitaria = infraccion_sanitaria(keys_sanitaria)
replace_null = null_values(keys_nullvalues)
replace_contra_autoridad = contra_autoridad(keys_contra_autoridad)
replace_desordenes_publ = desordenes_publ(keys_desordenes_publ)
replace_hurto_simple = hurto_simple(keys_hurto_simple)
replace_manejo_armas = manejo_armas(keys_manejo_armas)
replace_receptacion = receptacion(keys_receptacion)
replace_robo_intimidacion = robo_intimidacion(keys_robo_intimidacion)
replace_robo_lugar_no_habit = robo_lugar_no_habit(keys_robo_lugar_no_habit)
replace_robo_violencia = robo_violencia(keys_robo_violencia)
replace_contra_propiedad = contra_propiedad(keys_contra_propiedad)
replace_danos_propiedad = danos_propiedad(keys_danos_propiedad)

#reemplaza valores de la tabla MOTIVO del DF segun el dictionary entregado
df["MOTIVO"] = df["MOTIVO"].replace(replace_orden)
df["MOTIVO"] = df["MOTIVO"].replace(replace_sanitaria)
df["MOTIVO"] = df["MOTIVO"].replace(replace_null)
df["MOTIVO"] = df["MOTIVO"].replace(replace_contra_autoridad)
df["MOTIVO"] = df["MOTIVO"].replace(replace_desordenes_publ)
df["MOTIVO"] = df["MOTIVO"].replace(replace_hurto_simple)
df["MOTIVO"] = df["MOTIVO"].replace(replace_manejo_armas)
df["MOTIVO"] = df["MOTIVO"].replace(replace_receptacion)
df["MOTIVO"] = df["MOTIVO"].replace(replace_robo_intimidacion)
df["MOTIVO"] = df["MOTIVO"].replace(replace_robo_lugar_no_habit)
df["MOTIVO"] = df["MOTIVO"].replace(replace_robo_violencia)
df["MOTIVO"] = df["MOTIVO"].replace(replace_contra_propiedad)
df["MOTIVO"] = df["MOTIVO"].replace(replace_danos_propiedad)

#
df.to_csv('prueba.csv')