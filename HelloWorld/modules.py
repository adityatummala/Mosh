# write a function find_max to calculate the maximum
# should accept a list as input, find the maximum and return the largest number
# put this in a separate module called utils
# import utils into the current module and call this function. Print the result

import utils


source_list = input("Enter a set of numbers : ")
source_list_copy = source_list.split(' ')
max_value_copy = utils.find_max(source_list_copy)
print(utils.find_max(source_list_copy))
print(max_value_copy)
