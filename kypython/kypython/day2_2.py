import re

with open("./data/day2", "r") as ofile:
    contents = ofile.readlines()

"""The power of a set of cubes is equal to the numbers of red, green, and blue cubes multiplied together. The power of the minimum set of cubes in game 1 is 48. In games 2-5 it was 12, 1560, 630, and 36, respectively. Adding up these five powers produces the sum 2286.

For each game, find the minimum set of cubes that must have been present. What is the sum of the power of these sets?"""

game_regex = re.compile(r"Game\s(\d+)")
red_regex = re.compile(r"(\d+)\sred")
blue_regex = re.compile(r"(\d+)\sblue")
green_regex = re.compile(r"(\d+)\sgreen")

def maxer(line, r_object):
    color = r_object.findall(line)
    color_num = [int(x) for x in color]
    return max(color_num)

def power(red, blue, green):
    return red * blue * green

output_list = []
for line in contents:
    red_max = maxer(line, red_regex)
    blue_max = maxer(line, blue_regex)
    green_max = maxer(line, green_regex)
    together = power(red_max, blue_max, green_max)
    output_list.append(together)
print(sum(output_list))