from evo import Evo
import pandas as pd
import numpy as np

# read in data for global variables
sections_df = pd.read_csv("sections.csv")
tas_df = pd.read_csv("tas.csv")
test1 = pd.read_csv("test1.csv", header = None)
test2 = pd.read_csv("test2.csv", header = None)
test3 = pd.read_csv("test3.csv", header = None)


def overallo(test):
    # sum across the row using numpy arrays

    total_assigns = test.sum(axis=1)
    max_assigns = tas_df['max_assigned']

    difference = total_assigns.to_numpy() - max_assigns.to_numpy()

    return difference[difference > 0].sum()

def time_conflict(test):

    conflict = 0
    test = test.to_numpy()

    for ta in range(test.shape[0]):
        times = sections_df.daytime[test[ta]==1]
        if times.duplicated().sum() > 0:
            conflict += 1

    return conflict

def under_supp(test):
    # sum across columns using numpy arrays
    test = test.to_numpy()
    actual_assigns = test.sum(axis=0)

    min_assigns = sections_df['min_ta']

    difference = min_assigns.to_numpy() - actual_assigns

    return difference[difference > 0].sum()

def unwilling(test):
    conflict = 0
    test = test.to_numpy()


    for ta in range(test.shape[0]):
        for val in np.where(test[ta]==1):
            #print(tas_df.iloc[ta, np.where(test[0]==1)])
            assign = tas_df.iloc[ta, val] == 'U'
            print(assign)
            conflict += assign.sum()

    return conflict



    #print(tas_df.iloc[0, test[0]])


def unpreferred():
    pass




def main():
    print(unwilling(test1))
    '''# Create framework
    E = Evo()

    # Register the five objectives
    E.add_fitness_criteria("overallocations", overallo)
    E.add_fitness_criteria("time_conflicts", time_conflict)
    E.add_fitness_criteria("undersupport", under_supp)
    E.add_fitness_criteria("unwilling", unwilling)
    E.add_fitness_criteria("unpreferred", unpreferred)

    # Seed the population with an initial random solution
    N = 50
    L = 'test1.csv'
    E.add_solution(L)
    print(E)'''

if __name__ == '__main__':
    main()
