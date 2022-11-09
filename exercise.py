import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

data_a = np.arange(0,100,np.random.randint(3,10))

data_b = [num*(np.random.randint(1,5)) for num in data_a]

data_c = [num*(np.random.randint(-5,5)) for num in data_b]
print(f"{data_c =}")
#data_c = np.arange(0,101,2)
data_full = np.column_stack((np.column_stack((data_a,data_b)),data_c))

#data_full = np.append(np.append(data_a,data_b,axis=1),data_c,axis=1)
print(data_full)
data_visualize = pd.DataFrame(data = data_full,columns=["a - Random Line","b - Random Variation (a) multiply(1-5)","c - Random Variation (b) multiply(-5,+5)"])

pd.DataFrame()
data_visualize.plot()
plt.show()
#data_b = np.random.randint(0,101,size=(10,10))
#data_c = np.random.randint(0,101,size=(10,10))
