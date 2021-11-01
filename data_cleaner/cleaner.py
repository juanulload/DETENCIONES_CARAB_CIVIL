import pandas as pd

def cleaner(data_frame):
    
    keys_orden = pd.read_csv("data_cleaner/replace_data/orden_detencion.csv")['WORDS_TO_REPLACE'].tolist()
    keys_sanitaria = pd.read_csv("data_cleaner/replace_data/infraccion_sanitaria.csv")['WORDS_TO_REPLACE'].tolist()
    keys_nullvalues = pd.read_csv("data_cleaner/replace_data/null_values.csv")['WORDS_TO_REPLACE'].tolist()
    keys_contra_autoridad = pd.read_csv("data_cleaner/replace_data/contra_autoridad.csv")['WORDS_TO_REPLACE'].tolist()
    keys_desordenes_publ = pd.read_csv("data_cleaner/replace_data/desordenes_publicos.csv")['WORDS_TO_REPLACE'].tolist()
    keys_hurto_simple = pd.read_csv("data_cleaner/replace_data/hurto_simple.csv")['WORDS_TO_REPLACE'].tolist()
    keys_manejo_armas = pd.read_csv("data_cleaner/replace_data/manejo_armas.csv")['WORDS_TO_REPLACE'].tolist()
    keys_receptacion = pd.read_csv("data_cleaner/replace_data/receptacion.csv")['WORDS_TO_REPLACE'].tolist()
    keys_robo_intimidacion = pd.read_csv("data_cleaner/replace_data/robo_intimidacion.csv")['WORDS_TO_REPLACE'].tolist()
    keys_robo_lugar_no_habit = pd.read_csv("data_cleaner/replace_data/robo_lugar_no_habit.csv")['WORDS_TO_REPLACE'].tolist()
    keys_robo_violencia = pd.read_csv("data_cleaner/replace_data/robo_violencia.csv")['WORDS_TO_REPLACE'].tolist()
    keys_contra_propiedad = pd.read_csv("data_cleaner/replace_data/contra_propiedad.csv")['WORDS_TO_REPLACE'].tolist()
    keys_danos_propiedad = pd.read_csv("data_cleaner/replace_data/danos_propiedad.csv")['WORDS_TO_REPLACE'].tolist()
    
    keys_orden = {keys:"ORDEN DE APREHENSION" for keys in keys_orden}
    keys_sanitaria = {keys:"INFRACCION SANITARIA" for keys in keys_sanitaria}
    keys_nullvalues = {keys:"NO INFORMADO" for keys in keys_nullvalues}
    keys_contra_autoridad = {keys:"CONTRA LA AUTORIDAD" for keys in keys_contra_autoridad}
    keys_desordenes_publ = {keys:"DESORDENES PUBLICOS" for keys in keys_desordenes_publ}
    keys_hurto_simple = {keys:"HURTO SIMPLE" for keys in keys_hurto_simple}
    keys_manejo_armas = {keys:"MANEJO DE ARMAS PROHIBIDAS" for keys in keys_manejo_armas}
    keys_receptacion = {keys:"RECEPTACION" for keys in keys_receptacion}
    keys_robo_intimidacion = {keys:"ROBO CON INTIMIDACION" for keys in keys_robo_intimidacion}
    keys_robo_lugar_no_habit = {keys:"ROBO EN LUGAR NO HABITADO" for keys in keys_robo_lugar_no_habit}
    keys_robo_violencia = keys = {keys:"ROBO CON VIOLENCIA" for keys in keys_robo_violencia}
    keys_contra_propiedad = {keys:"CONTRA LA PROPIEDAD (OTROS)" for keys in keys_contra_propiedad}
    keys_danos_propiedad = keys = {keys:"DANOS A LA PROPIEDAD" for keys in keys_danos_propiedad}

    data_frame["MOTIVO"] = data_frame["MOTIVO"].fillna('NO INFORMADO')

    data_frame["MOTIVO"] = data_frame["MOTIVO"].replace(keys_orden)
    data_frame["MOTIVO"] = data_frame["MOTIVO"].replace(keys_sanitaria)
    data_frame["MOTIVO"] = data_frame["MOTIVO"].replace(keys_nullvalues)
    data_frame["MOTIVO"] = data_frame["MOTIVO"].replace(keys_contra_autoridad)
    data_frame["MOTIVO"] = data_frame["MOTIVO"].replace(keys_desordenes_publ)
    data_frame["MOTIVO"] = data_frame["MOTIVO"].replace(keys_hurto_simple)
    data_frame["MOTIVO"] = data_frame["MOTIVO"].replace(keys_manejo_armas)
    data_frame["MOTIVO"] = data_frame["MOTIVO"].replace(keys_receptacion)
    data_frame["MOTIVO"] = data_frame["MOTIVO"].replace(keys_robo_intimidacion)
    data_frame["MOTIVO"] = data_frame["MOTIVO"].replace(keys_robo_lugar_no_habit)
    data_frame["MOTIVO"] = data_frame["MOTIVO"].replace(keys_robo_violencia)
    data_frame["MOTIVO"] = data_frame["MOTIVO"].replace(keys_contra_propiedad)
    data_frame["MOTIVO"] = data_frame["MOTIVO"].replace(keys_danos_propiedad)

    return data_frame