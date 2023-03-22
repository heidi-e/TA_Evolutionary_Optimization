from evo import Evo
import pandas as pd

# read in data for global variables
sections_df = pd.read_csv("sections.csv")
tas_df = pd.read_csv("tas.csv")
test1 = pd.read_csv("test1.csv", header = None)
test2 = pd.read_csv("test2.csv", header = None)
test3 = pd.read_csv("test3.csv", header = None)

print(sections_df)
"""
times = {}
section_lst =[]

for index, row in sections_df['daytime'].items():
    times[row] = index
    section_lst.append(index)


print(section_lst)"""

"""groups = sections_df.groupby(["daytime"])

# Create an empty dictionary to store the sections for each group
section_lists = {}



# Loop through each group and extract the sections into a list
for sect_time, group in groups:
    section_lists[sect_time] = group['section'].tolist()

# Print the section lists for each group
for sect_time, sections in section_lists.items():
    print(f"Sections for Designated Time {sect_time}: {sections}")


print(section_lists)"""
list1 = [1, 2, 3, 4, 5]
list2 = [2, 4, 6, 8]

intersection = set(list1).intersection(list2)

print(intersection)