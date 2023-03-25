from evo import Evo
import pandas as pd
import numpy as np

# read in data for global variables
sections_df = pd.read_csv("sections.csv")
tas_df = pd.read_csv("tas.csv")
test1 = pd.read_csv("test1.csv", header=None)
test2 = pd.read_csv("test2.csv", header=None)
test3 = pd.read_csv("test3.csv", header=None)





def overallo(test):
    # sum across the row using numpy arrays

    # number of times
    total_assigns = test.sum(axis=1)

    # number of sections the TA prefers
    max_assigns = tas_df['max_assigned']

    difference = total_assigns.to_numpy() - max_assigns.to_numpy()

    return difference[difference > 0].sum()


def time_conflict(test):
    conflict = 0
    test = test.to_numpy()

    for ta in range(test.shape[0]):
        times = sections_df.daytime[test[ta] == 1]
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

    # iterate through all TAs
    for ta in range(test.shape[0]):
        # find index of section that the TA was allocated to
        for val in np.where(test[ta] == 1):
            # check if TA is unwilling to support that section index
            assign = tas_df.iloc[ta, val + 3] == 'U'
            conflict += assign.sum()

    return conflict


def unpreferred(test):
    conflict = 0
    test = test.to_numpy()

    for ta in range(test.shape[0]):
        for val in np.where(test[ta] == 1):
            assign = tas_df.iloc[ta, val + 3] == 'W'
            conflict += assign.sum()

    return conflict


def swapper(solutions):
    # AGENT
    """ Swap two random values """
    L = solutions[0]
    i = rnd.randrange(0, len(L))
    j = rnd.randrange(0, len(L))
    L[i], L[j] = L[j], L[i]
    return L




def another_agent(test):
    # AGENT
    # swap TAs that are overallocated

    # sum across the row using numpy arrays

    # number of times
    total_assigns = test.sum(axis=1)

    # number of sections the TA prefers
    max_assigns = tas_df['max_assigned']

    difference = total_assigns.to_numpy() - max_assigns.to_numpy()

    overallo_ta = np.where(difference > 0)


    for ta in overallo_ta:
        if difference[ta] == 2:
            L = tas_df[ta] == 'U'
            print(L)
            """i = 0
            j = 1
            L[i], L[j] = L[j], L[i]"""

def swapper(solutions):
    #AGENT
    """ Swap two random values """
    L = solutions[0]
    print(len(L))
    """i = rnd.randrange(0, len(L))
    j = rnd.randrange(0, len(L))
    L[i], L[j] = L[j], L[i]
    return L"""

def main():

    print(un(test1))
    """# Create framework
    E = Evo()

    # Register the five objectives
    E.add_fitness_criteria("overallocations", overallo)
    E.add_fitness_criteria("time_conflicts", time_conflict)
    E.add_fitness_criteria("undersupport", under_supp)
    E.add_fitness_criteria("unwilling", unwilling)
    E.add_fitness_criteria("unpreferred", unpreferred)

    # Register some agents
    E.add_agent("swapper", swap_overallo, k=1)

    # Seed the population with an initial random solution
    N = 50

    E.add_solution(test1)
    # E.add_solution(test2)
    # E.add_solution(test3)
    print(E)"""


if __name__ == '__main__':
    main()
