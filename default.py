import pandas as pd

# Chargement des données
df = pd.read_excel("default of credit card clients.xls",engine="openpyxl")

# Affichage des 5 premières lignes
print(df.head())