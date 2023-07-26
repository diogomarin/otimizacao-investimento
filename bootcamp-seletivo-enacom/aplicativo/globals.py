import pandas as pd
import os

if "df_categorias.csv" in os.listdir():
    df_categorias = pd.read_csv("df_categorias.csv", sep=",", index_col=0)
    categorias = df_categorias.values.tolist()

if "df_prioridades.csv" in os.listdir():
    df_prioridades = pd.read_csv("df_prioridades.csv", sep=",", index_col=0)
    prioridades = df_prioridades.values.tolist()