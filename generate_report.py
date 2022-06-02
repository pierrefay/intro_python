import glob
import pandas as pd

folder ='fichiers/'
fichiers = glob.glob(folder+"*.csv")
nombre_de_lignes = 0
sum = 0

for fichier in fichiers:
    tmpdf = pd.read_csv(fichier)
    nombre_de_lignes = nombre_de_lignes + int(tmpdf.shape[0])
    sum = sum + tmpdf['prix'].sum()

print('nombre de ligne:'+str(nombre_de_lignes))
print('sum:'+str(sum))
mean = sum/nombre_de_lignes
print('mean:'+str(int(mean)))