x = input()
l = len(x) 
for i in range(l):
    if i < l -1:
        print(x)
        x = x.replace(x[i], x[i + 1])
    else:
        print(x.replace(x[i], x[l-1]))

