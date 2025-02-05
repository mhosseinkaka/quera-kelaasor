# n = int(input())
# m = "".join(str(10**i) for i in range(n+1))
# print(m[n - 1])

# for i in range(n + 1):
#     v = 10 ** i
#     m += str(v)

def weird_sequence(n):
    i = int(((1 + (1 + 8 * (n - 1)) ** 0.5) / 2))
    return 1 if (i * (i - 1)) // 2 == (n - 1) else 0


desired_number = int(input())
print(weird_sequence(desired_number))



    
