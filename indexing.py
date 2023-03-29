import numpy as np

# obtain section index for each TA from best solution txt

File_data = np.loadtxt('best_solution.txt', dtype=int)

print(np.argwhere(File_data==1))

