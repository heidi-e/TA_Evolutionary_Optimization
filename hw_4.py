from evo import Evo
import pandas as pd
import numpy as np
import random as rnd
import csv

# read in data files and make global variables for each file
sections_df = pd.read_csv("sections.csv")
tas_df = pd.read_csv("tas.csv")
test1 = pd.read_csv("test1.csv", header=None)
test2 = pd.read_csv("test2.csv", header=None)
test3 = pd.read_csv("test3.csv", header=None)


def overallo(test):
    """Objective: Count number of times a ta is overallocated based on their availability"""

    # sum across the row using numpy arrays
    total_assigns = test.sum(axis=1)

    # number of sections the TA prefers
    max_assigns = tas_df['max_assigned']

    # calculate the difference between how much a ta is allocated vs how much they would like to be allocated
    difference = total_assigns.to_numpy() - max_assigns.to_numpy()

    return difference[difference > 0].sum()

def time_conflict(test):
    """Objective: Count time conflict for each TA. Multiple time conflicts still count as one time conflict"""

    # variable storing each of the time conflicts
    conflict = 0
    test = test.to_numpy()

    for ta in range(test.shape[0]):
        times = sections_df.daytime[test[ta]==1]
        if times.duplicated().sum() > 0:
            conflict += 1

    return conflict

def under_supp(test):
    """Objective: Count how many TAs are missing from each section"""

    # turn the test into a numpy array
    test = test.to_numpy()

    # calculates how many times TAs are assigned to each section
    actual_assigns = test.sum(axis=0)

    # variable for the minimum amount of TAs needed for each section
    min_assigns = sections_df['min_ta']

    # difference between the actual assigned and minimum assigned
    difference = min_assigns.to_numpy() - actual_assigns

    return difference[difference > 0].sum()

def unwilling(test):
    """Objective: Count how many times TAs are supporting a section they are unwilling to support"""

    test = test.to_numpy()
    # finds column index of which sections TA inputted as unwilling
    # true = unwilling
    count = tas_df.loc[:, '0':] == 'U'

    # compares TA preference to their assignment
    # true = TA assignment matches unwilling index
    return (np.array(count) & test).sum()


def unpreferred(test):
    """Objective: Count how many times TAs are supporting a section they do not preffer to support"""

    test = test.to_numpy()
    # finds column index of which sections TA inputted as willing
    # true = willing

    count = tas_df.loc[:, '0':] == 'W'

    # compares TA preference to their assignment
    # true = TA assignment matches willing index
    return (np.array(count) & test).sum()


def swap_assignment(solutions):
    """AGENT: Randomly swap TAs from an assigned class to an unassigned class (or vice versa)"""


    solution = solutions[len(solutions) - 1]

    # select a random row
    i = rnd.randrange(0, len(solution))

    # select a random column
    j = rnd.randrange(0, len(solution.columns))

    # swap out the assignment of a ta (change from 0 to 1 or vice versa)
    solution.loc[i, j] = int((solution.loc[i, j]) and False)



    return solution
    
    #int(x and False)


def swap_ta(solutions):
    """AGENT: Swap two random TAs' scheduled assignments"""

    # variable containing the last solution in our population
    solution = solutions[len(solutions) - 1]

    # select a random section
    j = rnd.randrange(0, len(solution.columns))

    # select a random ta
    i = rnd.randrange(0, len(solution))

    # select another random ta
    w = rnd.randrange(0, len(solution))

    # swapping their assignments
    solution.iloc[i, j], solution.iloc[w, j] = solution.iloc[w, j], solution.iloc[i, j]

    return solution



def minimize_overallo(solutions):
    #AGENT
    """ drop a TA from sections if they are overallocated and place them in a section that they are willing to be in"""

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


def output_sol(evo_keys):
    """output the solutions into a summary table """
    list_sol = []
    for solution in ((list(evo_keys.keys()))):
        sol_dict = dict(solution)
        sol_dict["groupname"] = "non_dom"
        list_sol.append(sol_dict)

    # set up csv file and add list to csv file
    field_names = ['groupname','overallocations', 'conflicts', 'undersupport', 'unwilling', 'unpreferred']
    with open('final_summary_table.csv', 'w') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=field_names)
        writer.writeheader()
        writer.writerows(list_sol)


def best_sol():

    summary_array = np.genfromtxt("Final_summary_table.csv", delimiter=',', skip_header=1)

    summary_array[np.isnan(summary_array)] = 0

    print(summary_array.sum(axis=1))

    best_sol_index = np.argmin(summary_array.sum(axis=1))

    print(best_sol_index)

    return best_sol_index

def main():

    # Create framework
    E = Evo()

    # Register the five objectives
    E.add_fitness_criteria("overallocations", overallo)
    E.add_fitness_criteria("conflicts", time_conflict)
    E.add_fitness_criteria("undersupport", under_supp)
    E.add_fitness_criteria("unwilling", unwilling)
    E.add_fitness_criteria("unpreferred", unpreferred)

    # Register the agents
    E.add_agent("minimize_overallo", minimize_overallo, k=1)
    E.add_agent("swap_ta", swap_ta, k=1)
    E.add_agent("swap_assignment", swap_assignment, k=1)


    E.add_solution(test1)
    #E.add_solution(test2)
    #E.add_solution(test3)



    # Run the evolver
    E.evolve(100000000, 100, 100000, 600)

    print(E)

    output_sol(E.evo_keys())



if __name__ == '__main__':
    main()
