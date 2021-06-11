input = [3, 5, 6, 1, 2, 4]


def find_max_num(array):
    max_num = array[0]
    for num in array:
        if num > max_num:
            max_num = num

    return max_num


result = find_max_num(input)
print(result)

# num = 3 > max_num= 3 // False
# num = 5 > max_num= 3 // True -> max_num = 5
# num = 6 > max_num = 5 // True -> max_num = 6
# num = 1 > max_num = 6 // False
# num = 2 > max_num = 6 // False
# num = 4 > max_num = 6 // False
# max_num = 6
