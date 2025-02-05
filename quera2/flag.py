def solution_num(number, seen={}):
    if number in seen:
        return seen[number]

    if number == 1 or number == 2:
        return 2
    elif number == 3:
        return 4

    seen[number] = solution_num(number - 1, seen) + solution_num(number - 2, seen)
    return seen[number]


number_of_walls = int(input())
print(solution_num(number_of_walls))