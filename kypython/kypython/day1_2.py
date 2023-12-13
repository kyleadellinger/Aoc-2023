
from pathlib import Path

data_dir = Path(r"C:\Users\kylea\OneDrive\Documents\AdventofCode\Aoc-2023\data")
file = data_dir / "day1"

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

def converter(line, bank=banker):
    for word in bank:
        if word in line:
            line = line.replace(word, bank.get(word))
            converter(line)
    return line

def first_list(file_contents=contents):
    output_list = []
    for line in file_contents:
        output_list.append(converter(line=line.strip()))
    return output_list

def remove_letters(output_list):
    letters_removed = []
    temp = ""
    for line in output_list:
        for x in line:
            if x in numbers:
                temp += x
        letters_removed.append(temp)
        temp = ""
    return letters_removed

def final_list(removed_letters):
    final_output = []
    for line in removed_letters:
        if line:
            boop = line[0] + line[-1]
            final_output.append(int(boop))
    return final_output

output_list = first_list(contents)
no_letters = remove_letters(output_list)
final = final_list(no_letters)

print(sum(final))

################
# debugging
################


