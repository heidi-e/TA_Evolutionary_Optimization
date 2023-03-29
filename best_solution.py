import numpy as np

# converts csv file into numpy array
summary_array = np.genfromtxt("final_summary_table.csv", delimiter=',', skip_header=1)

# converts nan to 0
summary_array[np.isnan(summary_array)] = 0

# prints sum of each row (each solution)
print(summary_array.sum(axis=1))

# finds index of lowest solution sum
lowest = np.argmin(summary_array.sum(axis=1))

# prints lowest solution array (row)
print(summary_array[lowest])






