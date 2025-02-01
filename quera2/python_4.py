x = int(input())
n = []
for i in range(1, x + 1):
    a = input()
    n.insert(-1, a)

seen = set()

final_list = filter(lambda num: num in seen or seen.add(num), n)

m = set(final_list)

for value in m:
    print(value)    