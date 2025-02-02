from collections import Counter

def rep(number):
    rep_list = Counter(number)
    result_1 = [i for i, count in rep_list.items() if count > 1]
    result_2 = "\n".join(result_1)
    return result_2

final_list = []
x = int(input())
for num in range(x):
    list_num = input().split()
    final_list.extend(list_num)

print(rep(final_list))