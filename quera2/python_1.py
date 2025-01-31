x = int(input("enter number of students: "))
a = []
for i in range(1, x + 1):
    name = input("enter name: ")
    a.append(name.split())

m = []
f = []
for value in a:
    if value[-1] == "M":
        m.append(value[0])
    elif value[-1] == "F":
        f.append(value[0])

print(f)
print(m)