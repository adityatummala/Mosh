
def find_max(input_list):
    max_value = input_list[0]
    for i in input_list:
        if i > max_value:
            max_value = i
    return max_value