def max_c_value(case):

    results = []
    if 2 ** len(case) == len(results):
        return max(results)

    c = [0]
    for i in range(len(case)):
        for j in range(len(c)):
            c[j] += case[i]
            results.extend(c)
            c[j] -= case[i]
            c[j] = abs(c[j] + case[i])
            results.extend(c)
            print(results)
            c.extend(results)
            print(c)
            del c[: 2**j + 1]
        max_c_value(c)
    print(max(results))


num_list = int(input())
num_list_final = []
for i in range(num_list):
    a = list(map(int, input().split()))
    result = max_c_value(a)
    del num_list_final[:]
