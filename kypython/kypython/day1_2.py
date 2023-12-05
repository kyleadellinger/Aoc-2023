import string
import re 

with open("./data/day1_1", "r") as ofile:
    contents = ofile.readlines()

numbers = [x for x in string.digits]

number_bank = ["zero","one", "two","three","four","five","six","seven","eight","nine"]
map = dict(zip(number_bank, numbers))
number_comp = [x for x in number_bank]


seven = contents[-4]
output_list = []

def converter(line, bank=number_bank, mapper=map, catcher=output_list):
    for word in bank:
        if word in line:
            line = line.replace(word, mapper.get(word))
            converter(line)
    return line

for line in contents:
    output_list.append(converter(line=line))

          