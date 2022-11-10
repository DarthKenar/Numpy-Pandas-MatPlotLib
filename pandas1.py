import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

months = ("Enero","Febrero","Marzo","Abril","Mayo","Junio","Julio",
        "Agosto","Septiembre","Octubre","Noviembre","Diciembre")
#years = [2010,2011,2012,2013,2014,2015,2016,2017,2018,2019,2020,2021]
info = {"2015":[],"2016":[],"2017":[],"2018":[],"2019":[],"2020":[]}
for year in info:
    for month in months:
        #info[year].append(int(input(f"How many info did in {year} -- {month}: ")))
        info[year].append(np.random.randint(0,1000))

df = pd.DataFrame(data=info, index=months)

df.plot()
plt.show()


