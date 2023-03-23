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
    groups = sections_df.groupby(["daytime"])

    # Create an empty dictionary to store the sections for each group
    section_lists = {}

    # Loop through each group and extract the sections into a list
    for sect_time, group in groups:
        section_lists[sect_time] = group['section'].tolist()

    """# Print the section lists for each group
    for sect_time, sections in section_lists.items():
        print(f"Sections for Designated Time {sect_time}: {sections}")"""


    for ta_id in tas_df["ta_id"]:
        ta_row = test.loc[[ta_id]]

        col_lst = []
        for col in ta_row.columns:
            if ta_row.iloc[0, col] == 1:
                col_lst.append(col)


        for key, val in section_lists.items():
            intersection = set(col_lst).intersection(set(val))

            if len(intersection) > 1:
                conflict += 1

                break


    return conflict






def under_supp():
    pass

def unwilling():
    pass


def unpreferred():
    pass




def main():
    print(overallo(test1))
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
