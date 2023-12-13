import re

with open("./data/day3", "r") as ofile:
    contents = ofile.readlines()

with open("./data/day3-examples", "r") as f:
    example = f.readlines()

valid_symbol = re.compile(r"()")

"""apparently any number adjacent to a symbol, even diagonally, is a "part number" and should be included in your sum. (Periods (.) do not count as a symbol.)"""

# in example, 114 and 58 are NOT adjacent
# the sum of the other numbers in example is 4361
# find sum of all numbers that ARE adjacent to symbols

memory = ""
for line in example:
    memory = 