import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

data_a = np.random.normal(size=15)
data_b = [num*(np.random.randint(1,5)) for num in data_a]
data_c = [num*(np.random.randint(-5,5)) for num in data_b]

print(f"{data_c =}")

data_full = np.column_stack((np.column_stack((data_a,data_b)),data_c))

print(data_full)

data_visualize = pd.DataFrame(data = data_full,columns=["a - Random Line, normal method","b - Random Variation (a) multiply(1-5)","c - Random Variation (b) multiply(-5,+5)"])

data_visualize.plot()
plt.show()
