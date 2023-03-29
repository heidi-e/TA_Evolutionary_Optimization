import numpy as np


File_data = np.loadtxt('solutionss.txt', dtype=int)


print(np.argwhere(File_data==1))

