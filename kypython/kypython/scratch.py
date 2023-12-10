
with open("./data/day1", "r") as ofile:
    contents = ofile.readlines()


number_bank = ["eighthree"]

found = []
for word in number_bank:
    for x, line in enumerate(contents):
        if word in line:
            found.append(f"found line {line.strip()} at {x}\n")
print(found)
with open("./data/my-output.txt", "w+") as ofile:
    ofile.writelines(found)











