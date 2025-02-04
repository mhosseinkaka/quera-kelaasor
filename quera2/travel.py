list_number = list(map(int, input().split()))
list_number = sorted(list_number)


def lost(list_people):
    if len(list_people) == list_people[-1]:
        result = len(list_people) + 1
    else:
        for i in range(len(list_people)):
            if int(list_people[i]) - i > 1:
                result = list_people[i] - 1
                break
    return result


# 1 2 3 4 5 6 7 8
# 0 1 2 3 4 5 6 7

print(lost(list_number))