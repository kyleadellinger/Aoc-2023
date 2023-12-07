import string

with open("./data/day1_1", "r") as ofile:
    contents = ofile.readlines()

numbers = ["8","8","2","1", "2", "3", "4", "5", "6", "7", "8", "9"]

number_bank = ["eightwo", "eighthree", "twone", "one", "two","three","four","five","six","seven","eight","nine"]
map = dict(zip(number_bank, numbers))

output_list = []

def converter(line, bank=number_bank, mapper=map):
    for word in bank:
        if word in line:
            line = line.replace(word, mapper.get(word))
            converter(line)
    return line

for line in contents:
    output_list.append(converter(line=line))


# remove letters
letters_removed = []
temp = str()
for line in output_list:
    for x in line:
        if x in numbers:
            temp += x
    letters_removed.append(temp)
    temp = ""


# code not finished
# and the answer wasn't right anyway

