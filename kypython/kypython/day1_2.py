
with open("./data/day1", "r") as ofile:
    contents = ofile.readlines()

numbers = ["82","83","21","1", "2", "3", "4", "5", "6", "7", "8", "9"]

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
    output_list.append(converter(line=line.strip()))

remove_letters = []
temp = ""
for line in output_list:
    for x in line:
        if x in numbers:
            temp += x
    remove_letters.append(temp)
    temp = ""

final_list = []
for line in remove_letters:
    if line:
        boop = line[0] + line[-1]
        final_list.append(int(boop))

print(sum(final_list))

# debugging
#y = 932
#print(output_list[y])
#print(remove_letters[y])
#print(final_list[y])
