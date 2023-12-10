
with open("./data/day1", "r") as ofile:
    ocontents = ofile.readlines()

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
    "two": "2",
    "one": "1"
}

examples = ["two1nine","eightwothree","abcone2threexyz","xtwone3four","4nineeightseven2","zoneight234","7pqrstsixteen","oneight","8fournine3svdlh5sevenoneighttsq"]

contents = ocontents[195:198]
first_output = []
for line in contents:
    for x in banker:
        if x in line.strip():
            line = line.replace(x, banker.get(x))
    first_output.append(line.strip())


second_output = []
for line in first_output:
    temp = ""
    for x in line:
        if x in numbers:
            temp += x
    second_output.append(temp)

first_last = []
for line in second_output:
    temp = line[0] + line[-1]
    first_last.append(int(temp))

for x, y, z in zip(contents, first_output, first_last):
    print(x.strip(), y, z)
print(first_output)
print(second_output)
print(first_last)
print(sum(first_last))

