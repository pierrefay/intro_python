from random import random, randrange
import pandas as pd

nbr_of_files=100
names = []
prix = []

for i in range(nbr_of_files):
    for j in range(randrange(10,100)):
        names.append('villa '+str(j))
        prix.append(randrange(60000,1000000))

    d = {'prix': prix, 'names': names}
    df = pd.DataFrame.from_dict(d)
    df.to_csv('fichiers/estimation_'+str(i)+'.csv', index=False)