import string

# get the two numbers from given string
# these combined are the numbers, then find sum of these numbers

with open("./data/day1_1", "r") as ofile:
    contents = ofile.readlines()

numbers = [x for x in string.digits]

# removes all letters from each string in each line
output_list = []
temp = ""
for line in contents:
    for x in line:
        if x in numbers:
            temp += x
    output_list.append(temp)
    temp = ""

# create new list with first and last number, creating list of two strings
new_out_list = []
for line in output_list:
    temp = line[0] + line[-1]
    new_out_list.append(temp)

new_out_num = [int(x) for x in new_out_list]
answer = sum(new_out_num)
print(answer)    