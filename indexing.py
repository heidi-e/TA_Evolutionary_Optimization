import numpy as np


file = 'solutionss.txt'


File_data = np.loadtxt(file, dtype=int)


print(np.argwhere(File_data==1))

