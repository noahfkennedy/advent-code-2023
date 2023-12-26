import re
from functools import reduce


f = open("day2_input.txt", "r")

# Problem has multiple parts 
    # First part is parsing out each line, separately. 
    # Then parse out each game within the line, separately. 
    # Then parse out the number associated with each color
    # Then check if that number is greater than ground truth. If so, skip 
    # If you get to the end of the line, and you haven't skipped, add it to the sum 

    # Assumption: each game only has one draw per color. So I wouldn't ever go '3 red, 10 red;'



#### Part 1 #### 
# truth_dict = {'red': 12, 'green': 13, 'blue': 14}
# total_sum = 0

# for item in f:
#     red_min = 0
#     green_min = 0
#     blue_min = 0
#     game_num = int(item.split(':')[0].split(' ')[1])
#     turns = re.split('[,;]' ,item.split(':')[1])
#     for turn_raw in turns:
#         turn = turn_raw.strip().split(' ')
#         if int(turn[0]) > truth_dict.get(turn[1]):
#             print(f"Game number {game_num} is not possible")
#             is_game_possible = False
#             break
#     if is_game_possible:
#         total_sum += game_num

# print(total_sum)
#### End Part 1 ####

#### Part 2 ####
total_sum = 0

for item in f:
    max_dict = {'red': 0, 'green': 0, 'blue': 0}
    game_power = 0
    turns = re.split('[,;]', item.split(':')[1])
    for turn_raw in turns:
        turn = turn_raw.strip().split(' ')
        if int(turn[0]) > max_dict.get(turn[1]):
            max_dict.update(
                {turn[1]: int(turn[0])}
            )
    game_power = reduce(lambda x, y: x * y, max_dict.values())
    total_sum += game_power

print(total_sum)


    


#### End Part 2 #### 
