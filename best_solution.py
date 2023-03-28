import pandas as pd
import numpy as np

summary_array = np.genfromtxt("final_summary_table.csv", delimiter=',', skip_header=1)

summary_array[np.isnan(summary_array)] = 0

print(summary_array.sum(axis=1))


lowest = np.argmin(summary_array.sum(axis=1))

print(summary_array[lowest])


