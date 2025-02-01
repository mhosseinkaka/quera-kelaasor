from collections import Counter

x = int(input())
a = []
for i in range(1, x + 1):
    name = input()
    a.append(name.split())

m = []
f = []
for value in a:
    if value[-1] == "M":
        m.append(value[0])
    elif value[-1] == "F":
        f.append(value[0])

m.sort()
f.sort()

count_f = Counter(f)
count_m = Counter(m)

count_f_f = count_f.most_common(1)
count_m_m = count_m.most_common(1)

print(count_f_f[0][0])
print(count_m_m[0][0])