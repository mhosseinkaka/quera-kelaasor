import copy


def lights_out(a, b, c):

    row1 = copy.deepcopy(a)
    row2 = copy.deepcopy(b)
    row3 = copy.deepcopy(c)

    for i in range(3):
        for j in range(3):
            if [a, b, c][i][j] % 2 == 1:
                if i > 0:
                    [row1, row2, row3][i - 1][j] += 1
                if i < 2:
                    [row1, row2, row3][i + 1][j] += 1
                if j > 0:
                    [row1, row2, row3][i][j - 1] += 1
                if j < 2:
                    [row1, row2, row3][i][j + 1] += 1

    on_off_row1 = list(map(str, [((item + 1) % 2) for item in row1]))
    on_off_row2 = list(map(str, [((item + 1) % 2) for item in row2]))
    on_off_row3 = list(map(str, [((item + 1) % 2) for item in row3]))

    print(" ".join(on_off_row1))
    print(" ".join(on_off_row2))
    print(" ".join(on_off_row3))


line1 = list(map(int, input().split()))
line2 = list(map(int, input().split()))
line3 = list(map(int, input().split()))

lights_out(line1, line2, line3)