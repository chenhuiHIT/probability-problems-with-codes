"""
Suppose you're on a game show, and you're given the choice of three doors: Behind one door is a car; 
behind the others, goats. You pick a door, say No. 1, and the host, who knows what's behind the doors, 
opens another door, say No. 3, which has a goat. He then says to you, "Do you want to pick door No. 2?" 
Is it to your advantage to switch your choice?
"""

import random

def run(repeat_nums):
    switch_win = 0
    no_switch_win  = 0
    # 0 means goat, 1 means car.always choose No.1 
    doors = [0, 0, 0]
    for i in range(repeat_nums):
        position = random.choice([0, 1, 2])
        if position == 0:
            no_switch_win += 1
        elif position == 1:
            switch_win += 1
        else:
            switch_win += 1
    
    print("switch win ratio {}".format(switch_win/repeat_nums))
    print("no switch win ratio {}".format(no_switch_win/repeat_nums))

if __name__ =='__main__':
    test_num = 1000000
    run(test_num)