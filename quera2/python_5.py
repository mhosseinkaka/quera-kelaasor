def child(kid):
    kid = list(kid)
    i = 0
    while i < len(kid):
        if kid[i] == "B" and kid[i + 1] == "G":
            kid[i], kid[i + 1] = kid[i + 1], kid[i]
            i += 1
        i += 1
    return "".join(kid)

kid_number = list(map(int, input().split()))
move = kid_number[1]
first = input().strip()

for kid in range(move):
    first = child(first)
print(first)