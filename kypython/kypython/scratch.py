import string

with open("./data/day1_1", "r") as ofile:
    contents = ofile.readlines()

numbers = [x for x in string.digits]

number_bank = ["zero", "one", "two","three","four","five","six","seven","eight","nine"]
map = dict(zip(number_bank, numbers))

confusing = ["eightwo", "eighthree", "zerone", "twone"]
potentials = []
def confuser(checks=confusing, files=contents):
    for word in checks:
        for place, line in enumerate(files, start=0):
            if word in line:
                print(f"{line} : {place}")
                potentials.append(line)



output_list = []

def converter(line, bank=number_bank, mapper=map):
    for word in bank:
        if word in line:
            line = line.replace(word, mapper.get(word))
            converter(line)
    return line


#first_ten = contents[:10]
#print(confuser())
#twelve = contents[29]
#print(twelve)
#print(converter(line=twelve))
with open("./data/examples.txt", "r") as ofile:
    contentx = ofile.readlines()
samples = []
for line in contentx:
    samples.append(converter(line=line))
for line in samples:
    print(line, end="")


