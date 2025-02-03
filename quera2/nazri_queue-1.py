x = int(input())
n = []
for i in range(1, x + 1):
    a = input()
    n.append(a)

seen = set()
m = []
# final_list = filter(lambda num: num in seen or seen.add(num), n)
for num in n:
    if num in seen:
        m.append(num)
    else:
        seen.add(num)

for value in m:
    print(value)      
