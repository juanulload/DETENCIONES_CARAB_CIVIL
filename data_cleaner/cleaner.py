import pandas as pd

def list_generator(csv_file):
    new_list = csv_file['WORDS_TO_REPLACE'].tolist()
    return new_list

def orden_aprehension(keys_values) :
    dictionary = {keys:"ORDEN DE APREHENSION" for keys in keys_values}
    return dictionary

def infraccion_sanitaria(keys_values):
    dictionary = {keys:"INFRACCION SANITARIA" for keys in keys_values}
    return dictionary

def null_values(keys_values):
    dictionary = {keys:"NO INFORMADO" for keys in keys_values}
    return dictionary

def contra_autoridad(keys_values):
    dictionary = {keys:"CONTRA LA AUTORIDAD" for keys in keys_values}
    return dictionary

def desordenes_publ(keys_values):
    dictionary = {keys:"DESORDENES PUBLICOS" for keys in keys_values}
    return dictionary

def hurto_simple(keys_values):
    dictionary = {keys:"HURTO SIMPLE" for keys in keys_values}
    return dictionary

def manejo_armas(keys_values):
    dictionary = {keys:"MANEJO DE ARMAS PROHIBIDAS" for keys in keys_values}
    return dictionary

def receptacion(keys_values):
    dictionary = {keys:"RECEPTACION" for keys in keys_values}
    return dictionary

def robo_intimidacion(keys_values):
    dictionary = {keys:"ROBO CON INTIMIDACION" for keys in keys_values}
    return dictionary

def robo_lugar_no_habit(keys_values):
    dictionary = {keys:"ROBO EN LUGAR NO HABITADO" for keys in keys_values}
    return dictionary

def robo_violencia(keys_values):
    dictionary = {keys:"ROBO CON VIOLENCIA" for keys in keys_values}
    return dictionary

def contra_propiedad(keys_values):
    dictionary = {keys:"CONTRA LA PROPIEDAD (OTROS)" for keys in keys_values}
    return dictionary

def danos_propiedad(keys_values):
    dictionary = {keys:"DANOS A LA PROPIEDAD" for keys in keys_values}
    return dictionary