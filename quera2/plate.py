list_plate = list(map(int, input().split()))

list_rev = []
for value in list_plate:
    if value == 1:
        value = 0
        list_rev.append(value)
    else:
        value = 1
        list_rev.append(value)

def find_range(list):
    range_list = []
    start = None
    for i, num in enumerate(list):
        if num == 1:
            if start is None:
                start = i
        else:
            if start is not None:
                range_list.append((start, i - 1))
                start = None
    if start is not None:
        range_list.append((start, len(list) - 1))
    return range_list

def big(range_list):
    big_range = max(range_list, key= lambda x:x[1] - x[0] + 1)
    max_one = big_range[1] - big_range[0] + 1
    return max_one

m = []
for num in list_plate:
    if num == 1:
        m.append(num)
final_plate = len(m) + big(find_range(list_rev))

print(final_plate)