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

    # finds column index of which sections TA inputted as unwilling
    # true = unwilling
    count = tas_df.loc[:, '0':] == 'U'

    # compares TA preference to their assignment
    # true = TA assignment matches unwilling index
    all_sum = (np.array(count) & test).sum()

    return all_sum.sum()


"""

    conflict = 0
    test = test.to_numpy()

    # iterate through all TAs
    for ta in range(test.shape[0]):
        # find index of section that the TA was allocated to
        for val in np.where(test[ta]==1):
            # check if TA is unwilling to support that section index
            assign = tas_df.iloc[ta, val + 3] == 'U'
            conflict += assign.sum()

    return conflict"""

def unpreferred(test):
    # finds column index of which sections TA inputted as willing
    # true = willing
    count = tas_df.loc[:, '0':] == 'W'

    # compares TA preference to their assignment
    # true = TA assignment matches willing index
    all_sum = (np.array(count) & test).sum()

    return all_sum.sum()

""" conflict = 0
    test = test.to_numpy()

    for ta in range(test.shape[0]):
        for val in np.where(test[ta] == 1):
            assign = tas_df.iloc[ta, val + 3] == 'W'
            conflict += assign.sum()

    return conflict"""

# AGENT IDEA
#randomly adding/removing a ta from a section


def swapper(solutions):
    #AGENT
    """ Swap two random values """
    L = solutions[0]
    i = rnd.randrange(0, len(L))
    j = rnd.randrange(0, len(L))
    L[i], L[j] = L[j], L[i]
    return L

def minimize_overallo(solutions):
    #AGENT
    """ yeet a TA from sections if they are overallocated and place them in a section that they are willing to be in"""

    #solutions = pd.DataFrame(solutions)

    # extract first test solution in solutions list
    solution = solutions[len(solutions) - 1]

    for i in range(len(solution)):
        num_allocated = solution.iloc[i].sum()  # get total allocations for the ta
        max_allocated = tas_df.iloc[i, 2]

        if (num_allocated > max_allocated):
            # this ta is overallocated

            for col in solution.columns:
                # if the section is assigned
                if solution.iloc[i, col] == 1:
                    # if the section assigned is unwilling for the ta
                    if tas_df.iloc[i, (col + 3)] == 'U':
                        solution.iloc[i, col] = 0
                        break

    return solution

def swap_unwilling(test, ta_file):
    #AGENT
    # swap TAs that are overallocated based on their availability
    #tah =

    # sum across the row using numpy arrays

    #for ta in
    pass



    """for
     
        L = solutions[0]
        i = rnd.randrange(0, len(L))
        j = rnd.randrange(0, len(L))
        L[i], L[j] = L[j], L[i]
    
    return L"""


def main():

    print(unpreferred(test3))
    """# Create framework
    E = Evo()

    # Register the five objectives
    E.add_fitness_criteria("overallocations", overallo)
    E.add_fitness_criteria("time_conflicts", time_conflict)
    E.add_fitness_criteria("undersupport", under_supp)
    E.add_fitness_criteria("unwilling", unwilling)
    E.add_fitness_criteria("unpreferred", unpreferred)

    # Register some agents
    E.add_agent("minimize_overallo", minimize_overallo, k=1)
    
    # Seed the population with an initial random solution
    N = 50

    E.add_solution(test1)
    #E.add_solution(test2)
    #E.add_solution(test3)
    # Run the evolver

    E.run_agent("minimize_overallo")
    #E.evolve(100000000, 100, 100000)

    print(E)"""


if __name__ == '__main__':
    main()
