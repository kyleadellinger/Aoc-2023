import re

with open("./data/day2", "r") as ofile:
    contents = ofile.readlines()

RED = 12
GREEN = 13
BLUE = 14

game_regex = re.compile(r"Game\s(\d+)")
red_regex = re.compile(r"(\d+)\sred")
blue_regex = re.compile(r"(\d+)\sblue")
green_regex = re.compile(r"(\d+)\sgreen")

game_counter = 0

def get_game(line):
    game_regex = re.compile(r"Game\s(\d+)")
    game = game_regex.findall(line)
    #print(game)
    return int(game[0])

def get_color(line, regex=None, limit=RED):
    color_reg = regex
    lines = color_reg.findall(line)
    finder = [int(x) for x in lines if int(x) <= limit]
    check_f = len(finder)
    check_l = len(lines)
    if check_f == check_l:
        return True
    else:
        return False

for line in contents:
    red_answer = get_color(line=line, regex=red_regex, limit=RED)
    blue_answer = get_color(line=line, regex=blue_regex, limit=BLUE)
    green_answer = get_color(line=line, regex=green_regex, limit=GREEN)
    if red_answer == True and blue_answer == True and green_answer == True:
        game_number = get_game(line)
        game_counter += game_number
    else:
        pass

print(game_counter)
# answer: 2476