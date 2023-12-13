
from pathlib import Path

import re

data_dir = Path(r"C:\Users\kylea\OneDrive\Documents\AdventofCode\Aoc-2023\data")
file = data_dir / "day1"

write_out = data_dir / "my-output.txt"

with open(file, "r") as ofile:
    contents = ofile.readlines()

numbers = ["1","2","3","4","5","6","7","8","9"]

banker = {
    "oneight": "18",
    "eightwo": "82",
    "nine": "9",
    "eight": "8",
    "eighthree": "83",
    "sevenine": "79",
    "seven": "7",
    "six": "6",
    "five": "5",
    "four": "4",
    "three": "3",
    "twone": "21",
    "two": "2",
    "one": "1"
}

examples = ["two1nine","eightwothree","abcone2threexyz","xtwone3four","4nineeightseven2","zoneight234","7pqrstsixteen"]

good_to_gos = [x for x in contents if any(k in x for k in banker)]
# digest this

catcher = re.compile(r"sevenine")
questionables = []
for place, line in enumerate(contents):
    if catcher.findall(line) != []:
        print(catcher.findall(line), place)


def word_replacer(file, bank):
    output_list = []
    for line in file:
        for word in bank:
            if word in line:
                line = line.strip().replace(word, bank.get(word))
        output_list.append(line)
    return output_list

def one_line_word_replacer(line, bank):
    output = []
    for word in bank:
        if word in line:
            line = line.replace(word, bank.get(word))
    output.append(line.strip())
    return output

def one_line_number(list_of_one):
    temp = ""
    for x in list_of_one[0]:
        if x.isalpha():
            pass
        else:
            temp += x 
    return temp

def first_last(string):
    return string[0] + string[-1]

x = 647
print(f"Untouched: {contents[x].strip()}")
output_list = one_line_word_replacer(contents[x], banker)
print(output_list)
no_letters = one_line_number(output_list)
print(no_letters)
fl = first_last(no_letters)
print(fl)

