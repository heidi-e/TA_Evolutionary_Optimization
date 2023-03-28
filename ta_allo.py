from evo import Evo
import pandas as pd

# read in data for global variables
sections_df = pd.read_csv("sections.csv")
tas_df = pd.read_csv("tas.csv")
test1 = pd.read_csv("test1.csv", header = None)
test2 = pd.read_csv("test2.csv", header = None)
test3 = pd.read_csv("test3.csv", header = None)


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

def overallo(test):
    # sum across the row
    # extract the ta csv

    penalties = 0
    for ta_id in tas_df["ta_id"]:
        assignments = 0
        ta_row = test.loc[[ta_id]]

        for col in ta_row.columns:
            if ta_row.iloc[0, col] == 1:
                assignments+=1


        difference = (assignments - tas_df.loc[ta_id, "max_assigned"])
        if difference > 0:
            penalties += difference

    return penalties


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

def unwilling(test):




    pass


def unpreferred():
    pass




def main():
    print(time_conflict(test3))
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
