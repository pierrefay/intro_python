import glob
import pandas as pd

fichiers = glob.glob("fichiers/*.csv")
nombre_de_lignes = 0
sum = 0

for fichier in fichiers:
    tmpdf = pd.read_csv(fichier)
    nombre_de_lignes = nombre_de_lignes + int(tmpdf.shape[0])
    sum = sum + tmpdf['prix'].sum()

mean = sum/nombre_de_lignes
print('Moyennes: '+str(int(mean)))
print('Nombre de Villas: '+str(int(nombre_de_lignes)))