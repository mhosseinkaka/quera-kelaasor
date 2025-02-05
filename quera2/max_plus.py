num_list = int(input())
num_list_final = []
for i in range(num_list):
    a = list(map(int,input().split()))
    num_list_final.append(a)

def max_c_value(cases):
    results_abs = []
    result = []
    
    for case in cases:
        c = 0
        for num in case:
            c1 = c + num
            c2 = abs(c + num)
            c = max(c1, c2)
        results_abs.append(c2)
        result.append(c1)
    
    return result, results_abs


def final(lst1, lst2):
    results = []
    for i in range(len(lst1)):
        if lst1[i] > lst2[i]:
            results.append(lst1[i])
        else:
            results.append(lst2[i])
    return results


lst1, lst2 = max_c_value(num_list_final)
result = final(lst1, lst2)
for res in result:
    print(res)