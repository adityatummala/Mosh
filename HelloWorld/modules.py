# write a function find_max to calculate the maximum
# should accept a list as input, find the maximum and return the largest number
# put this in a separate module called utils
# import utils into the current module and call this function. Print the result

import utils
import random


source_list = input("Enter a set of numbers : ")
source_list_copy = source_list.split(' ')
max_value_copy = utils.find_max(source_list_copy)
print(utils.find_max(source_list_copy))
print(max_value_copy)

print(random.random())

# Rolling a die.
# To define a class called Dice; have a method called roll which should generate 2 random values


class Dice:
    def roll(self):
        first_roll = random.randint(1, 6)
        second_roll = random.randint(1, 6)
        return first_roll, second_roll


dice_copy = Dice()
print(dice_copy.roll())






