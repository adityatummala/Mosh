prices = [10, 20, 30]
sum_total = 0
for i in prices:
    sum_total += i
print(f"Total: {sum_total} \n")


for x in range(5):
    if x in [1, 3, 4]:
        y = 2
        print("*" * y)
    else:
        y = 5
        print("*" * y)

print("\n\n")

some_list = [10, 30, 45, 108, 14, 56, 98, 67, 234]
max = some_list[0]
for i in some_list:
    if max <= i:
        max = i;
print(f"The max value in the list is: {max}")

some_list_copy = some_list
print(some_list_copy)

test_list = [7, 5, 6, 45]
test_list.pop(2)
print(test_list)

second_list = [4, 5, 4, 34, 4, 23, 34, 76, 23, 34]
second_list_nodups = []
i = 0
for i in second_list:
    if i not in second_list_nodups:
        second_list_nodups.append(i)
print(f"After removing duplicates : {second_list_nodups}")







